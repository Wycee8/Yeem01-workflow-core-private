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
| M1 - <named usable result> | <consumer can perform a job> | <decision/input or None now> | <observable use or quality proof> | <current/planned/blocked> |

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

Classify before keeping a row:
- **Milestone:** a remaining consumer-recognizable result, decision, verified
  result, or verified capability that closes one distinct finish-line
  criterion.
- **Step:** an action used to produce a milestone; keep research, drafting,
  editing, setup, implementation, migration, validation, and documentation in
  the current slice or `-plan full`.
- **Gate:** human or authority input; place it under `Need from Will`.
- **Proof:** evidence that closes the result; place it under `Accepted when`.

If two rows close the same finish-line criterion or can be accepted as one
consumer result without losing a real decision boundary, merge them.

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
7. Does every milestone close a distinct criterion that cannot merge into an
   adjacent result, with its steps, gate, and proof kept subordinate?
8. Is technical detail limited to `-plan full`, the current slice, or a safety need?
9. Is the stage/run owner known?
10. Are file paths or artifact targets named where technical detail is expanded?
11. Are acceptance criteria and validation testable?
12. Should this be a backlog item or just a local note?
13. Can the same canonical plan be updated without creating a progress copy?
