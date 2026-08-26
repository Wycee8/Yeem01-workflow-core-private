#!/usr/bin/env python3
"""Planning-only opportunity scan for `-improve all skills`.

This helper applies deterministic versions of the normal skill-target
improvement checks across the workspace skill registry. It does not edit files.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
REGISTRY = ROOT / "skills" / "skills_registry.json"
AUDIT_JSON = ROOT / "workspace_control" / "reports" / "skill_audit_report.json"
FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n?", re.DOTALL)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def section_present(text: str, pattern: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE) is not None


def live_body_chars(text: str) -> int:
    """Match the body-length evidence used by the canonical skill audit."""
    body = FRONTMATTER_RE.sub("", text, count=1)
    return len(body.strip())


def load_audits() -> dict[str, dict[str, Any]]:
    if not AUDIT_JSON.exists():
        return {}
    payload = load_json(AUDIT_JSON)
    return {item.get("path", ""): item for item in payload.get("audits", [])}


def evidence_for(entry: dict[str, Any], audit: dict[str, Any] | None) -> dict[str, Any]:
    path = ROOT / entry["path"]
    text = read_text(path)
    desc = entry.get("description") or ""
    lower = text.lower()
    description_lower = desc.lower()
    reference_dir = path.parent / "references"
    current_body_chars = live_body_chars(text)
    audit_body_chars = audit.get("body_chars") if audit else None
    audit_projection_stale = (
        audit_body_chars is not None and audit_body_chars != current_body_chars
    )
    refs = re.findall(r"`([^`]+/(?:[^`]+)\.md)`|`([^`]+\.md)`", text)
    flat_refs = [a or b for a, b in refs]
    return {
        "path": entry["path"],
        "text": text,
        "description": desc,
        "body_chars": current_body_chars,
        "findings": (
            audit.get("findings", [])
            if audit and not audit_projection_stale
            else []
        ),
        "audit_projection_stale": audit_projection_stale,
        "evidence_status": (
            "stale_audit_projection_ignored"
            if audit_projection_stale
            else ("current_audit_projection" if audit else "live_skill_only")
        ),
        "has_use_when": (
            any(term in description_lower for term in ["use when", "use for"])
            or re.search(r"\buse (?:this skill )?(?:when|only for)\b", lower) is not None
            or section_present(text, r"^##\s+Public Entrance\b")
        ),
        "has_do_not": any(term in lower for term in ["do not", "do-not", "when not", "do not use"]),
        "has_goal": (
            section_present(text, r"^##\s+(Goal|Job|Purpose|Objective|Highest Directive)\b")
            or re.search(
                r"^#\s+[^\n]+\n(?:\s*\n)?(?:(?!^##\s).){0,500}\b(?:is|answers|helps|owns|provides|routes)\b",
                text,
                flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
            )
            is not None
        ),
        "has_operating_principles": section_present(
            text,
            r"^##\s+(Operating Principles|Core Principle|Core Rule|Operator-facing Rule|Guardrails|Procedure|(?:Default )?Workflow|Rules|Boundaries)\b",
        ) or section_present(text, r"^##\s+\d+\.\s"),
        "has_mode_router": section_present(
            text,
            r"^##\s+(Mode|Modes|Public Entrance|Call Syntax|Depth Selection|Compact Command Routing|Hub Selection|Route By Intent)\b|mode router|call syntax",
        ),
        "has_output": section_present(
            text,
            r"^##\s+(?:Standard |Completion And )?Outputs?\b|output contract|primary output|expected output|report exactly one outcome|return only:",
        ),
        "has_validation": any(term in lower for term in ["validate", "validation", "checklist", "trigger test", "test case"]),
        "has_trigger_tests": (
            (reference_dir / "trigger-tests.md").exists()
            or (reference_dir / "trigger-cases.json").exists()
            or (reference_dir / "test-cases.md").exists()
            or "trigger-tests.md" in lower
            or "trigger tests" in lower
            or "trigger-cases.json" in lower
            or section_present(text, r"^##\s+(Trigger Tests|Tests)\b")
        ),
        "has_test_cases": (
            (reference_dir / "test-cases.md").exists()
            or "test-cases.md" in lower
            or "test cases" in lower
        ),
        "has_references": "references/" in lower,
        "has_scripts": "scripts/" in lower,
        "refs": flat_refs,
    }


def score_skill(entry: dict[str, Any], ev: dict[str, Any]) -> dict[str, Any]:
    score = 0
    reasons: list[str] = []
    recommendations: list[str] = []

    status = entry.get("status")
    kind = entry.get("kind")
    load_tier = entry.get("load_tier")
    user_invocable = bool(entry.get("user_invocable"))
    desc = ev["description"]
    text_lower = ev["text"].lower()
    body_chars = ev["body_chars"] or 0
    desc_lower = desc.lower()
    legacy_like = (
        bool(entry.get("legacy"))
        or entry.get("kind") == "compatibility"
        or bool(entry.get("replaced_by"))
        or desc_lower.startswith("legacy ")
        or desc_lower.startswith("legacy-")
        or desc_lower.startswith("archived ")
        or "compatibility slug" in desc_lower
        or "compatibility-only" in desc_lower
        or "compatibility-era" in desc_lower
        or "retired legacy" in desc_lower
        or "superseded by" in desc_lower
    )

    if legacy_like and status == "active":
        score += 28
        reasons.append("active legacy/compatibility surface may confuse routing")
        if entry.get("replaced_by"):
            replacement = ", ".join(entry.get("replaced_by") or [])
            recommendations.append(f"absorb into or redirect clearly to `{replacement}`")
        else:
            recommendations.append("decide whether to retire, demote, or sharpen redirect boundary")

    high_leverage = status == "active" and (kind in {"hub", "mode"} or load_tier in {"hub", "always"} or user_invocable)

    if status == "active" and not ev["has_use_when"]:
        score += 16
        reasons.append("trigger guidance could be more explicit")
        recommendations.append("clarify natural trigger and Use when guidance")

    if high_leverage and not ev["has_do_not"]:
        score += 12
        reasons.append("near-miss boundary is weak or implicit")
        recommendations.append("add or sharpen Do not use / adjacent-route boundary")

    if high_leverage and not ev["has_goal"] and not ev["has_operating_principles"]:
        score += 10
        reasons.append("purpose and operating procedure are both implicit")
        recommendations.append("clarify purpose or procedure when next touched")

    requires_mode_router = status == "active" and (kind == "hub" or load_tier == "hub")
    if requires_mode_router and not ev["has_mode_router"]:
        score += 14
        reasons.append("mode/call shape is weak for a routing hub")
        recommendations.append("add a compact mode or call-syntax table")

    if high_leverage and not ev["has_output"]:
        score += 10
        reasons.append("output contract is not explicit")
        recommendations.append("name the expected output or decision packet")

    if high_leverage and not ev["has_validation"]:
        score += 12
        reasons.append("validation path is not explicit")
        recommendations.append("add validation or proof guidance")

    if high_leverage and not ev["has_trigger_tests"]:
        score += 10
        reasons.append("missing trigger-test reference for high-use routing")
        recommendations.append("add trigger-test cases")

    if status == "active" and body_chars < 1200:
        score += 8
        reasons.append("body may be too thin for repeatable behavior")
        recommendations.append("expand only the minimum workflow needed")

    if body_chars > 14000 and not ev["has_references"]:
        score += 8
        reasons.append("large SKILL.md without obvious progressive-disclosure references")
        recommendations.append("move long detail into references")

    if "prefer mai control room" in text_lower and "dashboard" in (entry.get("slug") or ""):
        score += 20
        reasons.append("legacy dashboard route overlaps current MAI Control Room route")
        recommendations.append("convert to compatibility redirect or retire from active user-invocable routing")

    warning_findings = [
        finding for finding in ev["findings"]
        if finding.get("severity") in {"error", "warning"}
    ]
    if warning_findings:
        score += 30
        reasons.append("audit warning/error present")
        recommendations.append("repair audit findings first")

    info_findings = [
        finding for finding in ev["findings"]
        if finding.get("severity") == "info"
    ]
    if status == "dormant" and info_findings:
        score += 3
        reasons.append("dormant/compatibility skill may only need leave-dormant or retirement clarity")
        recommendations.append("leave dormant unless it re-enters active routing")

    # Leverage is a priority multiplier, not a defect. Apply it only when the
    # evidence above found a concrete improvement opportunity.
    if high_leverage and score > 0:
        score += 25

    if not reasons:
        reasons.append("no meaningful deterministic opportunity found")
        recommendations.append("no-op")

    # De-prioritize dormant skills unless they have hard findings.
    if status != "active" and not warning_findings:
        score = min(score, 7)
    if entry.get("is_symlink") and entry.get("legacy") and not warning_findings:
        score = min(score, 35)

    first_recommendation = recommendations[0] if recommendations else "no-op"
    return {
        "slug": entry.get("slug"),
        "name": entry.get("name"),
        "path": entry.get("path"),
        "status": status,
        "kind": kind,
        "load_tier": load_tier,
        "user_invocable": user_invocable,
        "score": score,
        "priority_context": "high_leverage" if high_leverage and score > 0 else "normal",
        "depth_verdict": "Fix" if score >= 30 else ("Review" if score >= 16 else "Keep"),
        "reasons": reasons[:5],
        "recommendations": recommendations[:5],
        "recommendation": first_recommendation,
        "evidence_status": ev["evidence_status"],
    }


def scan(include_dormant: bool) -> list[dict[str, Any]]:
    registry = load_json(REGISTRY)
    audits = load_audits()
    entries = registry.get("skills", [])
    rows: list[dict[str, Any]] = []
    for entry in entries:
        if entry.get("alias_of"):
            continue
        if entry.get("status") != "active" and not include_dormant:
            continue
        path = ROOT / entry["path"]
        if not path.exists() or path.name != "SKILL.md":
            continue
        audit = audits.get(entry["path"])
        ev = evidence_for(entry, audit)
        rows.append(score_skill(entry, ev))
    rows.sort(key=lambda item: (-item["score"], item["slug"] or ""))
    return rows


def shown_rows(rows: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return rows
    return rows[:limit]


def render_markdown(rows: list[dict[str, Any]], limit: int) -> str:
    shown = shown_rows(rows, limit)
    lines = [
        "# Improve All Skills Opportunity Scan",
        "",
        "Planning-only: no skill files were edited.",
        f"Skills shown: {len(shown)} of {len(rows)}.",
        "",
        "| Rank | Skill | Score | Verdict | Recommendation | Evidence |",
        "|---|---|---:|---|---|---|",
    ]
    for idx, row in enumerate(shown, 1):
        evidence = "; ".join(row["reasons"])
        lines.append(
            f"| {idx} | `{row['slug']}` | {row['score']} | {row['depth_verdict']} | "
            f"{row['recommendation']} | {evidence} |"
        )
    if not shown:
        lines.append("| - | none | 0 | Keep | no-op | no active skills scanned |")
    lines.extend([
        "",
        "Recommendation: start with the highest-scoring active skill only after explicit approval.",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Planning-only scan for `-improve all skills`.")
    parser.add_argument("--json", action="store_true", help="print machine-readable results")
    parser.add_argument("--limit", type=int, default=0, help="number of rows to show; default 0 means all")
    parser.add_argument("--include-dormant", action="store_true", help="include dormant/compatibility skills")
    args = parser.parse_args()

    rows = scan(include_dormant=args.include_dormant)
    shown = shown_rows(rows, args.limit)
    payload = {
        "mode": "planning_only",
        "skills_scanned": len(rows),
        "skills_shown": len(shown),
        "top": shown,
    }
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(render_markdown(rows, args.limit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
