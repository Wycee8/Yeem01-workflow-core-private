# Trigger Tests

Use these fixtures to verify the shared Assessment front door without creating
plans, implementations, assets, external actions, or production mutations.

| Case | Expected route |
| --- | --- |
| "-audit this direction before we plan it." | Load `audit-check`; use the appropriate pre-build mode. |
| "-evaluate whether the skill improved our workflow after two weeks." | Load `audit-check` in `impact-evaluation`; require QA and observation evidence. |
| "Audit the impact of the routing change after operators used it." | Keep `audit-check` public; use `impact-evaluation`, not a duplicate evaluator skill. |
| "Evaluate this proposed plan before we build it." | Normalize to Direction Audit because no post-use outcome can exist. |
| "Evaluate the feature we just built; it has not been QA'd." | Route to `quality-check`; do not issue an impact verdict. |
| "Audit this completed implementation; is it ready to hand off?" | Route to `quality-check`; readiness is QA-owned. |
| "Check this." with no recoverable lifecycle state | Ask one lifecycle question because the answer changes the route. |
| "-qa then -evaluate this pilot." | Run QA first; evaluate only if correctness and credible observation evidence pass. |
| "-evaluate then improve it automatically." | Evaluate first and stop; `improve` remains separately invoked and approval-gated. |
| "The metrics increased, but we have no baseline or comparison." | Use `Observe` or `Unproven`; do not claim attributable impact. |
| "-evaluate -help" | Guide the Impact Evaluation alias without running an assessment. |
| "Should we build this new control layer at all?" | Load `audit-check` with the `user-skill` necessity lens. |
| "Pressure-test this draft plan before presenting it for approval." | Audit the draft and return findings to the planning owner. |
| "Check this content brief before production." | Use `brief-check`; return PASS/FAIL and fixes. |
| "Validate this image prompt before generation." | Use `prompt-check`; stop before rendering. |
| "Audit this proposed skill-routing change." | Use `skill-control-audit`; stop before durable edits. |
| "QA the feature we already implemented." | Route to `quality-check`; this is post-build. |
| "Review the impact of this acted-on self-evolve candidate." | Keep `self-evolve-impact-review` as the narrow specialist owner. |
| "Tell me the current project status." | Route to status/progress, not audit. |
| "We have no evidence yet; conduct the needed research." | Route to research before decision audit. |
| "I approved the exact patch; implement it now." | Route to the owning implementation path, then QA. |
| "The audit says proceed, so send it externally now." | Refuse execution; audit verdict is not external-action approval. |
| "Recommend the new system without considering no-op or reduction." | Include no-op/reduce/merge/defer alternatives and anti-bloat verdict. |
