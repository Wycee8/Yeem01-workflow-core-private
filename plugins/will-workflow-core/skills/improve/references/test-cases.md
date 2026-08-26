# Improve Test Cases

## 1. Skill Logic Improvement

Input: `-improve skill routing for research`

Expected: classify target as skill/routing, return top 3 improvements, route to
Skill Control Layer / `yeem-skill`, and call `self-evolve` only when repeated
lesson evidence or future behavior change is the real target. Avoid creating a
new skill unless evidence supports it.

## 2. Proceed Recommended Option

Input: `-improve proceed`

Expected: execute the previously recommended plan only when its complete scope
is visible and explicitly approved. If only a diagnosis or recommendation is
visible, show the complete plan and stop for discussion or approval.

## 3. Explicit Option Override

Input: `-improve proceed option 2`

Expected: execute option 2 only when its complete plan is visible, explicitly
approved, local, safe, scoped, and has enough evidence. Otherwise show or revise
the plan and stop for approval or missing context.

## 3A. Audit And Plan First

Input: `-improve the imagen skill -discuss and plan all`

Expected: show the improvement audit and complete goal journey as milestones,
including key deliverables, human input, exit evidence, state, exclusions,
discussion points, and an exact approval phrase. Keep affected paths, command
modes, detailed validators, and rollback steps under `-plan full` or a later
execution handoff. Make no edits until Will approves that visible plan.

## 4. Design Improvement Near Miss

Input: `make this Figma output better`

Expected: route to `design - figma`; use `improve` only as a thin ranking lens
if the operator requested options.

## 5. QA Near Miss

Input: `-qa is this implemented correctly?`

Expected: route to `quality-check`; do not use `improve` because the work is
already built and needs a done-state verdict.

## 6. Auto Improvement

Input: `keep improving this toward the goal while I am away`

Expected: route to `adam-auto-loop` improve mode with goal, scope, tick budget,
hard stops, and return packet.

## 7. User-Value Gate

Input: `improve this by creating a new workspace system`

Expected: apply `user-skill` before durable creation; likely recommend reduce,
absorb, or a smaller reversible slice.

## 8. Evidence-First Skill Refinement

Input: `refine the -improve skill; check current usage, map current shape,
audit user-flow, audit efficiency, audit bloat, then ask or plan`

Expected: classify target as skill/routing behavior. Before recommending a
patch, check current usage signals, trigger phrases, scoped transcript evidence
when available, interaction patterns, hub/calling-framework wiring,
registry/index visibility, near-miss collisions, and runtime caveats. Map the
current skill shape, then return user-first, efficiency, and anti-bloat
findings. Recommend a lean docs/reference/test patch rather than a new skill,
controller, or broad hub rewrite.

## 9. User-Flow Misalignment

Input: `-improve this viewer because it is not usable`

Expected: audit the user's natural decision flow before visual polish. Check
whether the surface answers what this is, where we are, where we are going, how
we get there, what to watch, and what should happen next. Route implementation
to the owning design/workspace surface skill only after ranking options.

## 10. Efficiency And Bloat

Input: `-improve this workflow; it feels slow and overbuilt`

Expected: inspect current shape and usage first. Separate efficiency findings
from bloat findings. Prefer delete, absorb, merge, shrink, or reference-only
repairs before new files, skills, dependencies, dashboards, or runtime modes.

## 11. Self-Bootstrap

Input: `-improve the improve skill`

Expected: load the skill-improvement protocol, lock the patch boundary to
`skills/improve/`, rank bounded improvements, and prefer a lean reference,
trigger-test, or output-contract repair. Do not recursively route to
`self-evolve`, create a new meta-skill, or edit global routing docs unless the
operator separately approves that scope.

## 12. Fleet Improvement

Input: `-improve all skills`

Expected: run a planning-only fleet pass. Use Skill Control evidence to select
the skill inventory, run the normal skill-target diagnosis checks across each
skill, aggregate and rank opportunities, and return top recommendations. Do not
patch target skills during the first fleet pass.

## 13. Fleet Proceed

Input: `-improve all skills proceed` with no accepted fleet plan

Expected: treat `proceed` as approval to complete the planning-only fleet pass.
Do not patch target skills. Return the recommended first target cycle, patch
boundary, validation path, and exact approval phrase.

## 14. Fleet Target Cycle

Input: `-improve all skills proceed` after an accepted fleet plan names one
target

Expected: execute only the recommended bounded target when local, safe,
approved, and validated. Stop before broad multi-skill edits, runtime-loading
changes, destructive cleanup, or new controller/dashboard/cron creation.

## 15. Empty Health Queue Still Scans

Input: `-improve all skills` when Skill Control has zero audit warnings and an
empty priority queue

Expected: still run the opportunity scan across skills. Treat the clean audit as
"no urgent repair," not "nothing to improve." Return meaningful ranked
opportunities from qualitative skill-target checks, or explain why all
candidates fall below the threshold.

## 16. Generic Improve Does Not Seize Skill Ownership

Input: `-improve this Figma board; the layout is slow to review`

Expected: keep the target with the design/Figma owner and use `improve` only as
the audit-and-plan lens. Do not route the project task to the persistent
workspace skill-maintenance session unless the operator explicitly asks to
change a skill.

## 17. Explicit Skill Maintenance

Input: `-improve skill imagen based on the last 30 days`

Expected: bind the canonical `imagen` skill, route the maintenance cycle to the
persistent workspace skill owner, disclose usage-evidence limits, return the
bounded plan, and stop before mutation until approved.

## 18. Chartered Control Room Fleet Scan

Input: `scan every workspace skill with a frozen baseline, 30-day evidence,
checkpoints every ten, and no target writes`

Expected: use `control_room_skill_scan.py` to produce one record for every
canonical non-alias registry entry, active skills first, with a manifest,
cursor, bounded usage index, checkpoint files, and final hash verification.
Absence of a usage match remains unknown rather than unused.

## Conditional charter preflight

Input: `-improve this project workflow` with a resolvable project charter.

Expected: resolve by index/registry, read the project brief first, load the
charter only as needed, report charter alignment, then run normal improvement
passes.

Input: `-improve this standalone paragraph` with no project context.

Expected: skip charter discovery and keep the diagnosis lightweight.

Input: `-improve this project` where charter text conflicts with a root ADR.

Expected: classify `conflict`, follow the ADR, recommend a narrow charter
refresh, and do not infer execution approval.
