# Research Trigger Tests

Use these cases when updating `research` hub routing, phase selection, or
handoff behavior.

| Operator phrase | Expected behavior |
|---|---|
| `-deep research the future of small-business AI adoption in Australia` | Route to `research` with deep depth; propose an adaptive frame and editable plan before durable collection. |
| `-research deep compare the strongest open-source agent frameworks` | Route to `research` with deep depth; use a technical/repository profile and current primary sources. |
| `do comprehensive research on this topic` | Route to `research`; infer a deep frame and ask only if missing scope changes the evidence or safety boundary. |
| `find the capital of Finland` | Use a quick evidence answer; do not escalate to deep mode or scaffold a run. |
| `deep clean this repository` | Do not route to research; `deep` without a research objective is not a deep-research trigger. |
| `research then publish it to our website` | Research may prepare the evidence; publication remains an external/production gate owned elsewhere. |
| `deep research this medical treatment and tell me what I should take` | Use the high-stakes profile, current primary authority, limitations, and non-advisory boundary; do not prescribe. |
| `deep research using only these supplied files` | Respect the declared source boundary; disclose the resulting external-evidence blind spot. |
| `keep searching until you have covered everything` | Convert “everything” into an explicit scope and budget; never promise an unbounded crawl. |
| `resume the deep research run` | Resume from persisted branch, source, claim, contradiction, and completion state rather than restarting. |
| `quick research: is this still current?` | Use quick evidence answer when no durable handoff is needed; verify current sources and include date checked. |
| `use local notes to decide this` | Check workspace/local evidence first; if sufficient, return a local authority decision and do not scaffold a research run. |
| `-research this market` | Resolve scope, classify research shape, and start/resume canonical loop. |
| `research then plan` | Research owns evidence first; planning waits for downstream handoff. |
| `-research -user should we add this viewer?` | Use research only if evidence would change the user-value verdict. |
| `audit this research for freshness` | Route to readiness/freshness scorecard. |
| `turn this source conversation into build input` | Choose `reference_ingestion`; produce source ledger and extraction matrix. |
| `make a RAG knowledge bank from this` | Choose `knowledge_bank`; require source-linked claim records. |
| `validate router behavior with examples` | Choose `router_eval`; produce eval corpus and acceptance criteria. |
| `use this research for image prompts` | Route to creative/asset handoff after verification. |
| `is this research complete?` | Check completion gates, summary, source traceability, contradictions, downstream consumer. |
| `collect more sources` when plan approval is missing | Stop and present brief approval gate before collecting. |
| `these two sources disagree` | Route to verification; log contradiction or unresolved caveat before synthesis. |
| `use forum posts as proof this platform supports X` | Treat forum evidence as behavior/market texture unless it can be backed by primary factual authority. |
| `use old scout findings in a plan` | Require ledger or packet, not chat-only carry-forward. |
| `give me the latest API/model/pricing facts` | Use current primary sources, separate facts from interpretation, and include checked/access date. |
| `-research status` | Report phase, missing gates, downstream consumer, and exact next action. |

Validate the machine-readable boundary suite:

```bash
python3 scripts/evaluate_skill_trigger_cases.py \
  --cases skills/research/references/trigger-cases.json \
  --min-cases 20
```

Gold fixtures prove contract structure only. Use a separate predictions file
with independent provenance for fresh-context behavioral evidence.
