---
name: pipeline
description: Operator-facing hub for complete reusable workflows. Use for `-pipeline`, `-plan -dd`, `-dd`, `[pipeline - product]`, `startup-pattern-audit`, Double Diamond opportunity shaping, startup/founding/product idea audits, product build workflows, end-to-end workflow templates, and future workflow families such as marketing pipelines.
---

# Pipeline

Use this skill when Will asks for a complete reusable workflow, especially with
`-pipeline`. Use `-plan -dd` for Double Diamond planning workflow shaping; use
standalone `-dd` as shorthand for the same mode.

## Purpose

Route an end-to-end workflow into the smallest durable pipeline template that
can be reused, tested, and improved over time.

## Authority

This is a hub, not a new operating system.

Use existing workspace authorities:
- canonical project/run state under `client_cases/<client>/projects/<project>/`
- skill routing in `skills/HUB_MAP.md`
- product method in `skills/lean-product-factory/SKILL.md`
- reference ingestion in `skills/product-ingestion-to-slice-gate/SKILL.md`
- surface/prototype routing in `skills/creative-workflow/SKILL.md`
- implementation planning in `skills/workspace-implementation-planning/SKILL.md`
- startup intelligence pilot evidence under
  `client_cases/marketing_ai_optimisation/projects/startup_intelligence/`

Do not redefine paths, manifests, stages, active state, approvals, backlog
truth, or execution ownership.

These are host extensions, not portable runtime dependencies. When a named
path or owner is absent, use the self-contained mode and output contract in
this skill, work only from visible or supplied evidence, and state which
deeper host route is unavailable. Do not invent missing project state or block
a useful Double Diamond, startup-pattern, or compact product response.

## Modes

### `double-diamond`

Use when Will asks for `-plan -dd`, `-dd`, Double Diamond,
divergent/convergent workflow, opportunity exploration, research-to-plan
shaping, or "expand then narrow then test then decide".

Collision rule:
- hyphenated `-dd` means Double Diamond;
- explicit "Double Diamond" or Discover / Define / Develop / Deliver language
  means Double Diamond;
- uppercase `DD` or bare `dd` can mean due diligence in market, company,
  startup, investment, or research contexts, so clarify instead of routing
  automatically when the four-phase workflow is not explicit.

Positioning:
- this is a planning workflow method, not an audit method;
- standalone `-dd` should be treated as shorthand for `-plan -dd`;
- bare `DD`/`dd` without the hyphen is not enough in diligence-heavy contexts;
- keep `pipeline` as the reusable method engine while `-plan` remains the
  operator-facing output lane.

Default output:
- Discover: candidate space, facts/claims/unknowns, no-go red flags.
- Define: selected hypotheses, assumptions, constraints, and kill rules.
- Develop: lowest-risk tests, paper/prototype/simulation rows, and metrics.
- Deliver: playbook, approval packet, no-go, or next research question.

Guardrails:
- do not treat discovery as execution approval;
- do not create a new project, skill, backlog, runtime, or state layer by
  default;
- use `research` when freshness or external evidence matters;
- use `workspace-project-management` only when the output becomes canonical
  work;
- preserve hard approval gates for external sends, provider spend, production
  mutation, credentials, payment, destructive writes, and live trading.

### `startup-pattern-audit`

Use for startup/founding/product idea audits through YC/startup-pattern lenses.
This is a pipeline-level function, not a separate skillhub yet.

Read `references/startup_pattern_audit.md` when the request needs an audit,
scorecard, or reusable startup-pattern reasoning. For deeper evidence, use a
host's latest `startup_intelligence` run registry and pilot pattern cards when
present; otherwise request or research only the named evidence gap.

Default output:
- pattern matches
- category/customer/offer/wedge read
- missing proof
- riskiest assumption
- cheapest validation test
- suggested MVP wedge
- pipeline note when reusable

Guardrails:
- separate source facts from Adam inference
- no investment advice, fundraising claims, or market-size hallucination
- do not recommend a build before the validation gate is explicit
- promote to a dedicated `startup-intelligence` hub only after repeated use
  proves routing friction

### `product`

Use for product build, MVP, app/tool creation, prototype-to-build workflows, or
product-development methodology.

Default output:
- a reusable product pipeline packet
- one selected next gate or slice
- validation criteria
- method note only when reusable learning exists

Optional host template:
- `shared/templates/pipeline/product_pipeline.template.md`

When it is absent, use the seven workflow headings below as the complete
portable packet rather than treating the template as a blocker.

Workflow:
1. Scope
   - product thesis, target user, job-to-be-done, outcome, constraints, non-goals
2. Research existing
   - comparable products, reference workflows, source ledger, copy/adapt/reject matrix
3. Verify concepts
   - opportunity map, riskiest assumption, concept tests, pass/fail signal
4. MVP prototype
   - Figma or prototype-surface packet, core flow, key screens, test script
5. Operator refinement
   - keep/fix/cut, scope freeze, appetite, P0/P1 split
6. Development
   - implementation slices, affected files/surfaces, acceptance criteria, validation
7. Learn and optimise
   - proof, persevere/pivot/cut/defer decision, reusable method note if warranted

Routing:
- use `lean-product-factory` for product framing, slice shaping, acceptance
  criteria, and method notes
- use `product-ingestion-to-slice-gate` when external references, repos, exports,
  prior app lessons, or comparable product research must become one build slice
- use `creative-workflow - surface` for prototype surfaces and Figma handoff
- use `workspace-implementation-planning` only after the operator approves a
  development slice or implementation packet

Guardrails:
- do not build before the riskiest assumption and cheapest test are explicit
- do not treat Figma as implementation approval; it is a prototype/spec artifact
- do not expand into a full product packet when a compact slice will decide the
  next gate
- preserve approval gates for external sends, destructive writes, credentials,
  payments, production mutations, and existing external/Figma file mutation

### `marketing`

Status: planned route stub.

For now, route marketing pipeline requests through `marketing-system` and
`creative-workflow` until a real repeated workflow proves the need for a durable
`shared/templates/pipeline/marketing_pipeline.template.md`.

## Output Discipline

For discussion or planning, return the pipeline packet inline unless Will asks
to write it.

For durable capture, write to the closest canonical project/run location. Use a
scratch folder only when no client/project context exists and the artifact is
explicitly exploratory.

Always include:
- current gate
- next decision
- proof needed
- non-goals
- validation

## Trigger Tests

Read `references/trigger-tests.md` when validating pipeline routing, especially
the boundary between Double Diamond planning, startup-pattern audit, product
pipeline, and ordinary marketing/creative routing.
