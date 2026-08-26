#!/usr/bin/env python3
"""Focused regressions for Improve opportunity-scan evidence detection."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("scan_skill_opportunities.py")
SPEC = importlib.util.spec_from_file_location("scan_skill_opportunities", SCRIPT_PATH)
assert SPEC and SPEC.loader
scanner = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = scanner
SPEC.loader.exec_module(scanner)


def skill_text() -> str:
    base = """---
name: sample
description: Use for sample routing checks.
---

# Sample

## Job
Keep routing evidence accurate.

## Public Entrance
Route the request without exposing internal layers.

## Core Rule
Prefer existing evidence.

## Output
Return a ranked result.

## Validation
Run the focused test.

Do not mutate runtime loading.
"""
    # Keep this fixture above the scanner's intentional thin-body threshold so
    # the test isolates routing-evidence detection.
    return base + ("\nEvidence-backed procedure detail." * 50)


def sample_entry() -> dict[str, object]:
    return {
        "slug": "sample",
        "name": "sample",
        "path": "skills/sample/SKILL.md",
        "description": "Use for sample routing checks.",
        "status": "active",
        "kind": "hub",
        "load_tier": "hub",
        "user_invocable": True,
        "legacy": False,
        "replaced_by": [],
        "is_symlink": False,
    }


def test_live_artifacts_and_contract_equivalents_are_recognized() -> None:
    original_root = scanner.ROOT
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            scanner.ROOT = Path(temp_dir)
            skill_dir = scanner.ROOT / "skills" / "sample"
            references = skill_dir / "references"
            references.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(skill_text(), encoding="utf-8")
            (references / "trigger-cases.json").write_text("{}\n", encoding="utf-8")

            evidence = scanner.evidence_for(sample_entry(), None)
            assert evidence["has_use_when"], evidence
            assert evidence["has_goal"], evidence
            assert evidence["has_operating_principles"], evidence
            assert evidence["has_mode_router"], evidence
            assert evidence["has_trigger_tests"], evidence

            row = scanner.score_skill(sample_entry(), evidence)
            joined = "; ".join(row["reasons"])
            assert "trigger guidance could be more explicit" not in joined, row
            assert "mode/call shape is weak" not in joined, row
            assert "missing trigger-test reference" not in joined, row
            assert row["score"] == 0, row
            assert row["depth_verdict"] == "Keep", row
            assert row["recommendation"] == "no-op", row
    finally:
        scanner.ROOT = original_root


def test_stale_audit_findings_are_disclosed_and_ignored() -> None:
    original_root = scanner.ROOT
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            scanner.ROOT = Path(temp_dir)
            skill_dir = scanner.ROOT / "skills" / "sample"
            skill_dir.mkdir(parents=True)
            text = skill_text()
            (skill_dir / "SKILL.md").write_text(text, encoding="utf-8")
            stale_audit = {
                "body_chars": scanner.live_body_chars(text) - 1,
                "findings": [
                    {
                        "code": "stale_warning",
                        "severity": "warning",
                        "detail": "stale generated finding",
                    }
                ],
            }

            evidence = scanner.evidence_for(sample_entry(), stale_audit)
            assert evidence["audit_projection_stale"] is True, evidence
            assert evidence["evidence_status"] == "stale_audit_projection_ignored", evidence
            assert evidence["findings"] == [], evidence

            row = scanner.score_skill(sample_entry(), evidence)
            assert "audit warning/error present" not in row["reasons"], row
            assert row["evidence_status"] == "stale_audit_projection_ignored", row
    finally:
        scanner.ROOT = original_root


def test_high_leverage_only_amplifies_a_concrete_gap() -> None:
    original_root = scanner.ROOT
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            scanner.ROOT = Path(temp_dir)
            skill_dir = scanner.ROOT / "skills" / "sample"
            references = skill_dir / "references"
            references.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(skill_text(), encoding="utf-8")
            (references / "trigger-tests.md").write_text("# Trigger tests\n", encoding="utf-8")

            evidence = scanner.evidence_for(sample_entry(), None)
            evidence["has_output"] = False
            row = scanner.score_skill(sample_entry(), evidence)

            assert row["score"] == 35, row
            assert row["depth_verdict"] == "Fix", row
            assert row["priority_context"] == "high_leverage", row
            assert "output contract is not explicit" in row["reasons"], row
    finally:
        scanner.ROOT = original_root


def test_single_purpose_mode_does_not_require_a_mode_router() -> None:
    original_root = scanner.ROOT
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            scanner.ROOT = Path(temp_dir)
            skill_dir = scanner.ROOT / "skills" / "sample"
            references = skill_dir / "references"
            references.mkdir(parents=True)
            text = skill_text().replace("## Public Entrance", "## Procedure")
            (skill_dir / "SKILL.md").write_text(text, encoding="utf-8")
            (references / "trigger-tests.md").write_text("# Trigger tests\n", encoding="utf-8")
            entry = sample_entry()
            entry["kind"] = "mode"
            entry["load_tier"] = "always"

            evidence = scanner.evidence_for(entry, None)
            evidence["has_mode_router"] = False
            row = scanner.score_skill(entry, evidence)
            assert "mode/call shape is weak for a routing hub" not in row["reasons"], row
    finally:
        scanner.ROOT = original_root


def main() -> int:
    test_live_artifacts_and_contract_equivalents_are_recognized()
    test_stale_audit_findings_are_disclosed_and_ignored()
    test_high_leverage_only_amplifies_a_concrete_gap()
    test_single_purpose_mode_does_not_require_a_mode_router()
    print("improve opportunity scan evidence regressions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
