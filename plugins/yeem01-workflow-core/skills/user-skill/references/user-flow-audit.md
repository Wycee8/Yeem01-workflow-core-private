# User-Flow Audit

Use this reference for interactive systems, multi-step surfaces, dashboards,
viewers, review flows, and transactional journeys. For static assets and
identity work, check purpose and decision fit only; do not invent navigation.

## Contents

- [Authority and scope](#authority-and-scope)
- [Required scenarios](#required-scenarios)
- [Audit dimensions](#audit-dimensions)
- [Evidence levels](#evidence-levels)
- [Verdicts and blockers](#verdicts-and-blockers)
- [Metrics](#metrics)
- [Output contract](#output-contract)

## Authority and scope

Resolve current project authority before reviewing a durable product flow.
Treat root authority, the current charter, UI/UX authority, and current plan as
truth above this procedure. The audit tests the experience; it does not create
product intent or reopen locked decisions.

Name the user, task, start state, intended outcome, and cost of failure. If
these cannot be resolved, return an evidence gap instead of inventing a flow.

## Required scenarios

Walk at least these three scenarios at decision scale:

1. **Primary task** — enter, progress, and complete the main user job.
2. **Escape or switch** — leave an unwanted path or move to another intended
   action without forced completion or avoidable loss.
3. **Error or interruption** — encounter a realistic failure or interruption,
   recover, and resume with recoverable work preserved.

Use real task steps, not a generic heuristic list. Add scenarios only when
project risk justifies them.

## Audit dimensions

### Intent and entry

- Can the intended user tell what the surface is for and where to begin?
- Does the entry state match the user's goal rather than internal structure?

### Next action

- Is the likely next action visible, understandable, and connected to the goal?
- Does the user know the consequence before acting?

### Control and escape

- Can the user cancel, close, go back, undo, leave, or switch paths?
- Is recoverable work preserved?
- Are irreversible or high-cost commitments reviewable or confirmable?

### Alternative access

- Can the user reach another intended action through appropriate navigation,
  search, shortcut, or an equivalent route?
- Do not require multiple routes when the task is an ordered safety or
  completion sequence.

### Orientation and status

- Can the user tell where they are, what changed, what remains, and how to
  return?
- Are progress, loading, success, blocked, and stale states understandable?

### Error and recovery

- Are likely costly errors prevented?
- Are errors explained in task language, repairable, and resumable?
- Does correction retain valid input and context?

### Completion and continuation

- Is success unmistakable?
- Is the appropriate next downstream action clear?
- Does the flow avoid accidental dead ends and duplicate submissions?

### Accessibility and efficiency

- Can the flow be completed with keyboard and logical focus?
- Are there no keyboard traps, hidden focus changes, redundant entry, or
  unpredictable navigation?
- Does the design support repeat use without making first use obscure?

## Evidence levels

Label the strongest evidence actually inspected:

1. **Source inspection** — authority, copy, code, nodes, or specification.
   Predicts likely behavior but does not prove usability.
2. **Task walkthrough** — current rendered or interactive output walked with
   fresh task intent. Tests discoverability and behavior but is not
   representative-user validation.
3. **Observed use** — representative users or real telemetry. Supports outcome
   claims only within the observed context and sample.

When observed use could change a consequential verdict, route first to a
read-only research definition: name the user group, task, evidence question,
method, downstream decision, and approval boundary. Recruiting participants,
contacting users, instrumenting production, or collecting external data is a
later hard-gated action; do not treat the initial research handoff itself as
authorization for those actions.

Never describe source validity, node existence, dimensions, clean code, a
self-review, or a fixture-informed prediction as user validation.

## Verdicts and blockers

Classify each scenario:

- `PASS` — the task succeeds without material flow defect.
- `FRICTION` — the task succeeds but a named issue adds avoidable effort,
  uncertainty, or recovery cost.
- `BLOCK` — the user cannot safely or reasonably complete, escape, recover, or
  comply with locked authority.

Do not average away blockers. A failed primary task, inaccessible escape,
keyboard trap, unrecoverable commitment, lost recoverable work, or
locked-authority conflict fails the review.

When Design owns the overall review, preserve its `APPROVE`, `REVISE`,
`RETHINK`, and `DEFER` verdicts. Scenario results are diagnostic evidence, not
a second overall verdict system.

## Metrics

Use only measures that answer the current project question:

- primary-task completion;
- next-action recognition without prompting;
- wrong turns and backtracks;
- escape or switch success;
- recovery success and retained work;
- abandonment or drop-off;
- time or step count against a named comparison baseline;
- completion confidence or perceived ease;
- accessibility blockers;
- locked-authority deviations.

Do not introduce a universal UX score. Adoption, engagement, retention, and
satisfaction metrics require a project-specific observed-use plan and suitable
data.

## Output contract

Return:

```text
User-flow audit
User and task: <resolved user, start state, intended outcome>
Evidence: source inspection / task walkthrough / observed use
Primary task: PASS / FRICTION / BLOCK — <evidence>
Escape or switch: PASS / FRICTION / BLOCK — <evidence>
Recovery and resume: PASS / FRICTION / BLOCK — <evidence>
Accessibility: PASS / FRICTION / BLOCK / not applicable — <evidence>
Authority: aligned / provisional / conflict / missing
Smallest repair: <one highest-impact repair>
Recheck: <affected scenario plus primary-task replay>
```

Lead with the user consequence. Name the failed step and evidence; avoid
ceremonial checklist prose.
