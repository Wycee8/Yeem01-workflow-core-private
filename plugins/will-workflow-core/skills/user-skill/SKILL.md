---
name: user-skill
description: "Apply the -user lens: check operator-first and downstream-user value, simplicity, anti-bloat risk, and whether to use, reduce, clarify, or no-op before durable creation."
---

# User Skill

Use this skill when the operator invokes `-user`, `[adam - user]`, `[yeem - user]`, asks to check from a user perspective, asks whether something is useful, intuitive, overbuilt, worth creating, or should become a goal, charter, backlog item, skill, system, or canvas node.

## Job

Apply a user-centred lens before durable creation.

Check whether an idea, plan, output, charter, backlog candidate, skill, system, or creative surface is useful, simple, intuitive, and worth creating.

This skill may recommend no-op.

## Core Principle

User value before workspace structure.

Do not reward complexity. Do not create durable artifacts unless the user need, operator benefit, and validation path are clear.

In Will's workspace, `user` means both audiences in this order:

1. **Will / operator first** — does this reduce decision load, control burden,
   context switching, wasted work, or review friction?
2. **Downstream user second** — when the work is product, content, creative, or
   client-facing, does this improve the real customer/user experience?

If operator value and downstream user value conflict, state the trade-off and
prefer the smallest reversible action that protects both. Do not use operator
convenience as an excuse for poor product UX, and do not build product polish
that increases operator chaos without clear payoff.

Delete first before improving: for any proposed durable structure, first ask
whether the requirement, step, artifact, viewer, backlog item, or skill can be
removed, absorbed by an existing route, or kept as a one-off. Only optimize or
formalize what survives that check.

## Modes

Choose the smallest relevant mode:

- `check` — quick usefulness and anti-bloat pass.
- `goal-fit` — decide whether an operator idea should become a captured goal candidate.
- `plan-audit` — reduce a plan to the simplest useful action.
- `charter-fit` — decide whether durable charter context is justified.
- `viewer-fit` — decide whether a separate viewer reduces review/decision
  friction, or whether the existing report/charter is enough.
- `surface-flow` — for viewers, dashboards, reports, canvas nodes, and review
  surfaces, check whether the first screen follows the user's natural questions
  before internal artifact categories.
- `flow-audit` — for interactive or multi-step experiences, walk the primary,
  escape/switch, and recovery tasks; read
  `references/user-flow-audit.md`.
- `backlog-fit` — decide whether work belongs in global/project backlog or should remain intake/no-op.
- `skill-system-gate` — mandatory check before new skills, systems, control layers, backlog structures, or canvas nodes.
- `delete-first` — first-principles check for whether the proposed requirement
  should exist at all before planning, optimizing, or creating structure.
- `creative-use` — check creative/product/surface work for actual user value before production.
- `research-fit` — decide whether evidence is actually needed to settle the
  user-value verdict, or whether local proof is enough.
- `discussion-lens` — in `-discuss`, sharpen the idea around operator value,
  downstream user value, smallest useful version, and one clarifying question.

## Mandatory Use

Apply this skill before:

- creating a new skill,
- creating or materially changing a control layer,
- creating a new backlog structure,
- creating or materially changing charter systems,
- creating a MAI Canvas node,
- adding project/global backlog semantics,
- turning a vague operator idea into durable state.

For small ordinary tasks, use only when invoked or when overbuild risk is obvious.

## Output

Default to a compact decision lens. Use this shape for ordinary `-user`,
`-discuss -user`, and `-audit -user` replies unless durable creation is being
gated:

```md
**-user:** Use / Clarify / Reduce / No-op
**Operator value:** ...
**Downstream user value:** ...
**Smallest useful version:** ...
**Do not build:** ...
**Next:** ...
```

Use the fuller gate only when the proposal may create or materially change a
skill, system, control layer, charter, backlog structure, viewer, canvas node,
or other durable workspace surface:

```md
## -user Check

**Verdict:** Use / Clarify / Reduce / No-op
**Operator user:** ...
**Downstream user:** ...
**Need:** ...
**Friction:** ...
**User job:** ...
**Delete-first check:** delete / absorb / keep because ...
**Simplest useful version:** ...
**Success signal:** ...
**Overbuild risk:** Low / Medium / High
**Do not build:** ...
**Durable capture:** none / goal candidate / charter / backlog / project index / self-evolve candidate
**Next action:** ...
```

## User Logic

For anything that might create a skill, charter, viewer, backlog item, canvas
node, or control surface, answer these in plain language before recommending
work:

1. What does Will/operator need to decide, control, review, or stop repeating?
2. What downstream user or customer job is affected, if any?
3. What friction, confusion, risk, or wasted work exists now?
4. Can the proposed requirement, artifact, or control step be deleted or absorbed?
5. What is the smallest useful surface or action?
6. What should not be built?
7. What observable signal proves operator value and downstream user value improved?
8. For a viewer/dashboard/report surface, does the visible order match the
   user's mental flow: what is this, where are we, where are we going, how are
   we getting there, what should I know, and what should happen next?
9. For an interactive or multi-step experience, can the user complete the
   primary task, leave or switch paths, recover and resume, understand status,
   and operate the flow accessibly?

If any answer is vague, prefer `Clarify` or `Reduce`.

## Surface Flow Check

Use this check whenever the target is a viewer, dashboard, report, review
packet, canvas node, or any surface meant to help Will inspect and decide.

Ask:

1. Does the first screen answer the user's first questions in natural language?
2. Does it start from the project/user job instead of internal artifact labels?
3. Are goal, current state, path, next decision, and watchpoints visible before
   technical proof?
4. Can details be inspected without forcing them into the first decision layer?
5. Does every high-level answer trace back to source truth, or show a gap?

Verdict rule:

- `Use` only when the surface is useful and the information flow matches the
  user's decision path.
- `Reduce` when the surface is useful but starts in the wrong order, exposes
  technical proof too early, or uses internal categories before user questions.
- `Clarify` when the user job or decision path is unclear.
- `No-op` when the surface does not reduce review, decision, or orientation
  friction.

## Interactive Flow Audit

For apps, sites, operated dashboards, viewers, review flows, and transactions,
read `references/user-flow-audit.md`. Walk real task steps through the primary,
escape/switch, and recovery scenarios. Label the evidence level and never
present self-review, structural validity, or fixture-derived output as
representative-user validation.

## Verdict Rules

- `Use` — the need is clear and the proposed action is proportionate.
- `Clarify` — intent/user/need is ambiguous and would change the action.
- `Reduce` — useful direction, but current plan is larger than necessary.
- `No-op` — creation is not justified now.

## Combined Modes

- `-discuss -user`: stay conversation-locked. Refine the idea around operator
  value first, downstream user value second, and the smallest useful version.
  For viewer/dashboard/report surfaces, include the surface-flow check before
  recommending a plan or implementation.
  Do not output a plan or file targets unless Will also asks to capture, plan,
  or proceed.
- `-discuss -user -ask`: ask one high-leverage question at a time. Prefer
  questions that clarify the real user, user job, friction, success signal, or
  delete/absorb boundary.
- `-research -user` or `-user -research`: use research only when the evidence
  would change the `Use / Clarify / Reduce / No-op` verdict. If local evidence
  is enough, do not start a research run. If research is needed, name the exact
  user-value question and downstream consumer.
- `-audit -user`: include concise `User-first:` and `Anti-bloat:` verdict
  lines. Use the full `## -user Check` only for durable creation or major
  control/product decisions.
- `-plan -user`: reduce the plan before expanding it. Start with the smallest
  useful action and only add phases that survive the user-value check.

## Routing

- If operator-facing intent capture is needed, route through `adam-mode`.
- If creative/product/content/surface context is needed, route through `yeem`, `marketing-system`, or `creative-workflow`.
- If a separate project/session viewer is justified, route to
  `charter-session-viewer` and pass the user logic into the viewer projection.
- If durable project context is justified, route to `project-charter-docs` after the check.
- If actionable work is justified, route to `workspace-backlog` / `backlog-item-adder` after the check.
- If repeated friction appears across sessions, route the pattern to `self-evolve`.
- If Will asks for first-principles thinking, deletion-first analysis, ground
  truths, or assumption-challenge before creation, route through `adam-mode` /
  `adam-discuss-command-mode` and apply this skill when durable structure is in
  scope.

## Guardrails

- Do not write durable state during a `-user` check unless the operator explicitly approved that write.
- Do not invent a new system when modifying an existing route, skill, template, or view would satisfy the need.
- Do not optimize a requirement before testing whether it should be deleted,
  waived, absorbed, or treated as a one-off.
- Do not research by default; research only when evidence would change the
  user-value verdict or downstream handoff.
- Do not treat candidate goals as canonical until confirmed.
- Keep recommendations concise and decision-grade.

## Tests

Read `references/test-cases.md` when validating routing behavior or examples.
