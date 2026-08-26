---
name: improve
description: Default front-door audit-and-plan skillhub for improving an artifact, workflow, skill, design, plan, code slice, marketing asset, or workspace surface. Use when the operator invokes -improve, asks to make something better, asks for top improvement options, says improve then proceed, explicitly targets a workspace skill or the skill fleet, or uses -self evolve as a broad improvement request; keep generic improvement local to the named artifact or workflow, route explicit skill maintenance through the workspace skill owner, always show the audit and complete plan before edits, and use self-evolve only for recurring lessons or future behavior change.
---

# Improve

## Job
Audit how to make a selected target better, rank the best improvement options,
show the complete plan for discussion and approval, then route approved
execution and QA to the correct existing owner.

`improve` is the default operator-facing front door for "make this better"
requests. It is still a thin hub: it does not replace `design`,
`quality-check`, `self-evolve`, `adam-auto-loop`,
`workspace-project-management`, or domain skills.

Use `self-evolve` as a backend specialist only when the improvement target is a
recurring lesson, transcript-backed friction pattern, or future skill/workflow
behavior change. Do not ask the operator to choose `self-evolve` when a normal
`-improve` diagnosis can classify and route the work.

## Call syntax
- `-improve` - audit the target, show the complete improvement plan, and open
  discussion. Do not execute in the first pass.
- `-improve proceed` - execute the approved recommended plan. If no approved
  plan is visible, show the audit and complete plan, then stop at approval.
- `-improve proceed option 2` - execute option 2 only when its complete plan was
  shown and explicitly approved; otherwise revise and show the plan first.
- `-improve -ask` - ask one scoped question first when the target or quality
  bar changes the ranking.
- `-improve -auto` - route to `adam-auto-loop` improve mode for governed
  repeated ticks.
- `-improve current skills` - improve the small set of skills materially used
  by the current request or current-chat lane, not the whole fleet. Bind the
  target list from the current route, recent tool/skill usage, and visible
  friction, then show one connected audit and complete plan. Patch only the
  approved connected skills in a later execution pass.
- `-improve skill <name>` - bind explicitly to the named workspace skill and
  route maintenance through the persistent workspace skill owner. A generic
  `-improve` modifier on a project, design, report, or workflow does not by
  itself transfer ownership to the workspace skill lane.
- `-improve all skills` - run the normal skill-target diagnosis across every
  skill, then rank the resulting improvement opportunities. The first pass is
  planning-only and must not patch target skills. Always show the full ranked
  list inline in chat, not only the top targets.
- `-self evolve ...` as an improvement request - normalize through this hub
  first, then call `self-evolve` only for recurring lessons or future-behavior
  learning reports.

## Core rule
Default to audit, complete planning, and discussion before execution.

Run the evidence-first improvement passes before ranking:

```text
target bind -> project/charter alignment when applicable -> usage audit -> current shape map -> user-first audit ->
efficiency audit -> bloat audit -> rank -> complete plan -> discuss/approve -> execute -> QA
```

The first pass must return the improvement audit, top 3 ranked improvements,
one recommendation, and the complete implementation plan inline. The plan must
name phases, affected surfaces, risks, validation, rollback, exclusions, and
the exact approval gate. Keep the turn open for discussion or revision. Do not
change files, durable state, external systems, production surfaces,
credentials, payments, or client-facing artifacts until that displayed plan is
explicitly approved and the selected option is safe for the current lane.

When the target is `improve` itself, another skill, skill routing, or all
skills, load `references/skill-improvement-protocol.md` before recommending
patches. For `-improve all skills`, the first pass is planning-only even when
the operator says proceed: run the normal skill-target diagnosis across the
skill inventory, aggregate and rank the opportunities, then return a cycle
plan. Patch only one bounded target in a later pass after the plan or target is
explicitly approved, then validate and propose the next cycle.

Read `references/improvement-passes.md` when the target is a skill, workflow,
workspace surface, recurring behavior, or any target where current usage,
user-flow, efficiency, or overbuild risk changes the recommendation.

## Mode router
| Mode | Use when | Do not use when | Output | Done when |
|---|---|---|---|---|
| `diagnose` | The operator asks to improve something without approving a displayed plan. | A complete visible plan is already explicitly approved. | Improvement audit, top 3 improvements, recommendation, complete phased plan, discussion points, and approval gate. | The audit and complete plan are visible and execution is paused for discussion or approval. |
| `proceed` | The operator explicitly approves a visible complete improvement plan and asks to apply it. | No complete plan is visible or the plan changed materially after approval. | Scoped execution routed to the owning specialist, followed by QA. | The approved plan is implemented and QA reports the outcome and guardrails. |
| `route` | The target type is clear and a specialist should own the next move. | The target or quality bar is too vague to choose a route. | Route decision and handoff notes. | The correct owner, boundary, and validation path are named. |
| `auto` | The operator wants repeated governed improvement toward a goal. | The request is a one-off local improvement. | `adam-auto-loop` improve preflight. | Goal, cadence/tick scope, hard stops, and return packet are defined. |
| `current-skill-pass` | The operator asks to improve "current skills", "these skills", or "the skills involved here". | The request says every/all skills, runtime loading, or unrelated skill fleet cleanup. | Current skill set, shared weakness, complete connected plan, validation, runtime caveat, and approval gate. | The connected audit and plan are approved, or the approved plan is implemented and QA-complete. |
| `skill-target` | The operator explicitly names a skill, skill routing, or workspace skill maintenance. | `-improve` is only modifying a project artifact or domain workflow. | Bound skill identity, usage/shape evidence, top 3, bounded plan, persistent-owner route, and approval gate. | The skill owner and patch boundary are explicit. |
| `fleet-plan` | The operator says `-improve all skills`, `all skills`, or asks for a first pass over the skill fleet. | A single target was already selected and approved from a prior fleet plan. | Skill health, mapped skill diagnoses, ranked opportunity candidates, one recommendation, cycle plan, and approval gate. | The next single target and no-write boundary are clear. |
| `control-room-fleet` | The operator charters a deep, resumable every-workspace-skill scan with an evidence window and checkpoints. | A normal fleet ranking or one target cycle is enough. | Frozen manifest, bounded usage index, one record per skill, checkpoint reports, collective report, and sequenced plan. | Every frozen skill is scanned exactly once, hashes verify, and target skills remain unchanged. |

## Boundaries
- Hub owns: target classification, ranking, recommendation, proceed semantics,
  approval boundaries, and specialist handoff.
- Specialist skills own: domain execution, validation details, and file
  contracts.
- Do not duplicate: `design` visual-quality workflow, `quality-check`
  post-build QA, `self-evolve` recurring lesson capture and proposal reports,
  `adam-auto-loop` governed repeated ticks, or `workspace-project-management`
  control truth.
- Approval gate: external send, destructive write, credential/payment change,
  production/client-facing mutation, runtime-loading authority change, broad
  multi-owner work, or missing target/evidence.

## Ranking criteria
Rank improvement options by:

1. User/operator value.
2. Leverage against the stated quality goal.
3. Reversibility.
4. Validation clarity.
5. Risk and approval burden.
6. Fit with existing skill ownership.

The recommended option is usually option 1, but may be option 2 or 3 when the
highest-value move is blocked, too risky, or needs missing evidence first.

## Proceed semantics
- Plain `-improve proceed` executes the recommended plan only when that complete
  plan is visible and explicitly approved.
- Without an approved visible plan, `-improve proceed` completes the audit and
  plan, opens discussion, and stops before writes.
- `proceed option 2` overrides the recommendation only when option 2's complete
  plan is visible, explicitly approved, local, safe, and sufficiently scoped.
- If discussion changes target, scope, files, risk, or validation materially,
  show the revised complete plan and obtain fresh approval.
- If the recommended option is gated, ask for the exact approval phrase instead
  of silently executing another option.
- If no prior diagnosis is visible, run `diagnose` first.

## Minimum workflow
1. Identify the target, target type, quality goal, and current weakness.
2. Run the conditional project-charter preflight below when the target belongs
   to a project or may change persistent project behavior.
3. Check current usage of the target. Use target-specific evidence: for skills,
   inspect recent usages when available, trigger phrases, transcripts when
   scoped, interaction patterns, routing/wiring, registry/index visibility,
   near-miss collisions, and runtime caveats.
   When a fresh compact operator Pattern Profile exists, query only the
   target-relevant slice through `adam-pattern`; open checkpoint evidence or
   transcripts only when the slice is insufficient, stale, or contradicted.
   Treat transcript-derived counts as directional evidence. Exclude injected
   context and delegation envelopes, disclose deduplication/coverage limits,
   and never interpret no match as proof that a skill is unused.
4. Map the current shape: purpose, owner, modes, inputs, outputs, dependencies,
   routes, validation path, and known gaps.
5. Audit user-flow and user value. Check Will/operator value first, then
   downstream user value when relevant. Flag misalignment when the target
   optimizes internal structure before useful user outcomes.
6. Audit efficiency: duplicated work, avoidable context load, weak validation,
   missing deterministic helper, fragile handoff, or specialist-route mismatch.
7. Audit bloat: delete, absorb, merge, shrink, or reference-only before adding
   new files, modes, skills, surfaces, dependencies, or workflows.
8. Check `references/target-route-map.md` for the owning route.
9. For skill targets, check `references/skill-improvement-protocol.md` before
   any write recommendation, especially for self-improvement or fleet requests.
10. For `current-skill-pass`, identify the small connected skill set before
   writing: the hub/mode skill, the execution leaf, any adjacent handoff skill,
   and the validation path. Keep one shared weakness in scope, such as handoff
   truth, approval readiness, or DAM routing. Do not use this mode to patch
   unrelated skills, generated registries, runtime loading, or retired aliases.
11. For `-improve all skills`, run `fleet-plan` first. This first pass may
   refresh/read Skill Control evidence and use
   `{baseDir}/scripts/scan_skill_opportunities.py`, but it must not patch
   target skills.
   The response must include the full ranked list inline. Use compact columns
   if needed, but do not replace the full list with only top targets.
    When the operator charters a Control Room scan, use
    `{baseDir}/scripts/control_room_skill_scan.py`: collect bounded usage
    evidence, freeze
    the registry/path/hash baseline, scan in active-first registry order, emit
    one record per skill and a checkpoint after every ten active skills, then
    verify hashes. The generated report directory is programme evidence, not a
    second registry or runtime authority.
12. If intent or evidence would change the recommendation, ask one scoped
    question. Otherwise produce the audit, top 3 ranked improvements, and one
    recommendation.
13. Show the complete implementation plan inline: phases, owners or routes,
    affected surfaces, risks, validation, rollback, exclusions, and exact
    approval phrase. Name the evidence needed and do-not-change boundary.
14. Open discussion and stop before writes unless the visible plan is
    explicitly approved. Reissue a materially revised plan for fresh approval.
15. Route `self-evolve` only for recurring lessons, repeated routing friction,
    or future skill/workflow behavior change.
16. If proceeding, route to the owning specialist and execute only the safe,
    approved, local scope.
17. Validate with the specialist's validator, targeted checks, or proof, then
    return the minimum learning receipt when outcome evidence is available.
18. State runtime availability separately from on-disk skill integration.

## Conditional Project-Charter Preflight

Use this preflight when an owning project resolves and a project brief or
charter exists, or when the proposed improvement may alter durable project
purpose, scope, authority, architecture, UX/design law, persistent workflow, or
validation gates.

1. Resolve the project through its index or registry before deep browsing.
2. Read `PROJECT_BRIEF.md` first when available.
3. Read `PROJECT_CHARTER.md` when the brief is insufficient or the proposed
   change may affect durable project direction or constraints.
4. Read companion files only when the conflict concerns their owned detail.
5. Classify alignment as `aligned`, `stale`, `conflict`, or `charter_missing`.
6. If charter text conflicts with higher authority, name the conflict and route
   a narrow charter refresh through `project-charter-docs`; do not treat the
   charter as execution or approval authority.

Skip the preflight for isolated non-project artifacts, generic advice, or
targets with no persistent project context. Do not invent a charter merely to
complete an improvement diagnosis.

For `-improve cleanup`, `make cleanup easier`, cleanup-session friction, or
cleanup-lane manageability, diagnose here and route the bounded implementation
to `proceed-all-cleanup`. Prefer its read-only cleanup control packet over a new
dashboard, queue, skill, state store, or recurring loop.

## Output
```text
-improve diagnosis
Target:
Target type:
Quality goal:
Current weakness:
Charter alignment: aligned / stale / conflict / charter_missing / not_applicable
Current usage:
Current shape:
User-first:
Efficiency:
Anti-bloat:
Top 3 improvements:
1. ...
2. ...
3. ...
Recommendation:
Evidence needed:
Do not change:
Complete plan:
- Phase:
- Affected surfaces:
- Risk and rollback:
- Validation:
- Exclusions:
Discussion points:
Approval gate:
```

## Fleet Output Contract

For `-improve all skills`, return:

- scan mode and skill count;
- full ranked list inline, including every scanned skill;
- columns: rank, skill, score, verdict, recommendation;
- top recommendation and approval gate;
- no-write boundary for the first fleet pass.

For a chartered Control Room fleet scan, also return manifest/cursor paths,
checkpoint paths, evidence limitations, drift-verification result, and a
collective implementation sequence. The fleet scan may write report artifacts
but must not edit the scanned target skills.

If dormant or compatibility skills are included, label them in the list or use
the scanner's status column. Do not hide dormant rows when Will asks for every
skill.

## Resources
- `references/target-route-map.md` - target type to owner route.
- `references/skill-improvement-protocol.md` - safe protocol for improving
  `improve`, one skill, or the skill fleet one bounded target at a time.
- `references/improvement-passes.md` - evidence-first usage, shape,
  user-first, efficiency, and bloat passes by target type.
- `references/trigger-tests.md` - representative trigger and near-miss cases.
- `references/test-cases.md` - behavior examples for diagnosis and proceed.
- `{baseDir}/scripts/scan_skill_opportunities.py` - deterministic helper for applying
  skill-target diagnosis checks across the skill inventory and ranking
  planning-only opportunities.
- `{baseDir}/scripts/control_room_skill_scan.py` - resumable audit-only programme helper
  for a frozen workspace-skill inventory, bounded recent-usage evidence,
  per-skill records, ten-active-skill checkpoints, and hash verification.
- `../adam-pattern/references/pattern-profile.md` - bounded observed-pattern
  evidence retrieval for target-specific improvement diagnosis.
