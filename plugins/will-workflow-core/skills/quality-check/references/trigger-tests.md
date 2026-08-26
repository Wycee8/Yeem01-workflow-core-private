# Quality Check Trigger Tests

Use these cases when updating post-build QA routing or done-state verdicts.

| Operator phrase | Expected behavior |
|---|---|
| `-qa` | Post-build QA gate with verdict, proof, and residual risk. |
| `-QA brutal` | Adversarial post-build check; strongest failure case first. |
| `check if this is done` | Verify completed work against intent, implementation, acceptance criteria, and proof. |
| `is this implemented correctly?` | Inspect behavior and integration fit; cite evidence. |
| `audit this before planning` | Do not use `quality-check`; route to pre-build audit. |
| `be critical about this idea` | Do not use `quality-check`; route to audit/discuss unless implementation exists. |
| `ready to publish?` | Verify release/publish readiness with caveats and untested assumptions. |
| `looks good?` | Require evidence; do not mark done from impression alone. |
| `-qa the bugfix` | Replay the original symptom through the user-visible path and cap verdict at Done with caveats if only helper/unit proof exists. |
| `why did previous QA miss this? -improve -qa skill` | Reproduce the earlier evidence ceiling, identify the unverified delivery boundary, patch the QA skill narrowly, and prove the revised contract assigns the lower safe verdict. |
| `-qa this skill update; source and registry pass but the root .agents projection does not expose it` | Return `Revise` and `source-ready`; a missing active-CWD projection is a delivery defect, not a future proof item. |
| `-qa this routed skill; source, registry and projection pass but no fresh-session activation was run` | Return at most `Done with caveats` and `ready-for-canary`; state that implicit activation remains unproven. |
| `-qa this routed skill; a fresh root session selected the intended owner and response contract` | Return `Done` / `ready-for-use` only when the source-to-user path and adjacent route boundaries also pass. |
| `-qa this wording-only SKILL.md correction; metadata and runtime behavior are unchanged` | Validate the relevant source contract without demanding a fresh-session probe or widening scope. |
| `the acceptance criteria omit deployment, but the requested outcome says the live page works` | Add deployment and live interaction as implied acceptance criteria because the user-visible outcome cannot otherwise be true. |
| `test this Figma-to-app match` | Use visual/rendered evidence and `ui-viewer` when relevant. |
| `-qa animation` | Use `design-engineering-polish` strict motion review standards and cite rendered proof or proof gap. |
| `validate this run output` | Use stage validators/contracts first, then summarize QA verdict. |
| `can I hand this off?` | State ready-for target and required fixes. |
| no proof available | Return Done with caveats, Revise, or Not done; never unconditional Done. |
