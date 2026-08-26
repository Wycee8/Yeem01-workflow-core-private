---
name: audit-check
description: Assessment front door for -audit and -evaluate. Use Direction Audit before commitment to pressure-test decisions, assumptions, plans, briefs, prompts, or skill/control changes; use Impact Evaluation after credible use to decide whether a completed implementation or skill should be kept, iterated, simplified, observed, rolled back, retired, or scaled. Route built-but-unverified work to quality-check; do not use evaluation as QA or automatic improvement execution.
---

# Audit Check Skill

## Goal

Give Will one low-friction assessment entrance while keeping lifecycle truth
clear:

- before commitment, test whether the direction is right;
- after delivery but before proof, hand off to QA;
- after credible use, test whether the result helped enough to keep, change, or
  scale.

## Operating Principles

- Lifecycle first: infer whether the decision concerns direction, correctness,
  or observed impact before choosing a mode.
- Decision-grade output: lead with the verdict, confidence, strongest for/against
  arguments, weak assumptions, missing evidence, and recommended direction.
- Evidence honesty: technical correctness is not outcome impact. Missing
  observation evidence is `Unproven`, not proof of value or failure.
- User value first: test whether the target helps Will/operator goals and, when
  relevant, downstream users before optimizing process or structure.
- Anti-bloat by default: include no-op, reduce, merge, defer, and research-first
  alternatives before recommending more work.
- QA stays independent: route built-but-unverified work to `quality-check` and
  consume QA proof rather than recreating it during evaluation.
- Gated actions stay gated: an audit verdict is not approval to execute,
  generate, send externally, mutate production, change credentials, delete, or
  push git.

## Job

Classify the assessment stage, then run the smallest correct mode:

```text
proposed direction or change -> Direction Audit
completed but correctness unproven -> quality-check handoff
QA-proven and credibly observed -> Impact Evaluation
```

`-audit` is the assessment front door. `-evaluate` is an explicit alias that
requests Impact Evaluation, but it cannot manufacture the QA or observation
evidence needed for that conclusion. If the target is proposed, normalize to
Direction Audit. If it is built but unverified, route to `quality-check`.

Planning skills should draft the concrete plan after a minimal necessity and
authority gate, then audit that draft before presenting it. Use this full
audit workflow when the draft contains disputed direction, weak evidence, durable
skill/control creation, hard approval gates, or a reduce/merge/no-op decision
that needs more evidence.

For content briefs and image prompts, this skill can still run the legacy audit
gate templates. For finished implementation checks, use `quality-check`.

Core contrast:

```text
-audit / Direction Audit = Are we thinking about this correctly?
-qa / -QA = Did we execute it correctly?
-audit impact / -evaluate = Did the verified result help after use?
```

## Use When

- Will says `-audit`, `audit this`, `pressure-test this`, `is this the right
  direction?`, `should we build this?`, or asks to audit before planning.
- Will says `-evaluate`, `evaluate the impact`, `did this help?`, `is this worth
  keeping?`, or asks whether a completed implementation or skill should be
  kept, changed, retired, or scaled after use.
- When the question is whether a durable artifact, page, skill, system, or
  control should exist at all, load `user-skill` as the necessity and
  anti-bloat lens; do not load the proposed artifact's production specialist
  until the audit establishes a real need.
- A plan, brief, image prompt, skill/control change, or decision has uncertain
  assumptions, weak evidence, high approval burden, or possible no-op/reduce
  outcome.
- A compact planning gate finds disputed direction and needs a full
  decision-grade audit.

## Do Not Use When

- The work is built but needs correctness, completion, readiness, handoff, or
  publish verification: use `quality-check`.
- The operator asks only for current status or progress: use status/progress
  routes.
- The target is a pure evidence gap with no decision to pressure-test yet: use
  `research`.
- The operator asks to improve or repair the target: use `improve` after the
  assessment decision is accepted; do not mutate the target inside Audit.
- The operator already approved a specific safe local patch and asks to execute:
  use the owning implementation route, then QA afterward.

## Modes

| Mode | Use when | Output | Stop condition |
| --- | --- | --- | --- |
| `assessment-check-in` | Bare `-audit` and lifecycle state is not explicit | Stage classification and one recommended route | Ask one question only if stage changes ownership or evidence |
| `quick-gate` | Low-risk direction check | Proceed/revise/research/no-op verdict | Stop if full Direction Audit is needed |
| `direction-audit` | Proposed direction is disputed or high-risk | Decision-grade Direction Audit | Stop before planning or execution |
| `brief-check` | Content brief exists as target | PASS/FAIL plus fixes | Stop before content production |
| `prompt-check` | Image prompt exists as target | PASS/FAIL plus fixes | Stop before generation |
| `skill-control-audit` | Skill/routing/control change is target | Use/reduce/no-op/revise verdict | Stop before durable change |
| `impact-evaluation` | Completed, QA-proven subject has credible use evidence | Keep/iterate/simplify/observe/rollback/retire/scale decision | Stop before `improve` or execution |
| `qa-handoff` | Target is completed but correctness/readiness is unproven | Exact QA target and evidence gap | Stop and route to `quality-check` |

## Steps

1. Bind the target and the decision Will needs.
2. Classify lifecycle state:
   - proposed direction or change;
   - completed but unverified;
   - verified and observed;
   - genuinely unclear.
3. If unclear and the answer changes route or proof, ask once:

   > Are you deciding whether to build or change it, whether it was built
   > correctly, or whether it helped after real use?

4. For Direction Audit, identify the target:
   - decision or judgment
   - plan direction
   - content brief
   - image prompt
   - skill/routing/control change
   - no-op / reduce / merge question
   - existence/necessity question, which requires the `user-skill` lens
5. Gather evidence from the relevant indexes, registry entries, brief, prompt,
   design guidance, prior decisions, or source files.
6. Pressure-test Direction Audit targets:
   - intent and problem framing
   - assumptions and missing evidence
   - alternatives, including no-op, reduce, merge, defer, or research first
   - trade-offs, risks, timing, user value, and anti-bloat
   - cheapest validation before planning
   - whether a compact planning gate is enough, or a full audit artifact is
     needed before planning continues
7. For content/image prompt gate validation, run
   `python3 {baseDir}/scripts/audit_gate.py --type <type> --input <path>` when
   the input is available as a file. The script and its checklist references
   travel with this skill; do not assume a Yeem01 workspace root.
8. For Impact Evaluation, read
   `{baseDir}/references/impact-evaluation.md`, verify the original goal, consume
   QA evidence, classify the observation level, select only relevant dimensions,
   and return one lifecycle decision.
9. Return the mode-specific decision. Do not execute the recommendation.

When the audit target is a plan draft, return material findings to the planning
owner for revision. Do not present the unaudited draft as the approval target.

## Common Triggers

- `-audit`
- `-evaluate`
- `audit whether this helped after use`
- `evaluate whether we should keep this skill`
- `did this implementation actually improve the workflow?`
- `audit this decision`
- `audit before planning`
- `pre-plan audit gate failed`
- `plan audit gate found risk`
- `pressure-test this`
- `is this the right direction?`
- `should we build this?`
- `check this content brief`
- `check this image prompt`
- `run audit check`
- `validate my prompt`

## Output

Lead with the decision, plain-language meaning, actual evidence limitation, and
next meaningful action. Put technical receipts below. Treat the following
fields as a loss-prevention checklist, not a one-line-per-field template: merge
overlapping facts, omit inapplicable fields, and state each decision-changing
fact once.

Direction Audit returns:

- proceed / revise judgment / research first / reduce / no-op / blocked;
- confidence, strongest for/against arguments, weak assumptions, alternatives,
  missing evidence, cheapest validation, and recommended direction.

Impact Evaluation returns:

- keep / iterate / simplify / observe / rollback / retire / scale;
- confidence separate from quality;
- evidence level and relevant dimension judgments using `Strong`, `Adequate`,
  `Weak`, `Unproven`, or `N/A`;
- what was learned, why it matters, actual limitation, and next action;
- no default aggregate score.

QA handoff returns the correctness/readiness question, missing outer boundary,
and `quality-check` route. It does not issue an impact decision.

For content/image prompt template gates, include PASS/FAIL and the specific
failures to fix.

## Validation

- The output distinguishes Direction Audit, post-build QA, and post-use Impact
  Evaluation.
- The verdict includes confidence and the strongest argument against the
  recommended direction when Direction Audit is used.
- Missing evidence and cheapest validation are named before planning continues.
- Impact claims require credible observation evidence; otherwise use `Observe`
  or mark the affected dimension `Unproven`.
- `-evaluate` proposed-work cases normalize to Direction Audit and
  built-but-unverified cases route to QA.
- Any script-based content/image audit cites the command and PASS/FAIL result.
- If execution is recommended, the response names the owning route and approval
  gate instead of executing inside the audit.

Trigger fixtures: `{baseDir}/references/trigger-tests.md`

Boundary case packet: `{baseDir}/references/trigger-cases.json`

Fresh-context behavior packet:
`{baseDir}/references/behavior-eval-cases.json`

Impact Evaluation contract: `{baseDir}/references/impact-evaluation.md`

## Usage in Session
```
User: check this brief
{"objective": "Increase signups", "audience": "founders", "cta": "Sign up"}

→ Run audit, return result

User: -evaluate the new routing after two weeks of use

→ Verify QA and observation evidence, then run Impact Evaluation or return the
smallest missing-evidence plan.
```

---
*Skill v2.0 — 2026-08-19*
