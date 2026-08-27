#!/usr/bin/env python3
"""Install Yeem01 Workflow Core into a documented Agent Skills directory."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path


CHANNEL_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = CHANNEL_ROOT / "plugins" / "yeem01-workflow-core"
SOURCE_ROOT = PLUGIN_ROOT / "skills"
PLUGIN_MANIFEST = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
INSTALL_MANIFEST_NAME = ".yeem01-workflow-core-install.json"
PACK_NAME = "yeem01-workflow-core"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def files_under(root: Path) -> list[Path]:
    files = []
    for path in sorted(root.rglob("*")):
        require(not path.is_symlink(), f"symlink not allowed in skill source: {path}")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
            files.append(path)
    return files


def tree_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for path in files_under(root):
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(sha256(path).encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def source_state() -> tuple[str, dict[str, str]]:
    require(PLUGIN_MANIFEST.is_file(), f"plugin manifest missing: {PLUGIN_MANIFEST}")
    version = read_json(PLUGIN_MANIFEST)["version"]
    skills = {
        path.name: tree_hash(path)
        for path in sorted(SOURCE_ROOT.iterdir())
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    require(len(skills) == 10, f"expected 10 bundled skills, found {len(skills)}")
    require(PACK_NAME in skills, "front-door skill missing")
    return version, skills


def resolve_target(args: argparse.Namespace) -> Path:
    if args.target is not None:
        target = args.target.expanduser().resolve()
    elif args.provider == "cursor" and args.scope == "user":
        target = (Path.home() / ".cursor" / "skills").resolve()
    elif args.provider == "cursor" and args.scope == "project":
        require(args.project_root is not None, "--project-root is required for project scope")
        project_root = args.project_root.expanduser().resolve()
        require(project_root != Path(project_root.anchor), "project root cannot be a filesystem root")
        target = (project_root / ".cursor" / "skills").resolve()
        require(target.is_relative_to(project_root), "resolved target escaped project root")
    else:
        raise RuntimeError("--target is required for the generic agent-skills provider")

    require(target.name == "skills", "target must be an exact directory named 'skills'")
    require(target != Path(target.anchor), "target cannot be a filesystem root")
    require(target != Path.home().resolve(), "target cannot be the user home directory")
    return target


def expected_manifest(
    version: str,
    skills: dict[str, str],
    provider: str,
    scope: str,
) -> dict:
    return {
        "schema_version": "yeem01_workflow_core_agent_skills_install.v1",
        "pack": PACK_NAME,
        "version": version,
        "provider": provider,
        "scope": scope,
        "skills": dict(sorted(skills.items())),
    }


def load_existing_manifest(target: Path) -> dict | None:
    path = target / INSTALL_MANIFEST_NAME
    if not path.exists():
        return None
    payload = read_json(path)
    require(payload.get("pack") == PACK_NAME, "existing install manifest belongs to another pack")
    require(isinstance(payload.get("skills"), dict), "existing install manifest is invalid")
    return payload


def check_install(target: Path, expected: dict) -> dict:
    existing = load_existing_manifest(target)
    require(existing is not None, f"install manifest missing: {target / INSTALL_MANIFEST_NAME}")
    require(existing == expected, "installed manifest does not match this checkout; run update")
    for name, expected_hash in expected["skills"].items():
        destination = target / name
        require((destination / "SKILL.md").is_file(), f"installed skill missing: {name}")
        require(tree_hash(destination) == expected_hash, f"installed skill differs: {name}")
    return {
        "status": "PASS",
        "action": "check",
        "version": expected["version"],
        "provider": expected["provider"],
        "scope": expected["scope"],
        "skill_count": len(expected["skills"]),
        "target": str(target),
    }


def write_manifest_atomic(target: Path, payload: dict) -> None:
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=target,
        prefix=".yeem01-manifest-",
        delete=False,
    ) as handle:
        handle.write(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        temporary = Path(handle.name)
    temporary.replace(target / INSTALL_MANIFEST_NAME)


def install_or_update(
    target: Path,
    expected: dict,
    action: str,
    dry_run: bool,
) -> dict:
    existing = load_existing_manifest(target) if target.exists() else None
    if action == "install" and existing is not None:
        try:
            result = check_install(target, expected)
            result["action"] = "install-noop"
            return result
        except RuntimeError as exc:
            raise RuntimeError(f"pack is already managed but differs: {exc}; use --action update") from exc
    require(action != "update" or existing is not None,
            "cannot update an unmanaged target; run install first")

    old_skills = set(existing["skills"]) if existing else set()
    new_skills = set(expected["skills"])
    for name in sorted(new_skills):
        destination = target / name
        require(not destination.exists() or name in old_skills,
                f"unmanaged skill collision: {destination}")

    if dry_run:
        return {
            "status": "DRY_RUN",
            "action": action,
            "version": expected["version"],
            "provider": expected["provider"],
            "scope": expected["scope"],
            "skill_count": len(new_skills),
            "target": str(target),
        }

    target.mkdir(parents=True, exist_ok=True)
    require(target.is_dir(), f"target is not a directory: {target}")
    staging = Path(tempfile.mkdtemp(prefix=".yeem01-stage-", dir=target.parent))
    staged_skills = staging / "new"
    backups = staging / "backup"
    staged_skills.mkdir()
    backups.mkdir()
    changed: list[str] = []
    backed_up: list[str] = []
    try:
        for name in sorted(new_skills):
            shutil.copytree(SOURCE_ROOT / name, staged_skills / name)
            require(tree_hash(staged_skills / name) == expected["skills"][name],
                    f"staged skill hash mismatch: {name}")

        for name in sorted(old_skills | new_skills):
            destination = target / name
            if destination.exists():
                destination.rename(backups / name)
                backed_up.append(name)
            if name in new_skills:
                (staged_skills / name).rename(destination)
                changed.append(name)
        write_manifest_atomic(target, expected)
    except Exception:
        for name in reversed(changed):
            destination = target / name
            if destination.exists():
                shutil.rmtree(destination)
        for name in reversed(backed_up):
            backup = backups / name
            if backup.exists():
                backup.rename(target / name)
        raise
    finally:
        if staging.exists():
            shutil.rmtree(staging)

    result = check_install(target, expected)
    result["action"] = action
    return result


def uninstall_managed(target: Path, dry_run: bool) -> dict:
    """Remove only an intact installation recorded by this pack's manifest."""
    require(target.is_dir(), f"managed target missing: {target}")
    existing = load_existing_manifest(target)
    require(existing is not None, f"install manifest missing: {target / INSTALL_MANIFEST_NAME}")

    managed_skills = existing["skills"]
    for name, expected_hash in sorted(managed_skills.items()):
        destination = target / name
        require((destination / "SKILL.md").is_file(),
                f"managed skill missing; refusing uninstall: {name}")
        require(tree_hash(destination) == expected_hash,
                f"managed skill differs; refusing uninstall: {name}")

    result = {
        "status": "DRY_RUN" if dry_run else "PASS",
        "action": "uninstall",
        "version": existing.get("version", "unknown"),
        "provider": existing.get("provider", "unknown"),
        "scope": existing.get("scope", "unknown"),
        "skill_count": len(managed_skills),
        "target": str(target),
        "target_removed": False,
    }
    if dry_run:
        return result

    staging = Path(tempfile.mkdtemp(prefix=".yeem01-uninstall-", dir=target.parent))
    moved: list[str] = []
    manifest_path = target / INSTALL_MANIFEST_NAME
    manifest_moved = False
    try:
        for name in sorted(managed_skills):
            (target / name).rename(staging / name)
            moved.append(name)
        manifest_path.rename(staging / INSTALL_MANIFEST_NAME)
        manifest_moved = True
    except Exception:
        if manifest_moved and (staging / INSTALL_MANIFEST_NAME).exists():
            (staging / INSTALL_MANIFEST_NAME).rename(manifest_path)
        for name in reversed(moved):
            backup = staging / name
            if backup.exists():
                backup.rename(target / name)
        raise
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=("cursor", "agent-skills"), default="cursor")
    parser.add_argument("--scope", choices=("user", "project", "explicit"), default="user")
    parser.add_argument("--project-root", type=Path)
    parser.add_argument("--target", type=Path)
    parser.add_argument(
        "--action",
        choices=("install", "update", "check", "uninstall"),
        default="install",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        version, skills = source_state()
        target = resolve_target(args)
        expected = expected_manifest(version, skills, args.provider, args.scope)
        if args.action == "check":
            require(not args.dry_run, "--dry-run cannot be combined with check")
            result = check_install(target, expected)
        elif args.action == "uninstall":
            result = uninstall_managed(target, args.dry_run)
        else:
            result = install_or_update(target, expected, args.action, args.dry_run)
    except (RuntimeError, OSError, json.JSONDecodeError) as exc:
        if args.json:
            print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2, sort_keys=True))
        else:
            print(f"FAIL: {exc}")
        return 1

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(
            f"{result['status']}: {result['action']} {result['skill_count']} skills "
            f"for {result['provider']} at {result['target']} (version {result['version']})"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
