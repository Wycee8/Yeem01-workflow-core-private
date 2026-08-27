# Yeem01 Workflow Core Use Manual — `0.6.1`

## What The Pack Does

Yeem01 Workflow Core gives authorized devices a consistent command front door
and the same ten portable workflow owners used for common Yeem01 operations. It
helps a user decide, discuss, plan, execute a bounded lane, verify build quality,
observe real use, evaluate impact, and propose the next improvement.

It does not carry Yeem01's whole workspace. It provides no credentials,
connectors, project role, client authority, publication right, provider spend,
or permission to change an external system.

## Included Skills

### 1. `yeem01-workflow-core`

**Job:** command front door, onboarding, composition and host boundaries.

**Use it when:** Will uses an explicit workflow token, asks for onboarding, or combines discussion, planning, execution and assurance modes.

**Boundary:** Preserves command semantics but supplies no project authority, credentials, connector access or external-action permission.

### 2. `audit-check`

**Job:** direction audit and impact evaluation.

**Use it when:** pressure-testing a direction before commitment or judging impact after credible use.

**Boundary:** Does not replace post-build QA and does not execute an improvement.

### 3. `workspace-implementation-planning`

**Job:** current-slice, milestone and full planning.

**Use it when:** turning approved intent into -plan, -plan all or -plan full.

**Boundary:** Plans the work but does not execute it.

### 4. `artifact-lane-output-defaults`

**Job:** operator artifact and summary contracts.

**Use it when:** making plans, audits, QA and handoffs readable with clear proof and decision gates.

**Boundary:** Shapes outputs but creates no project or execution authority.

### 5. `quality-check`

**Job:** post-build quality assurance.

**Use it when:** checking whether completed work was built correctly before handoff or close.

**Boundary:** Does not infer real-world impact from build evidence.

### 6. `improve`

**Job:** evidence-backed improvement proposals.

**Use it when:** turning observed friction or evaluation findings into a ranked, bounded proposal.

**Boundary:** Does not silently self-edit, accept or release a change.

### 7. `pipeline`

**Job:** portable reusable workflow and Double Diamond routing.

**Use it when:** running a complete reusable workflow or shaping uncertain work through staged discovery and delivery.

**Boundary:** Coordinates stages but does not replace the specialist that owns the deliverable.

### 8. `research`

**Job:** evidence-backed research workflows.

**Use it when:** resolving a named evidence gap or producing a sourced investigation.

**Boundary:** Must not fabricate evidence or treat research as permission for external action.

### 9. `project-charter-docs`

**Job:** durable project charter and authority context.

**Use it when:** creating or refreshing durable project context and authority packs.

**Boundary:** Records accepted authority; it does not create approval or authorization.

### 10. `user-skill`

**Job:** user-first durable skill/change gate.

**Use it when:** checking that a durable skill or workflow change begins with the user's job and evidence.

**Boundary:** Uses supplied or authorized context only and does not infer sensitive traits.

`-discuss`, `-explore`, `-suggest`, `-ask`, and bounded `proceed` belong to the
`yeem01-workflow-core` front door. They are behaviours, not additional bundled
skill folders.

## Command Map

| Command | What it does | Default boundary |
|---|---|---|
| `-help <command>` | Explains a command with one example | Guide only |
| `-onboarding` | Introduces setup, workflow and a safe practice | Guide only |
| `-explain <target>` | Explains purpose, flow and limits | Guide only |
| `-ask` | Asks one decision-changing question at a time | Conversation only |
| `-user` | Makes the intended user's job and constraints visible | Authorized context only |
| `-audit` | Pressure-tests a direction before commitment | No implementation |
| `-discuss` | Refines a working hypothesis together | Conversation-locked |
| `-explore` | Maps plausible options, unknowns and cheap probes | No commitment by itself |
| `-suggest` | Recommends one route and its strongest challenge | Advice only |
| `-research` | Resolves a named evidence gap | Evidence only |
| `-plan` | Plans the current actionable slice | No execution |
| `-plan all` | Plans the complete three-to-seven-milestone journey | No execution |
| `-plan full` | Adds tasks, paths, validators, rollback and handoff | No execution |
| `proceed` | Continues one visible bounded lane | Host rules still apply |
| `proceed all` | Continues dependency-valid work in an approved plan | Never unlimited authority |
| `-qa` | Checks whether completed work was built correctly | Post-build evidence |
| `-evaluate` | Judges value after credible use | Post-use evidence |
| `-improve` | Proposes the smallest evidence-backed change | No writes by default |

## Complete Audit-To-Improvement Workflow

Scenario: an associate proposes a shared campaign-brief workflow.

1. Pressure-test the direction:

   ```text
   -audit the shared campaign-brief workflow before we commit
   ```

2. Refine and open the option space:

   ```text
   -discuss and -explore how a strategist and associate would use it
   ```

3. Plan the complete journey:

   ```text
   -plan all the surviving route, including owners, gates and acceptance checks
   ```

4. Build only a named safe slice when the host permits it:

   ```text
   proceed with milestone one only; stop before external writes
   ```

5. Verify the build:

   ```text
   -qa the completed milestone against its acceptance checks
   ```

6. Use it and record only minimal redacted observations.

7. Judge impact:

   ```text
   -evaluate the workflow using these redacted observations
   ```

8. Propose the smallest change:

   ```text
   -improve the recurring handoff ambiguity found in the evaluation
   ```

9. A maintainer updates the canonical Yeem01 owner, adds a regression case,
   releases a new version and reruns QA and a fresh-session canary.

## Audit, QA And Evaluation Are Different

| Stage | Question | Evidence |
|---|---|---|
| `-audit` | Is this the right direction before commitment? | Assumptions, options, risks and cheap validation |
| `-qa` | Was the completed work built correctly? | Requirements, tests, edge cases and implementation proof |
| `-evaluate` | Did it create value in credible use? | Real observations separated from inference |

A passing QA is not impact evidence. Missing impact evidence produces an
observation plan, not an invented evaluation.

## Using The Pack By Provider

- Codex: subscribe to the private marketplace and install the plugin. The
  plugin exposes all ten skills together.
- Cursor local: clone the private channel and run
  `scripts/install_agent_skills.py --provider cursor`. Start a new chat.
- Compatible Agent Skills host: use the adapter with an explicit directory
  whose name is `skills`. The host must document that it discovers Agent
  Skills there; the pack does not claim universal provider compatibility.
- Remote or cloud agents: prefer project-scoped skills or a prepared worker
  image. A local user-scope install does not prove remote-worker availability.

See `SUBSCRIBER_SETUP.md` for exact commands and security choices.

## Feedback And Central Improvement

Submit only a minimal redacted note containing the audience class, command and
intended outcome, friction, recurrence, observable effect, redaction
confirmation and an optional rule suggestion. Never submit raw transcripts,
credentials, client data, sensitive personal information or employee scores.

The maintainer decides whether the evidence belongs in the shared core. Users
do not edit installed copies, and the pack does not learn or release itself.

## First Safe Practice

Use fictional data in a new task:

```text
-audit then -plan all a fictional weekly content-review workflow. Explain the
host boundaries and stop before execution.
```

The response should audit first, show the complete milestone journey and make
no writes.
