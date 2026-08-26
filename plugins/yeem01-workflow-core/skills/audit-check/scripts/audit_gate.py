#!/usr/bin/env python3
"""Run the portable content-brief or image-prompt audit gate."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
REFERENCES_DIR = SKILL_DIR / "references"
CHECKLISTS = {
    "content": "content-audit-checklist.md",
    "image": "image-prompt-checklist.md",
}


def load_checklist(kind: str) -> dict[str, list[dict[str, str]]]:
    path = REFERENCES_DIR / CHECKLISTS[kind]
    if not path.is_file():
        raise FileNotFoundError(f"Checklist not found: {path}")
    sections: dict[str, list[dict[str, str]]] = {}
    current = ""
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        elif current and (match := re.match(r"- \[ \] \*\*(.+?)\*\* — (.+)", line)):
            sections[current].append({
                "key": match.group(1).strip(),
                "description": match.group(2).strip(),
            })
    return sections


def validate_content(brief: dict) -> list[str]:
    groups = {
        "required field": ("objective", "audience", "key_message", "cta", "channels", "timeline"),
        "brand alignment": ("brand_voice", "brand_style", "brand_messaging", "brand_visuals"),
        "audience fit": ("relevance", "language", "journey_stage", "value_prop"),
        "fact-check": ("claims_verified", "source_attribution", "no_hallucinations"),
    }
    failures = [
        f"Missing {label}: {field}"
        for label, fields in groups.items()
        for field in fields
        if not brief.get(field)
    ]
    if brief.get("seo_applicable", False):
        missing = [
            field for field in ("primary_keyword", "secondary_keywords", "meta_description")
            if not brief.get(field)
        ]
        if missing:
            failures.append(f"SEO fields missing: {', '.join(missing)}")
    return failures


def validate_image(prompt: str) -> list[str]:
    lower = prompt.lower()
    groups = {
        "subject": ("person", "woman", "man", "group", "object", "scene"),
        "context": (" in ", " at ", " with ", " near ", " during "),
        "style": ("photorealistic", "digital art", "flat", "vector", "painting", "photo"),
        "technical": ("lighting", "light", "camera", "resolution", "warm", "cool"),
    }
    failures = [
        f"Missing core element: {label}"
        for label, terms in groups.items()
        if not any(term in f" {lower} " for term in terms)
    ]
    if "person" in lower and not any(term in lower for term in ("woman", "man", "girl", "boy", "group")):
        failures.append("Subject not specific enough (generic 'person')")
    if not any(term in lower for term in ("brand", "color", "palette", "logo", "yellow", "blue", "red", "green")):
        failures.append("No brand elements detected")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--type", choices=sorted(CHECKLISTS))
    parser.add_argument("--input", type=Path)
    parser.add_argument("--check-template", choices=sorted(CHECKLISTS))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.check_template:
        checklist = load_checklist(args.check_template)
        if args.json:
            print(json.dumps(checklist, indent=2))
        else:
            print(f"# {args.check_template.upper()} CHECKLIST")
            for section, items in checklist.items():
                print(f"\n## {section}")
                for item in items:
                    print(f"- [ ] **{item['key']}** — {item['description']}")
        return 0

    if args.type is None or args.input is None:
        parser.error("--type and --input are required unless --check-template is used")
    if not args.input.is_file():
        parser.error(f"input file not found: {args.input}")

    load_checklist(args.type)
    if args.type == "content":
        try:
            failures = validate_content(json.loads(args.input.read_text(encoding="utf-8")))
        except json.JSONDecodeError as exc:
            print(f"FAIL — invalid content JSON: {exc}", file=sys.stderr)
            return 1
    else:
        failures = validate_image(args.input.read_text(encoding="utf-8"))

    result = {"type": args.type, "input": str(args.input), "passed": not failures, "failures": failures}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{'PASS' if not failures else 'FAIL'} — {args.type} validation")
        for failure in failures:
            print(f"- {failure}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
