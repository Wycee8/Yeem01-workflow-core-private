# Yeem01 Workflow Core Command Contract

Use this reference for combined commands, execution requests, QA/evaluation,
improvement proposals, and ambiguous scope or authority.

## Core Law

A command token selects a method. It does not grant authority.

The effective action is the intersection of:

```text
explicit operator intent
AND current repository/project authority
AND visible selected plan
AND available tools and owning procedures
AND unblocked safety and privacy gates
```

If a required term is missing, narrow the action, return a plan, or stop. The
core does not define or change the host's access rules.

## Host Capability Precedence

The applicable bundled specialist or host canonical project owner owns the
deliverable. `yeem01-workflow-core` composes Will's command mode around that
route. Its fallback procedures apply only when no owner is available.

Route, when available:

- `-user` to user-context authority;
- `-audit` and `-evaluate` to direction-audit/impact-evaluation authority;
- `-research`, planning depths, `-qa`, `-pap`/`-dap`, `-design`, provider work,
  and project operations to their owning procedures; and
- `-improve` to the owning improvement/control-change procedure.

Package presence never becomes project, device, connector, or execution
authority.

## Composition Law

Compose explicit tokens through this phase order while preserving the strictest
boundary:

```text
guide -> context -> direction -> plan -> execute -> QA -> use -> evaluate
-> improve proposal -> central update -> QA/canary
```

| Combination | Required behavior |
|---|---|
| `-help`, `-onboarding`, or `-explain` plus any mode | Explain the requested mode or lifecycle; do not perform it |
| `-ask -user` | Reflect the user lens, then ask at most one decision-changing question |
| `-audit -suggest` | Audit first; recommendation must answer the audit |
| `-audit -plan` | Pressure-test direction, then plan only the surviving route |
| `-discuss -explore` | Open options while remaining conversation-locked |
| `-discuss -suggest` | Recommend, then remain conversation-locked |
| `-discuss -plan` | Discuss briefly, state assumptions, then provide the plan without writes |
| `-explore -plan` | Map plausible routes, narrow, then plan the selected/recommended route |
| `-research -suggest` | Resolve the named gap, then recommend from evidence |
| `-plan` | Current actionable slice, dependencies, validation, gate, completion test |
| `-plan all` | Complete three-to-seven-milestone journey with owners and acceptance checks |
| `-plan full` or `full -plan` | Milestones plus tasks, paths, sequencing, validators, rollback, handoff |
| `-plan proceed` | Plan first; execute only inside visible scope and passed host gates |
| `proceed all` | Require a selected plan/lane; never bind by recency alone |
| `auto proceed` | Current-turn continuation only unless a separate loop contract exists |
| `-qa -evaluate` | QA the build first; evaluate impact only from separate credible use evidence |
| `-evaluate -improve` | Evaluate, then create a proposal from supported findings; no writes |
| `-improve proceed` | Require a visible complete plan and bounded local lane |

When tokens conflict, preserve the more restrictive behavior. A read-only
guide, discussion lock, missing evidence, or hard gate cannot be overridden by
a later `proceed` token.

## Lifecycle State Model

| State | Question | Typical mode | Exit evidence |
|---|---|---|---|
| Direction | Is this the right problem and route? | `-audit`, `-discuss`, `-explore`, `-research`, `-suggest` | selected direction and known assumptions |
| Commitment | What journey and current slice are visible? | planning depth | owners, dependencies, gates, acceptance checks |
| Build | Was the bounded work executed? | `proceed` | changed artifacts and implementation proof |
| Quality | Was it built correctly? | `-qa` | requirements/tests/edge/safety verdict |
| Use | What happened in real use? | observation outside this skill | minimal redacted use evidence |
| Impact | Should it be kept or changed? | `-evaluate` | keep/iterate/simplify/observe/rollback/retire/scale |
| Improvement | What smallest rule should change? | `-improve` | reviewed proposal and regression case |
| Release | Is the version safe for a named receiver? | host release process | version, hashes, canary, receipt, rollback |

Do not use QA as impact evidence. Do not use evaluation as build QA. Do not use
improvement as automatic execution.

## Safe Current-Turn Work

Inside a named visible lane, safe work is usually:

- read-only inspection;
- requested local planning and documentation;
- bounded source edits on claimed paths;
- deterministic tests, fixtures, privacy checks, and validators;
- reversible local artifact generation; and
- evidence and handoff preparation.

Safe does not mean automatically authorized. The action must still be within
the named goal and project boundary.

## Hard Gates

Stop and name the host-owned boundary before:

- external communication, uploads, or publication;
- cloud/service writes, including Drive and Trello;
- connector installation or authentication;
- secrets, credentials, pairing, or permission changes;
- provider spend or live remote canaries;
- runtime, default, production, deployment, or cutover changes;
- destructive actions, deletion, retention, or archive moves;
- Git remote, push, merge, tag, release, or publication;
- client-facing or Figma mutation;
- root authority, architecture, or broad multi-owner rollout; and
- plugin transfer, installation, update, removal, device canary, or user rollout.

The core identifies these boundaries but does not own their decision process.

## Proceed Preflight

Before execution, answer internally:

1. What exact lane and outcome are visible?
2. For which user, device, project, or audience is the work scoped?
3. Are dependencies and resource claims current?
4. Which files and systems are in scope?
5. Could the action create an external effect, spend, or privacy exposure?
6. Is a retry allowed?
7. What proof and rollback exist?
8. What exact condition ends this continuation?

If live mutation invalidates a hash, dependency, reviewed packet, or privacy
assumption, fail closed and refresh the plan or evidence.

## Portable Device Boundary

A package is an onboarding input, not the control plane:

```text
named receiver and compatible host
-> trusted package source and immutable checksum
-> host-managed transfer and install
-> fresh-task trigger, abstention and authority canary
-> explicit capability and project-binding receipts
-> stable promotion or rollback
```

Every receiver/device receives a unique reference and receipts. It inherits no
credentials, connectors, client access, project role, data scope, or previous
device authority.

Codex marketplace installation is the verified plugin route. Cursor and other
Agent Skills hosts may use a generated file-layout adapter only when the host
documents the selected discovery directory. A successful copy is adapter
proof, not a claim that every provider or remote worker loaded the skills.

## Central Source And Release

The editable command front door lives at:

```text
starter_workspace/plugins/yeem01-workflow-core
```

The released plugin is a generated projection of that front door plus the
allowlisted canonical owners under `starter_workspace/skills/`. The packaged
`BUNDLE_MANIFEST.json` names every included owner and source-tree hash. A receiving device
and later devices receive versioned packages; installed copies and old releases
are never edited in place.

## Improvement Proposal Contract

The core may grow only through evidence-backed proposals:

```text
explicit minimal feedback
-> redact client, personal and credential data
-> record recurring friction in a small structure
-> propose one bounded behavior change and non-goals
-> identify owner and authority impact
-> add a failing/expected regression fixture
-> update the Yeem01 source in a host-owned lane
-> QA and run a named canary
-> accept, revise or reject
-> version and preserve rollback
```

Required proposal fields:

```text
proposal_id:
affected audience and command:
user problem:
redacted evidence and recurrence:
confidence and alternatives:
proposed rule / non-goals:
authority and privacy impact:
regression fixture:
implementation / QA / canary:
rollback:
owner decision:
```

Default evidence excludes raw transcripts. Never collect work patterns
silently, centralize client data, score employees, identify sensitive traits,
self-edit, auto-accept, or auto-release.

## Fallback Output Contracts

Audit/advice:

```text
verdict / evidence and assumptions / strongest challenge / recommendation
/ cheapest validation / decision needed
```

QA:

```text
scope / requirements / tests and proof / defects by severity / limitations
/ pass|conditional|fail / remaining gate
```

Evaluation:

```text
decision / credible use evidence / inference / harms and trade-offs
/ keep|iterate|simplify|observe|rollback|retire|scale / next measurement
```

Execution:

```text
completed / impact / proof / not performed / remaining gate
/ next exact decision
```

Do not call maintenance, scaffolding, or generated-view refresh progress unless
it reduced a real risk or unlocked an outcome.
