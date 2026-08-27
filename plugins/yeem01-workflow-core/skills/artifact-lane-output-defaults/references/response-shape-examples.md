# Artifact Response Shape Examples

Use this reference only when a lane owner needs examples beyond the root
contract. The root `SKILL.md` remains the authority for required behavior.

## Decision Gate

```markdown
**Decision Gate**
Decision needed: approve the staged cleanup plan.
Target preview: Phase 1 updates command-mode contracts; Phase 2 refreshes registry; Phase 3 validates fleet.
What this does for Will/user: makes the plan reviewable in chat.
What approval allows: local doc and registry edits in the named files.
What approval does not allow: external sends, production changes, or unrelated rewrites.
Evidence / source: current workspace skill docs and validators.
```

Put the single exact reply phrase in the mandatory summary's final `Next`
bullet. Add a separate Decision Ask only when two or three distinct choices are
genuinely needed.

## Alignment-First `-plan all`

```markdown
**Goal and Milestone Check**

- Goal: make planning easier to understand and resume.
- Primary usable deliverable: one durable milestone roadmap that Will can steer and a future session can resume.
- Consumer and intended use: Will uses it to choose direction; the next worker uses it to continue the current milestone.
- Minimum useful completed set: the two remaining deliverables, current focus, human-input gates, and acceptance proof.
- Representative finished example: M1 is a usable persistent plan that Will can steer and a future session can resume.
- Acceptance proof: Will can identify what he receives, what decision is needed, and what evidence closes each milestone without reading technical controls.
- Finish line: Will can steer the complete journey without reading task-level controls.
- Milestone arc: usable persistent plan -> independent behavior result.
- Current position: the direction brief is accepted; M1 is the first remaining outcome.
- On track: Yes - the current milestone directly unlocks independent behavior proof.
- Need from Will: None. Alignment is locked from the approved project goal and current canonical plan.

| Milestone deliverable | What it enables | Need from Will | Accepted when | State |
| --- | --- | --- | --- | --- |
| M1 - Usable persistent plan | Will can steer the journey and a future session can resume it | None now | Will can identify each remaining outcome, decision, and acceptance condition without reading task-level controls | Current |
| M2 - Independent behavior result | Will can decide whether the planning behavior is ready for routine use | None now | The fixed fresh-context canary follows the deliverable-first route across its boundary cases | Planned |

**Current focus**

- Complete M1, then run focused contract checks and the fixed fresh-context canary.
- Human input: none; the approved boundary-case pack supplies the test prompts.
```

Use `-plan full` to add the task/path/dependency/validator table. Do not add a
separate critical path when the milestone order already expresses it.

When the goal, primary usable deliverable, consumer or intended use, minimum
useful set, acceptance proof, finish line, milestone arc, owner, or approval
boundary is materially ambiguous, keep the same first section, show concrete
deliverable interpretations and one recommendation, ask one exact question,
and stop before architecture, this milestone table, or any approval phrase.

## Critical Path

```markdown
| Order | Phase / Work Item | Why Critical | Depends On | Gate / Stop Risk | Validation | Next Action |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Patch owner contracts | Unlocks consistent behavior | Approved scope | Mixed ownership | Skill validators | Edit scoped docs |
| 2 | Refresh registry | Makes generated views match source | Owner patches | Registry drift | Registry validator | Regenerate |
| 3 | Fleet validation | Proves batch is safe | Registry refresh | Failed validator | Audit and scan | Report next target |
```

## Summary Footer

```markdown
**-summary**

- **Outcome:** The scoped skill update is ready for review without opening raw files.
- **State:** Needs decision — local checks pass, but independent behavior has not been observed.
- **Boundary:** Specialist ownership and gates remain unchanged.
- **Next:** Need from Will — reply `Approve the next target` or name the revision.
```

Use extra bullets only when they add a separate decision, limit, proof ceiling,
or resume fact. Do not expand this example back into one field per checklist
item.

## Adaptive Summary Modes

### Subject overview

```markdown
**-summary**

- **Outcome:** The audit recommends simplifying the existing owner.
- **Why it matters:** Fewer layers make the operator route easier to understand.
- **State:** Needs decision — no implementation has started.
- **Recommendation:** Keep one owner and remove the duplicate entry path.
- **Evidence ceiling:** The audit proves overlap, not post-change usefulness.
- **Next:** Need from Will — approve the bounded simplification or revise it.
```

### Plan review

```markdown
**-summary**

- **Outcome:** The goal and five-deliverable journey are aligned.
- **Why it matters:** Will can steer the complete path without reading task-level controls.
- **State:** In progress — milestone 2 is current.
- **Goal and milestone:** Deliver the verified review capability; the contract is being implemented now.
- **Decision:** None now; independent evaluation remains separately gated.
- **Proof:** The approved plan defines each deliverable and acceptance condition.
- **Next:** Continuing now — complete milestone 2 inside the approved boundary.
```

### Implementation/result review

```markdown
**-summary**

- **Outcome:** The local repair is complete and the broken route now resolves correctly.
- **Why it matters:** Users reach the intended owner without manual recovery.
- **State:** Done locally — no deployment occurred.
- **Changed:** The route and focused regression now agree.
- **Limit:** Production behavior has not been observed.
- **Proof:** Focused and registry checks pass at the local evidence ceiling.
- **Next:** Recommended — authorize a separate live canary if production evidence is needed.
```

### Continuity/handoff review

```markdown
**-summary**

- **Outcome:** The approved implementation is complete and ready for independent review.
- **Why it matters:** The next owner can resume without repeating research or build work.
- **State:** In progress — observation remains separately gated.
- **Decisions:** One existing owner, four modes, and the local acceptance corpus are locked.
- **Current state:** Local tests pass; no fresh-context result exists.
- **Resume point:** Start the isolated evaluator from the supplied case pack.
- **Next:** Need from Will — authorize one fresh-context evaluator when ready.
```

### Adversarial failures

Reject a summary when it:

- calls a proposal approved or an untested implementation ready;
- leads with a passing-test total while hiding a hard failure;
- drops the open decision or changes the requested next action;
- shows hashes, IDs, or validator inventories that do not affect Will's
  decision;
- uses a plan summary for a handoff and omits the exact resume point;
- invents follow-up work when the correct terminal state is `None`.

## Operator-First Reporting

### Scored technical result

Avoid:

```markdown
Candidate A and the local baseline tied at 211; the current composer scored 113.
56/56 tests pass.
```

Use:

```markdown
The current composer is not ready for promotion. Two candidate designs cover
substantially more of the required reading structure, but neither can yet prove
that every interpretation came from the correct source data and calculation
configuration. The traceability contract is now repaired; the next step is to
implement one candidate against it and review the resulting reading quality.

Control receipt:
- Score basis: 211 and 113 are sums of structural coverage points, not quality
  percentages.
- What the tests prove: all 56 contract and rejection checks pass.
- What the tests do not prove: the final readings are insightful,
  user-appropriate, or production-ready.
```

### Governance status

Avoid:

```markdown
`BLOCKED_AUTHORITY`. WI-123 remains at revision 607.
```

Use:

```markdown
The change cannot proceed because the source configuration has not been
approved. No implementation has started, so the current workspace remains
unchanged. The next decision is whether to approve that configuration or keep
the work parked.

Control receipt: `BLOCKED_AUTHORITY`; work item `WI-123`; revision `607`.
```

### Explicit receipt-only request

```markdown
Receipt-only: work item `WI-123` remains blocked at revision `607`; no files
changed and no retry was attempted.
```

### Control baselines with no operator meaning

Avoid:

```markdown
Current control baselines:
- P5 schema: 04ac0ed0f35cdd1db7bd427b14d4ab7eaf5cb17ad07171ce6f159621f9d7ca3a
- P5 validator: d2713c3580db5eea89401eb6c33a9404659695e41068d6a01f82beba10052776
```

Use:

```markdown
P5 is the only remaining decision. The local contracts pass, and the technical
baselines have been captured for the executor; you do not need to review them.

Control receipt: six baselines recorded; no source, production, or external
action occurred. Exact values remain in the durable handoff because no current
operator decision binds to them.
```

The fact that a packet lists P5 as a decision beside these baselines does not
make the decision hash-bound. Only show the exact values when the operator or
governing authority explicitly binds approval to them, or a verified mismatch
makes execution unsafe.

### Exact value justified by a blocker

```markdown
The repair cannot start safely because the source changed after the work was
approved. This may overwrite newer work, so execution is stopped until the
baseline is reviewed.

Control receipt: expected source hash `04ac...ca3a`; current source hash
`91fe...440c`; affected action: P5 schema repair.
```

### Explicit baseline receipt

```markdown
Receipt-only: P5 schema
`04ac0ed0f35cdd1db7bd427b14d4ab7eaf5cb17ad07171ce6f159621f9d7ca3a`;
P5 validator
`d2713c3580db5eea89401eb6c33a9404659695e41068d6a01f82beba10052776`.
Scope: baseline identity only; these values do not prove behavioral or
production readiness.
```
