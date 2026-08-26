# Summary Behavior Modes

Read this reference whenever composing an explicit `-summary` review or the
mandatory summary footer for an operator-facing artifact. The root `SKILL.md`
owns the stable response contract; this reference defines how the middle of the
summary adapts to the operator's review job.

## Summary Job

A summary is a review lens over current authority, not a replacement for the
source artifact. It should let Will answer, in one scan:

1. What is the result or subject?
2. Why does it matter?
3. What is its actual state or readiness?
4. Which decision-changing facts must be retained?
5. What happens next?

## Subject Resolution

For an explicit `-summary`, resolve the subject in this order:

1. the source, artifact, plan, run, or subject named in the current message;
2. the artifact or result just created or reviewed in the current turn;
3. one uniquely resolvable current source from the same conversation and
   project authority.

If two materially different subjects remain plausible, ask one exact question
and stop. Do not combine them or choose by recency. Subject recovery grants no
approval and cannot change canonical state.

For a mandatory footer, the subject is the completed action and its practical
consequence. Do not summarize the entire conversation again.

## Mode Selection

Choose the mode that answers the operator's current review question. Explicit
review intent outranks the source document's filename or original type.

| Mode | Use when | Required middle content |
| --- | --- | --- |
| Subject overview | Explaining, auditing, researching, recommending, or reviewing a mixed subject | two to four key points or decisions; the important limit when one exists |
| Plan review | Reviewing Plan All, a roadmap, proposal, milestone journey, or execution approval | governing goal; current milestone or position; primary deliverables; open decision or `None` |
| Implementation/result review | Reviewing a build, repair, QA result, canary, or completed change | what changed; practical impact; actual readiness; failed or untested area when material |
| Continuity/handoff review | Resuming, transferring ownership, closing context, or asking where work stands | governing goal; locked decisions; current state; unresolved items; exact resume point |

When signals conflict, choose the mode that serves the current decision. A Plan
All document reporting completed work uses implementation review; a handoff of
that work uses continuity review.

## Stable Review Spine

Every ordinary operator summary keeps these anchors in order:

1. `Outcome`.
2. `State`, with a plain readiness consequence when useful.
3. One terminal `Next`.

Add `Why it matters`, mode-specific fields, and `Proof` or `Evidence ceiling`
only when they carry meaning not already present in an anchor. Merge the
practical consequence into `Outcome` when that remains clear. Do not emit empty
or repetitive bullets to satisfy a fixed count. Normally use three to eight
short bullets and one decision-changing idea per bullet. Preserve an additional
decision-changing fact rather than obeying a hard word limit.

An explicitly requested receipt-only response may omit the ordinary spine. It
must identify itself as receipt-only, provide the requested controls, state
their scope, and say what they do not prove.

## Loss-Intolerant Preservation Gate

Before drafting, answer these questions from the source:

- What is the governing subject or goal?
- What is the primary outcome or usable deliverable?
- Which material decisions are locked, open, blocked, or still proposals?
- What is the actual state or readiness?
- Which limitation could change Will's decision?
- What is the strongest proof, and what is its evidence ceiling?
- What is the exact next action, owner, decision, or stop condition?

Reject and revise the draft when it contradicts one answer, omits an applicable
decision-changing answer, changes a proposal into an approval, invents
completion, or makes a broader readiness claim than the proof supports.

## Operator Relevance And Disclosure

Keep hashes, IDs, validator inventories, file lists, and other machine controls
out of the first screen unless they change Will's decision, explain a blocker,
bind an approval, identify the deliverable for a receiver, or were explicitly
requested. Otherwise link the evidence or use one compact `Control receipt`
below the human meaning.

A Control receipt must state its scope and what it does not prove. Do not hide a
receiver-required hash, but do not expose unrelated baselines merely because
they exist beside a decision.

## Self-Review

Before returning the summary, verify:

- the selected mode matches the current review job;
- Outcome, State, and Next are present unless receipt-only; the practical
  consequence is explicit either in Outcome or a separate Why it matters;
- every applicable loss-intolerant fact is preserved;
- no approval, completion, production, impact, or usability claim exceeds the
  evidence;
- the first screen contains no machine-only detail;
- `Next` is the final bullet and uses the root control-state wording;
- the summary compresses the response instead of repeating it.

For local regression and later canary scoring, use
`summary-behavior-eval-cases.json`. Passing that fixture proves only the local
contract and supplied examples; independent usefulness remains a separate
evidence gate.
