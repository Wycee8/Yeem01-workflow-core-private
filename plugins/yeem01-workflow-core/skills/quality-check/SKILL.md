---
name: quality-check
description: Use for post-build QA when the operator invokes -qa or -QA, asks whether an implementation is done correctly, or wants completed work tested from multiple angles before handoff, publish, or close.
---

# Quality Check

Quality Check is the post-build QA gate.

It answers: **was the thing built or implemented correctly, and is it actually
done?**

Use `-qa` as the canonical flag. Treat `-QA` as an exact alias.

## Use when

Use when work has already been built, implemented, generated, edited, or
assembled and Will asks:

- `-qa`
- `-QA`
- `QA this`
- `check if this is done`
- `verify this implementation`
- `is this implemented correctly?`
- `brutally check this`
- `is this ready to hand off / publish / close?`

Prefer stage-specific validators, tests, screenshot checks, schema validators,
or domain QA tools when a formal file contract exists. Use this skill to tie
those checks into a clear operator verdict.

For post-build animation or motion QA, route through
`design-engineering-polish` for strict UI motion standards, then cite rendered
evidence or a proof gap before marking the work ready.

Do not use `quality-check` for pre-build decision analysis. Route those requests
to `-audit` / `audit-check` or the relevant domain audit route.

## Procedure

Check the completed work from multiple angles:

1. Intent match: does it solve what was asked, not just what was convenient to
   build?
2. Implementation correctness: does the code, artifact, or workflow behave as
   intended?
3. Acceptance criteria: are explicit and implied requirements satisfied?
4. Regression risk: did it break adjacent behavior, routing, styling, state,
   contracts, or downstream workflows?
5. Edge cases: test empty, stale, interrupted, mobile, weird input, missing
   file, permission, and partial-state paths when relevant.
6. Evidence: cite tests, diffs, screenshots, validators, logs, commands, or
   manual probes. "Looks good" is not enough.
7. Integration fit: does it follow the existing system patterns instead of
   being bolted on?
8. User/operator usefulness: can Will or the end user trust and use it now?
9. Done-state honesty: state what remains untested, assumed, partial, or risky.

## Evidence topology gate

Before assigning a verdict for a user-facing capability:

1. Restate success as an operator or end-user action, not as a file or test
   result.
2. Challenge the supplied acceptance criteria. If the requested outcome cannot
   be true without an omitted integration, projection, deployment, runtime, or
   interaction boundary, add that boundary as an implied acceptance criterion.
   Do not expand into unrelated systems.
3. Map only the delivery path implicated by the claim, for example:

   ```text
   canonical source -> registry or manifest -> projection or package
   -> runtime or loader -> user-visible interaction
   ```

4. Test the outermost relevant boundary that is available. Passing an inner
   boundary does not prove a later boundary.
5. Name the evidence ceiling:
   - `source-ready`: source and structural contracts are valid, but delivery is
     not proven;
   - `ready-for-canary`: integration or projection is valid, but an isolated
     runtime or user-path probe remains;
   - `ready-for-use`: the outermost user-visible boundary has direct evidence.

If a required delivery boundary is missing or fails, return `Revise`,
`Blocked`, or `Not done`. Use `Done with caveats` / `ready-for-canary` only when
the implemented path is intact and the remaining proof is an explicitly named
isolated canary. Never translate source-ready evidence into ready-for-use.

### Skill and routing changes

When the changed capability is a skill, command, alias, registry route, or
runtime-discovered workflow, check the applicable path end to end:

1. canonical skill source and trigger metadata;
2. generated registry or index alignment when those surfaces consume the
   change;
3. the projection visible from the operator's actual current working directory;
4. runtime discovery or loading in an isolated fresh context;
5. intended owner/supporting-skill selection and operator-facing response.

A missing or wrong active-CWD projection is `Revise`, even when source,
registry, and structural fixtures pass. Correct projection without a fresh
activation probe is at most `Done with caveats` / `ready-for-canary`. Do not
require runtime or fresh-context proof for a source-only change that makes no
runtime, routing, or user-availability claim.

For bugfix, regression, or operator-correction QA, add an original-complaint
replay before assigning the verdict:

1. Restate the exact symptom or correction that triggered the fix.
2. Identify the user-visible path where that symptom appeared, not only the
   helper or unit that was patched.
3. Verify the old failure would fail before the fix or name why that proof is
   unavailable.
4. Verify the new behavior on representative real or fixture data, including
   stale/missing/partial metadata when that was part of the complaint.
5. Check the adjacent display/API boundary that carries the data end to end.

When QA is being repaired because it missed a defect, treat that escaped defect
as the original complaint: reproduce the earlier evidence ceiling, identify the
unverified boundary, and prove that the revised QA contract now assigns the
lower safe verdict.

If the QA only proves the new helper/unit but not the original user-visible
symptom, the maximum verdict is `Done with caveats`.

For every material conclusion, use the proof chain:

```text
claim -> concrete evidence -> plain-language meaning
```

This keeps technical verification useful to the operator without weakening the
evidence standard.

For `-qa brutal` or `-QA brutal`, assume the work is flawed until it survives
angle-based pressure testing. Name the strongest failure case first.

## Output

Return the smallest complete verdict. Preserve the following as a
loss-prevention checklist, merge overlapping fields, and omit empty categories:

- verdict: Done / Done with caveats / Revise / Blocked / Not done
- confidence: high / medium / low
- what passed
- what failed
- angles checked
- untested assumptions
- required fixes
- outermost boundary tested
- evidence ceiling: source-ready / ready-for-canary / ready-for-use
- proof: tests, validators, screenshots, logs, diffs, or manual checks
- ready for: use / handoff / execution / publish / close / not ready

If proof is unavailable, return `Done with caveats`, `Revise`, or `Not done`.
Do not mark work `Done` from impression alone.

## Trigger Tests
Read `references/trigger-tests.md` when validating QA routing, especially the
boundary between pre-build audit and post-build quality check.
