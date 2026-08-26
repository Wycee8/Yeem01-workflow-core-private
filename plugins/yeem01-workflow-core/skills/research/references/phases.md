# Research Phase Procedures

These are internal procedures for the `research` hub. The operator should
invoke `-research`; do not ask Will to choose phase-wrapper skill names.

## Phase Selection

| State | Internal procedure |
| --- | --- |
| Narrow question; local proof or a small sourced answer is enough; no durable handoff is needed | Quick Evidence Answer |
| No objective or no matching run | Ask one concise clarification or initialize run |
| Brief/plan missing or scope changed | Plan |
| Brief approval missing | Present brief approval gate; do not collect yet |
| Brief approved but ledgers missing/incomplete | Collect |
| Ledgers exist but contradictions/freshness/confidence are unclear | Verify |
| Evidence verified but insights/recommendations are missing | Synthesize |
| Recommendations exist but final report/content input/summary is missing | Report |
| Final report exists and downstream handoff is needed | Bridge |
| Readiness, freshness, contradiction, traceability, approval, or reuse safety is unclear | Scorecard |
| Canonical artifacts complete and no handoff is needed | Close or summarize next step |

When `research_depth=deep`, read `deep-mode.md` and apply its Adaptive Research
Frame, goal breakdown, inquiry ladder, adaptive evidence loop, completion thresholds, progress
contract, and report contract across the matching procedures below. Deep mode
does not add a parallel phase system.

## Quick Evidence Answer

Use when the operator needs a concise evidence-backed answer, not a durable
research run.

1. Check current chat, workspace authority, existing reports, source ledgers,
   and relevant local files before public-web lookup when project context exists.
2. Use public-web/current sources only when freshness, market evidence, source
   upgrades, or external validation matters.
3. Prefer primary sources for factual, policy, pricing, API/model, legal,
   medical, financial, platform, or regulatory claims.
4. Use forums, social posts, reviews, and competitor pages only for behavior,
   language, UX, objections, or market texture unless the task explicitly asks
   for perception evidence.
5. Return the answer with:
   - source basis;
   - confidence or caveat;
   - date checked for volatile claims;
   - whether a durable run is recommended.
6. Escalate to Plan when the question splits into multiple clusters, needs a
   future handoff, requires approval before collection, or cannot be answered
   safely from the available evidence.

## Plan

Use when starting or refreshing a research run.

1. Read `01_SESSION_BRIEF.md` if it exists; otherwise create it from the template.
2. Read the client brief, session-resolved context, work-item/goal views,
   registries, manifests, and relevant project authority before any external
   source plan.
3. Confirm that the run necessity gate requires durable research. If a quick
   evidence answer or local authority decision is enough, do not scaffold.
4. Fill or update `00_RUN_MANIFEST.json`, `01_SESSION_BRIEF.md`, and
   `02_RESEARCH_PLAN.md`.
5. Classify the research shape: `standard_report`, `knowledge_bank`,
   `taxonomy_or_schema`, `router_eval`, `reference_ingestion`,
   `creative_or_asset_handoff`, or `refresh_or_scorecard`.
6. Select research depth: `quick`, `standard`, or `deep`. Normalize explicit
   `-deep research`, `-research deep`, and comprehensive multi-cluster research
   requests to `deep`.
7. Lock the deliverable interpretation before defining the output contract:
   - primary deliverable;
   - minimum output unit;
   - coverage universe and explicit sampling/exclusions;
   - one representative finished example;
   - measurable completion and retrieval/use checks.
   When two or more materially different interpretations remain, show the
   alternatives with one sample output each, recommend one, ask one exact
   question, and stop before collection. For explicit `-ask`, show this check
   even when it confirms an already explicit contract.

   Then define the shape-specific output contract:
   - `standard_report`: report, recommendations, decision gate when needed, summary.
   - `knowledge_bank`: index/pages, claim schema, JSONL or table records, source-linked caveats.
   - `taxonomy_or_schema`: categories, fields, examples, validation rules; if
     the primary deliverable is a database, inventory, catalogue, or action
     map, require populated source-linked records plus coverage and retrieval
     checks rather than an empty schema.
   - `router_eval`: eval corpus, gold labels, safety flags, template IDs, acceptance criteria.
   - `reference_ingestion`: source ledger, extraction matrix, adopted/rejected patterns.
   - `creative_or_asset_handoff`: evidence-based handoff packet with cautions and next stage.
   - `refresh_or_scorecard`: readiness label, reuse decision, required fixes.
8. Define source tiers, question clusters, stop rules, and any needed subagent tasks.
   Use this source priority when project context exists:
   - current project authority: charter, decisions, run registry, reports, active docs;
   - prior research and source ledgers;
   - local transcripts, exports, reference repos, uploaded materials;
   - primary or high-quality external sources;
   - competitor/forum/social evidence only for behavior, phrasing, UX, or market signals.
9. Define claim handling: source IDs, source tier, checked/access date for
   volatile claims, confidence label, and contradiction path.
10. For deep mode, add the exact `Research depth: deep` marker and
   `Research contract: inquiry_ladder.v1` to `02_RESEARCH_PLAN.md`, then include:
   - `## Adaptive Research Frame`;
   - `## Inquiry Ladder` using stable `BR-*` IDs and the ordered fields in
     `deep-mode.md`;
   - `## Completion Thresholds`.
   Use the schemas and topic profiles in `deep-mode.md`. Preserve
   operator-provided questions as authoritative, label inferred and
   evidence-discovered questions, and make dependencies point only to earlier
   questions. Do not add this structure to quick evidence answers.
11. Add an inline visualization plan when research feeds UX, product strategy,
   creative, design, dashboards, knowledge banks, taxonomy/router work, or
   decision review. If visuals are not useful, state `Inline visualisation: not
   applicable` and why.
12. Present the brief approval gate before collection:
   - objective, scope, and key questions;
   - research shape and downstream consumer in plain language;
   - primary deliverable, minimum output unit, coverage universe, representative
     finished example, and completion test;
   - if a material interpretation decision remains, ask the one exact
     sample-based question from step 7; otherwise ask: "Does this concrete
     deliverable and research boundary look right? Any material change?"
   - wait for explicit confirmation before collecting;
   - after approval, create `02a_BRIEF_APPROVAL.md`.
13. Set `briefApproved: true` and `nextPhase: "RESEARCH_COLLECT"` in the manifest.
14. Keep the plan compact and decision-oriented.

## Collect

Use when the run is scoped and evidence gathering is next.

1. Read `01_SESSION_BRIEF.md`, `02_RESEARCH_PLAN.md`, and the selected output contract.
2. Collect internal authority before public-web discovery when project context
   exists: project charter, decisions, prior reports, source ledgers, active
   docs, transcripts/exports, reference repos, and uploaded materials.
3. Break collection into small question clusters tied to the output contract.
4. Spawn `scout` for public-web discovery when freshness, market evidence,
   source upgrades, or external validation matters.
5. Spawn `extractor` only when bulky local files, transcripts, repos, PDFs, or
   source exports need structured condensation.
6. Capture results in `03_SOURCE_LEDGER.md` and `04_EVIDENCE_NOTES.md`.
7. For structured outputs, capture machine-usable evidence:
   - knowledge bank: claim candidates, source IDs, confidence, validation status;
   - taxonomy/schema: fields, examples, counterexamples, validation rules, and
     populated source-linked records when the approved deliverable is a
     database, inventory, catalogue, or action map;
   - router/eval: prompt examples, gold labels, answer modes, safety flags;
   - reference ingestion: extraction matrix and adopted/rejected patterns.
8. For each material source, capture source ID, URL/path, source tier,
   publish/update date when available, date checked, owner/publisher, and the
   claims it supports.
9. For deep mode:
   - begin with a broad landscape scan before targeted deep dives;
   - link every source to branch IDs and supported claim IDs;
   - update the existing inquiry ladder in `02b_RESEARCH_PROGRESS.md`, retain
     covered questions, and add evidence-discovered questions without
     restarting the plan;
   - when examples reveal wrong deliverable grain or coverage, revise the
     Adaptive Research Frame and record the contract change before continuing;
   - include `## Source Coverage` in `03_SOURCE_LEDGER.md`;
   - include `## Claim Coverage` in `04_EVIDENCE_NOTES.md`;
   - update branch status and information-gain state after each material round.
10. Stop when the plan's minimum evidence threshold is met, the output contract
   can be filled, or contradictions appear.

## Verify

Use after evidence collection and before final synthesis.

1. Read `03_SOURCE_LEDGER.md` and `04_EVIDENCE_NOTES.md`.
2. Spawn `critic` when contradictions, stale evidence, or weak claims need review.
3. Record unresolved issues in `05_CONTRADICTION_LOG.md`.
4. Check whether volatile claims have current enough sources and date checked.
5. Tag claims that are safe to carry into synthesis and claims that must stay open.
6. For deep mode:
   - test citation entailment: the cited source supports the claim as written;
   - distinguish independent corroboration from derivative repetition;
   - test must-answer coverage, counterevidence, source diversity, and
     information gain;
   - include `## Resolution Status` in `05_CONTRADICTION_LOG.md`.
7. Stop if evidence is too weak for a recommendation.
8. For structured outputs, verify the approved record unit, coverage universe,
   representative example, and retrieval/use checks. Do not clear a populated
   database or action-map request from categories plus an empty schema.

Verification is complete only when each important claim is either cleared for
synthesis or explicitly held back with a reason.

## Synthesize

Use when evidence is good enough to turn into insights.

1. Read `04_EVIDENCE_NOTES.md` and `05_CONTRADICTION_LOG.md`.
2. Write `06_INSIGHT_BANK.md` with clear, scoped, evidence-backed statements.
3. Write `07_RECOMMENDATIONS.md` with explicit linkage to insight IDs.
4. Keep risks, unknowns, and freshness limits visible.
5. Do not let synthesis hide contradictions.
6. Keep facts, interpretation, and recommended action visibly separate when a
   decision will be made from the output.
7. For deep mode, organize the insight bank around must-answer branches and
   preserve counterevidence, rejected interpretations, confidence, and open
   questions beside the affected conclusion. Follow inquiry-ladder order and
   state how each answer advances the governing goal, deliverable, or next
   question.

Every recommendation should point back to evidence, confidence, and unresolved
caveats. If that link is missing, return to verification.

## Report

Use at the end of a research run.

1. Read `06_INSIGHT_BANK.md`, `07_RECOMMENDATIONS.md`, and
   `05_CONTRADICTION_LOG.md`.
2. Write `08_FINAL_REPORT.md` so it stands alone and is useful in the Report Viewer.
3. If Will needs to approve, accept, revise, defer, or choose a downstream
   action, add a compact decision gate inside the final report or final chat response.
4. Write `09_CONTENT_INPUT_PACK.md` or the shape-appropriate downstream pack:
   - content/creative input;
   - product prototype input;
   - RAG/knowledge retrieval input;
   - taxonomy/schema implementation input;
   - router/eval implementation input;
   - reference-ingestion decision packet;
   - asset/DAM/V3 handoff.
5. Write `10_SESSION_SUMMARY.md` with the exact next step.
6. Update `RESEARCH_INDEX.md` and any approved `CLIENT_CASE_MEMORY.md` entries.

For intelligence reports, include executive brief, source/dataset boundary,
top signals, landscape, examples, downstream implications, reusable checklist
or rubric, confidence/caveats, and exact next action.

For high-volatility topics, include a `Checked on` date and explicit freshness
limit in the final report or handoff packet.

For deep mode, `08_FINAL_REPORT.md` must include:
- `## Scope and Method`;
- `## Counterevidence and Unknowns`;
- `## Confidence and Limitations`.

The deep-mode `10_SESSION_SUMMARY.md` must state:
- `Deep completion status: complete`, `partial`, or `blocked`;
- `Stop reason: evidence_saturated`, `budget_limited`, or `blocked`;
- `Must-answer branches: <covered>/<total>`;
- `Open must-answer branches: <count>`;
- `Material claims supported: <supported>/<total>`;
- `Unsupported material claims: <count>`;
- `Unresolved material contradictions: <count>`;
- source authority, source diversity, freshness, and citation-entailment
  threshold results using the exact labels in `deep-mode.md`;
- the exact unresolved gaps for partial or blocked runs.

Keep `BR-*`, `SRC-*`, and `CLM-*` records aligned with those summary counts.
Do not mark a deep run complete when required sections contain placeholders or
when the measured records contradict the completion block.

## Scorecard

Use when a research run may be incomplete, stale, unsafe to reuse, or about to
feed planning, product, RAG, taxonomy/schema, router/evals, creative, prompts,
DAM, V3 assets, or execution.

Score as `pass`, `partial`, `fail`, or `not_applicable`:

1. scope clarity
2. brief approval / collection permission
3. source traceability
4. source diversity and tiering
5. freshness / date limits
6. contradiction handling
7. confidence tagging
8. recommendation-to-evidence linkage
9. downstream packet readiness
10. closeout summary
11. approval/readiness state
12. transcript-only evidence risk
13. research shape/output contract fit
14. deliverable resolution, representative example, and record-level coverage
15. claim-layer or schema traceability when applicable
16. eval corpus and acceptance criteria when applicable
17. safety/risk routing when applicable
18. reference-ingestion extraction/adoption decision when applicable

Prefer writing `stage01_Research/RESEARCH_QUALITY_SCORECARD.md`; if no stage
folder exists, write `RESEARCH_QUALITY_SCORECARD.md` at run root.

Readiness labels:

- `needs_plan`
- `needs_collection`
- `needs_verification`
- `ready_for_synthesis`
- `ready_for_report`
- `ready_for_handoff`
- `ready_for_productization`
- `complete`

## Bridge

Bridge research into the next downstream workflow while preserving research as
the evidence authority. Do not merge research and creative workflow.

First classify evidence state:

- `verified`
- `usable_with_cautions`
- `hypothesis_only`
- `blocked`

If the state is not `verified`, keep caution labels visible in all packets.

Choose only the downstream packet needed:

| Need | Output |
| --- | --- |
| campaign/content planning update | `stage01_Research/V2_PLAN_CHANGE_RECOMMENDATIONS.md` |
| product prototype implementation | `stage01_Research/PRODUCT_PROTOTYPE_INPUT_PACK.md` |
| RAG or knowledge retrieval | `stage01_Research/RAG_KNOWLEDGE_INPUT_PACK.md` |
| taxonomy or schema implementation | `stage01_Research/TAXONOMY_SCHEMA_INPUT_PACK.md` |
| router or eval implementation | `stage01_Research/ROUTER_EVAL_INPUT_PACK.md` |
| reference ingestion decision | `stage01_Research/REFERENCE_INGESTION_DECISION_PACKET.md` |
| creative exploration input | `stage01_Research/CREATIVE_DIRECTION_INPUT_PACK.md` |
| visual/motion research | `stage01_Research/VISUAL_CONTENT_RESEARCH_PACK.md` |
| prompt compilation | `stage01_Research/IMAGE_PROMPT_INPUT_BRIEF.md` |
| DAM wide-to-narrow lane | `stage01_Research/DAM_LANE_INPUT_PACK.md` |
| V3 asset generation | `stage01_Research/V3_ASSET_HANDOFF_BRIEF.md` |
| approval/review | `stage01_Research/APPROVAL_AND_GUARDRAIL_BRIEF.md` |

Every packet must include source/evidence basis, confidence/caution labels,
target downstream consumer, exact next action, acceptance criteria, approval
gates or blockers, and scorecard caveats when a scorecard exists.

Do not mutate canonical V2/V3 plan JSON unless explicitly approved.
