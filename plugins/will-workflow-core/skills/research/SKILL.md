---
name: research
description: User-facing hub for evidence-backed answers and research runs, including comprehensive adaptive deep research. Use for -research, -deep research, -research deep, quick sourced answers, multi-source investigations, starting or resuming durable research, freshness and contradiction audits, research reports, knowledge banks, or evidence handoffs. The hub selects quick, standard, or deep depth, then internally coordinates scope, plan, collect, verify, synthesize, report, scorecard, and handoff procedures without exposing component skills.
---

# Research Hub

## Job
Route research work into the canonical loop while keeping `-research` as the
only operator-facing skill call.

First decide whether a durable research run is necessary. Use the canonical
loop only when the answer must become reusable project evidence, a report, a
handoff packet, a scored readiness decision, or downstream build/creative input.

Durable run loop:
`route → brief → plan → collect → verify → synthesize → report → handoff/close`

This hub owns the internal phase procedures. It selects the needed procedure
from `references/phases.md`, then reports back in operator language. Do not
require the operator to know or choose sub-skill names such as plan, collect,
verify, scorecard, report, or bridge.

When `self-evolve` identifies recurring research, freshness, contradiction, or
downstream handoff gaps, this hub is the routing surface that should absorb the
fix. Prefer the scorecard or bridge procedure in `references/phases.md` rather
than leaving the lesson as a one-off report.

## Operator-facing rule
If the operator says `-research`, treat that as sufficient intent to enter this
hub. Ask only when the missing answer would change client/project/run, primary
deliverable, minimum output unit, coverage universe, research shape, evidence
plan, completion proof, material cost, approval gate, or external/action risk.
When that ambiguity is material, show two to three concrete interpretations
with one sample output each, recommend one, and ask one exact question before
collection. Do not replace this with a generic "anything to change?" prompt.

Normalize `-deep research`, `-research deep`, `deep research`, `comprehensive
research`, and equivalent requests for an extensive multi-source investigation
to this hub with `research_depth=deep`. Do not create or route to a second
`deep-research` skill.

Treat explicit legacy `$research-task-strategist` invocation as compatibility
intent for this public owner. Do not direct-load the private retired record.
Apply this hub's run-necessity gate, research-shape classification,
start/resume procedure, and brief-approval stop so the former strategist's
useful scoping behavior remains available without a second public route.

Normal replies should show:
- selected research depth
- the research shape
- current phase in plain language
- missing gates
- downstream consumer
- exact next action

Do not expose internal sub-skill names unless debugging skill routing, auditing
the skillhub, or the operator explicitly asks how the hub is wired.

## Depth selection

Select depth independently from output shape:

| Depth | Use when | Effort |
| --- | --- | --- |
| `quick` | One narrow question can be answered from local authority or a small current source set and needs no durable handoff. | Answer directly; do not scaffold. |
| `standard` | A durable decision or handoff needs a planned, traceable research loop with bounded question clusters. | Use the current canonical run loop. |
| `deep` | The request explicitly asks for deep/comprehensive research, spans several material question clusters, needs competing explanations or cross-domain evidence, or would be unsafe to conclude from a shallow scan. | Lock the goal and deliverable, build an ordered inquiry ladder, scan broad before drilling down, close material evidence gaps iteratively, and apply explicit completion thresholds. |

Do not interpret `deep` as unlimited or exhaustive. Set a time/source/effort
budget and return a truthful partial result when the budget is reached before
the completion thresholds pass. Reserve any future `exhaustive` profile for
explicit operator scope and budget approval.

For deep mode, read `references/deep-mode.md` before planning or collecting.
Use its adaptive frame, goal breakdown, inquiry ladder, evidence-gap loop,
stopping rules, progress contract, report contract, and safety controls.
Before collection, surface every Adaptive Research Frame field, including
`primary deliverable`, `minimum output unit`, `coverage universe`,
`representative example`, and `adjacent discovery areas`. Keep the initial
inquiry ladder to four to eight primary questions when deep scope warrants
them; merge overlaps and treat scoring or final selection as synthesis within
those questions rather than as an extra ninth branch. Order questions by what
they unlock, preserve operator-provided questions as authoritative, and record
inferred or evidence-discovered questions separately. When later operator
input refines the goal, revise the same ladder in place, preserve completed
work, and re-rank the open questions instead of restarting.

Do not force the deep frame or inquiry ladder onto a quick evidence answer.
Use the smallest research structure that can prove the requested result.

## Run necessity gate
Before creating or resuming run files, choose one path:

| Path | Use when | Output |
| --- | --- | --- |
| `quick_evidence_answer` | The request is narrow, answerable from local proof or a small number of current sources, and no durable project artifact or handoff is needed. | Concise answer, source basis, confidence/caveat, recommended next action; no run scaffold. |
| `local_authority_decision` | Workspace docs, existing ledgers, or current-chat evidence are enough to decide. | Decision or status with source paths; state that no new research run is needed. |
| `durable_research_run` | The work feeds a client/project/run, future reuse, planning, product, RAG, taxonomy/schema, router/evals, creative, assets, execution, or an operator decision that needs traceable evidence. | Canonical research artifacts and downstream packet. |
| `scorecard_or_refresh` | Existing research may be stale, contradictory, incomplete, unsafe to reuse, or near handoff. | Readiness scorecard and required fixes before reuse. |

Do not scaffold a run just because the word `research` appears. Scaffold or
resume only when durability, traceability, approval, handoff, or multi-cluster
investigation is actually needed.

For time-sensitive, regulatory, market, product, price, company, model, API,
platform, or social/current claims, verify with current sources before answering
or carrying the claim into a run. In durable runs, record checked/access dates
and freshness limits in the ledger or evidence notes.

## Source and claim standard
Every material claim should have a visible evidence basis:

- Prefer current project authority and existing ledgers before public web when
  project context exists.
- Prefer primary sources for facts, specs, policies, pricing, legal/regulatory,
  medical, financial, model/API, and platform claims.
- Use competitor, forum, social, or review evidence for behavior, language,
  objections, UX signals, or market texture; do not treat it as primary factual
  authority.
- Separate facts, interpretation, and recommendations.
- Mark confidence and unresolved caveats for claims that affect decisions.
- Preserve source IDs or links when a claim will feed planning, product,
  creative, assets, execution, RAG, taxonomy/schema, or router/eval work.

## `-user` research fit
When `-research` is combined with `-user`, research serves the user-value
verdict. Do not start or resume a research run just because `-research` appears
if local evidence is already enough to decide `Use / Clarify / Reduce / No-op`.

Use research only when evidence would change one of these:
- Will/operator value;
- downstream user or customer value;
- the smallest useful version;
- delete / absorb / keep decision;
- success signal or handoff consumer.

If research is needed, name the exact user-value question and downstream
consumer before collecting. If not, return the `-user` verdict and the local
evidence basis.

## Research shapes
Classify the output before planning or collecting:

| Shape | Use when | Typical outputs |
| --- | --- | --- |
| `standard_report` | A decision, market, audience, platform, or capability question needs evidence and recommendations. | final report, source ledger, recommendations, inline decision gate when needed |
| `knowledge_bank` | Research must become durable retrieval/wiki/RAG material. | index, pages, claim schema, claim records, source-linked caveats |
| `taxonomy_or_schema` | The work needs categories, labels, routing fields, or machine-readable structure. | taxonomy JSON, schema, examples, mapping table; when the requested deliverable is a database, inventory, or action map, populated source-linked records and coverage/retrieval checks are mandatory |
| `router_eval` | Research must validate classification, answer modes, safety routing, or prototype behavior. | eval corpus, gold labels, template specs, acceptance criteria |
| `reference_ingestion` | A source conversation, repo, product, app, paper, or external reference must be extracted before build work. | source ledger, extraction matrix, adopted/rejected patterns |
| `creative_or_asset_handoff` | Evidence must feed planning, creative direction, prompts, DAM, V3 assets, execution, or review. | handoff packet with evidence basis and cautions |
| `refresh_or_scorecard` | Existing research may be stale, incomplete, unsafe to reuse, or ready for handoff. | readiness scorecard, required fixes, reuse decision |

## Start / resume procedure
1. Read `WORKSPACE_INDEX.md`; resolve current chat/session context, workspace session context, work-item views, registries, and manifests before selecting research scope.
2. Apply the run necessity gate. If `quick_evidence_answer` or
   `local_authority_decision` is enough, answer directly with source basis and
   do not create run files.
3. For durable work, identify client, project, run, objective, and current research phase.
4. Prefer the active run when it matches the objective; otherwise create/resume a research run using the workspace scripts and registry conventions.
5. Inspect only the phase-critical files first:
   - `01_SESSION_BRIEF.md`
   - `02_RESEARCH_PLAN.md`
   - `02a_BRIEF_APPROVAL.md`
   - `03_SOURCE_LEDGER.md` or stage-local equivalent
   - `04_EVIDENCE_NOTES.md` or stage-local equivalent
   - `05_CONTRADICTION_LOG.md`
   - `06_INSIGHT_BANK.md`
   - `07_RECOMMENDATIONS.md`
   - `08_FINAL_REPORT.md`
   - `09_CONTENT_INPUT_PACK.md`
   - `10_SESSION_SUMMARY.md`
6. Internally select the next procedure and return only the plain-language
   research phase, missing gates, and exact next action.

## Internal phase routing
Choose one next procedure internally. Read `references/phases.md` when phase
details are needed. Keep the operator-facing response as `-research` unless
skill routing itself is under audit.

| State | Internal route |
| --- | --- |
| Narrow question; local proof or small sourced answer is enough; no durable handoff | quick evidence answer; do not scaffold |
| No objective or no matching run | ask one concise clarification or initialize run |
| Brief/plan missing or scope changed | plan procedure |
| Brief approval missing | present brief for approval; do not collect yet |
| Brief approved but ledgers missing/incomplete | collect procedure |
| Ledgers exist but contradictions/freshness/confidence not checked | verify procedure |
| Evidence verified but insights/recommendations missing | synthesize procedure |
| Recommendations exist but final report/content input/summary missing | report procedure |
| Final report exists and downstream planning/product/RAG/router/creative/asset handoff is needed | bridge procedure |
| Readiness, freshness, contradiction, source traceability, approval state, or reuse safety is unclear | scorecard procedure |
| Canonical artifacts complete and no handoff needed | close or summarize next step |

## Completion gates
Do not call a research run complete unless:
- `10_SESSION_SUMMARY.md` exists, or an explicit stage-local summary equivalent exists.
- Source evidence is traceable through `03_SOURCE_LEDGER.md` / stage-local source ledger.
- Evidence notes or final report identify weak claims and unknowns.
- Contradictions are logged, or the absence of contradictions is explicitly stated.
- High-volatility claims include checked/access dates and freshness caveats.
- The next downstream consumer is named: planning, product prototype, RAG/knowledge retrieval, router/evals, creative workflow, image prompts, DAM, V3 asset generation, execution/review, operator decision, or none.
- The primary deliverable, minimum output unit, coverage universe,
  representative example, and completion test are explicit when they determine
  whether the output is useful.
- The goal breakdown and ordered inquiry ladder are explicit for new deep runs;
  each primary question records its origin, dependencies, why it is next, what
  it unlocks, required evidence, output destination, completion condition, and
  current state.
- Operator steering updates the same ladder, preserves answered questions, and
  records whether a concrete example changed deliverable grain, coverage, or
  the goal itself.
- A structured run requested as a database, inventory, catalogue, or action map
  contains the approved populated records and passes representative coverage
  or retrieval checks. Categories plus an empty schema are complete only when
  a schema-only deliverable was explicitly approved.

For `research_depth=deep`, also require:
- every must-answer question is covered, explicitly deferred, or blocked with a reason;
- the final synthesis follows inquiry order and states how each answered
  question advanced the governing goal or deliverable;
- every material report claim maps to evidence in the source ledger;
- competing evidence and unresolved contradictions remain visible;
- source diversity, source authority, and freshness meet the plan's thresholds;
- the final report separates facts, inferences, recommendations, counterevidence, unknowns, confidence, and limitations;
- the summary records `complete`, `partial`, or `blocked` truthfully and names
  whether the run stopped through evidence saturation, an approved budget
  boundary, or an unresolved blocker.

## Quality warning triggers
Warn and route to repair/scorecard when any are true:
- final report exists but source ledger is missing
- recommendations exist but no contradiction/freshness status exists
- material current/web claims lack checked dates or source tier labels
- scout/subagent findings appear only in chat, not in a ledger or packet
- final answer gives a recommendation without separating evidence from interpretation
- downstream product/RAG/router/creative/V2/V3 work is being derived from research without a handoff packet
- a knowledge-bank, taxonomy, schema, or eval output lacks source-linked records or acceptance criteria
- a requested database, inventory, catalogue, or action map is represented only
  by categories, representative bullets, or an empty record template
- the plan approved a broad output label without showing a representative
  finished record or resolving materially different deliverable interpretations
- the run has many research files but no `10_SESSION_SUMMARY.md`
- current status labels conflict with visible downstream artifacts
- a self-evolve finding references research gaps, contradiction/freshness gaps, approval ambiguity, carry-forward gaps, or handoff uncertainty

## Downstream bridge
Before closing research, name the downstream consumer: planning, product prototype, RAG/knowledge retrieval, router/evals, creative workflow, image prompts, DAM, V3 asset generation, execution/review, operator decision, or none.

Use the bridge procedure in `references/phases.md` when verified research must become:
- product prototype input
- RAG/knowledge retrieval input
- taxonomy/schema/router/eval implementation input
- creative direction input
- visual/image/video content research
- image prompt brief
- DAM lane input pack
- V2 plan change recommendations
- V3 asset handoff brief

Use the scorecard procedure in `references/phases.md` when the operator asks
whether a run is ready, complete, stale, reusable, safe to hand off, or
approval-gated. Keep scorecard caveats visible in downstream packets.

## Self-evolve integration
If invoked as part of a skill-improvement or self-evolve pass:
1. Identify the recurring pattern, not just the current file gap.
2. Use the scorecard procedure for evidence/freshness/approval/readiness ambiguity.
3. Use the bridge procedure for planning, creative, prompt, DAM, V3, or execution carry-forward.
4. Preserve research as evidence authority; do not merge it into creative workflow.
5. Persist the future behaviour change in the target skill/report when the change is local and reversible.

Self-evolve completion evidence should include either:
- a scorecard showing the gap and target behaviour change, or
- a bridge packet showing the downstream handoff and validation criteria.

## Trigger Tests
Read `references/trigger-tests.md` when validating research hub routing,
near-miss boundaries, or trigger changes.

Read `references/deep-mode.md` whenever `research_depth=deep` is selected or
when auditing deep-run scope, evidence coverage, progress, or completion.

## Phase Procedures
Read `references/phases.md` when validating or executing the internal plan,
collect, verify, synthesize, report, scorecard, or bridge procedures.

## Validation

After changing routing, deep-mode behavior, or the durable run contract, run:

```bash
python3 scripts/test_validate_research_run.py
python3 scripts/evaluate_skill_trigger_cases.py \
  --cases skills/research/references/trigger-cases.json \
  --min-cases 20
python3 scripts/test_evaluate_skill_trigger_cases.py
python3 scripts/test_evaluate_research_deep_behavior_cases.py
python3 scripts/evaluate_research_deep_behavior_cases.py \
  --cases skills/research/references/behavior-eval-cases.json \
  --predictions <fresh-context-behavior-predictions.json>
python3 scripts/validate_skills_registry.py --json
```

The trigger fixture proves structural expectations only. Supply a separate
prediction file with explicit independent provenance before claiming
fresh-context behavioral evidence.

## Output shape
```markdown
## Research Summary
- Client/project/run:
- Run decision:
- Research depth:
- Research shape:
- Evidence mode:
- Objective:
- Current phase:
- Missing gates:
- Downstream consumer:
- Recommended next action:
```
