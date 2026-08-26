#!/usr/bin/env python3
"""Resumable, no-target-write Control Room scan for workspace skills.

The helper complements ``scan_skill_opportunities.py``. It freezes the
canonical registry inventory, compiles privacy-bounded directional usage
signals from Codex session JSONL, writes one audit record per skill, emits
ten-active-skill checkpoints, and verifies that scanned skill bodies did not
drift after the baseline.

It never edits a skill file. Output is limited to the operator-selected report
directory.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parents[2]
REGISTRY = ROOT / "skills" / "skills_registry.json"
RANKER_PATH = SCRIPT_DIR / "scan_skill_opportunities.py"
CONTROL_PATH = Path(__file__).resolve()
SCHEMA_VERSION = "1.0.0"
CHECKPOINT_EVERY = 10
MAX_USER_MESSAGE_BYTES = 200_000
MAX_EXAMPLES = 3

SKIP_USER_PREFIXES = (
    "# AGENTS.md instructions",
    "<codex_internal_context",
    "<codex_delegation",
    "<recommended_plugins>",
    "<environment_context>",
)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def session_date(path: Path) -> date | None:
    parts = path.parts
    for idx in range(len(parts) - 3):
        if re.fullmatch(r"20\d{2}", parts[idx] or ""):
            try:
                return date(int(parts[idx]), int(parts[idx + 1]), int(parts[idx + 2]))
            except (ValueError, IndexError):
                return None
    return None


def session_id(path: Path) -> str:
    match = re.search(r"(019[0-9a-f-]{33,})", path.name)
    return match.group(1) if match else path.stem


def iter_session_files(root: Path, start: date, end_exclusive: date) -> Iterable[Path]:
    for path in sorted(root.rglob("*.jsonl")):
        observed = session_date(path)
        if observed is not None and start <= observed < end_exclusive:
            yield path


def extract_user_text(payload: dict[str, Any]) -> str | None:
    if payload.get("type") != "response_item":
        return None
    item = payload.get("payload") or {}
    if item.get("type") != "message" or item.get("role") != "user":
        return None
    chunks: list[str] = []
    for content in item.get("content") or []:
        if content.get("type") == "input_text" and isinstance(content.get("text"), str):
            chunks.append(content["text"])
    text = "\n".join(chunks).strip()
    if not text or text.startswith(SKIP_USER_PREFIXES):
        return None
    return text


def canonical_entries() -> list[dict[str, Any]]:
    payload = load_json(REGISTRY)
    entries = [entry for entry in payload.get("skills", []) if not entry.get("alias_of")]
    indexed = list(enumerate(entries))
    indexed.sort(key=lambda pair: (pair[1].get("status") != "active", pair[0]))
    return [entry for _, entry in indexed]


def command_terms(entry: dict[str, Any]) -> list[str]:
    terms = {entry.get("slug") or "", entry.get("name") or ""}
    terms.update(entry.get("aliases") or [])
    for item in entry.get("entrypoints") or []:
        if isinstance(item, str):
            terms.add(item.lstrip("-"))
    # The registry does not yet project every operator alias. Admit only
    # command tokens from a description's explicit "invokes" or "Use for"
    # clause; do not scrape routed commands from the full skill body.
    description = entry.get("description") or ""
    for clause in re.findall(r"\b(?:invokes?|use for)\s+([^,.;]+)", description, flags=re.I):
        terms.update(re.findall(r"(?<!\w)-([A-Za-z][A-Za-z0-9-]*)", clause))
    return sorted({normalize_text(term).lower() for term in terms if normalize_text(term)})


def match_usage(text: str, entry: dict[str, Any]) -> tuple[bool, bool]:
    lower = normalize_text(text).lower()
    explicit = False
    direct = False
    for term in command_terms(entry):
        term_pattern = r"[- ]".join(re.escape(part) for part in re.split(r"[- ]+", term))
        if re.search(rf"(?<![\w-])-{term_pattern}(?![\w-])", lower):
            explicit = True
        if re.search(rf"\b(?:{term_pattern}\s+skill|skill\s+{term_pattern})\b", lower):
            direct = True
    return explicit, direct


def collect_usage(sessions_root: Path, start: date, end_exclusive: date) -> dict[str, Any]:
    entries = canonical_entries()
    evidence: dict[str, dict[str, Any]] = {
        entry["slug"]: {
            "explicit_command_count": 0,
            "direct_skill_target_count": 0,
            "matched_unique_prompt_count": 0,
            "source_session_count": 0,
            "examples": [],
            "_sessions": set(),
        }
        for entry in entries
    }
    stats = {
        "session_files_considered": 0,
        "session_files_read": 0,
        "json_lines_read": 0,
        "invalid_json_lines": 0,
        "oversized_lines_skipped": 0,
        "eligible_user_messages": 0,
        "unique_user_prompts": 0,
        "duplicate_prompt_copies_ignored": 0,
    }
    seen_prompts: set[str] = set()

    for path in iter_session_files(sessions_root, start, end_exclusive):
        stats["session_files_considered"] += 1
        file_read = False
        with path.open("rb") as handle:
            for raw in handle:
                stats["json_lines_read"] += 1
                if b'"role":"user"' not in raw and b'"role": "user"' not in raw:
                    continue
                if len(raw) > MAX_USER_MESSAGE_BYTES:
                    stats["oversized_lines_skipped"] += 1
                    continue
                try:
                    payload = json.loads(raw)
                except (UnicodeDecodeError, json.JSONDecodeError):
                    stats["invalid_json_lines"] += 1
                    continue
                text = extract_user_text(payload)
                if text is None:
                    continue
                file_read = True
                stats["eligible_user_messages"] += 1
                normalized = normalize_text(text)
                prompt_hash = sha256_bytes(normalized.encode("utf-8"))
                if prompt_hash in seen_prompts:
                    stats["duplicate_prompt_copies_ignored"] += 1
                    continue
                seen_prompts.add(prompt_hash)
                stats["unique_user_prompts"] += 1
                sid = session_id(path)
                for entry in entries:
                    explicit, direct = match_usage(normalized, entry)
                    if not explicit and not direct:
                        continue
                    row = evidence[entry["slug"]]
                    row["explicit_command_count"] += int(explicit)
                    row["direct_skill_target_count"] += int(direct)
                    row["matched_unique_prompt_count"] += 1
                    row["_sessions"].add(sid)
                    if len(row["examples"]) < MAX_EXAMPLES:
                        row["examples"].append({
                            "prompt_sha256": prompt_hash,
                            "session_id": sid,
                            "excerpt": normalized[:240],
                        })
        if file_read:
            stats["session_files_read"] += 1

    for row in evidence.values():
        row["source_session_count"] = len(row.pop("_sessions"))

    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": utc_now(),
        "source": "local_codex_session_jsonl_user_messages_only",
        "window": {"start": start.isoformat(), "end_exclusive": end_exclusive.isoformat()},
        "privacy": {
            "raw_transcripts_copied": False,
            "stored_examples_per_skill": MAX_EXAMPLES,
            "maximum_example_characters": 240,
            "oversized_user_message_limit_bytes": MAX_USER_MESSAGE_BYTES,
        },
        "limitations": [
            "Counts are directional routing evidence, not proof that a skill loaded or completed work.",
            "Exact duplicate prompt text is counted once to reduce copied-session inflation; repeated identical real prompts may be undercounted.",
            "Absence of a match is unknown usage, never evidence that a skill is unused.",
            "Only explicit -command forms and direct '<name> skill' phrases are matched; semantic invocations can be missed.",
            "Injected context, delegation envelopes, oversized lines, and non-user message roles are excluded.",
        ],
        "stats": stats,
        "skills": evidence,
    }


def load_ranker() -> Any:
    spec = importlib.util.spec_from_file_location("improve_opportunity_ranker", RANKER_PATH)
    if not spec or not spec.loader:
        raise RuntimeError(f"could not load {RANKER_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def inventory_row(entry: dict[str, Any], order: int) -> dict[str, Any]:
    path = ROOT / entry["path"]
    return {
        "order": order,
        "slug": entry.get("slug"),
        "name": entry.get("name"),
        "path": entry.get("path"),
        "status": entry.get("status"),
        "kind": entry.get("kind"),
        "load_tier": entry.get("load_tier"),
        "user_invocable": bool(entry.get("user_invocable")),
        "sha256": sha256_file(path),
    }


def build_manifest(programme_id: str, usage_path: Path) -> dict[str, Any]:
    usage = load_json(usage_path)
    entries = canonical_entries()
    return {
        "schema_version": SCHEMA_VERSION,
        "programme_id": programme_id,
        "created_at": utc_now(),
        "mode": "audit_only_no_target_skill_writes",
        "root": str(ROOT),
        "registry": {
            "path": str(REGISTRY.relative_to(ROOT)),
            "sha256": sha256_file(REGISTRY),
        },
        "engine": [
            {"path": str(RANKER_PATH.relative_to(ROOT)), "sha256": sha256_file(RANKER_PATH)},
            {"path": str(CONTROL_PATH.relative_to(ROOT)), "sha256": sha256_file(CONTROL_PATH)},
        ],
        "evidence_window": usage.get("window"),
        "usage_index": {
            "path": str(usage_path),
            "sha256": sha256_file(usage_path),
            "source": usage.get("source"),
            "limitations": usage.get("limitations", []),
        },
        "checkpoint_every_active_skills": CHECKPOINT_EVERY,
        "skill_count": len(entries),
        "active_skill_count": sum(entry.get("status") == "active" for entry in entries),
        "skills": [inventory_row(entry, idx) for idx, entry in enumerate(entries, 1)],
    }


def extract_headings(text: str, pattern: str) -> list[str]:
    return [match.group(1).strip() for match in re.finditer(pattern, text, flags=re.MULTILINE | re.IGNORECASE)]


def depth_verdict(entry: dict[str, Any], ranked: dict[str, Any]) -> str:
    if entry.get("status") != "active" and entry.get("kind") in {"retired", "compatibility", "alias"}:
        return "Retire" if ranked.get("score", 0) >= 16 else "Keep"
    return "Fix" if ranked.get("score", 0) >= 16 else "Keep"


def skill_record(
    inventory: dict[str, Any],
    entry: dict[str, Any],
    ranked: dict[str, Any],
    usage: dict[str, Any],
    ranker: Any,
) -> dict[str, Any]:
    path = ROOT / entry["path"]
    text = path.read_text(encoding="utf-8", errors="replace")
    audit = ranker.load_audits().get(entry["path"])
    structural = ranker.evidence_for(entry, audit)
    refs = sorted({item for item in structural.get("refs", []) if item})
    modes = extract_headings(text, r"^###\s+(.+)$")
    scripts_dir = path.parent / "scripts"
    scripts = sorted(str(item.relative_to(ROOT)) for item in scripts_dir.glob("*") if item.is_file()) if scripts_dir.exists() else []
    usage_state = "observed" if usage.get("matched_unique_prompt_count", 0) else "not_observed_unknown"
    verdict = depth_verdict(entry, ranked)
    reasons = ranked.get("reasons", [])
    recommendations = list(ranked.get("recommendations") or [ranked.get("recommendation", "no-op")])
    if usage_state == "not_observed_unknown":
        recommendations.append("preserve until semantic/runtime evidence exists; absence is not non-use")
    if verdict == "Keep":
        recommendations.append("no target-skill mutation in this scan")
    while len(recommendations) < 3:
        recommendations.append("retain current boundary pending target-specific outcome evidence")
    cheapest_test = (
        "Run one isolated trigger/near-miss fixture before any patch."
        if ranked.get("score", 0) > 0
        else "No test required until new friction appears; retain current validators."
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "identity": inventory,
        "shape": {
            "description": entry.get("description"),
            "routes_to": entry.get("routes_to") or [],
            "depends_on": entry.get("depends_on") or [],
            "aliases": entry.get("aliases") or [],
            "body_characters": structural.get("body_chars"),
            "level_three_headings": modes,
            "reference_mentions": refs,
            "script_files": scripts,
            "has_use_when": structural.get("has_use_when"),
            "has_near_miss_boundary": structural.get("has_do_not"),
            "has_mode_router": structural.get("has_mode_router"),
            "has_output_contract": structural.get("has_output"),
            "has_validation": structural.get("has_validation"),
            "has_trigger_tests": structural.get("has_trigger_tests"),
        },
        "recent_usage": {
            **usage,
            "evidence_state": usage_state,
            "interpretation": "directional only; absence is unknown, not unused",
        },
        "user_first": {
            "operator_or_user_language_present": bool(re.search(r"\b(operator|user|client|customer|audience)\b", text, re.I)),
            "output_contract_present": structural.get("has_output"),
            "finding": (
                "User-facing output is structurally named."
                if structural.get("has_output")
                else "User-facing outcome is implicit and should be tested before any repair."
            ),
        },
        "efficiency": {
            "progressive_disclosure_present": structural.get("has_references"),
            "deterministic_helper_present": structural.get("has_scripts"),
            "finding": reasons[0] if reasons else "no deterministic friction found",
        },
        "bloat": {
            "large_without_references": bool((structural.get("body_chars") or 0) > 14000 and not structural.get("has_references")),
            "thin_active_body": bool(entry.get("status") == "active" and (structural.get("body_chars") or 0) < 1200),
            "preferred_action": "delete/absorb/shrink before adding new surfaces",
        },
        "diagnosis": {
            "score": ranked.get("score", 0),
            "priority_context": ranked.get("priority_context", "normal"),
            "depth_verdict": verdict,
            "top_findings": reasons[:3],
            "top_improvements": recommendations[:3],
            "confidence": "medium" if usage_state == "observed" else "low_to_medium",
            "cheapest_test": cheapest_test,
            "patch_boundary": str(path.relative_to(ROOT).parent) + "/**",
            "scan_disposition": "plan_only_no_write",
        },
    }


def verify_manifest(manifest: dict[str, Any]) -> list[dict[str, str]]:
    drift: list[dict[str, str]] = []
    for item in manifest.get("engine", []):
        path = ROOT / item["path"]
        observed = sha256_file(path) if path.exists() else "missing"
        if observed != item["sha256"]:
            drift.append({"slug": f"engine:{item['path']}", "expected": item["sha256"], "observed": observed})
    for item in manifest.get("skills", []):
        path = ROOT / item["path"]
        observed = sha256_file(path) if path.exists() else "missing"
        if observed != item["sha256"]:
            drift.append({"slug": item["slug"], "expected": item["sha256"], "observed": observed})
    return drift


def render_checkpoint(number: int, records: list[dict[str, Any]]) -> str:
    lines = [
        f"# Control Room Skill Improvement Checkpoint {number:02d}",
        "",
        "Audit-only checkpoint. No target skill was edited by the fleet scan.",
        "",
        "| Skill | Status | Score | Verdict | Usage | Primary finding |",
        "|---|---|---:|---|---|---|",
    ]
    for record in records:
        identity = record["identity"]
        diagnosis = record["diagnosis"]
        usage = record["recent_usage"]
        finding = (diagnosis["top_findings"] or ["no deterministic friction found"])[0].replace("|", "/")
        lines.append(
            f"| `{identity['slug']}` | {identity['status']} | {diagnosis['score']} | "
            f"{diagnosis['depth_verdict']} | {usage['evidence_state']} | {finding} |"
        )
    lines.extend(["", "Next: continue from `SCAN_CURSOR.json`; do not patch target skills in this programme."])
    return "\n".join(lines) + "\n"


def render_all_skills(records: list[dict[str, Any]]) -> str:
    lines = [
        "# Control Room Skill Improvement Scan — Full Ranked Index",
        "",
        "Planning evidence only. Scores prioritize structural follow-up; they are not automatic edit or retirement authority.",
        "Usage is directional explicit-command/direct-skill evidence; `unknown` never means unused.",
        "",
        "| Rank | Skill | Status / kind | Score | Verdict | Usage | Primary finding | First option |",
        "|---:|---|---|---:|---|---:|---|---|",
    ]
    for rank, record in enumerate(records, 1):
        identity = record["identity"]
        diagnosis = record["diagnosis"]
        usage = record["recent_usage"]
        finding = (diagnosis["top_findings"] or ["no deterministic friction found"])[0].replace("|", "/")
        option = (diagnosis["top_improvements"] or ["no-op"])[0].replace("|", "/")
        lines.append(
            f"| {rank} | `{identity['slug']}` | {identity['status']} / {identity['kind']} | "
            f"{diagnosis['score']} | {diagnosis['depth_verdict']} | "
            f"{usage.get('matched_unique_prompt_count', 0)} | {finding} | {option} |"
        )
    return "\n".join(lines) + "\n"


def run_scan(output_dir: Path) -> dict[str, Any]:
    manifest_path = output_dir / "SCAN_MANIFEST.json"
    manifest = load_json(manifest_path)
    drift = verify_manifest(manifest)
    if drift:
        raise RuntimeError(f"baseline drift detected before scan: {json.dumps(drift, ensure_ascii=False)}")

    registry_by_slug = {entry["slug"]: entry for entry in canonical_entries()}
    usage_payload = load_json(Path(manifest["usage_index"]["path"]))
    usage_by_slug = usage_payload.get("skills", {})
    ranker = load_ranker()
    rank_by_slug = {row["slug"]: row for row in ranker.scan(include_dormant=True)}
    records: list[dict[str, Any]] = []
    checkpoint_buffer: list[dict[str, Any]] = []
    checkpoint_number = 0
    active_seen = 0

    cursor = {
        "schema_version": SCHEMA_VERSION,
        "programme_id": manifest["programme_id"],
        "status": "in_progress",
        "total": manifest["skill_count"],
        "completed": 0,
        "next_order": 1,
        "last_slug": None,
        "checkpoints_written": 0,
    }
    write_json(output_dir / "SCAN_CURSOR.json", cursor)

    for item in manifest["skills"]:
        slug = item["slug"]
        entry = registry_by_slug[slug]
        record = skill_record(item, entry, rank_by_slug[slug], usage_by_slug.get(slug, {}), ranker)
        write_json(output_dir / "skills" / f"{slug}.json", record)
        records.append(record)
        cursor.update({"completed": len(records), "next_order": len(records) + 1, "last_slug": slug})
        write_json(output_dir / "SCAN_CURSOR.json", cursor)
        if item["status"] == "active":
            active_seen += 1
            checkpoint_buffer.append(record)
            if active_seen % CHECKPOINT_EVERY == 0:
                checkpoint_number += 1
                (output_dir / "checkpoints").mkdir(parents=True, exist_ok=True)
                (output_dir / "checkpoints" / f"CHECKPOINT_{checkpoint_number:02d}.md").write_text(
                    render_checkpoint(checkpoint_number, checkpoint_buffer), encoding="utf-8"
                )
                checkpoint_buffer = []
                cursor["checkpoints_written"] = checkpoint_number
                write_json(output_dir / "SCAN_CURSOR.json", cursor)

    if checkpoint_buffer:
        checkpoint_number += 1
        (output_dir / "checkpoints").mkdir(parents=True, exist_ok=True)
        (output_dir / "checkpoints" / f"CHECKPOINT_{checkpoint_number:02d}.md").write_text(
            render_checkpoint(checkpoint_number, checkpoint_buffer), encoding="utf-8"
        )

    ranked = sorted(records, key=lambda row: (-row["diagnosis"]["score"], row["identity"]["slug"]))
    write_json(output_dir / "FLEET_SCAN_RECORDS.json", {"schema_version": SCHEMA_VERSION, "records": ranked})
    (output_dir / "ALL_SKILLS_REPORT.md").write_text(render_all_skills(ranked), encoding="utf-8")
    cursor.update({
        "status": "complete",
        "next_order": None,
        "checkpoints_written": checkpoint_number,
        "completed_at": utc_now(),
    })
    write_json(output_dir / "SCAN_CURSOR.json", cursor)
    return cursor


def parse_date(value: str) -> date:
    return date.fromisoformat(value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    usage_parser = subparsers.add_parser("collect-usage", help="compile privacy-bounded recent usage evidence")
    usage_parser.add_argument("--sessions-root", type=Path, required=True)
    usage_parser.add_argument("--start", type=parse_date, required=True)
    usage_parser.add_argument("--end-exclusive", type=parse_date, required=True)
    usage_parser.add_argument("--output", type=Path, required=True)

    baseline_parser = subparsers.add_parser("baseline", help="freeze registry order and skill hashes")
    baseline_parser.add_argument("--programme-id", required=True)
    baseline_parser.add_argument("--usage-index", type=Path, required=True)
    baseline_parser.add_argument("--output-dir", type=Path, required=True)

    scan_parser = subparsers.add_parser("scan", help="write one no-write audit record per frozen skill")
    scan_parser.add_argument("--output-dir", type=Path, required=True)

    verify_parser = subparsers.add_parser("verify", help="verify skill hashes against the frozen baseline")
    verify_parser.add_argument("--output-dir", type=Path, required=True)

    args = parser.parse_args()
    if args.command == "collect-usage":
        payload = collect_usage(args.sessions_root.expanduser(), args.start, args.end_exclusive)
        write_json(args.output, payload)
        print(json.dumps({"status": "ok", "output": str(args.output), "stats": payload["stats"]}, indent=2))
        return 0
    if args.command == "baseline":
        args.output_dir.mkdir(parents=True, exist_ok=True)
        manifest = build_manifest(args.programme_id, args.usage_index.resolve())
        write_json(args.output_dir / "SCAN_MANIFEST.json", manifest)
        print(json.dumps({"status": "ok", "skill_count": manifest["skill_count"]}, indent=2))
        return 0
    if args.command == "scan":
        cursor = run_scan(args.output_dir)
        print(json.dumps(cursor, indent=2))
        return 0
    manifest = load_json(args.output_dir / "SCAN_MANIFEST.json")
    drift = verify_manifest(manifest)
    print(json.dumps({"status": "clean" if not drift else "drift", "drift": drift}, indent=2))
    return 0 if not drift else 1


if __name__ == "__main__":
    raise SystemExit(main())
