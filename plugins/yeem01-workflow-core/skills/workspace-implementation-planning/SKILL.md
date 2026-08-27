---
name: workspace-implementation-planning
description: Turn approved intent into workspace plans. Use for -plan (the current actionable slice), -plan all (the complete minimum-necessary 1-7 milestone journey), -plan full or full -plan (milestones plus bounded tasks, paths, dependencies, gates, and validators), durable backlog normalization, or execution handoffs.
---

# Workspace Implementation Planning

Use this skill to convert approved intent into executable work.

For every `-plan`, `-plan all`, `-plan full`, or `full -plan` request, load
`artifact-lane-output-defaults` before the final response. The planning skill
owns plan substance; the artifact contract owns the operator-facing shape,
decision visibility, and required inline `**-summary**`.

Explicit legacy `$build-handoff` is compatibility intent for this public
owner's Handoff Packet mode. Do not direct-load the private retired
compatibility record `build-handoff`.

## Goal

Produce a plan that Will can understand and steer at milestone level, while a
fresh worker or future session can open the same canonical plan and execute the
current slice without guessing.

A good plan in this workspace should:
- map to the active run, stage, or workspace objective
- confirm the governing goal, usable deliverable, consumer and intended use,
  minimum useful completed set, representative finished example, acceptance
  proof, finish line, milestone arc, and current position before exposing
  implementation detail or requesting approval
- separate the complete goal journey from technical execution depth
- make the current milestone, human input, exit evidence, and next action clear
- produce canonical backlog items or build packets
- define exact file paths where possible
- include acceptance criteria and validation
- draft the concrete plan before substantive audit, then revise it before
  presenting the approval target
- show a separate critical path only when milestone order does not explain the
  dependencies or gates
- avoid hidden assumptions

## Mode Router

| Mode | Use when | Output | Stop condition |
| --- | --- | --- | --- |
| Current slice (`-plan`) | Small approved task or active milestone | Current outcome, immediate deliverables, human input, exit proof, next action | Stop at ready-to-execute slice |
| Milestone roadmap (`-plan all`) | The operator needs the complete goal journey | Goal and Milestone Check, then the minimum-necessary 1-7 audited deliverable milestones when alignment is clear | Stop at one exact alignment question or before execution |
| Full execution plan (`-plan full`) | A worker needs exact implementation detail | Milestone roadmap plus tasks, paths, dependencies, command modes, and validators | Stop before execution unless approved |
| Critical-path view | Milestone order cannot explain blockers, gates, or parallel lanes | Ordered unlocking chain plus parallel/later work | Stop at gate or next executable lane |
| Backlog-normalized plan | Work should become durable shared tasks | Pre-plan audit verdict, canonical backlog item seeds, validation | Stop before writing backlog unless authorized |
| Handoff packet | A fresh session or subagent needs context | Objective, scope, files, gates, pre-plan audit verdict, validation, next action | Stop at handoff-ready packet |

Handoff Packet mode owns generic next-worker or next-session execution
handoffs. Keep creative or asset handoffs with `creative-workflow`, closure
handoffs with `close-run` / `session-wrap-up`, and canonical approval packets
with `approval-packet-builder`.

## Planning workflow

1. Identify the governing objective.
   - operator request
   - approved design
   - packet objective
   - backlog item

2. Identify workspace authority.
   - active run / stage
   - canonical work items in `workspace_control/work_items/WORK_ITEMS.json`
   - project/run registries and selected run manifests under `client_cases/`
   - relevant contracts or module docs

3. Run only a minimal necessity and authority gate before drafting.
   - Stop only for a missing target, wrong authority, unsafe ambiguity, obvious
     no-op, or a hard gate that prevents even local planning.
   - Do not present this gate as the substantive plan audit.

4. Run charter preflight.
   - Does this plan need durable purpose, scope, non-goals, approval gates, decisions, success criteria, or a read-order pointer?
   - Would another session, stage, or reviewer lose important context without a charter?
   - If yes, use `project-charter-docs` to create or refresh only the necessary charter context before or alongside the plan.
   - If no, keep assumptions and constraints inside the plan without creating a separate charter artifact.

5. Run the Goal and Milestone Check before decomposing work.
   - Goal: what Will ultimately wants to become true.
   - Primary usable deliverable: the named result or result set that completes
     the request; it may be an asset, decision, report, dataset, or verified
     capability.
   - Consumer and intended use: who will use it and for what job.
   - Minimum useful completed set: the smallest set that is still useful, not
     merely structurally present.
   - Representative finished example: one concrete example of the expected
     granularity and quality.
   - Acceptance proof: the observable use or quality evidence that proves the
     deliverable works for the consumer.
   - Finish line: the usable and verifiable completed result.
   - Milestone arc: the 1-7 outcomes strictly necessary to reach the finish
     line, in one line.
   - Current position: where the project is now.
   - On track: `Yes`, `At risk`, or `Off track`, with one plain-language reason.
   - Need from Will: one exact question or `None`.

   Compare these fields against the operator request and current project,
   charter, plan, run, or work-item authority. Classify the relationship as
   aligned, drifted, conflicting, or missing. Verify that every proposed
   milestone is required by the finish line, the current milestone unlocks the
   next outcome, and no technical-control milestone exists without an
   operator-visible result. For every candidate row ask: **If this row
   disappeared, which exact finish-line acceptance criterion would become
   impossible?** If no exact criterion can be named, merge, nest, or remove
   the row.

   Treat these fields as one **Deliverable Lock** inside the existing Goal and
   Milestone Check, not as a new planning layer. If uncertainty changes the
   goal, primary usable deliverable, consumer or intended use, minimum useful
   set, representative example, acceptance proof, finish line, milestone arc,
   current milestone, owner, authority, material cost, or approval boundary,
   show two or three concrete interpretations when useful, recommend one, ask
   one exact question at the earliest affected milestone, and stop before
   architecture, roadmap detail, or approval language. If the authority is
   clear, state the alignment source and continue without a redundant
   question. This is a working planning lock; do not mutate a canonical plan
   unless capture or update was requested.

   For a combined sequence such as `-audit then -plan all`, the completed
   Direction Audit may appear first. Once the `Plan All` section begins, its
   first content must be `**Goal and Milestone Check**`; do not place the plan
   identity, revision, status, owner, canonical path, proof, or approval
   metadata between the section heading and that check.

   Then apply the lean-change check.
   - What assumption is being made?
   - Is there more than one plausible interpretation?
   - What is the primary usable deliverable, consumer and intended use,
     minimum useful completed set, coverage universe, representative finished
     example, and acceptance proof?
   - What is the smallest reversible slice?
   - Which files or state paths are intentionally in scope?
   - What validation will prove success?

   Treat competing interpretations as material when choosing between them
   would change the primary usable deliverable, output granularity, coverage,
   evidence plan, completion proof, milestone path, or material cost. For
   `-plan all -ask`, always make the deliverable interpretation visible inside
   the Goal and Milestone Check: state the locked interpretation when the
   request is already explicit, or show two to three concrete interpretations
   with one sample output each, recommend one, and ask one exact question. This
   preserves the Deliverable Interpretation Check contract without adding a
   second user-facing planning layer. Do not ask when the answer is already
   explicit; record the contract and continue.

6. Draft the complete concrete plan before substantive criticism. Begin with
   the complete minimum-necessary milestone journey and use 1-7 deliverable
   milestones. `All` means every outcome required to reach the accepted finish
   line, not every known phase, past activity, backlog item, future idea, or
   possible improvement. For each milestone define:
   - milestone deliverable: the named usable result, genuine decision,
     verified result, or verified capability;
   - what it enables for the named consumer;
   - human input or decision, or `None now`;
   - acceptance evidence;
   - state.

   Apply the **Utility Gate** to every candidate row before it enters the
   roadmap:
   - name the consumer-recognizable result and the use it unlocks;
   - name the exact finish-line acceptance criterion that would become
     impossible if the row were removed;
   - keep the row only when that consequence is concrete and unique enough not
     to merge into another milestone;
   - move completed history into `Current position` or proof, not the active
     completion path;
   - omit optional, deferred, later, parked, or speculative work from the main
     roadmap unless the operator explicitly asks to see it, then show it in a
     separate non-critical appendix;
   - treat authority packs, schemas, validators, audits, research, setup,
     freezes, backups, and other controls as subordinate enablers unless
     governance or recovery is itself the requested consumer result.

   Apply the **Milestone-versus-step classification** before keeping a row:
   - a **milestone** is a remaining consumer-recognizable result, genuine
     decision, verified result, or verified capability that closes one
     distinct finish-line acceptance criterion;
   - a **step** is an action that produces a milestone, such as research,
     drafting, editing, implementation, setup, migration, validation, or
     documentation;
   - a **gate** is human or authority input that unlocks a milestone; show it
     under `Need from Will`, not as a separate roadmap row;
   - **proof** is the observable evidence that closes a milestone; show it
     under `Accepted when`, not as a separate roadmap row.

   Classify milestone candidates internally as `usable_deliverable`,
   `decision`, `verified_result`, `verified_capability`, `enabler`, `control`,
   or `time_marker`. Top-level milestones normally use the first four classes.
   For each retained row, name its distinct finish-line criterion and run a
   merge test: if an adjacent row closes the same criterion, or both can be
   accepted as one consumer result without losing a real decision boundary,
   merge them. Nest, merge, or remove steps, enablers, controls, proofs, gates,
   and time markers unless the operator explicitly requested one as the
   deliverable. Treat time as a constraint or sequencing input, not the
   default completion unit; retain a real external deadline when it materially
   defines acceptance.

   After drafting the milestone map, scan it for unresolved human decisions.
   Ask only when a decision would change scope, authority, ownership, primary
   deliverable, output unit, coverage universe, side effects, material cost,
   success evidence, or which milestone can advance. Name the exact
   decision at the milestone it unlocks and use the inline decision gate from
   `artifact-lane-output-defaults`. When no such decision exists, record `None
   now` and continue; do not ask a generic "are there any decisions?" question
   or stop current work for a later non-blocking preference.

   Keep `Need from Will` consistent with the later decision gate. If a current
   approval or choice is required before the displayed next milestone can
   advance, name that exact decision in the Goal and Milestone Check. Use
   `None` only when no current operator input or decision is required; do not
   report `None` and then request approval later in the same plan.

7. Apply the requested level of detail.
   - `-plan`: expand only the current actionable slice.
   - `-plan all`: show the complete required path only; do not expand every
     task, completed phase, optional idea, or deferred lane by default.
   - `-plan full`: expand the milestones into bounded technical tasks.

8. When technical detail is required, break the work into small bounded tasks.
   Prefer tasks that:
   - can be verified independently
   - have one clear owner
   - affect a narrow file set
   - avoid mixing discovery and execution in one step

9. Mark a separate critical path only when milestone order leaves the unlocking
   sequence ambiguous because of cross-owner dependencies, blockers, gates,
   parallel lanes, or multiple plausible execution orders. The critical path
   is not every task in the plan.

10. For each expanded technical task, define:
   - title
   - scope
   - exact or likely file paths
   - dependencies
   - acceptance criteria
   - validation gate
   - for any approval packet, the coupled before-state validators and their
     command modes
   - whether it should become a backlog item, packet, or immediate action

   Use the existing packet-readiness vocabulary:

   - validator phase: `before_state_required`, `expected_before_failure`,
     `after_state_required`, or `observation_only`;
   - command mode: `read_only`, `write_requires_claim`, or
     `isolation_required`.

   A packet may become decision-ready only after all coupled before-state
   validators pass or one exact expected-before failure is recorded. Matching
   hashes without semantic proof are insufficient.

11. Audit the concrete draft. Pressure-test assumptions, evidence, feasibility,
    dependencies, user value, gates, anti-bloat, and the strongest alternative.
    For `-plan all`, re-run the Utility Gate: reduce, merge, nest, or remove
    weak milestones and compress lane-level findings into the affected
    milestone or the audit delta. A shorter complete plan is better than a
    padded plan; one or two milestones are valid when they are sufficient.

12. Revise the draft. Apply every material audit finding or record why it was
    rejected. Present only the revised plan as the approval target and show a
    compact audit delta.

13. Decide output form.
   Use one of:
   - canonical backlog item(s)
   - build packet
   - stage-local plan artifact
   - compact execution checklist

## Workspace planning rules

- Do not create a second task system outside `workspace_control/work_items/WORK_ITEMS.json`, project/run registries, or stage-owned run manifests.
- Treat `.autonomy/` as legacy support evidence during retirement, not as the default authority for new planning or task claims.
- If the concrete-draft audit verdict is `reduce-scope`, `merge`, `research-first`,
  `no-op`, or `blocked`, do not inflate it into a full implementation plan by
  default. Return the verdict, validation-before-planning, and the smallest next
  action unless the operator explicitly asks to plan anyway.
- `-plan` controls charter lifecycle: use `project-charter-docs` only when charter preflight shows that the plan needs long-lived project context. Otherwise keep assumptions inside the plan.
- For `-plan all`, draft and audit the complete minimum-necessary milestone
  journey first. Show all required outcomes, not all implementation tasks,
  completed history, optional improvements, or deferred work. Use `-plan full`
  for the task expansion.
- Lock the usable deliverable before database, system, schema, integration, or
  other architecture planning. Architecture is an enabler unless the operator
  explicitly asks for architecture itself as the completed deliverable.
- A deliverable is not limited to a physical asset. A decision, research
  report, populated dataset, or verified operational capability is valid when
  a named consumer can use it and its acceptance proof is explicit.
- Do not use elapsed weeks, phases, workshops, audits, schemas, validators, or
  setup work as top-level completion milestones when the actual result is a
  website, campaign asset set, report, dataset, decision, or verified
  capability.
- Do not keep a top-level roadmap row merely because work exists, was already
  completed, needs control, or might be useful later. The main roadmap is the
  active required completion path. Put completed evidence in `Current
  position`; omit optional/deferred/later work unless explicitly requested.
- Keep one canonical persistent plan. Record `Plan ID`, `Revision`, `Status`,
  `Goal`, `Current milestone`, `Last meaningful update`, and `Supersedes`.
  Update the plan in place; do not create a new dated/versioned copy merely to
  record progress.
- Keep stable goal and milestone outcomes separate from volatile current-focus,
  evidence, and state fields so long-context continuation does not require
  rewriting the whole plan.
- Do not request approval for a plan ID or revision that is absent from both
  the displayed target and the canonical plan. A proposed revision must be
  visibly labelled as proposed, show the milestone-level target being decided,
  and state whether approval would create, replace, or merely execute it.
  Otherwise repair the identity or ask the exact alignment question first.
- If the plan creates durable shared work, normalize it into canonical backlog items.
- Keep stage-owned outputs in the active run.
- Prefer explicit validation over vague success language.
- Run coupled validators before presenting a gated packet and repeat them
  immediately before mutation. Never defer the first clean-baseline check until
  after source edits.
- Inspect command behavior before using `--help`, `--check`, `--json`, or an
  unflagged invocation as a read-only preflight. Write-capable commands require
  exact claims; uncertain commands require isolation.
- Separate candidate ideas from committed tasks.
- Do not add speculative flexibility, abstractions, or adjacent cleanup unless the governing objective requires it.
- If ambiguity affects scope, owner, approval boundary, primary usable deliverable,
  minimum output unit, coverage universe, material cost, or success criteria,
  ask or mark an exact blocker instead of silently choosing.
- Do not confuse a valid abstraction with the requested deliverable. A
  framework, taxonomy, or schema does not complete a request for a populated
  database, inventory, action map, or other record-level artifact.

## Good plan qualities

A strong plan is:
- small enough to execute safely
- specific enough to verify
- aligned to a real stage/run owner
- understandable from the Goal and Milestone Check and milestone map before technical detail
- deliverable-first: the named consumer can recognize what they will receive
  and how it will be accepted before reading architecture or controls
- clear about the critical path when milestone order is insufficient
- clear about what proof will count as done

## Output Contract

When planning, preserve the following facts. The list is a completeness
checklist, not a requirement for one line or section per field: combine related
facts, omit inapplicable technical detail, and do not restate the same sequence
in the check, roadmap, critical path, and summary.
- for `-plan all` and `-plan full`, a first section named
  `**Goal and Milestone Check**` containing Goal, Primary usable deliverable,
  Consumer and intended use, Minimum useful completed set, Representative
  finished example, Acceptance proof, Finish line, Milestone arc, Current
  position, On track, and Need from Will
- for combined Audit then Plan All, the audit may precede the plan, but the
  Plan All section starts immediately with that Goal and Milestone Check
- minimal necessity/authority gate
- concrete-draft audit verdict and compact audit delta
- assumptions
- when material ambiguity exists, alternatives, sample outputs, a
  recommendation, and one exact question inside the Goal and Milestone Check;
  for `-plan all -ask`, expose the deliverable interpretation there even when
  it confirms an explicit interpretation and requires no decision
- scope boundary / intentionally excluded work
- a milestone map for `-plan all` and `-plan full`
- current focus, next action, and required human input
- a technical task list and validation per task only for `-plan full`, an
  execution handoff, or when omission would be unsafe
- a separate critical path only when dependencies, blockers, gates, or
  parallel lanes are not clear from milestone order
- recommended canonical write target

For `-plan all` and `-plan full`, include this milestone chart:

| Milestone deliverable | What it enables | Need from Will | Accepted when | State |
| --- | --- | --- | --- | --- |

For `-plan full`, follow it with:

| Phase / Task | Deliverable | Owner / Surface | Dependency / Gate | Validation | Next Action |
| --- | --- | --- | --- | --- | --- |

Use a separate critical-path table only when the milestone map cannot express
the unlocking chain. Keep parallel or later work out of that chain.

## Validation

Before returning the plan, check:

- the governing objective and workspace authority are named;
- `-plan all` and `-plan full` start with
  `**Goal and Milestone Check**`;
- the Deliverable Lock names the primary usable deliverable, consumer and use,
  minimum useful set, representative example, and acceptance proof before
  architecture or roadmap detail;
- the Goal and Milestone Check appears before roadmap detail, technical proof,
  plan identifiers, or approval language;
- a combined Audit then Plan All response places no plan metadata between the
  Plan All heading and the Goal and Milestone Check;
- material alignment ambiguity stops the response after one exact question;
- clear alignment names its authority source and does not ask a redundant
  question;
- the plan distinguishes breadth (`all` milestones) from depth (`full`
  technical detail);
- the minimal necessity/authority gate is visible but not mislabeled as the
  substantive audit;
- the plan was drafted before the substantive audit;
- every material audit finding was applied or explicitly rejected;
- only the revised plan is presented as the approval target;
- every approval target has an identity visible in the displayed target or the
  canonical plan and states what approval would authorize;
- charter preflight was run and did not create unnecessary artifacts;
- scope boundary and exclusions are explicit;
- every top-level milestone has a named usable deliverable, genuine decision,
  verified result, or verified capability, plus human input, acceptance
  evidence, and state;
- every top-level milestone passes the Utility Gate with an exact acceptance
  consequence if removed; 1-2 milestones remain valid when they complete the
  finish line without padding;
- completed history is represented in `Current position` or proof, and
  optional/deferred/later work is absent from the main roadmap unless the
  operator explicitly requested that appendix;
- enablers, controls, and time markers are subordinate unless they are the
  explicit requested deliverable, and real deadlines remain constraints;
- each expanded technical task has acceptance criteria and validation;
- every gated execution task has current packet-readiness evidence and explicit
  command modes;
- critical path is shown only when milestone order is insufficient;
- persistent plan metadata and a short revision log support long-context
  continuation without copy proliferation;
- approval gates are visible and not bypassed.
- `-plan all` asks one exact route-changing decision when required, records
  `None now` when none exists, and never substitutes a generic decision query;
- `Need from Will` names the same current decision as any later approval gate
  and never reports `None` when that gate blocks the next milestone;
- `-plan all -ask` exposes the deliverable interpretation, and a material
  ambiguity is not resolved without concrete alternatives, sample outputs,
  a recommendation, and one exact question;
- the locked plan records the primary usable deliverable, consumer and use,
  minimum useful completed set, coverage universe, representative example,
  and acceptance proof whenever those fields determine usefulness;

## Trigger Tests

| Input | Expected mode | Expected output |
| --- | --- | --- |
| `-plan this approved fix` | Current slice | Current milestone, immediate deliverables, human input, exit evidence, next action |
| `-plan all` | Milestone roadmap | Show the Goal and Milestone Check first; when aligned, continue to the minimum-necessary 1-7 deliverable milestones without completed, optional, deferred, or control-only padding |
| `-plan all -ask map the main marketing functions and activities into a reusable database` | Milestone roadmap with material ambiguity | Inside the Goal and Milestone Check, show strategic capability map, populated action database, and layered-both interpretations with sample outputs; recommend one, ask which deliverable governs completion, and stop before research collection or roadmap detail |
| `-plan all the marketing work; deliver a website, social media plan, service offering sheet, and branding assets` | Milestone roadmap | Lock the asset set and intended use first; organize milestones by accepted assets, not weeks or database architecture |
| `-plan all the database architecture for our marketing intelligence` | Milestone roadmap with material ambiguity | Ask which usable deliverable and consumer job the architecture must enable, then stop before architecture detail |
| `-plan all a research report and reusable evidence dataset` | Milestone roadmap | Treat the report and dataset as valid nonphysical deliverables with named users and acceptance proof |
| `make a full implementation plan` | Full execution plan | Goal and Milestone Check, milestone roadmap, complete technical task chart, gates, and summary |
| `turn this into backlog items` | Backlog-normalized plan | Backlog seeds, no silent mutation |
| `handoff this to a subagent` | Handoff packet | Fresh-session execution packet |

Read `references/templates.md` for reusable task and packet planning templates.
