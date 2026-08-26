# Improve Trigger Tests

Use these cases when validating `improve` routing and proceed behavior.

| Operator phrase | Expected behavior |
|---|---|
| `-improve this skill logic` | Audit the target, show the complete phased plan inline, open discussion, and stop before edits pending explicit approval. Route later execution through Skill Control Layer and `yeem-skill`. |
| `-improve this skill based on recent usage` | Run usage audit first: invocations, trigger phrases, scoped transcript evidence, interaction patterns, wiring, registry/index visibility, near-miss collisions, and runtime caveat; then rank options. |
| `-improve this landing page` | Keep ownership with the page/design route; the word `improve` alone must not transfer the task to the persistent workspace skill-maintenance lane. |
| `-improve skill design` | Bind explicitly to the canonical `design` skill and route maintenance through the persistent workspace skill owner; do not treat this as a request to redesign an artifact. |
| `-improve the improve skill` | Use the skill-improvement protocol, lock scope to `skills/improve/`, recommend a lean reference/test/output-contract patch, and avoid recursive self-evolve or global routing edits unless separately approved. |
| `-improve all skills` | Run normal skill-target diagnosis across the skill inventory, aggregate/rank opportunities, return recommendations, and do not patch target skills during the first planning pass. |
| `run a chartered Control Room scan across every workspace skill with 30-day evidence and checkpoints` | Freeze the canonical inventory, compile privacy-bounded directional usage evidence, write one no-write record per skill, checkpoint every ten active skills, and verify hashes; do not edit target skills. |
| Control Room usage index has zero matches for a skill | Report `not_observed_unknown`; never call the skill unused or recommend retirement from absence alone. |
| Control Room baseline hash changes during the scan | Stop the scan and report drift; do not mix old and new skill bodies into one fleet baseline. |
| `do an improvement pass on the current skills` | Bind to the skills materially used by the current request/lane, show one connected audit and complete plan, and stop for approval. On a later approved pass, patch only the connected shared weakness and validate; do not treat it as an all-skills fleet pass. |
| `capture this plan to another TUI, then improve current skills` | Preserve the session handoff gate, label delivery certainty, patch the current route/handoff skills only, and stop before unrelated fleet edits. |
| `-improve all skills proceed` with no accepted fleet plan | Treat as approval to complete the planning-only fleet pass; do not patch target skills in the first pass. |
| `-improve all skills proceed` after an accepted fleet plan | Execute only the recommended bounded target when safe and approved; stop before broad multi-skill edits, runtime-loading changes, or destructive cleanup. |
| `make this UI better` | Route to `design` unless the operator explicitly wants generic ranking first. |
| `-improve this viewer, the flow is confusing` | Audit user-flow first: user's natural questions, first-screen order, decision path, and source traceability; then route to design/workspace owner. |
| `-improve this business plan` | Return top 3 improvement options; use audit/research only when evidence changes ranking. |
| `-improve efficiency of this workflow` | Inspect current shape, duplicated work, avoidable context load, weak validation, fragile handoffs, and specialist owner before ranking. |
| `-improve bloat in this system` | Run delete/absorb/merge/shrink/reference-only check before recommending new files, modes, skills, views, or workflows. |
| `-improve proceed` after a diagnosis but without an approved complete plan | Show the complete plan, open discussion, and stop before writes. |
| `-improve proceed` with no visible diagnosis | Run the audit and complete plan first or ask for the target; do not infer from unrelated recency or execute. |
| `-improve proceed` after explicit approval of the visible complete plan | Execute the recommended bounded plan when local, safe, scoped, and ungated, then run QA. |
| `-improve proceed option 2` | Execute option 2 only when its complete visible plan is explicitly approved, safe, and sufficiently scoped. |
| `-improve -discuss` | Show the improvement audit and complete plan, then keep the lane conversation-locked for revision; do not edit. |
| `-improve -plan all` | Show Plan Compass plus the complete improvement journey as outcome milestones with deliverables, human input, exit evidence, state, exclusions, and approval gate. Keep task/path/validator detail under `-plan full`; do not treat planning as execution approval. |
| `-improve the current -proceed behaviour -discuss then plan` | Audit existing command contracts first, then plan; do not patch until approved. |
| `-improve current auto proceed behaviour proceed` | Patch the approved bounded command contract only; route long-running `auto proceed` semantics to `adam-auto-loop` preflight. |
| `keep improving this overnight` | Route to `adam-auto-loop` improve mode, not one-off `improve`. |
| `self-evolve this pattern` | Normalize through `improve`; call `self-evolve` only if the target is recurring lesson capture or future behavior change. |
| `-qa check if this is done` | Route to `quality-check`, not `improve`. |
| `audit this before planning` | Route to `audit-check` or domain audit, not `improve`. |
| `create a new control layer to improve this` | Apply `user-skill` first; do not create structure by default. |
| `create a new meta-skill to improve every skill` | Prefer the existing `improve` + Skill Control protocol; recommend absorb/reduce unless evidence proves a new skill is necessary. |
| `-improve -ask` | Ask one scoped question if target or quality bar changes ranking. |
| `-improve` with no visible target | Ask one scoped target question; do not infer from unrelated recency. |
| `-improve everything` | Ask for the target or scope; do not start a broad workspace sweep. |
| `-improve all skills` when audit queue is empty | Still run opportunity ranking across skills; clean audit means no urgent repair, not no meaningful improvement. |
| `-improve this based on how I usually work` with a fresh Pattern Profile | Query the bounded target slice through `adam-pattern`; preserve confidence, limitations, and provenance; do not rescan transcripts by default. |
| `-improve this based on how I usually work` with a stale or contradicted profile | Name the stale/contradicted evidence and use the retrieval ladder; refresh only when needed, not automatically. |
| `-improve this because I disliked the last answer` | Treat direct feedback as a useful selected signal, not representative proof; name the limitation and propose the cheapest reversible test. |
| `-improve this workflow; users keep retrying` | Separate the observed retry signal from the inferred cause; define a hypothesis, user outcome, and non-regression guardrail before planning. |
| `-improve this skill -research` | Route to research only when external facts, contradictions, representative evidence, or durable evidence authority would change the recommendation. |
| `-improve this skill -explore` | Widen materially different directions before ranking; do not turn `improve` into the exploration owner. |
| `-improve, then -audit and -plan all` | Keep one evidence packet across the compound journey; show the audit and complete milestone roadmap, open discussion, and do not treat audit or planning as execution approval. |
| `-improve proceed` after an evidence-loop diagnosis | Execute only the approved bounded hypothesis; preserve the stated outcome metric and guardrail for post-build QA. |
| `-qa the improvement` | Use `quality-check` to verify implementation and guardrails, then emit the minimum learning receipt; structural pass alone is not outcome proof. |
| `learn from this improvement for future sessions` | Promote to `self-evolve` only when the observed lesson recurs or should change future behavior; do not promote an unobserved hypothesis. |
| `-improve this project workflow` and the project has a brief/charter | Resolve the project through its index, read the brief first, and classify charter alignment before ranking. |
| `-improve this standalone paragraph` with no project context | Skip charter discovery and run the normal lightweight diagnosis. |
| `-improve this project` where the charter conflicts with root authority | Report `conflict`, follow higher authority, and route a narrow charter refresh; do not treat charter text as approval. |
| `-improve this project` where no charter exists | Report `charter_missing`; continue unless persistent context is necessary, and do not create a charter by habit. |
