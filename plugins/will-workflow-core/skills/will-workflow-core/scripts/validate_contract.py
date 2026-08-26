#!/usr/bin/env python3
"""Validate Will Workflow Core without external dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
PLUGIN_DIR = SKILL_DIR.parents[1]
VERSION = "0.4.1"

COMMANDS = (
    "help",
    "onboarding",
    "explain",
    "ask",
    "user",
    "audit",
    "discuss",
    "explore",
    "research",
    "suggest",
    "plan",
    "qa",
    "evaluate",
    "improve",
)

URL_PATTERN = re.compile(r"https?://")

CORE_EXPECTED_FILES = {
    ".codex-plugin/plugin.json",
    "skills/will-workflow-core/SKILL.md",
    "skills/will-workflow-core/agents/openai.yaml",
    "skills/will-workflow-core/references/command-contract.md",
    "skills/will-workflow-core/references/maintenance.md",
    "skills/will-workflow-core/references/onboarding.md",
    "skills/will-workflow-core/references/validation-cases.json",
    "skills/will-workflow-core/scripts/validate_contract.py",
}

PORTABLE_SKILLS = {
    "artifact-lane-output-defaults",
    "audit-check",
    "improve",
    "pipeline",
    "project-charter-docs",
    "quality-check",
    "research",
    "user-skill",
    "workspace-implementation-planning",
}

IGNORED_PARTS = {".DS_Store", "__pycache__", ".pytest_cache"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read_text(path: Path) -> str:
    require(path.is_file(), f"missing file: {path}")
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tree_sha256(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        if (not path.is_file() or IGNORED_PARTS.intersection(path.parts)
                or path.suffix == ".pyc"):
            continue
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(sha256(path).encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def detect_tokens(prompt: str) -> list[str]:
    """Approximate explicit command-token recognition for fixture validation."""
    lower = prompt.lower()
    found: list[str] = []
    for token in COMMANDS:
        if re.search(rf"(?<![a-z0-9-])-{token}(?![a-z0-9])", lower):
            found.append(token)
    if re.search(
        r"(?<![a-z0-9-])(?:adam\s+)?(?:auto\s+)?proceed(?:\s+all)?(?![a-z0-9-])",
        lower,
    ):
        found.append("proceed")
    return sorted(set(found))


def plugin_files() -> set[str]:
    return {
        path.relative_to(PLUGIN_DIR).as_posix()
        for path in PLUGIN_DIR.rglob("*")
        if path.is_file()
        and not IGNORED_PARTS.intersection(path.parts)
        and path.suffix != ".pyc"
    }


def validate_manifest() -> None:
    manifest_path = PLUGIN_DIR / ".codex-plugin" / "plugin.json"
    manifest = json.loads(read_text(manifest_path))
    require(manifest["name"] == "will-workflow-core", "manifest name mismatch")
    require(manifest["version"] == VERSION, f"manifest must be version {VERSION}")
    require(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]) is not None,
            "invalid semver")
    require(manifest["skills"] == "./skills/", "skills path must be ./skills/")
    for forbidden in ("mcpServers", "apps", "hooks", "repository", "homepage"):
        require(forbidden not in manifest, f"forbidden component declared: {forbidden}")
    require(manifest["author"] == {"name": "Yeem01 Workspace"},
            "author metadata must identify the canonical source and remain URL-free")
    require("Yeem01-backed" in manifest["description"],
            "manifest must declare the Yeem01-backed source model")
    require({"private", "yeem01", "onboarding", "workflow"} <= set(manifest["keywords"]),
            "manifest keywords must declare source, privacy, onboarding, and workflow")
    defaults = manifest["interface"]["defaultPrompt"]
    require(isinstance(defaults, list) and 1 <= len(defaults) <= 3,
            "invalid default prompts")
    require(manifest["interface"]["displayName"] == "Will Workflow Core",
            "display name must preserve the current core skill name")
    require(URL_PATTERN.search(manifest_path.read_text(encoding="utf-8")) is None,
            "manifest must not expose public URLs")


def validate_marketplace(marketplace_path: Path) -> None:
    marketplace = json.loads(read_text(marketplace_path))
    matches = [
        item for item in marketplace["plugins"]
        if item.get("name") == "will-workflow-core"
    ]
    require(len(matches) == 1, "marketplace must contain exactly one plugin entry")
    entry = matches[0]
    require(entry["source"] == {
        "source": "local",
        "path": "./plugins/will-workflow-core",
    }, "marketplace source mismatch")
    require(entry["policy"]["installation"] == "AVAILABLE",
            "installation policy mismatch")
    require(entry["policy"]["authentication"] == "ON_INSTALL",
            "auth policy mismatch")
    require(marketplace["name"] == "will-private",
            "marketplace must be will-private")
    require(marketplace.get("interface", {}).get("displayName") == "Will Private",
            "marketplace display name mismatch")


def validate_skill() -> None:
    skill = read_text(SKILL_DIR / "SKILL.md")
    yaml = read_text(SKILL_DIR / "agents" / "openai.yaml")
    contract = read_text(SKILL_DIR / "references" / "command-contract.md")
    onboarding = read_text(SKILL_DIR / "references" / "onboarding.md")
    maintenance = read_text(SKILL_DIR / "references" / "maintenance.md")

    require("[TODO:" not in skill, "SKILL.md contains TODO placeholder")
    require(len(skill.splitlines()) < 500, "SKILL.md exceeds compact context budget")
    require(len(skill.encode("utf-8")) < 18000, "SKILL.md exceeds 18 KB")
    require(len(onboarding.encode("utf-8")) < 14000,
            "onboarding reference exceeds 14 KB")
    require(len(maintenance.encode("utf-8")) < 9000,
            "maintenance reference exceeds 9 KB")
    for command in COMMANDS:
        require(f"-{command}" in skill, f"missing command contract: -{command}")
    require("proceed" in skill, "missing command contract: proceed")
    for boundary in (
        "connector", "credentials", "provider spend", "Git publication",
        "production", "destructive",
    ):
        require(boundary in skill, f"missing host boundary: {boundary}")
    require("$will-workflow-core" in yaml, "default prompt must name the skill")
    require("allow_implicit_invocation: true" in yaml,
            "implicit invocation must be explicit")
    require("dependencies:" not in yaml,
            "portable skill must not declare tool dependencies")
    require("Yeem01-backed" in skill,
            "missing Yeem01-backed source declaration")
    require("Distribution and access decisions live outside this core" in skill,
            "core must keep access decisions out of scope")
    require("## Host Capability Precedence" in skill,
            "skill must declare host capability precedence")
    require("BUNDLE_MANIFEST.json" in skill,
            "skill must explain the generated portable suite")
    require("fallback below only when the host exposes no applicable" in skill,
            "skill must make fallback conditional")
    for planning_depth in ("`-plan`:", "`-plan all`:", "`-plan full`"):
        require(planning_depth in skill,
                f"missing planning-depth contract: {planning_depth}")
    for owner_token in ("`-qa`", "`-evaluate`", "`-pap`/`-dap`", "`-design`"):
        require(owner_token in skill or owner_token in contract,
                f"missing specialist-delegation declaration: {owner_token}")
    require("## Lifecycle" in skill, "skill must define the complete lifecycle")
    require("QA asks whether work was built correctly" in skill,
            "QA purpose is not explicit")
    require("Judge impact only after credible use evidence exists" in skill,
            "evaluation evidence gate is missing")
    require("Never silently collect raw transcripts" in skill,
            "improvement privacy boundary is missing")
    require("## Portable Device Boundary" in contract,
            "command contract must define device onboarding")
    require("inherits no" in contract and "credentials" in contract,
            "device onboarding must refuse inherited authority")
    require("## Central Source And Release" in contract,
            "command contract must define the central source")
    require("## Improvement Proposal Contract" in contract,
            "command contract must define improvement proposals")
    for section in (
        "## What It Is", "## Where It Comes From", "## Getting Started",
        "## How To Invoke It", "## Compact Command Map",
        "## Worked Audit-To-Improvement Example", "## Simple Improvement Feedback",
        "## First Safe Practice",
    ):
        require(section in onboarding, f"onboarding missing section: {section}")
    for lifecycle_mode in ("-audit", "-discuss", "-plan all", "-qa", "-evaluate", "-improve"):
        require(lifecycle_mode in onboarding,
                f"onboarding lifecycle missing {lifecycle_mode}")
    for section in (
        "## Source And Output", "## Normal Update Flow",
        "## Simple Feedback Contract", "## Future Central Distribution",
        "## Release Rule",
    ):
        require(section in maintenance, f"maintenance missing section: {section}")
    combined_core = "\n".join((skill, contract, onboarding, maintenance)).lower()
    for forbidden_phrase in (
        "approval gate", "approved user", "owner approves", "grant approval",
        "private pilot rule",
    ):
        require(forbidden_phrase not in combined_core,
                f"access decision leaked into core behavior: {forbidden_phrase}")


def validate_bundle_manifest(files: set[str]) -> int:
    manifest_path = PLUGIN_DIR / "BUNDLE_MANIFEST.json"
    if not manifest_path.is_file():
        require(files == CORE_EXPECTED_FILES,
                "canonical source plugin may contain only the command-front-door files")
        return 1

    manifest = json.loads(read_text(manifest_path))
    require(manifest["schema_version"] == "will_workflow_core_bundle.v1",
            "bundle manifest schema mismatch")
    require(manifest["plugin"] == "will-workflow-core", "bundle plugin mismatch")
    require(manifest["version"] == VERSION, "bundle version mismatch")
    entries = manifest["skills"]
    names = {entry["name"] for entry in entries}
    require(names == PORTABLE_SKILLS,
            f"portable skill allowlist mismatch: {sorted(names)}")
    require(len(entries) == len(names), "duplicate bundled skill entry")
    for entry in entries:
        name = entry["name"]
        require((PLUGIN_DIR / "skills" / name / "SKILL.md").is_file(),
                f"bundled skill missing SKILL.md: {name}")
        require(entry["source_path"].endswith(f"/skills/{name}"),
                f"bundled skill source path mismatch: {name}")
        require(re.fullmatch(r"[0-9a-f]{64}", entry["tree_sha256"]) is not None,
                f"bundled skill tree hash invalid: {name}")
        require(re.fullmatch(r"[0-9a-f]{64}", entry["source_tree_sha256"]) is not None,
                f"bundled source tree hash invalid: {name}")
        require(tree_sha256(PLUGIN_DIR / "skills" / name) == entry["tree_sha256"],
                f"bundled skill tree hash mismatch: {name}")
    actual_dirs = {
        path.name for path in (PLUGIN_DIR / "skills").iterdir()
        if path.is_dir() and path.name != "will-workflow-core"
    }
    require(actual_dirs == PORTABLE_SKILLS,
            f"packaged skill directories mismatch: {sorted(actual_dirs)}")
    return 1 + len(PORTABLE_SKILLS)


def validate_privacy_and_inventory() -> int:
    files = plugin_files()
    require(CORE_EXPECTED_FILES <= files,
            f"core file inventory incomplete: {sorted(CORE_EXPECTED_FILES - files)}")
    for path in PLUGIN_DIR.rglob("*"):
        relative_parts = path.relative_to(PLUGIN_DIR).parts
        require(not IGNORED_PARTS.intersection(relative_parts) and path.suffix != ".pyc",
                f"generated cache/noise is not allowed: {path.relative_to(PLUGIN_DIR)}")
    skill_count = validate_bundle_manifest(files)
    email_pattern = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
    secret_patterns = (
        re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
        re.compile(r"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    )
    for relative in sorted(files):
        path = PLUGIN_DIR / relative
        require(not path.is_symlink(), f"symlink not allowed in plugin: {relative}")
        require(path.stat().st_mode & 0o002 == 0,
                f"world-writable plugin file: {relative}")
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        require(email_pattern.search(text) is None,
                f"private email address found in {relative}")
        if relative in CORE_EXPECTED_FILES or relative == "BUNDLE_MANIFEST.json":
            require(URL_PATTERN.search(text) is None,
                    f"public URL found in core distribution control: {relative}")
        for pattern in secret_patterns:
            require(pattern.search(text) is None,
                    f"secret-like value found in {relative}")
        require(path.stat().st_size < 100_000,
                f"unexpectedly large plugin file: {relative}")
    return skill_count


def validate_cases() -> int:
    cases_path = SKILL_DIR / "references" / "validation-cases.json"
    payload = json.loads(read_text(cases_path))
    require(payload["schema_version"] == "3.0", "fixture schema must be 3.0")
    cases = payload["cases"]
    require(len(cases) >= 55, "insufficient validation coverage")
    ids = [case["id"] for case in cases]
    require(len(ids) == len(set(ids)), "duplicate validation case id")
    for case in cases:
        actual = detect_tokens(case["prompt"])
        expected = sorted(case["expect_tokens"])
        require(actual == expected,
                f"{case['id']}: expected {expected}, got {actual}")
        require(case["expect"], f"{case['id']}: missing outcome expectation")
    required_outcomes = {
        "activate_onboarding": "load_compact_onboarding_guide_only",
        "activate_plan_slice": "current_slice_plan_no_execution",
        "activate_plan_all": "complete_milestone_journey_no_execution",
        "activate_plan_full": "full_technical_plan_no_execution",
        "activate_qa": "post_build_quality_verification",
        "activate_evaluate": "post_use_impact_decision",
        "activate_improve": "evidence_backed_proposal_no_writes",
        "compose_full_lifecycle_guide": "explain_complete_lifecycle_without_execution",
        "delegate_qa": "route_to_available_quality_specialist",
        "delegate_evaluate": "route_to_available_evaluation_specialist",
        "gate_device_install": "explicit_device_install_gate",
        "privacy_no_passive_learning": "refuse_passive_transcript_collection",
        "privacy_no_employee_scoring": "refuse_employee_performance_scoring",
        "maintenance_explain_source": "yeem01_source_generated_release_model",
        "maintenance_no_device_edit": "edit_yeem01_source_not_device_copy",
        "stop_core_access_decision": "guide_only_host_owns_access_decision",
    }
    by_id = {case["id"]: case["expect"] for case in cases}
    for case_id, outcome in required_outcomes.items():
        require(by_id.get(case_id) == outcome,
                f"{case_id}: required outcome mismatch")
    categories = {case["id"].split("_", 1)[0] for case in cases}
    require({
        "activate", "compose", "delegate", "stop", "gate", "privacy",
        "maintenance", "abstain",
    } <= categories, "missing validation category")
    return len(cases)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--marketplace",
        type=Path,
        help="Validate the private distribution marketplace at this path.",
    )
    parser.add_argument(
        "--print-hashes",
        action="store_true",
        help="Print deterministic SHA-256 values for all plugin files.",
    )
    args = parser.parse_args()
    try:
        validate_manifest()
        validate_skill()
        skill_count = validate_privacy_and_inventory()
        if args.marketplace is not None:
            validate_marketplace(args.marketplace.resolve())
        count = validate_cases()
    except (AssertionError, KeyError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: will-workflow-core {VERSION} contract; {count} fixtures")
    print(f"PASS: portable suite with {skill_count} skills; onboarding, maintenance, privacy, inventory, and host boundaries")
    if args.marketplace is not None:
        print("PASS: private marketplace wiring")
    if args.print_hashes:
        for relative in sorted(plugin_files()):
            print(f"{sha256(PLUGIN_DIR / relative)}  {relative}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
