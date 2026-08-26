---
name: "artifact-lane-output-defaults"
description: "Operator-facing response defaults for -plan, -plan all, -plan full or full -plan, -charter, -audit, -qa/-QA, backlog, summaries, and decision gates. Use to keep current-slice, milestone-roadmap, full-execution-detail, proof, and approval visibility distinct."
---

# Artifact Lane Output Defaults

## Purpose
Make key planning, audit, QA, and approval artifacts immediately usable after
they are created, updated, moved, filed, emitted by a skill, or selected as the
active output.

This supersedes the narrower backlog/charter-only convention by wiring default output behavior into `-plan`, `-audit`, and `-qa` workflows too.

## Use When

Use this skill whenever an operator-facing artifact is created, updated,
selected, reviewed, emitted, or used as an approval target for `-charter`,
`-plan`, `-plan all`, `-audit`, `-qa`, `-QA`, backlog, handoff, proposal,
approval packet, or report work.

Do not use it to invent new artifact lanes, bypass owner skills, or replace the
actual planning, audit, QA, or backlog workflow. It defines response defaults
and approval visibility only.

## Mode Router

| Mode | Use when | Output | Stop condition |
| --- | --- | --- | --- |
| Summary footer | A charter, plan, audit, QA, report, proposal, or packet was created or reviewed | Inline `**-summary**` | Stop after exact next action |
| Summary review | Will explicitly asks for `-summary` or a concise review of a named/current subject | Resolve the subject, select one adaptive review mode, preserve decision-changing facts | Stop after one terminal next action, or one exact subject question when ambiguous |
| Decision gate | Will must approve, revise, defer, or choose | Decision target, preview, boundary, exact ask | Wait for decision |
| Plan slice | `-plan` or a tactical plan is produced | Current milestone, bounded next work, human input, proof | Stop at ready-to-execute slice |
| Milestone roadmap | `-plan all` asks for the complete goal journey | Goal and Milestone Check, then the minimum-necessary 1-7 deliverable milestones when aligned | Stop at one exact alignment question or before execution approval |
| Full execution plan | `-plan full`, `full -plan`, or exact implementation detail is requested | Milestone roadmap plus tasks, paths, dependencies, gates, and validators | Stop before execution approval |
| Critical path | Dependencies, blockers, gates, or parallel lanes make milestone order insufficient | Ordered unlocking chain and parallel/later lanes | Do not treat visibility as approval |
| Audit summary | `-audit` output is produced | Findings table, principle verdicts when required | Stop before implementation |
| QA verdict | `-qa` / `-QA` output is produced | Done-state verdict and proof | Stop if proof is missing |

## Trigger Principle
Trigger from artifact intent and destination, not only the literal phrase `add to`.

Run this procedure when the operator or a workflow asks to:

- add to
- move to
- file under
- convert into
- append to
- create from
- update
- refresh
- emit
- summarize
- promote
- review
- audit

any of these artifact lanes:

- `-backlog`
- `-charter`
- `-plan`
- `-plan all`
- `-plan full`
- `full -plan`
- `-audit`
- `-qa`
- `-QA`

## Output Contract

Every covered artifact turn must end with the chat-visible output that lets
Will decide without opening raw folders first:

- for `-plan all`, begin with a compact `**Goal and Milestone Check**` that
  locks the goal, primary usable deliverable, consumer and intended use,
  minimum useful completed set, representative finished example, acceptance
  proof, finish line, milestone arc, current position, on-track state, and one
  exact need from Will or `None`;
- an inline summary when the artifact lane requires it;
- a decision gate when approval, revision, defer, or choice is needed;
- a minimal necessity/authority gate, followed by the concrete-draft audit
  verdict and revision delta for `-plan`; lane-level audit deltas for `-plan all`;
- the current actionable slice for ordinary `-plan`;
- all deliverable milestones, but not every technical task, for `-plan all`;
- the milestone roadmap plus complete technical execution detail for `-plan
  full` or `full -plan`;
- a critical path only when dependencies, blockers, gates, or parallel lanes
  are not already obvious from milestone order;
- validation or proof appropriate to the lane;
- the exact next action or exact approval phrase.

## Human Meaning Gate

For every covered operator-facing response, make the first screen useful before
showing the control receipt. Except when Will explicitly requests a
receipt-only response, begin with the smallest complete plain-language meaning
layer, normally one to three semantic units, that answers:

1. What actually changed, was learned, or was decided?
2. Why does that matter to Will or the downstream user?
3. Is the result usable, blocked, or only technically validated?
4. What meaningful action or decision comes next?

One semantic unit is a sentence, bullet, row, or labelled line whose removal
would change understanding, action, readiness, risk, authority, or recovery.
This is the artifact lane's minimum-sufficient-answer rule.
Combine answers when one unit can carry them without ambiguity; do not produce
four sentences merely because four questions are listed. This meaning layer
must appear before raw scores, validator or test totals,
status codes, work-item IDs, hashes, file lists, or specialist acronyms. Preserve
those details as proof below the meaning layer when they help governance.

For `-plan all` and `-plan full`, the `**Goal and Milestone Check**` is the
Human Meaning Gate. Do not add a separate technical preamble before it. If
material alignment ambiguity remains, ask one exact question there and stop
before roadmap detail, control receipts, plan IDs, or approval language.

For a combined `-audit then -plan all` sequence, the Direction Audit may appear
first. Once the `Plan All` section begins, place
`**Goal and Milestone Check**` immediately after its heading. Plan identity,
revision, status, owners, source paths, proof, and approval metadata come only
after the check. If a later decision gate asks for a current approval or
choice, `Need from Will` must name that same decision; `None` means no current
operator decision is required.

Apply these translation rules:

- A score must name its scale or basis and explain what the difference means.
- A test or validator total must state what it proves and what it does not
  prove. Structural validation must not be presented as product, semantic,
  visual, experiential, or production readiness.
- Define an acronym or internal status in ordinary language on first use, or
  move it to the proof/control-receipt layer.
- A status such as `READY`, `NOT_READY`, or `BLOCKED_AUTHORITY` cannot be the
  entire outcome. State the practical consequence beside it.
- Use a compact `Control receipt` when IDs, hashes, detailed validators,
  exclusions, or lifecycle state are needed. Do not force them into the
  operator explanation.
- Do not repeat the same explanation in both the opening and `**-summary**`.
  The summary should compress the meaning and next action, not duplicate the
  evidence narrative.

An explicitly requested receipt-only response may lead with the requested
control state, but must identify itself as receipt-only and must not make a
broader readiness claim than the evidence supports.

### Operator Relevance Gate

After establishing meaning, decide whether each supporting detail should be
shown to Will at all. Include a detail in the operator narrative only when at
least one answer is yes:

1. Does it change what Will should decide or do?
2. Does it explain a material risk, limitation, or readiness claim?
3. Can Will interpret it without opening another file or decoding an internal
   convention?
4. Is Will, rather than another agent or validator, the intended consumer?

When every answer is no, omit the detail from the operator response. Preserve
it only when another executor, auditor, or recovery path needs it, using one
compact labelled control receipt or the durable handoff—not a second narrative.

Use this visibility policy:

- **Always show:** outcome, human consequence, actual readiness or limitation,
  decision or blocker, and the next meaningful action when one exists.
- **Show conditionally:** risks, test results, scope limits, and evidence that
  directly explain or qualify the claim being made.
- **Compact trace:** paths, work-item IDs, totals, and lifecycle state only when
  they enable audit, recovery, execution continuity, or an approval decision.
- **Hide by default:** hashes and schema digests, claim baselines, raw commands
  or command output, timestamps, internal revisions, and validator mechanics.

Exact technical values are justified when Will explicitly asks for a receipt,
an approval binds to those values, a mismatch is the blocker, or recovery or
handoff cannot proceed without them. Explain the human consequence first, then
show only the minimum exact values needed. Do not use a crude ban on hashes or
IDs: apply the audience and decision test to their purpose.

Do not infer approval binding merely because a status packet lists a decision
beside hashes or baselines. Treat exact values as decision-binding only when
the operator or governing authority states that approval is valid at those
values, or when a verified mismatch makes safe execution depend on them. Do
not invent a hash-bound approval target to justify displaying machine evidence.

For cross-agent reporting, keep the operator summary and executor evidence in
the same response only when both audiences need the handoff. Label the machine
section `Control receipt`, keep it below the human meaning, and do not tell Will
to review machine-only baselines.

## Mandatory Inline `-summary` Response Contract

Whenever the operator uses `-charter`, `-plan`, `-audit`, `-qa`, or `-QA`, or
asks to create, update, capture, refresh, select, emit, or review a charter,
plan, audit, report, approval packet, handoff packet, Skill Workshop proposal,
scored pilot/gate report, or other operator-facing artifact, the final chat
response must include a concise inline `**-summary**` section after the file
operation or review action completes.

This is required even when the response already includes artifact links,
validation notes, a findings table, a plan chart, or a short prose close-out.

The inline summary must be shown in chat, not only saved to a file.

Use this exact section label:

**-summary**

For an explicit `-summary` or a mandatory artifact footer, read
`references/summary-behavior-modes.md`. Resolve the subject, select the review
mode, and run its loss-intolerant preservation gate before drafting. The
summary is a review lens over current authority; it never replaces the source
artifact, PAP, plan, evidence, or work-item state.

Write the summary for high-level reading-to-do, using this stable review spine.
`Outcome`, `State`, and `Next` are the three required anchors. Add or merge the
other fields only when they carry separate decision-changing meaning:

```markdown
**-summary**

- **Outcome:** The single most important result, verdict, or recommendation.
- **Why it matters:** The practical effect for Will or the downstream user; merge this into `Outcome` when the consequence is already explicit.
- **State:** `Done`, `Needs decision`, `Blocked`, or `In progress`, plus the practical readiness consequence when useful.
- **[Mode-specific review fields]:** Preserve the plan, implementation, subject, or continuity facts that change the current decision.
- **Proof / Evidence ceiling:** The strongest validation or evidence and what it does not establish when overclaim risk exists.
- **Next:** Start with exactly one of `Continuing now —`, `Need from Will —`, `Recommended —`, or `None —`, then give the exact action, decision phrase, owner, or stop condition.
```

Summary rules:

- use short labelled bullet points; do not return the summary as a prose block;
- normally use three to eight bullets and one decision-changing idea per
  bullet; do not emit an empty, overlapping, or repetitive bullet merely to
  meet a count;
- always put `Outcome` first and `Next` last; when the root turn-close contract
  applies, keep the stable `Next` label, start its value with exactly one of the
  four states above, and do not append another close;
- write `Outcome` as the plain-language result or consequence, not as an
  unexplained score, identifier, validator total, or status code;
- include `State` in every ordinary covered summary; include `Why it matters`
  as its own bullet only when the practical effect is not already clear in
  `Outcome`;
- choose exactly one primary review mode: subject overview, plan review,
  implementation/result review, or continuity/handoff review;
- name mode-specific fields for the human review job instead of forcing generic
  `Key points` or `Continuity` bullets into every subject;
- include continuity or PAP state only when a material operator input, active
  goal, project binding, ownership transfer, or PAP component was inspected or
  changed;
- preserve an additional decision-changing fact rather than enforcing a hard
  word limit;
- omit file lists unless a file is the deliverable or is needed as proof;
- keep detailed validation, exclusions, paths, and implementation narrative
  outside the summary;
- use numbered steps only when the next action is genuinely sequential;
- keep a decision gate separate and immediately before the summary.

An explicitly requested receipt-only response may omit the ordinary review
spine. It must identify itself as receipt-only, show only the requested
controls, name their scope, and state what they do not prove.

Use `references/summary-behavior-eval-cases.json` only for local regression or
later canary scoring. Passing that supplied corpus proves the local contract and
reference outputs, not fresh-context usefulness or production readiness.

For `-charter`, summarize the current charter purpose, scope/decision changes,
open questions, and next action.

For `-plan`, also include the compact pre-plan audit verdict and a compact
implementation chart when the plan itself is the main deliverable.

For `-audit`, include the top findings/recommendation summary and the required
principle verdict lines; do not paste the full audit unless asked.

For `-qa` / `-QA`, include the done-state verdict, failed angles, proof, and
ready-for state; do not mark work done from impression alone.

For decision turns, show the decision target and approval boundary inline
directly before asking.

Do not end a `-charter`, `-plan`, `-audit`, `-qa`, `-QA`, or operator-facing
artifact turn with only links, validation, or file paths. Always add
`**-summary**` inline.

## Mandatory Inline Decision Gate

Operator review files are retired as a live workflow. Do not create, refresh, or
depend on `OPERATOR_REVIEW.md` / `*_OPERATOR_REVIEW.md` for new work.
Historical review files may be read only as legacy evidence.

When Will needs to approve, accept, revise, defer, or choose a next action, the
final response must show an inline decision gate. The gate must include the
actual target being decided, not only a path or abstract label.

Use this response shape as a fact checklist, not a fixed seven-line form:

```markdown
**Decision Gate**
Decision needed: ...
Target preview: ...
What this does for Will/user: ...
What approval allows: ...
What approval does not allow: ...
Evidence / source: ...
```

Normally compress it to four units: `Decision`, `Target`, `Boundary`, and the
exact `Ask`. Split `Boundary` into allows/excludes or add evidence only when
that distinction changes the approval or makes the action safer.

Keep the target preview compact but substantive:
- for plans, show the phase or action table being decided;
- for audits, show the top findings and recommendation;
- for QA, show passed/failed angles and ready-for state;
- for design or image work, show or link the concrete visual evidence and name
  the exact object/state being decided;
- for reports, show the core conclusion and recommended next action.

Optional fields such as confidence, risk, why now, success signal, stop
condition, owner/surface, and refresh trigger may be included when they clarify
the decision. Do not make the gate so long that it slows the operator down.

Ask for the exact decision once. For one recommended approval, put the exact
reply phrase only in the final summary `Next` bullet; do not add a separate
Decision Ask block. When two or three genuinely distinct response options are
needed, place this block immediately after the gate:

```markdown
**Decision Ask**
Please reply with one of:
- `Approve ...`
- `Revise ...`
- `Defer ...`
```

In that multi-option case, the summary `Next` may say `select one option above`
instead of repeating every phrase. Do not repeat the same approval wording in
the gate, Decision Ask, and summary.

Use the concrete approval phrase, revision target, or defer action from the
primary artifact or the current chat. Do not end an approval-gated artifact turn
without this inline ask unless no decision is required.

Never request approval for a plan revision that is not visible in the target
preview or present in the canonical plan. A proposed revision must be labelled
as proposed and state whether approval creates, replaces, or executes it.

Include `**-summary**` when this skill's artifact-lane response contract
requires it; its final `Next` remains the terminal turn-close cue.

## Plan Breadth And Detail

Treat plan breadth and plan detail as separate controls:

- `-plan` shows the current actionable slice: the active milestone, immediate
  deliverables, human input, exit evidence, and next action.
- `-plan all` shows the complete goal journey as the minimum-necessary 1-7
  stable deliverable milestones, expressed as named usable deliverables,
  genuine decisions, verified results, or verified capabilities. `All` means
  all outcomes required for the accepted finish line, not all known work. It
  must not expand every task, file path, completed phase, optional/deferred
  lane, validator, or control receipt by default.
- `-plan full`, `full -plan`, or `show full plan inline` shows the same
  milestone roadmap followed by the complete technical execution detail.

Use this milestone chart for `-plan all` and as the first planning chart for
`-plan full`:

| Milestone deliverable | What it enables | Need from Will | Accepted when | State |
| --- | --- | --- | --- | --- |

Use 1-7 milestones and stop at the smallest complete set. Name milestones by the operator-visible
deliverable, decision, verified result, or capability, not the internal
subsystem. Treat architecture, setup, audits, schemas, validators, and other
controls as subordinate enablers unless one is the explicitly requested
deliverable. Treat time as a constraint or sequencing input rather than the
default completion unit; preserve a real external deadline when it defines
acceptance. Put task IDs, paths, command modes, validators, hashes, and rollback
mechanics in a compact control section or in the technical table for `-plan
full`.

Apply the Utility Gate before keeping any roadmap row: if the row disappeared,
name the exact finish-line acceptance criterion that would become impossible.
If no exact consequence exists, merge, nest, or remove the row. Put completed
history in `Current position` or proof. Keep optional, deferred, later, parked,
and speculative work outside the main roadmap unless the operator explicitly
asks for a separate non-critical appendix.

Use this technical table only for `-plan full`, an execution handoff, or when
the omitted detail would make the plan unsafe or ambiguous:

| Phase / Task | Deliverable | Owner / Surface | Dependency / Gate | Validation | Next Action |
| --- | --- | --- | --- | --- | --- |

Show a separate critical path only when milestone order does not make the
unlocking sequence clear because of blockers, parallel tracks, cross-owner
dependencies, or multiple plausible execution orders. Otherwise the milestone
order is the critical path. The mandatory `**-summary**` footer still applies.

## Lane Defaults

### `-backlog`
When work is added, moved, promoted, emitted, or refreshed into `-backlog`:

1. Confirm the backlog mutation.
2. Show the relevant work plan as a compact chart/table.
3. Include at minimum: priority, item, status, owner/stage, dependency/blocker, and next action.
4. Mark newly created or changed items clearly.
5. Scope to the current client/project/run unless the operator asks for a global view.

Recommended chart:

| Priority | Item | Status | Owner/Stage | Depends On / Blocker | Next Action |
| --- | --- | --- | --- | --- | --- |

### `-charter`
When a charter is created, updated, selected, or expanded:

1. Confirm the charter mutation.
2. Keep the durable charter bundle single-file-first by default.
3. Provide a lean operator-facing summary inline in the response or inside the charter's existing summary/current-slice section.
4. Create or refresh a separate `-summary` artifact only when one of these is true:
   - a canonical summary path already exists;
   - an external review, audit package, handoff, or dashboard needs the summary as its own artifact;
   - the charter is too long for the summary to remain scannable inline.
5. Prefer refreshing an existing canonical summary over creating a duplicate.
6. If the charter contains a phased build path, staged implementation, rewrite/migration phases, rollout stages, or build gates, summarize only the charter-level durable intent and point to the active plan or recommend `-plan`; do not duplicate the whole staged plan inline unless the operator explicitly asks for a full plan view.

Recommended inline summary sections:

- Purpose
- Scope
- Current Decisions
- Operating Principles
- Open Questions
- Next Action

### `-plan`
When a plan is created, updated, selected, or produced by a planning skill:

1. Start `-plan all` and `-plan full` with
   `**Goal and Milestone Check**`:
   - Goal
   - Primary usable deliverable
   - Consumer and intended use
   - Minimum useful completed set
   - Representative finished example
   - Acceptance proof
   - Finish line
   - Milestone arc
   - Current position
   - On track: `Yes`, `At risk`, or `Off track`, with one reason
   - Need from Will: one exact question or `None`
2. Compare the request with current project authority before roadmap detail.
   - If aligned, name the authority source and continue without asking.
   - Treat the deliverable fields as one Deliverable Lock inside this check,
     not another planning layer.
   - If drifted, conflicting, or missing in a way that changes the goal,
     primary usable deliverable, consumer or use, minimum useful set,
     representative example, acceptance proof, finish line, milestone arc,
     owner, authority, cost, or approval boundary, show concrete
     interpretations when useful, recommend one, ask one exact question, and
     stop before architecture, roadmap, or approval language.
   - Treat this as a working planning lock, not a durable write unless capture
     or update was requested.
   - In a combined Audit then Plan All response, allow the completed audit
     first, then start the Plan All section immediately with this check.
   - Keep `Need from Will` identical in meaning to any later decision gate; do
     not report `None` when approval blocks the displayed next milestone.
3. Show a compact pre-plan audit verdict without turning the first screen into
   an internal lane audit:
   - verdict: `proceed-to-plan`, `reduce-scope`, `merge`, `research-first`,
     `no-op`, or `blocked`;
   - user/operator value;
   - anti-bloat result;
   - validation-before-planning.
4. Run a compact charter preflight before decomposing execution:
   - Does future work need durable purpose, scope, non-goals, approval gates, decisions, or success criteria?
   - Would another session or stage lose important context without a charter pointer?
   - Is this only a tactical task that can keep assumptions inside the plan?
5. Create or refresh charter context only when the preflight justifies durable context. Prefer a short charter section or active charter pointer inside the plan; update a separate charter file only when reuse, audit, ownership, or lifecycle requires it.
6. Decompose the goal into the minimum-necessary 1-7 deliverable milestones
   before technical tasks.
   Each milestone must name the usable deliverable, genuine decision, verified
   result, or verified capability; what it enables for the consumer; whether
   Will must decide or provide anything; what acceptance evidence closes it;
   and its state. Apply the Utility Gate to each row: identify the exact
   finish-line acceptance criterion that becomes impossible if it is removed.
   Nest, merge, or omit rows without that consequence, including process-only,
   time-only, completed, optional, deferred, later, enabler, and control rows,
   unless the operator explicitly requested one as the result or asked for a
   separate non-critical appendix.
7. Apply the requested depth:
   - `-plan`: show only the current actionable slice;
   - `-plan all`: show every milestone and the current focus;
   - `-plan full`: show every milestone, then the complete technical task plan.
8. Show a separate critical path only when milestone order is not sufficient to
   explain dependencies, blockers, gates, or parallel work.
9. Compress lane-audit results into the affected milestone or a short audit
   delta. Do not duplicate a lane table, critical path, and technical task table
   when they express the same sequence.
10. Keep one canonical persistent plan. Update stable goal and milestones only
   when direction changes; update current focus, evidence, state, and revision
   as work advances. Do not create versioned plan copies merely for progress.
11. Keep review packet components merged into the primary plan artifact by default: copy blocks, brief notes, intake notes, proof notes, design notes, and approval notes should remain together for review until one section becomes independently owned, long-lived, reused across artifacts, or operationally large enough to justify a separate file.
12. When a separate file is justified, add a short pointer in the primary plan explaining why it is separate and how it should be used.
13. If the plan introduces backlog items, also run the `-backlog` default and show the updated work plan chart.
14. If the plan changes charter-level scope, refresh only the charter delta: purpose, scope, non-goals, decisions, gates, or success criteria that changed. Do not reprint or duplicate the full charter unless the operator asks for a charter view.

Recommended milestone chart for `-plan all` and `-plan full`:

| Milestone deliverable | What it enables | Need from Will | Accepted when | State |
| --- | --- | --- | --- | --- |

Recommended technical chart for `-plan full`:

| Phase / Task | Deliverable | Owner / Surface | Dependency / Gate | Validation | Next Action |
| --- | --- | --- | --- | --- | --- |

### `-audit`
When an audit is created, updated, selected, or produced by an audit/review workflow:

1. Treat audit as mostly pre-plan decision analysis: pressure-test judgment,
   direction, assumptions, options, risks, evidence, timing, user value,
   anti-bloat, and validation before planning or building.
2. Use a findings or decision-analysis table when three or more materially
   different findings need comparison; otherwise use one compact verdict with
   the strongest risk and recommendation.
3. Preserve severity, evidence, impact, recommendation, and owner/next action
   where they change the decision; merge overlapping fields and omit empty
   columns.
4. Include the core judgment, strongest argument for, strongest argument
   against, weak assumptions, missing evidence, options considered, and
   validation before planning when the audit is about a decision or direction.
5. Include a brief user-first check unless the operator explicitly scopes it out. Ask whether the recommendation improves the operator's ability to understand, decide, steer, recover, or receive useful output without forcing raw folder traversal or extra process.
6. Include a brief anti-bloat check unless the operator explicitly scopes it out. Ask whether the recommendation creates unnecessary files, skills, hubs, runtime modes, dependencies, abstractions, or workflow layers when an existing surface can absorb it.
7. Use anti-bloat tags when useful: `delete`, `stdlib`, `native`, `yagni`, `shrink`, `merge`, `reference-only`.
8. For workspace structure, control-layer, skillhub, module, routing, viewer, dashboard, automation, or durable process audits, emit both principle verdict lines exactly once:

```text
User-first: pass|weak|fail - one-sentence reason.
Anti-bloat: ok|reduce|merge|reference-only - one-sentence reason.
```

Use `User-first: pass` only when the recommendation clearly improves Will's practical control, comprehension, or output quality. Use `weak` when value is indirect or unproven, and `fail` when the change mainly serves internal structure without an operator benefit.

Use `Anti-bloat: ok` only when no unnecessary surface is being added. Use `reduce`, `merge`, or `reference-only` when an existing skill, artifact, hub, registry, native capability, or generated projection should absorb the need.
9. If findings become backlog work, also run the `-backlog` default and show the updated work plan chart.
10. If the audit changes project direction, operating rules, acceptance criteria, or charter scope, also run the `-charter` default and refresh the inline charter summary or justified canonical summary artifact.
11. Keep audit output distinct from implementation approval; audit findings are not authorization for irreversible action.

Recommended chart:

| Severity | Finding | Evidence | Impact | Recommendation | Owner / Next Action |
| --- | --- | --- | --- | --- | --- |

Recommended principle verdict lines:

`User-first: pass|weak|fail - one-sentence reason.`

`Anti-bloat: ok|reduce|merge|reference-only - one-sentence reason.`

### `-qa` / `-QA`
When QA is produced for completed work:

1. Treat QA as post-build verification: was the thing implemented correctly,
   integrated safely, evidenced, and actually done?
2. Lead with a done-state verdict: `Done`, `Done with caveats`, `Revise`,
   `Blocked`, or `Not done`.
3. Preserve confidence, what passed or failed, relevant angles, untested
   assumptions, required fixes, proof, evidence ceiling, and ready-for state.
   Merge them into the fewest non-repeating units; omit empty categories.
4. Use `-qa brutal` / `-QA brutal` for adversarial QA: name the strongest
   failure case first, then test from multiple angles.
5. Do not mark work `Done` without proof from tests, screenshots, validators,
   logs, diffs, or manual checks.

### Inline `-summary` after artifacts

This section is a mandatory output footer for `-charter`, `-plan`, `-audit`,
and operator-facing artifact turns, and a default output footer for adjacent
artifact lanes.

Do not end an artifact turn with only links or validation. Always add
`**-summary**` inline when the turn creates, updates, selects, emits, or reviews
operator-facing artifacts.

Trigger this for:
- `-audit` artifacts
- `-qa` / `-QA` results
- `-plan` artifacts
- reports
- Skill Workshop proposals
- scored pilot/gate reports
- handoff or approval packets

Select the adaptive review mode in
`references/summary-behavior-modes.md`, keep the stable review spine, and
preserve only the loss-intolerant facts that affect the operator's current
review. Do not force file lists, validation inventories, continuity, or
approval state into every summary; include them only when they change the
decision, readiness claim, recovery path, or receiver handoff.

Do not paste the full artifact unless the operator asks. Keep the summary short enough to review in chat.

If the operator explicitly asks `show me -summary for review in line`, display the relevant summary inline even when the artifact already exists.

## Cascading Defaults
Use these cascades when a workflow touches multiple lanes:

- `-plan` creates work items -> update `-backlog` chart.
- `-plan` changes project scope -> refresh the charter's inline summary or justified canonical summary artifact.
- `-audit` creates remediation work -> update `-backlog` chart.
- `-audit` changes direction, policy, acceptance criteria, or scope -> refresh the charter's inline summary or justified canonical summary artifact.
- `-charter` creates execution implications -> show a compact `-plan` chart if concrete next work exists.

## Validation

Before final response, check:

- the right lane default was selected from the mode router;
- any decision target is substantive enough to decide inline;
- `-plan` output includes a compact pre-plan audit verdict;
- `-plan all` starts with `**Goal and Milestone Check**`; when aligned it
  locks the usable deliverable and intended use, then includes the complete
  minimum-necessary 1-7 deliverable journey, current focus, human input, and
  acceptance evidence;
- a combined Audit then Plan All response starts the Plan All section with the
  Goal and Milestone Check before plan identity, ownership, paths, or approval
  metadata;
- `Need from Will` and the later decision gate name the same current decision,
  and `None` is used only when no such decision exists;
- architecture and controls appear after the Deliverable Lock and stay
  subordinate unless explicitly requested as the deliverable;
- process-only and time-only roadmap rows are rejected or nested, while real
  external deadlines remain visible constraints;
- every roadmap row passes the counterfactual Utility Gate, while completed
  history and optional/deferred/later work stay outside the active completion
  path unless explicitly requested;
- material goal or milestone ambiguity produces one exact question and stops
  before roadmap detail or approval language;
- clear alignment names its source and does not ask a redundant question;
- ordinary `-plan` stays on the current actionable slice;
- `-plan full` includes the milestone roadmap plus every required technical
  task, dependency, gate, and validator;
- a separate critical path appears only when milestone order does not make the
  unlocking sequence clear;
- one canonical persistent plan records revision and current milestone without
  creating progress-copy files;
- audit and QA responses include required proof/verdict lines;
- approval gates remain explicit and unbypassed.

## Trigger Tests

| Input | Expected mode | Expected output |
| --- | --- | --- |
| `-plan all the remaining steps` | Milestone roadmap | Starts with Goal and Milestone Check; if aligned, continues to the minimum-necessary 1-7 deliverable milestones and `**-summary**` with no completed, optional, deferred, control-only, or task padding |
| `show full -plan inline` | Full execution plan | Goal and Milestone Check, milestone roadmap, every required task/dependency/gate/validator, summary |
| `-plan the next step` | Plan slice | Current milestone, immediate deliverables, human input, proof, next action |
| `-audit this direction` | Audit summary | Findings, principle verdicts when applicable, summary |
| `-qa brutal` | QA verdict | Strongest failure case, proof, ready-for state |
| `-summary this plan` | Summary review — plan | Goal, current milestone, deliverables, open decision, evidence ceiling, exact next action; no execution or closure |
| bare `-summary` after one artifact was reviewed | Summary review — current subject | Use that uniquely resolvable artifact; ask one exact subject question only when materially ambiguous |
| `approve/revise/defer this artifact` | Decision gate | Target preview and exact decision ask |

For compact examples of the expected response shapes, read
`references/response-shape-examples.md`.

## Constraints
- Do not create a separate `-summary` file by default for `-charter` updates.
- Do not duplicate summaries or charts when a canonical artifact can be refreshed.
- Do not expand into a full report unless requested.
- Use registries, indexes, and active run/project summaries before deep browsing.
- Keep outputs lean and decision-ready.
- Preserve approval gates for external sends, destructive writes, credential changes, payments, and production mutations.
