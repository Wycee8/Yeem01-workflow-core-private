# Will Workflow Core Onboarding

Use this guide for `-onboarding`, a new user or device, or a request to explain
the complete workflow.

## What It Is

`will-workflow-core` is Will's command front door for consistent work with
Codex. The released plugin also carries the portable operator owners for
audit/evaluation, planning, output defaults, QA, improvement, pipelines,
research, charters, and user-first skill-change checks. An explicit token such
as `-audit`, `-plan all`, or `-qa` selects the method and routes to the relevant
bundled or host owner.

It is useful for:

- checking a direction before committing;
- discussing or exploring without accidental execution;
- choosing the right planning depth;
- continuing a visible bounded lane;
- checking build quality separately from real-world impact; and
- turning repeated friction into a small, reviewable improvement proposal.

It does not provide tools, connectors, credentials, project roles, client
data, device access, publication rights, installation authority, or external
action authority. Those remain with the host workspace and its owner.

## Where It Comes From

The command front door is edited in the Yeem01 workspace at:

```text
starter_workspace/plugins/will-workflow-core
```

The release builder adds allowlisted canonical skill directories from
`starter_workspace/skills/` and records their exact inventories and hashes.
AT-Will and later compatible devices receive versioned generated packages,
not editable copies that drift independently.

## Getting Started

The handoff package is a small local Codex marketplace. Setup is:

1. receive one versioned archive and checksum through the chosen private
   transfer path;
2. verify and extract it;
3. add the extracted directory as a local marketplace;
4. install `will-workflow-core@will-private`; and
5. start a fresh task and enter `-onboarding`.

The exact verified commands and rollback steps live in that release's
`AT_WILL_HANDOFF.md`. Installing the package does not copy the full Yeem01
workspace, credentials, connectors, project data, domain systems, or another
device's settings.

## How To Invoke It

Put one or more explicit tokens in the request:

```text
-audit this proposed workflow before we build it

-discuss and -explore the options with me

-plan all the surviving route, including gates and acceptance checks

proceed with the current bounded local slice

-qa the completed implementation

-evaluate the workflow after we have credible use evidence

-improve this recurring workflow friction
```

Ordinary nouns do not activate commands. "Audit log", "research paper", and
`plan.png` are not command invocations.

## Compact Command Map

| Command | Use it for | Default boundary |
|---|---|---|
| `-help <command>` | Short command guide and example | Guide only |
| `-onboarding` | Setup, lifecycle, and practice flow | Guide only |
| `-explain <target>` | Purpose, flow, limits, example | Guide only |
| `-ask` | One high-value question at a time | Conversation, no assumed writes |
| `-user` | Make the intended user and job visible | Authorized context only |
| `-audit` | Pressure-test direction before commitment | No implementation |
| `-discuss` | Refine together | Conversation-locked |
| `-explore` | Map options, unknowns, and cheap probes | No decision or execution by itself |
| `-suggest` | One best recommendation plus challenge | Advice only |
| `-research` | Resolve a named evidence gap | Evidence only |
| `-plan` | Current actionable slice | No execution |
| `-plan all` | Complete three-to-seven-milestone journey | No execution |
| `-plan full` | Journey plus tasks, paths, validators, rollback, handoff | No execution |
| `proceed` | Continue the current visible bounded lane | Host rules still apply |
| `proceed all` | Continue dependency-valid work in a selected plan | Never unlimited authority |
| `-qa` | Verify completed work was built correctly | Post-build proof |
| `-evaluate` | Judge impact after credible use | Post-use evidence |
| `-improve` | Propose the smallest evidence-backed improvement | No writes by default |

`auto proceed` and `Adam proceed` mean bounded current-turn continuation. They
do not create an unattended loop.

## Worked Audit-To-Improvement Example

Scenario: a BOOOOM operator proposes a shared campaign-brief workflow.

### 1. Audit the direction

```text
-audit the shared campaign-brief workflow before we commit
```

Expected: a verdict, case for and against, assumptions, risk, options, and the
cheapest useful validation. No build occurs.

### 2. Discuss and explore

```text
-discuss and -explore how a strategist and an associate would use it
```

Expected: user tensions, plausible routes, edge cases, and at most one useful
question at a time. The conversation remains uncommitted.

### 3. Plan the whole journey

```text
-plan all the surviving route, including owners, gates and acceptance checks
```

Expected: three to seven milestones from foundation through use and review,
plus the current slice. No implementation occurs.

### 4. Continue one bounded slice

When the host workspace permits the named work:

```text
proceed with milestone one only; stop before external writes
```

Expected: local, reversible work, followed by proof, what was not performed,
and the next host boundary.

### 5. QA the build

```text
-qa the completed milestone against its acceptance checks
```

Expected: requirements, behavior, edge cases, safety/privacy, evidence,
defects by severity, limitations, and a pass/conditional/fail verdict.

QA answers: "Did we build it correctly?"

### 6. Use and observe

Use the workflow in its intended context. Record only the intended outcome,
command used, friction, recurrence, and observable result. Remove client,
personal, and credential data. Raw transcripts are not the default evidence.

### 7. Evaluate impact

```text
-evaluate the workflow using these redacted observations
```

Expected: observed evidence separated from inference and one decision: keep,
iterate, simplify, observe, roll back, retire, or scale.

Evaluation answers: "Did it help in credible use?"

### 8. Propose an improvement

```text
-improve the recurring handoff ambiguity found in the evaluation
```

Expected: up to three ranked opportunities and one smallest high-value
proposal, including privacy impact, a regression fixture, implementation,
QA, canary, and rollback. The core is not edited by this command.

### 9. Update centrally and verify again

A maintainer applies an accepted proposal to the Yeem01 source, bumps the
version, adds the regression fixture, generates a new package, and runs `-qa`.
The receiving device updates only to that versioned package; it does not edit
its installed copy.

## Why QA, Evaluation, And Improvement Are Separate

```text
QA:         Was it built correctly?
Evaluation: Did it create value in credible use?
Improve:    What smallest reviewed rule should change next?
```

A passing QA cannot prove user impact. A weak outcome does not automatically
prove a build defect. An improvement proposal does not edit or release the
core.

## Simple Improvement Feedback

An associate can submit one minimal, redacted note:

```text
-improve using this note:
role or audience class:
command and intended outcome:
friction observed:
recurrence count:
observable effect:
client, personal and credential data removed: yes|no
suggested rule, if any:
```

The maintainer converts supported feedback into a Yeem01 source change and a
new regression fixture. Notes are not raw session logs or employee performance
records.

## First Safe Practice

Use fictional, non-sensitive content in a fresh task:

```text
-audit then -plan all a fictional weekly content-review workflow. Explain the
host boundaries and stop before execution.
```

Check that the response audits first, presents the complete journey, names the
current slice and boundaries, and performs no writes.

## When To Stop

Stop and name the exact host-owned boundary before contacting another person,
writing to a service, uploading, publishing, deploying, spending, pushing,
merging, installing, changing credentials or permissions, deleting data, or
exposing private, client, personal, or employee-sensitive information.
