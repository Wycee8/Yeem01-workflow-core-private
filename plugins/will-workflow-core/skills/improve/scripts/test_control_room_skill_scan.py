#!/usr/bin/env python3
"""Focused regressions for the Control Room workspace-skill scan helper."""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("control_room_skill_scan.py")
SPEC = importlib.util.spec_from_file_location("control_room_skill_scan", SCRIPT_PATH)
assert SPEC and SPEC.loader
scanner = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = scanner
SPEC.loader.exec_module(scanner)


def write_session(path: Path, texts: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for text in texts:
        rows.append({
            "type": "response_item",
            "payload": {
                "type": "message",
                "role": "user",
                "content": [{"type": "input_text", "text": text}],
            },
        })
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


def test_usage_is_user_only_deduplicated_and_directional() -> None:
    original_registry = scanner.REGISTRY
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            registry = root / "skills_registry.json"
            registry.write_text(json.dumps({"skills": [
                {
                    "slug": "improve",
                    "name": "improve",
                    "status": "active",
                    "aliases": [],
                    "entrypoints": [],
                    "alias_of": None,
                },
                {
                    "slug": "quality-check",
                    "name": "quality check",
                    "description": "Use when the operator invokes -qa or -QA, or asks for completed-work verification.",
                    "status": "active",
                    "aliases": [],
                    "entrypoints": [],
                    "alias_of": None,
                },
            ]}), encoding="utf-8")
            scanner.REGISTRY = registry
            session_a = root / "sessions" / "2026" / "08" / "05" / "rollout-019f1111-1111-1111-1111-111111111111.jsonl"
            session_b = root / "sessions" / "2026" / "08" / "06" / "rollout-019f2222-2222-2222-2222-222222222222.jsonl"
            prompt = "Use -improve, then audit the quality check skill with -qa."
            write_session(session_a, [prompt, "<codex_internal_context> -improve"])
            write_session(session_b, [prompt])

            payload = scanner.collect_usage(
                root / "sessions",
                scanner.date(2026, 8, 1),
                scanner.date(2026, 8, 7),
            )
            assert payload["stats"]["eligible_user_messages"] == 2, payload["stats"]
            assert payload["stats"]["unique_user_prompts"] == 1, payload["stats"]
            assert payload["stats"]["duplicate_prompt_copies_ignored"] == 1, payload["stats"]
            assert payload["skills"]["improve"]["explicit_command_count"] == 1
            assert payload["skills"]["quality-check"]["direct_skill_target_count"] == 1
            assert payload["skills"]["quality-check"]["explicit_command_count"] == 1
            assert "absence" in payload["limitations"][2].lower()
    finally:
        scanner.REGISTRY = original_registry


def test_active_first_manifest_and_hash_drift_detection() -> None:
    original_root = scanner.ROOT
    original_registry = scanner.REGISTRY
    original_ranker = scanner.RANKER_PATH
    original_control = scanner.CONTROL_PATH
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "skills" / "active").mkdir(parents=True)
            (root / "skills" / "dormant").mkdir(parents=True)
            (root / "skills" / "active" / "SKILL.md").write_text("active\n", encoding="utf-8")
            (root / "skills" / "dormant" / "SKILL.md").write_text("dormant\n", encoding="utf-8")
            registry = root / "skills" / "skills_registry.json"
            registry.write_text(json.dumps({"skills": [
                {"slug": "dormant", "name": "dormant", "path": "skills/dormant/SKILL.md", "status": "dormant", "kind": "retired", "alias_of": None},
                {"slug": "active", "name": "active", "path": "skills/active/SKILL.md", "status": "active", "kind": "hub", "alias_of": None},
            ]}), encoding="utf-8")
            usage = root / "usage.json"
            usage.write_text(json.dumps({"window": {}, "source": "fixture", "limitations": []}), encoding="utf-8")
            scanner.ROOT = root
            scanner.REGISTRY = registry
            scanner.RANKER_PATH = root / "ranker.py"
            scanner.CONTROL_PATH = root / "control.py"
            scanner.RANKER_PATH.write_text("ranker\n", encoding="utf-8")
            scanner.CONTROL_PATH.write_text("control\n", encoding="utf-8")

            manifest = scanner.build_manifest("fixture", usage)
            assert [item["slug"] for item in manifest["skills"]] == ["active", "dormant"]
            assert scanner.verify_manifest(manifest) == []
            (root / "skills" / "active" / "SKILL.md").write_text("changed\n", encoding="utf-8")
            drift = scanner.verify_manifest(manifest)
            assert len(drift) == 1 and drift[0]["slug"] == "active", drift
    finally:
        scanner.ROOT = original_root
        scanner.REGISTRY = original_registry
        scanner.RANKER_PATH = original_ranker
        scanner.CONTROL_PATH = original_control


def main() -> int:
    test_usage_is_user_only_deduplicated_and_directional()
    test_active_first_manifest_and_hash_drift_detection()
    print("control room skill scan regressions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
