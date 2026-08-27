# Yeem01 Workflow Core Use Manual — `0.7.0`

## What The Pack Does

Yeem01 Workflow Core gives a new device a consistent command front door and
the same ten portable workflow owners used for common Yeem01 operations. It
helps a user decide, discuss, plan, execute a bounded lane, verify build
quality, observe real use, evaluate impact and propose the next improvement.

It does not carry Yeem01's whole workspace. It provides no credentials,
connectors, project role, client authority, publication right, provider spend,
device authorization or permission to change an external system.

## Included Skills

### 1. `yeem01-workflow-core`

**Job:** command front door, onboarding, composition and host boundaries.

**Use it when:** a user invokes an explicit workflow token, asks for onboarding, or combines discussion, planning, execution and assurance modes.

**Boundary:** Preserves command semantics but supplies no project authority, credentials, connector access or external-action permission.

### 2. `audit-check`

**Job:** direction audit and impact evaluation.

**Use it when:** pressure-testing a direction before commitment or judging impact after credible use.

**Boundary:** Does not replace post-build QA and does not execute an improvement.

### 3. `workspace-implementation-planning`

**Job:** current-slice, milestone and full planning.

**Use it when:** turning accepted intent into -plan, -plan all or -plan full.

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

**Boundary:** Does not silently scan sessions, self-edit, accept or release a change.

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
| `-explore` | Maps options, unknowns and cheap probes | No commitment by itself |
| `-suggest` | Recommends one route and its strongest challenge | Advice only |
| `-research` | Resolves a named evidence gap | Evidence only |
| `-plan` | Plans the current actionable slice | No execution |
| `-plan all` | Plans the complete three-to-seven-milestone journey | No execution |
| `-plan full` | Adds tasks, paths, validators, rollback and handoff | No execution |
| `proceed` | Continues one visible bounded lane | Host rules still apply |
| `proceed all` | Continues dependency-valid work in a selected plan | Never unlimited authority |
| `-qa` | Checks whether completed work was built correctly | Post-build evidence |
| `-evaluate` | Judges value after credible use | Post-use evidence |
| `-improve` | Proposes the smallest evidence-backed change | No writes by default |

## Complete Audit-To-Improvement Workflow

Scenario: an associate proposes a shared campaign-brief workflow.

1. Audit the direction before commitment:

   ```text
   -audit the shared campaign-brief workflow before we commit
   ```

2. Discuss and explore how people would use it:

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

5. Verify the completed build:

   ```text
   -qa the completed milestone against its acceptance checks
   ```

6. Use it and record only minimal redacted observations.

7. Judge impact after credible use:

   ```text
   -evaluate the workflow using these redacted observations
   ```

8. Propose the smallest change:

   ```text
   -improve the recurring handoff ambiguity found in the evaluation
   ```

9. A maintainer updates the canonical Yeem01 owner, adds a regression case,
   builds a new version and reruns QA and a fresh-session canary.

## Audit, QA And Evaluation Are Different

| Stage | Question | Evidence |
|---|---|---|
| `-audit` | Is this the right direction before commitment? | Assumptions, options, risks and cheap validation |
| `-qa` | Was the completed work built correctly? | Requirements, tests, edge cases and implementation proof |
| `-evaluate` | Did it create value in credible use? | Real observations separated from inference |

A passing QA is not impact evidence. Missing impact evidence produces an
observation plan, not an invented evaluation.

## Using The Pack By Provider

- Codex CLI/Desktop: add the public marketplace pinned to `v0.7.0` and
  install the plugin.
- Cursor: clone the tagged public channel and run
  `scripts/install_agent_skills.py`; project scope is the associate default.
- Compatible Agent Skills host: use the adapter with an exact documented
  directory named `skills`.
- Remote or cloud agents: use project-scoped skills or a prepared worker image.
  A local user-scope install does not prove remote-worker availability.

File-layout compatibility does not prove that an untested provider discovers
or follows the skills. See `SUBSCRIBER_SETUP.md` for exact commands.

## Feedback And Central Improvement

Use `IMPROVEMENT_NOTE_TEMPLATE.md`. Submit only a minimal redacted note through
a private BM/YEEM channel designated by the maintainer. Never submit raw
transcripts, credentials, client data, sensitive personal information or
employee scores, and never place sensitive feedback in a public issue.

The maintainer decides whether evidence belongs in the shared core, updates the
canonical source, adds a regression fixture, builds a new immutable version and
runs QA. Users do not edit installed copies, and the pack does not passively
learn or release itself.

## First Safe Practice

Use fictional data in a new task:

```text
-audit then -plan all a fictional weekly content-review workflow. Explain the
host boundaries and stop before execution.
```

The response should audit first, show the complete milestone journey and make
no writes.
