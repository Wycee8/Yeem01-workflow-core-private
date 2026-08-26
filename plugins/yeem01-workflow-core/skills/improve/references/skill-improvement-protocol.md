# Skill Improvement Protocol

Use this reference when the target is `improve` itself, another skill, skill
routing, command-mode behavior, or the whole skill fleet.

## Core Rule

Improve one bounded skill target per cycle.

Use evidence to learn, not only to justify a patch:

```text
signal -> limitation -> insight -> hypothesis -> cheapest test
-> user outcome + guardrail -> observation -> learning
```

The signal may come from a bounded Pattern Profile slice, direct operator
feedback, corrections, interviews, task outcomes, tests, logs, or another
target-appropriate source. Pattern frequency is optional evidence, never an
automatic requirement.

`-improve all skills` means apply the same normal skill-target diagnosis to the
skill inventory, aggregate the results, and rank the resulting opportunities.
Skill Control evidence is baseline input, not the decider. Bulk edits, global
routing changes, new controllers, runtime-loading changes, and broad
multi-owner changes remain gated even when the operator says proceed.

Keep ownership explicit: a generic `-improve` modifier stays with the named
artifact, project, or domain owner. Route through the persistent workspace
skill-maintenance lane only when the operator explicitly targets a skill,
skill routing, current skills, or the skill fleet.

Conceptually:

```text
map:    run normal -improve <skill> diagnosis for each skill
reduce: rank opportunities across the fleet
output: top targets, one recommendation, no-write cycle plan
```

## First Fleet Pass Is Planning Only

The first `-improve all skills` pass is always no-write for target skill bodies.
It may refresh generated Skill Control evidence, inspect registry/audit state,
run `{baseDir}/scripts/scan_skill_opportunities.py`, inspect selected candidates in more
detail, and return a fleet cycle plan, but it must not patch any selected target
skill in the same pass.

This holds even when the operator says `proceed all` or `-improve all skills
proceed` without a previously accepted fleet plan. Treat that as approval to
complete the planning pass, not approval to edit the fleet.

The first pass should return:

1. current Skill Control health;
2. the full ranked list of mapped skill diagnoses inline;
3. one recommended first cycle target or a stop/no-op verdict;
4. evidence source for the recommendation;
5. patch boundary for the next pass;
6. exact approval phrase for the first target cycle.

Do not collapse the first pass to only top targets. The top targets can be
summarized above the table, but the complete ranked list must appear inline in
the chat response when Will asks for `-improve all skills`.

## Self-Bootstrap Rule

When improving `improve` itself:

1. Lock the target to `skills/improve/` unless the operator separately approves
   global routing docs.
2. Prefer a concise reference, trigger test, or output-contract repair before
   adding modes, scripts, or new skills.
3. Do not route self-improvement through `self-evolve` unless the evidence is a
   recurring future-behavior lesson.
4. Do not claim runtime availability from an on-disk edit; state the caveat.
5. After validation, use the upgraded protocol on one pilot skill before
   recommending fleet cadence.

## Cycle

| Step | Question | Output |
|---|---|---|
| 1. Bind | Which exact skill or route is being improved? | Target path, quality goal, do-not-change boundary |
| 2. Evidence | What proves the weakness exists? | Usage signals, audit result, trigger phrases, wiring, validator status |
| 3. Shape | What does the skill currently own? | Job, modes, references, scripts, owner route, validation |
| 4. Depth | Is the skill deep enough for its job? | Keep / Fix / Absorb / Split / Retire verdict |
| 5. Rank | What are the best bounded repairs? | Top 3 improvements and one recommendation |
| 6. Gate | Is the selected repair safe to write? | Approval phrase or no-write diagnosis |
| 7. Patch | What is the smallest useful change? | Local diff in the target skill only |
| 8. Validate | Did the skill and registry still pass? | Validator, registry, audit, or focused proof |
| 9. Integrate | Is it only on disk or workspace-integrated? | Integration status and runtime caveat |
| 10. Next | What is the next skill target, if any? | One next-best target or stop reason |

## Evidence-To-Learning Contract

Before recommending a material skill change, record the smallest useful
version of these fields:

| Field | Required question |
|---|---|
| Signal source | What observed behavior, feedback, failure, or outcome supports the need? |
| Permission / boundary | Is this source allowed for the current use, and what must not be retained or inferred? |
| Limitation / bias | Is the signal directional, selected, stale, incomplete, or unrepresentative? |
| Insight | What user job or friction does the signal suggest? |
| Hypothesis | What bounded behavior change should improve that job? |
| Cheapest test | What is the smallest reversible test that could disprove the hypothesis? |
| User outcome | What practical result should improve for Will or the downstream user? |
| Guardrail | What must not regress: safety, routing, latency, cost, clarity, or approval boundaries? |
| Observation | What happened after the test? |
| Learning | Keep, revise, roll back, or promote to `self-evolve` if recurring? |

Do not require a full research run for every improvement. Route to `research`
when the decision depends on current external facts, representative user
evidence, unresolved contradictions, or evidence collection that should become
durable authority. Route to `explore` when the known target is clear but the
option space is artificially narrow or materially different directions have
not been considered. Use `audit-check` to pressure-test direction before a
plan, and `quality-check` to verify implementation and guardrails afterward.

When a fresh Pattern Profile exists, let `adam-pattern` own compilation,
refresh, provenance, confidence, and staleness. Consume only a bounded
target-relevant slice. Drill into checkpoint evidence only when the slice is
insufficient or contradicted; refresh the corpus only when stale, explicitly
requested, or materially contradicted. Do not copy raw transcripts into an
improvement artifact.

### Minimum learning receipt

After a pilot or approved patch, return:

```text
Signal and limitation:
Hypothesis tested:
User outcome:
Guardrail:
Observed result:
Decision: keep / revise / roll back / promote recurring lesson
```

Structural validation alone is not outcome proof. If the result cannot yet be
observed, state the observation window or owner and do not claim the behavior
improved.

## Skill Evidence Checklist

Before recommending a skill patch, inspect:

- frontmatter trigger clarity and natural phrases;
- near-miss boundaries and adjacent skill ownership;
- mode router, inputs, outputs, and done conditions;
- references/scripts linked from `SKILL.md`;
- `skills/HUB_MAP.md` and `skills/SKILL_CALLING_FRAMEWORK.md` only when routing
  behavior is part of the weakness;
- `skills/SKILLS_INDEX.md` and `skills/skills_registry.json` visibility;
- local validator output and workspace skill-audit findings;
- runtime availability caveat.

## Fleet Selection

For `-improve all skills`, run the normal skill-target checklist across the
inventory before choosing a target. Use this ranking order:

1. active high-use hub or mode with weak trigger, mode, output, or validation
   logic;
2. confusing overlap cluster with unclear primary/fallback route;
3. operator-corrected or repeated routing friction;
4. skill with audit errors, warnings, broken references, or registry drift;
5. dormant/compatibility skill where the best diagnosis is retire, absorb, or
   leave dormant.

Return the full ranked list inline by default for `-improve all skills`.
Summarize the top 3 above the full list when useful. A clean health audit can
reduce urgency, but it must not collapse the fleet scan into "nothing to
improve."

## Fleet Scan Helper

Use `{baseDir}/scripts/scan_skill_opportunities.py` when available. It applies
deterministic versions of the normal skill-target checks to every registry skill:

- trigger clarity and natural phrase quality;
- near-miss and adjacent-route boundaries;
- mode shape, output contract, and validation path;
- progressive disclosure and reference/test support;
- audit findings and registry visibility;
- active/dormant status and hub/mode leverage.

The helper is evidence for planning, not automatic authority. Inspect the top
candidate's actual `SKILL.md` before recommending a patch cycle.

When used for an operator-facing `-improve all skills` response, run the helper
with a limit that includes every scanned skill or use the JSON output to render
the full list inline.

### Chartered Control Room scan

Use `{baseDir}/scripts/control_room_skill_scan.py` only for an explicitly chartered,
resumable scan of every canonical workspace skill. It adds programme evidence
without replacing the registry:

1. `collect-usage` streams recent Codex user messages only, removes injected
   control/delegation envelopes, deduplicates exact prompt copies, stores at
   most three short examples per skill, and discloses all coverage limits.
2. `baseline` freezes active-first registry order plus each `SKILL.md` hash.
3. `scan` refuses baseline drift, writes one audit-only record per skill, and
   emits a checkpoint after every ten active skills.
4. `verify` proves whether any frozen target skill changed after the baseline.

Counts from this helper are directional routing signals. They do not prove a
skill loaded, executed correctly, or was unused when absent. Generated
manifests, cursors, records, and checkpoints are report evidence only; never
treat them as a runtime registry, task database, or skill ownership authority.

## Patch Boundaries

Allowed after approval:

- target skill `SKILL.md`;
- target skill `references/`, `templates/`, or `scripts/` when already justified;
- generated registry/index files after skill-folder changes;
- workspace-control event/report updates when significant.

Stop and ask before:

- editing multiple unrelated skills in one cycle;
- changing root authority docs;
- changing runtime-loading assumptions;
- deleting skills or compatibility aliases;
- creating a new controller, proposal database, dashboard, or cron loop;
- external sends, credentials, payments, production mutation, or destructive
  writes.

## Output Add-On

For skill targets, append these lines to the normal `-improve diagnosis`:

```text
Skill protocol:
Depth verdict: Keep / Fix / Absorb / Split / Retire - ...
Fleet impact:
Fleet pass: planning-only / target-cycle
Patch boundary:
Validation:
Runtime caveat:
Next skill target:
```
