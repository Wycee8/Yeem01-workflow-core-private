# Impact Evaluation Contract

Use this reference only after the Assessment front door classifies the target
as completed and credibly observed. It defines the `impact-evaluation` mode
used by `-audit impact` and the `-evaluate` alias.

## Question

Did the verified result help enough to keep, change, or scale?

## Preconditions

Bind:

1. the completed subject and owning authority;
2. its original goal and intended beneficiary;
3. QA/readiness proof or an explicit QA gap;
4. the observation window and evidence source;
5. the baseline, alternative, or reason none exists;
6. the lifecycle decision Will needs.

If correctness is unproven, stop at `qa-handoff`. If use evidence is missing,
return `Observe` with the smallest measurement plan. Do not treat structural
tests, documentation, or a single self-authored fixture as outcome proof.

## Evidence ladder

Classify the strongest supported level:

1. `Specified` — intended behavior is documented.
2. `Technically verified` — source, integration, or delivery path is proven.
3. `Observed` — real or representative use is directly seen.
4. `Outcome improved` — the intended result improved against a baseline or
   alternative.
5. `Impact attributable` — available evidence reasonably links the improvement
   to the evaluated subject.

The lifecycle decision cannot imply a higher level than the evidence supports.
One canary proves the tested path only.

Apply these evidence ceilings before selecting the lifecycle decision:

- Keep the result at `Observed` when a source only says the outcome was
  "better", "improved", or "useful" without an explicit comparable baseline
  or alternative and a traceable result. Do not infer a baseline from those
  words or from repeated use alone.
- Use `Outcome improved` when either an explicit comparable baseline or
  alternative shows a traceable change, or a traceable measurement statement
  names the changed outcome across multiple independent representative pilots.
  A bare qualitative claim such as "source quality improved" remains
  `Observed`; a measured claim such as decision time improving across named
  independent pilots may support `Outcome improved` even when a compact
  operator summary omits the raw values.
- Use `Impact attributable` only when attribution evidence reasonably links
  the improvement to the evaluated subject rather than timing, selection, or
  another plausible cause. Repetition, temporal sequence, or a lifecycle
  decision does not establish attribution by itself.
- Keep the lifecycle decision and evidence level separate. In particular, a
  `Scale` decision does not raise the evidence level. Recommend `Keep` at the
  current scope after one bounded pilot, even when it shows a strong improved
  outcome. Recommend governed `Scale` at `Outcome improved` only when multiple
  independent representative pilots also show stable control fit and the
  response names the tested-scope limitation.

When the evidence is ambiguous between two levels, select the lower level and
state the smallest missing comparison needed to support the higher one.

## Dimensions

Select only dimensions that affect the decision:

| Dimension | Question |
| --- | --- |
| Goal and authority fit | Did the subject solve the intended problem while respecting its owner and higher authority? |
| Build quality | Is the delivered behavior correct, coherent, resilient, and maintainable? |
| Operator usefulness | Did it reduce decision load, correction, confusion, or review friction? |
| Workflow efficiency | Was useful work achieved with proportionate time, steps, dependencies, and operating burden? |
| Control fit | Are routing, approvals, ownership, evidence boundaries, and reversibility appropriate? |
| Observed outcome | What changed for the intended beneficiary, including unintended effects? |
| Evidence quality | Is the evidence current, relevant, traceable, representative, and sufficient for this decision? |

For skills, include routing accuracy, instruction economy, wrong-route
protection, fresh-context behavior, and operator-facing response quality under
the relevant dimensions. Do not create a universal skill scorecard.

Judge each selected dimension as `Strong`, `Adequate`, `Weak`, `Unproven`, or
`N/A`. State confidence separately. Do not average the labels into a default
score.

## Lifecycle decisions

- `Keep` — useful and controlled at the current scope.
- `Iterate` — valuable direction with one bounded improvement need.
- `Simplify` — value exists but avoidable process, surface, or maintenance cost
  obscures it.
- `Observe` — promising but outcome evidence is not mature enough.
- `Rollback` — the recent change should be reversed through its owning route.
- `Retire` — the subject no longer earns its operating or cognitive cost.
- `Scale` — evidence supports broader governed use.

Hard gates override dimension strength:

- goal fit must be explicit;
- evidence must support the claimed decision;
- real-use proof is required for observed-value or scale claims;
- workspace control fit cannot be traded away for apparent speed or quality.

## Operator-facing output

Lead with:

1. lifecycle decision and confidence;
2. what changed or was learned;
3. why it matters;
4. actual evidence level and limitation;
5. next meaningful action.

Then show a compact dimension table and a `Control receipt` containing the
subject, observation window, evidence sources, QA state, baseline/alternative,
scope, and what the evidence does not prove.

## Handoffs

- correctness or readiness gap -> `quality-check`;
- evidence collection would change the decision -> `research` or the owning
  measurement specialist;
- accepted lifecycle decision needs a change plan -> explicit `improve`;
- narrow specialist evaluation already exists -> that specialist remains the
  primary owner and may reuse this contract as a lens;
- external, provider, production, destructive, credential, spend, publication,
  or authority mutation -> preserve its normal gate.

Impact Evaluation is advisory. It does not repair, execute, publish, deploy,
retire, roll back, or scale the subject by itself.
