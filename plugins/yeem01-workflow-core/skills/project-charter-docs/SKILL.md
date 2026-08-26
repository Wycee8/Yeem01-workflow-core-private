---
name: project-charter-docs
description: Create, inspect, refresh, or package persistent project charter context and Project Authority Packs (PAP), including the read-only design facet invoked as -pap design or -dap; default to one lean charter file and split only when justified.
---

# Project Charter Docs

Create or refresh durable project context docs without inventing a new task system.

## Core rule

This skill creates **context durability**, not execution authority.

Do not replace or duplicate:
- `workspace_control/work_items/WORK_ITEMS.json`
- project `RUN_REGISTRY.json` / `REPORT_REGISTRY.json`
- selected run manifests
- stage contracts
- active work-item claims
- canonical backlog items

Link to those authorities when they exist.

## Charter / viewer boundary

`-charter` is the compact canonical project context layer. It should preserve
durable truth: what the project is, the captured goal, current state, roadmap or
critical path, plan shape, project model, user logic, component/aspect maps,
scope, non-goals, success criteria, constraints, active decisions, validation
gates, source links, and read order.

Use `charter-session-viewer` when the operator needs a user-facing projection
of that charter plus related plan/report/validation evidence. The viewer may
unpack and interpret source refs for reading and decision support, but it must
not become the canonical charter, task store, approval store, or source app
dashboard.

## Project Authority Pack / PAP

**Project Authority Pack** or **PAP** is the short bundle label for a project's
decision-governing docs. The compact alias is `-pap`.

When the operator says `PAP`, `project authority pack`, or `-pap`, resolve the
current project and inspect or update the relevant source-of-truth bundle. A PAP
usually includes `PROJECT_CHARTER.md`, `PRODUCT_UIUX_DESIGN_AUTHORITY.md`,
`DECISIONS.md`, `BUILD_PACKET.md`, `IMPLEMENTATION_PLAN.md`,
`REFERENCE_INDEX.md`, and validation or read-order docs when present.

PAP is a bundle label, not a new authority layer or mandatory file. It points to
existing project authorities and must not override root control docs, stage
contracts, run manifests, registries, backlog/work-item state, or approval
gates.

### Design Authority Pack / DAP

`-pap design` is the canonical design-authority view inside the current
project's PAP. `-dap` and `design authority pack` are thin aliases for the same
view. DAP is not a skill, mandatory file, nested task system, or higher
authority than the PAP sources it resolves.

Bare `-dap` is read-only. It answers only:

- which sources currently own project design truth;
- which brand, product/UIUX, reference and task constraints are locked;
- which design decisions are provisional, missing or conflicting;
- which current plan, task/run and evidence pointers apply.

It does not recommend a new visual direction or perform design work. Route
those jobs to `design`, which consumes DAP before acting.

Resolve DAP in this order without copying source content:

1. `PROJECT_CHARTER.md` for project intent, user, scope and declared authority pointers;
2. `PRODUCT_UIUX_DESIGN_AUTHORITY.md` when repeated product/UIUX work justifies it;
3. a declared reusable brand authority such as `BRAND_STYLE_GUIDE.md`, or another explicitly named project design authority;
4. the current implementation plan and task/run brief for scoped requirements and current state;
5. current Figma, asset and validation evidence only as evidence until an owning authority promotes a decision.

For an explicit project and a read-only `-dap` or `-pap design` call, use the
bounded DAP fast path. Read only the charter's current state and authority
pointers, the declared UI/UX or brand authority, the current plan's state and
gates, and the reference index. Inspect the project registry or current run
manifest only when the answer depends on a run-bound design fact. Do not read
`active/*` compatibility projections, workspace-wide control views, unrelated
runs or reports, `SKILL_CALLING_FRAMEWORK.md`, `HUB_MAP.md`, or the Design
skill on a clean single-owner call. Expand only when the project target is
ambiguous, applicable sources conflict, or the operator asks for exact evidence.
Stop as soon as the sources, locks, gaps, conflicts and current pointers are
answered.

Fast-path read budget: after the explicit project and alias resolve, do not run
recursive route discovery, broad `find`, or workspace-wide `rg`. Do not
full-read a project authority longer than 200 lines. Use exact heading/status
matches plus bounded ranges and inspect no more than 250 project-authority lines
in total—including command output—before the first answer. When a run pointer
is requested, query only `activeRunId` plus the matching run's `id`, `status`,
`type` and `manifestPath` from `RUN_REGISTRY.json`; do not full-read the registry
or run manifest unless a named fact is absent from that projection. If the
budget cannot resolve a decision-grade fact, name the missing fact and expand
only to its owning source.

When two applicable sources conflict, report the exact conflict and remain
read-only. Missing authority permits only clearly disclosed reversible defaults;
it never permits invented brand law, destructive writes, generation, external
effects or a claim that the design is approved.

### Client and multi-project boundary

Keep PAP scoped to exactly one project. When a request concerns a business,
client, portfolio, or several projects under one business, do not create a
business PAP, umbrella `PROJECT_CHARTER.md`, or mega-project.

Resolve that request through the existing client authority bundle:

1. `CLIENT_BRIEF.md` for client-wide direction and accepted cross-project
   decisions;
2. `PROJECT_REGISTRY.json` for project membership, lifecycle, parent/covered
   relationships, and session policy;
3. the affected projects' PAP sources only where the client-wide decision has
   a material local impact.

The portfolio Adam owner coordinates visibility, overlap, sequencing, gates,
and handoffs. Adam does not become the source-file owner for every project or
absorb project execution.

For a client-wide decision, name the affected projects and classify each local
impact as `update_required`, `already_current`, `not_applicable`, or `blocked`.
Emit the existing PAP delta receipt only for materially affected projects;
`not_applicable` is a portfolio impact result, not a new ledger PAP result.
Treat cross-project audits and reports as evidence. Capture accepted client
truth in `CLIENT_BRIEF.md` or `PROJECT_REGISTRY.json`, and project-specific
truth in the owning project's PAP sources.

### PAP impact and delta receipt

For every material operator instruction, classify whether it changes one or
more PAP components before reporting completion:

| Change | PAP component to inspect or refresh |
| --- | --- |
| goal, objective, scope, non-goal | project charter |
| approved decision, selected concept, canonical lock | decisions and the owning authority |
| plan, phase, build path, implementation direction | current plan/build packet pointer |
| UI/UX, representation, fidelity, Figma or Imagen direction | product UI/UX design authority |
| source, acceptance rule, validation or read order | reference index or validation/read-order docs |

No impact means no PAP write. An applicable impact requires a compact delta
receipt in the operator-input/session-continuity record before the material
input is marked complete:

```text
pap_impact: [affected component categories]
pap_delta_refs: [source-of-truth files inspected or updated]
pap_result: updated | already_current | blocked
```

`already_current` requires source inspection; it must not be inferred from a
prior assistant summary. `blocked` keeps the operator input unresolved and
names the missing authority or conflicting decision. The receipt is metadata
on existing continuity state, not a new PAP artifact.

The operator-input ledger must reject a `completed` material record when
`pap_impact` is non-empty unless `pap_delta_refs` is non-empty and `pap_result`
is `updated` or `already_current`. This validation applies at the canonical
record boundary, not only in a CLI wrapper or agent instruction.

## Charter Shape

Keep the charter source-oriented, not dashboard-shaped. The top of
`PROJECT_CHARTER.md` should make these high-level facts easy to find before
longer details:

- **Captured goal:** what the project is trying to achieve.
- **Current state:** where the project is now, including the active gate.
- **Roadmap / critical path:** where the project is going and the major path.
- **Plan shape:** how work is expected to move, with dependencies or gates.
- **Project model:** identity, audience/user, success signals, constraints, and
  non-goals.
- **User logic:** who benefits, what job/friction is being solved, and what the
  simplest useful version is.
- **Component / aspect map:** important surfaces, workflows, modules, assets,
  data, UX/brand/research/architecture/operations/commercial/safety aspects.
- **Source authority:** which files own truth and which generated viewers only
  project it.

If one of these facts is unknown, mark it as unknown or link the source needed
to resolve it. Do not invent a goal, roadmap, or model to make the charter look
complete.

## User-value rule

Default to the smallest artifact that keeps future work oriented.

For lightweight or high-level planning, create or refresh **one**
`PROJECT_CHARTER.md` first. Do not split into multiple files merely because
templates exist. Split into companion docs only when a section has enough
operational detail, reuse, or audit value to justify a separate file.

Capture guard: when the operator says `capture this -charter`, `capture this as
charter`, or similar, update the existing `PROJECT_CHARTER.md` or create that
single file first. Do not create a separate plan, operator-review, decision log,
or summary file unless the split is explicitly justified by reuse, audit,
ownership, or lifecycle.

## Use when

- The operator says “project charter”, “creation charter”, “persistent planning docs”, “long-lived project docs”, “durable project context”, or “capture this as charter docs”.
- A product/app/creative/client project needs reusable reference docs before build or audit.
- A plan needs to survive chat/session drift.
- An external audit package needs a stable read order and source-of-truth summary.

## Mode router

Choose one mode from the request:

| Mode | Use when | Output |
|---|---|---|
| `inspect` | Charter docs may exist or be stale | Gap report + recommendation |
| `create` | Durable context is missing | Lean charter; companion files only when justified |
| `refresh` | Existing docs need current state | Targeted doc updates |
| `audit-pack` | Preparing external review | Audit brief/read order/package guidance |

If the operator only asks to evaluate or plan, do not write files. If they ask to “capture”, durable local docs are allowed.

## Output contract

Return:

1. selected mode and resolved project/client scope
2. authority files inspected and their current/unknown state
3. files created or refreshed, or a no-write gap recommendation
4. PAP impact receipt (`pap_impact`, `pap_delta_refs`, `pap_result`) when applicable
5. validation performed, unresolved conflicts, and next bounded action

Trigger fixtures: `{baseDir}/references/trigger-tests.md`

## Minimum workflow

1. Resolve the project root.
   - Prefer explicit path.
   - Otherwise use current app/project selection and indexes before deep browsing.
   - If the request spans a client or several projects, resolve the client
     authority bundle first and do not silently bind it to the most recent
     project.
2. Identify authority files.
   - Workspace/project indexes, registries, run manifests, source docs, architecture decisions.
3. Apply the necessity gate.
   - What context keeps getting lost?
   - Who/what needs to reuse it?
   - What is the smallest durable bundle?
4. Choose the bundle.
  - Default to `PROJECT_CHARTER.md` only.
  - Keep the high-level charter shape in the charter itself; use companion docs
    for detail only after a section becomes too large, separately owned, reused,
    or independently reviewed.
   - Split companion docs only when a section is substantial, frequently reused, independently owned, or needed for audit/review.
   - If the phrase is `capture this -charter`, treat one-file-first as the
     default answer even when the project already has companion charter files.
5. Write or refresh narrowly.
   - Preserve existing decisions unless explicitly superseded.
   - Avoid broad rewrites.
6. Validate.
   - Check files exist, references are sane, and no new task system was created.
7. Commit workspace changes after successful edits only when the operator requested or approved a commit.

## Charter Cleanup Checklist

When the operator asks to make sure a charter is latest, clean up dated or
retired files, and publish or push, use this narrow cleanup pattern:

1. Refresh the living `PROJECT_CHARTER.md` first with the current state,
   current roadmap, active source links, and dated decision log entry.
2. Keep active specs, runbooks, standards, indexes, and current roadmap/report
   files visible in the project docs root.
3. Move superseded dated audit, evidence, or one-off cleanup packets into a
   dated archive folder such as `docs/archive/retired_YYYY-MM-DD/`.
4. Add or update an archive `README.md` that explains why each packet moved and
   which current doc replaces it.
5. Search for stale links to moved files and update only the current source docs
   that still reference retired paths.
6. Validate before commit or push: diff hygiene, relevant local tests or
   contract checks, and any project-specific restore/health check that proves
   the cleanup did not disturb runtime assumptions.
7. Commit or push only when the operator explicitly requested or approved that
   Git side effect.

Do not delete evidence by default. Do not mix docs cleanup with runtime,
credential, Drive, Sheet, Photoshop, deployment, or production mutations unless
the operator explicitly approves those separate side effects.

## Default bundle

Default file:

```txt
PROJECT_CHARTER.md       # captured goal, state, roadmap, model, scope, validation, read order
```

Optional split files:

```txt
BUILD_PACKET.md          # current build slice and acceptance criteria
IMPLEMENTATION_PLAN.md   # executable sequence, dependencies, validation
DECISIONS.md             # durable product/architecture decisions
PRODUCT_UIUX_DESIGN_AUTHORITY.md # product UI/UX design law and promoted design decisions
UX_GUIDELINES.md         # lightweight UI/product/creative guidance when a full authority doc is not justified
AUDIT_BRIEF.md           # external review handoff
VALIDATION_LOG.md        # repeated checks matter
REFERENCE_INDEX.md       # many source docs/assets/APIs matter
```

Bundle alias:

```txt
Project Authority Pack / PAP / -pap
# shorthand for the current project's charter, UI/UX authority, decisions,
# plan/build packets, reference index, and validation/read-order docs

Design Authority Pack / DAP / -dap / -pap design
# read-only design facet of the same PAP; resolves existing design-authority
# sources and never creates a separate pack or mandatory file
```

Use split files when one of these is true:
- the section is long enough to make the charter hard to scan;
- different agents or stages will update it independently;
- it has a distinct validation/review lifecycle;
- external reviewers need a separate packet;
- the project already has populated split files and merging them would create churn.
- product UI/UX or design-to-build jobs need a persistent design authority for
  app design law: journeys, IA, screen states, components, visual direction,
  copy/safety rules, free/paid UX, and promoted design decisions.
- keep the current generation-ready prompt pack, active low-fi/high-fi state,
  declared Figma target, current project-plan pointer, review decision, and next
  design action in the design authority; keep detailed execution phases, large
  ledgers, generated outputs, screenshots, validation, approvals, and run-state
  receipts external and link their current records.

Read `references/charter-bundle-contract.md` when deciding exact bundle shape.

Compatibility rule: for product/UIUX projects, prefer
`PRODUCT_UIUX_DESIGN_AUTHORITY.md` over `UX_GUIDELINES.md`. Do not blindly
rename or delete populated legacy files; add a short alias or migration note
when compatibility matters.

## Templates

Use templates only when creating missing files:
- `templates/PROJECT_CHARTER.template.md`
- `templates/BUILD_PACKET.template.md`
- `templates/IMPLEMENTATION_PLAN.template.md`
- `templates/DECISIONS.template.md`
- `templates/PRODUCT_UIUX_DESIGN_AUTHORITY.template.md`
- `templates/UX_GUIDELINES.template.md`
- `templates/AUDIT_BRIEF.template.md`

Do not overwrite a populated file with a template.

## Routing boundaries

Read `references/routing-boundaries.md` when the request overlaps planning, backlog, creation, or skill governance.

Quick boundary:
- Use `workspace-implementation-planning` for execution decomposition.
- Use `project-charter-docs` when the output must become durable project context.
- Use `backlog-item-adder` for canonical backlog items.
- Use `create-guide` when the creation intent is not shaped enough.
- Use `yeem-skill` when designing or modifying a skill.

## Validation checklist

Before claiming completion:
- charter docs have a clear read order
- canonical authority is linked, not duplicated
- viewer/projection outputs are linked as generated views, not source truth
- current build slice is explicit or marked unknown
- decisions are durable and dated
- validation gates are concrete
- optional docs are justified by project need
- no secrets, caches, build outputs, or raw session noise were added
