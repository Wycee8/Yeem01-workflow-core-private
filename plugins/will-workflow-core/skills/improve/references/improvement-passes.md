# Improve Passes

Use this reference when an improvement target needs evidence before ranking.
Keep the pass compact in the final answer unless the operator asks for detail.

## Pass Sequence

| Pass | Question | Output |
|---|---|---|
| Target bind | What exactly is being improved, and why? | Target, type, quality goal, current weakness |
| Charter alignment | Does an owning project charter constrain or contradict the improvement? | aligned / stale / conflict / charter_missing / not_applicable |
| Usage audit | How is it currently used? | Current usage evidence and friction |
| Shape map | What is the target's current structure? | Purpose, owner, modes, routes, outputs, validation |
| User-first audit | Does it serve the user before the system? | Use / Clarify / Reduce / No-op style verdict |
| Efficiency audit | Is the build or behavior technically/workflow efficient? | Efficiency finding and likely repair |
| Bloat audit | Is the improvement larger than necessary? | Delete / absorb / merge / shrink / reference-only / ok |
| Ask or rank | Is a decision missing? | One scoped question, or top 3 ranked options |
| Plan and discuss | What would the complete change require? | Phases, affected surfaces, risks, validation, rollback, exclusions, and approval gate |
| Route or proceed | Is the displayed plan explicitly approved, and who owns it? | Discussion/revision, or specialist execution followed by QA |

## Usage Evidence By Target Type

| Target type | Check current usage by looking at |
|---|---|
| Skill, routing behavior, command mode | Recent visible invocations, trigger phrases, near-miss phrases, operator corrections, transcript snippets when explicitly scoped, `skills/HUB_MAP.md`, `skills/SKILL_CALLING_FRAMEWORK.md`, generated skill index/registry visibility, linked references, validator output, and runtime availability caveat |
| Workflow or workspace system | Current source of truth, active work-item/state files, reports or views used by Will, handoff points, repeated manual steps, stale projections, and recovery or approval gates |
| UI/UX, Figma, viewer, surface | Primary user journey, first-screen question order, interaction/state coverage, rendered evidence, design-system fit, accessibility, responsive behavior, and whether the surface starts from user questions before internal artifact categories |
| Code/app implementation | Entry points, current callers, tests, build/lint commands, error logs, repeated defects, local architecture, dependency boundaries, and post-build `quality-check` needs |
| Marketing, content, creative, asset, campaign | Audience, claim, channel, offer, asset use context, creative references, approval state, production constraints, and expected market/user reaction |
| Business plan, strategy, offer, startup idea | Decision being improved, assumptions, evidence quality, strongest alternatives, validation cost, timing, and whether research would change the verdict |
| Long-running improve-toward-goal loop | Goal contract, allowed actions, cadence, hard stops, material-progress signal, current loop/runtime status, and whether `adam-auto-loop` owns the work |
| Recurring operating lesson | Repeated pattern, future-session beneficiary, target skill/artifact, smallest reversible behavior change, and whether `self-evolve` should absorb the lesson |

## Conditional Charter Alignment

For project-scoped targets, resolve the project through indexes or registries,
read `PROJECT_BRIEF.md` first when present, and load `PROJECT_CHARTER.md` only
when the brief is insufficient or durable project behavior may change. Check
goal, current state, scope, non-goals, authority, active decisions, and
validation gates. Companion files are progressive-disclosure evidence, not a
default bundle load.

Skip this pass for isolated non-project artifacts, generic advice, and targets
without persistent project context. Higher authority wins over charter text;
route stale or conflicting charter context to `project-charter-docs` and do not
treat it as approval to execute.

## Skill Target Checklist

When the target is a skill or routing behavior, check:

1. Current calls: how Will phrases the need, including aliases and compact flags.
2. Recent usage: visible session examples first; read transcripts only when the
   request scopes them or the evidence is necessary and safe.
3. Interaction pattern: whether the skill should discuss, ask, audit, plan,
   execute, or route.
4. Wiring: frontmatter description, hub-map route, calling-framework pattern,
   registry/index visibility, linked references, validators, and near-miss
   boundaries.
5. Shape: job, modes, inputs, outputs, owner route, approval gates, validation,
   and runtime caveat.
6. User-flow: whether the skill answers Will's natural first question before
   exposing internal implementation categories.
7. Efficiency: whether repeated reasoning should become a reference, trigger
   test, output contract, or deterministic helper.
8. Bloat: whether the change can be a smaller edit to an existing skill,
   reference, trigger test, or route note instead of a new skill or system.

## User-First Audit

Use this order:

1. Will/operator value: does the improvement reduce decision load, review
   friction, context switching, repeated correction, or control burden?
2. Downstream user value: for product, content, creative, client, or viewer
   targets, does the change improve the real user's task or experience?
3. Flow fit: does the target start from the user's question and next action,
   or from internal artifact categories?
4. Misalignment: flag when the target prioritizes building, routing elegance,
   dashboards, abstractions, or polish before a usable outcome.

Verdicts:

| Verdict | Meaning |
|---|---|
| Use | The improvement directly improves user value and is proportionate. |
| Clarify | The user, job, target, or quality bar would change the action. |
| Reduce | The direction is useful but should be smaller or absorbed. |
| No-op | The improvement is not justified by current evidence. |

## Efficiency Audit

Check for:

- repeated manual reasoning that belongs in a compact reference or test case;
- duplicated routes, overlapping skill ownership, or unclear specialist owner;
- avoidable context loading from putting long examples in `SKILL.md`;
- weak validation, missing trigger tests, or no proof path;
- fragile handoff between diagnosis, proceed, specialist execution, and QA;
- missing deterministic helper only when repeated checks are structured and
  error-prone;
- technical debt that blocks the target's actual user value.

Prefer the smallest repair that improves throughput or reliability.

## Bloat Audit

Before recommending creation, ask whether the improvement can be:

| Tag | Use when |
|---|---|
| delete | The requirement or step is unnecessary. |
| absorb | Existing skill, artifact, route, or native capability can own it. |
| merge | Two adjacent pieces duplicate one job. |
| shrink | A smaller version creates the same user value. |
| reference-only | A reference or test case is enough; root instructions should stay lean. |
| ok | No unnecessary surface is being added. |

Do not call necessary safety, validation, accessibility, recovery, or approval
work bloat merely because it adds structure.

## Ranking Rule

Rank options after the passes, not before them. Use the normal improve criteria:

1. User/operator value.
2. Leverage against the quality goal.
3. Reversibility.
4. Validation clarity.
5. Risk and approval burden.
6. Fit with existing skill ownership.

If the strongest option is gated or missing evidence, recommend the cheapest
evidence-gathering or reduction step instead of silently choosing a weaker
implementation.

## Compact Output Add-On

Use these lines in the diagnosis when evidence-first passes matter:

```text
Current weakness:
Current usage:
Current shape:
User-first: Use / Clarify / Reduce / No-op - ...
Efficiency:
Anti-bloat: delete / absorb / merge / shrink / reference-only / ok - ...
```
