# Planning Templates

## Goal and Milestone Check

- Goal:
- Primary usable deliverable:
- Consumer and intended use:
- Minimum useful completed set:
- Representative finished example:
- Acceptance proof:
- Finish line:
- Milestone arc:
- Current position:
- On track: <Yes / At risk / Off track, with one reason>
- Need from Will: <one exact question or None>

These deliverable fields are the Deliverable Lock inside this check. If
material ambiguity remains, show two or three concrete interpretations with
sample deliverables when useful, recommend one, ask one exact question, and
stop before architecture, roadmap detail, or approval language. If alignment
is clear, name the authority source and continue without a redundant question.

## Milestone map

| Milestone deliverable | What it enables | Need from Will | Accepted when | State |
| --- | --- | --- | --- | --- |
| M1 - <named usable result> | <consumer can perform a job> | <decision/input or None> | <observable use or quality proof> | <planned/current/done/blocked> |

Use this map for `-plan all`. Keep it to the minimum-necessary 1-7 deliverable
milestones. A top-level row should normally be a usable deliverable, genuine
decision, verified result, or verified capability. Before keeping a row, answer
internally: `If this row disappeared, which exact finish-line acceptance
criterion would become impossible?` Merge, nest, or remove it when no exact
consequence exists. Keep completed history in `Current position` or proof, and
keep optional, deferred, later, parked, and speculative work outside the main
roadmap unless the operator explicitly requests a separate non-critical
appendix. Nest enablers, controls, and time markers; retain a real external
deadline as a constraint. Do not expand every implementation task unless the
operator requests `-plan full` or omission would make execution unsafe.

## Current focus

- Milestone outcome:
- Immediate deliverables:
- Need from Will:
- Exit evidence:
- Next action:

## Technical task template (`-plan full` or execution handoff)

- Title:
- Objective:
- Owner / lane:
- Files or paths:
- Dependencies / gate:
- Acceptance criteria:
- Validation gate and command mode:
- Canonical write target:

## Packet template

- Objective
- Evidence / why now
- Bottleneck
- Proposed next action
- Expected KPI movement
- Validation plan
- Lineage

## Planning checklist

1. Is the objective explicit?
2. Does the first screen lock the primary usable deliverable, consumer and use,
   minimum useful set, representative example, acceptance proof, finish line,
   milestone arc, current position, on-track state, and exact need from Will?
3. If material ambiguity exists, did the response ask once and stop before
   roadmap detail or approval?
4. If alignment is clear, is its authority source named without a redundant
   question?
5. Do 1-7 minimum-necessary deliverable milestones cover the complete required
   journey without completed, optional, deferred, or control-only padding?
6. For every row, can you name the exact finish-line acceptance criterion that
   becomes impossible if the row is removed?
7. Does every milestone name a usable result, human input, and acceptance
   proof rather than only a process, time box, enabler, or control?
8. Is technical detail limited to `-plan full`, the current slice, or a safety need?
9. Is the stage/run owner known?
10. Are file paths or artifact targets named where technical detail is expanded?
11. Are acceptance criteria and validation testable?
12. Should this be a backlog item or just a local note?
13. Can the same canonical plan be updated without creating a progress copy?
