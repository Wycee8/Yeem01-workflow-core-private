---
name: yeem01-workflow-core
description: Apply Will's Yeem01-backed Codex workflow when a request explicitly uses -help, -onboarding, -explain, -ask, -user, -audit, -discuss, -explore, -suggest, -research, -plan, -qa, -evaluate, -improve, proceed, proceed all, auto proceed, or Adam proceed. Use it to preserve familiar cross-device command semantics, compose modes, teach the audit-to-improvement lifecycle, and collect redacted improvement proposals. Do not trigger from incidental nouns, filenames, bare BM, or general questions; this skill supplies no project logic, connector, credential, tool, permission, access decision, or external-action authority.
---

# Yeem01 Workflow Core

## Purpose

Translate Will's explicit command tokens into one predictable working method.
This is the front door for a private, Yeem01-backed portable operator suite.
The released plugin keeps familiar workflow semantics available on another
compatible device and includes a dependency-complete set of shared operator
skills without copying the full Yeem01 workspace.

The skill never grants a tool, connector, permission, project role, data
source, device access, or authority inherited from another user or machine.
Distribution and access decisions live outside this core.

Keep context compact. Load only what the request needs:

- read `references/onboarding.md` for `-onboarding`, general `-help`, a new-user
  introduction, or the complete lifecycle example;
- read `references/command-contract.md` for combined commands, `proceed`,
  `-qa`, `-evaluate`, `-improve`, or ambiguous scope/authority;
- read `references/maintenance.md` when asked how the pack is sourced,
  distributed, updated, or improved; and
- read `references/validation-cases.json` only when testing or changing the
  skill.

## Resolve The Request

For broad, combined, or execution-bearing work, establish internally:

```text
goal:
target and user:
mode(s):
constraints:
available owner/specialist:
host boundary:
expected output and proof:
```

Infer these from visible context when safe. Ask one scoped question only when
the answer would materially change scope, authority, side effects, evidence,
or validation.

Recognize only explicit command tokens. Incidental phrases such as "audit
log", "research paper", or `plan.png` do not activate a mode. Bare `BM` does
not route this skill or market analysis.

When multiple explicit tokens appear, compose them in this order:

1. guide: `-help`, `-onboarding`, `-explain`;
2. context: `-ask`, `-user`;
3. direction: `-audit`, `-discuss`, `-explore`, `-research`, `-suggest`;
4. commitment: `-plan`;
5. execution: `proceed` variants;
6. assurance and learning: `-qa`, `-evaluate`, `-improve`;
7. verify and report.

A guide token is read-only. A later execution token never erases an earlier
discussion, planning, specialist, or host boundary.

## Host Capability Precedence

This skill is the portable command front door. A generated release also
contains the allowlisted portable specialist owners named in
`BUNDLE_MANIFEST.json`. Before using a fallback method:

1. route to the bundled or host specialist skill or canonical project owner
   that owns the deliverable;
2. use this skill to preserve Will's command semantics around that route; and
3. use the compact fallback below only when the host exposes no applicable
   specialist or project procedure.

Do not impersonate, copy, or weaken an owner. In particular:

- `-user` routes to an available user-context owner;
- `-audit` and `-evaluate` route to an available audit/evaluation owner;
- `-research`, planning depths, `-qa`, design, PAP/DAP, provider work, and
  project-specific execution route to their available owners; and
- `-improve` routes to the owning improvement procedure when one exists.

Prefer a bundled owner over the compact fallback. State when a fallback is
necessary or when a requested domain route depends on the host workspace.

## Guide And Context Modes

### `-help`, `-onboarding`, and `-explain`

These are guide-only modes. Do not execute work merely because a guide
describes execution.

- `-help <command>`: what it does, what it returns, its boundary, and one
  short example.
- `-onboarding`: load `references/onboarding.md` and give the compact setup,
  command map, lifecycle, boundaries, and first safe practice task.
- `-explain <target>`: explain purpose, flow, limits, and one example in
  language suited to the visible user.

### `-ask`

Use question-led refinement. Reflect the working assumption and ask at most
one high-leverage question at a time. If context already answers it, act
within the other explicit mode instead of asking mechanically.

### `-user`

Make the intended user's job, knowledge, constraints, and success condition
visible. Use only supplied or authorized context; do not infer sensitive
traits, search for personal data, or create employee performance judgments.

Return a compact user lens when no other mode is present:

```text
user / job / friction / desired outcome / constraints / evidence gap
```

## Direction Modes

### `-audit`

Perform pre-commitment direction analysis. Do not implement.

Return:

- verdict and confidence;
- strongest case for and against;
- weak assumptions and missing evidence;
- options and trade-offs;
- risk, timing, and cheapest useful validation;
- one recommended next move.

For durable workflow, skill, or control-layer proposals, include:

```text
User-first: pass|weak|fail - reason
Anti-bloat: ok|reduce|merge|reference-only - reason
```

Prefer deleting, shrinking, merging, or using a native capability when that
serves the user better.

### `-discuss`

Enter conversation-locked refinement. Reflect the working hypothesis,
identify tensions, and ask at most one high-leverage question at a time.

Do not create files, produce an implementation plan, or execute unless the
same request explicitly asks to capture, plan, or proceed.

### `-explore`

Open the option space before commitment. Map plausible routes, edge cases,
unknowns, and cheap probes. Label inference and avoid presenting exploration
as a decision or plan.

If combined with `-discuss`, keep the exchange conversation-locked. If
combined with `-plan`, narrow the option space first and plan only the selected
or clearly recommended route.

### `-research`

Research only the named evidence gap. Prefer primary or authoritative sources,
cite claims, distinguish sourced fact from inference, and state what decision
the evidence informs. Do not widen into a general scan or execute changes.

### `-suggest`

Give one primary recommendation, why it fits, one material challenge,
evidence status, and the cheapest useful validation. Do not turn a suggestion
into execution.

## Planning And Execution Modes

### `-plan`

Match planning depth to the explicit form:

- `-plan`: current actionable slice, dependencies, validation, gate, and
  completion test;
- `-plan all`: complete three-to-seven-milestone journey with outcomes,
  dependencies, owners, gates, and acceptance checks; and
- `-plan full` or `full -plan`: milestone journey plus bounded technical tasks,
  paths, sequencing, validators, rollback, and handoff detail.

Preserve live-workspace volatility rather than assuming a frozen tree. Stop
before implementation unless an explicit execution token is present and the
host permits that work.

### `proceed`

Continue only the current visible, bounded lane. Reconfirm target, remaining
safe work, dependencies, proof, rollback, and gates. Prefer reversible local
work and validate proportionately.

`proceed all`, `auto proceed`, or `Adam proceed` never means unlimited
authority:

- require a selected plan or named lane;
- execute only dependency-valid work inside visible scope;
- do not retry a failed transition unless the plan permits it;
- stop at a hard gate, consequence-changing ambiguity, or exhausted safe work;
- report outcome, proof, remaining gates, and the next exact decision.

Recurring or absent operation requires a separate loop/automation contract.
This skill alone authorizes current-turn continuation only.

## Assurance And Learning Modes

### `-qa`

Verify built or completed work before handoff, publish, or close. Route to the
available quality owner. In fallback, inspect requirements, behavior, edge
cases, integrations, safety/privacy, and evidence; report severity, proof,
limitations, and a pass/fail/conditional verdict.

QA asks whether work was built correctly. It does not decide whether the work
delivered value after real use.

### `-evaluate`

Judge impact only after credible use evidence exists. Route to the available
evaluation owner. Separate observed evidence from inference and recommend one
of: keep, iterate, simplify, observe, roll back, retire, or scale.

If credible use evidence is missing, return an observation plan; do not
pretend QA output is impact evidence and do not auto-improve.

### `-improve`

Convert verified friction or evaluation findings into a bounded proposal.
Rank up to three opportunities and recommend the smallest high-value change.
Stop before writes by default.

For a core-skill change, output:

```text
problem and affected users
evidence, recurrence and confidence
privacy/redaction check
proposed rule and non-goals
affected command/owner
new regression fixture
implementation, review and rollback
```

Never silently collect raw transcripts, score employees, self-edit the skill,
or auto-promote a release. `-improve proceed` requires a visible complete
plan, a bounded local lane, dependency validity, and no unmet host gate.

## Lifecycle

Use the complete workflow when the decision and implementation warrant it:

```text
-audit
-> -discuss and/or -explore
-> -plan all
-> bounded proceed when the host permits it
-> -qa
-> use and minimal redacted observation
-> -evaluate
-> -improve proposal
-> Yeem01 source update through a host-owned maintenance lane
-> -qa and versioned canary
```

Do not collapse QA, evaluation, or improvement into one step. The worked
example lives in `references/onboarding.md`; the central update model lives in
`references/maintenance.md`.

## Host Boundary

The controlling order is:

1. system and developer instructions;
2. the operator's current explicit instruction;
3. repository and nested `AGENTS.md` instructions;
4. accepted project charter/PAP and visible plan;
5. owning specialist or connected-provider procedure;
6. this command-mode behavior.

This core does not define, grant, store, or change access decisions. Stop and
name the host-owned boundary before external messages, service writes,
credentials, provider spend, runtime/default changes, production, destructive
actions, Git publication, plugin transfer or installation, device rollout,
or client-facing mutation.

## Audience Separation

- BOOOOM and MSport behavior remains with their own plugin or project.
- The same core can later be packaged for a named BM employee or associate,
  but distribution, access, project bindings, credentials, canary, and rollback
  are managed outside this skill.
- A portable packet never enrolls a device, binds a project, copies credentials,
  or grants client authority.
- Create an audience-specific package when private context, terminology, data,
  or authority differs materially.

## Response Shape

Lead with the outcome. Use the smallest structure the mode needs. For material
routing, a compact line is acceptable:

```text
Usage: pattern=<request>, mode=<mode>, route=yeem01-workflow-core -> <owner>
```

Do not emit the route mechanically. End execution work with completed items,
impact, proof, what was not performed, unresolved gates, and the next exact
decision.
