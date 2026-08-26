# Charter Bundle Contract

## Default doc

### PROJECT_CHARTER.md
Durable project identity, high-level compass, boundaries, current slice,
decisions, and validation summary.

Must include:
- captured goal
- current state
- roadmap or critical path
- plan shape
- purpose
- current objective
- project model
- user logic
- component/aspect map
- scope
- non-goals
- success criteria
- constraints
- current build slice or planning slice
- active decisions
- validation gates
- source-of-truth links
- read order

## Project Authority Pack / PAP

**Project Authority Pack** or **PAP** is the bundle label for the project's
decision-governing docs. The compact alias is `-pap`.

Use PAP to mean the current project's source-of-truth bundle, usually:

- `PROJECT_CHARTER.md`
- `PRODUCT_UIUX_DESIGN_AUTHORITY.md` when product/UIUX decisions exist
- `DECISIONS.md` when decision history is split out
- `BUILD_PACKET.md` when a bounded build slice exists
- `IMPLEMENTATION_PLAN.md` when sequencing is split out
- `REFERENCE_INDEX.md` when sources are distributed
- validation, read-order, or audit docs when they are active authorities

PAP is not a mandatory file and not a higher authority than its member docs. It
must not override root control docs, stage contracts, run manifests, registries,
backlog/work-item state, or approval gates.

### Design Authority Pack / DAP facet

`-pap design` is the canonical read-only design-authority facet of PAP and
`-dap` is its thin alias. It resolves existing charter, product/UIUX, declared
brand, current plan/task and evidence pointers without copying them. It reports
sources, locks, gaps and conflicts; `design` owns recommendations and design
actions after this resolution. DAP is not a skill, mandatory file, nested pack
or second authority layer.

## Client and multi-project authority

PAP always refers to one project. For a business or client containing multiple
projects, use the existing client authority bundle instead:

- `CLIENT_BRIEF.md` owns client-wide orientation and accepted cross-project
  decisions;
- `PROJECT_REGISTRY.json` owns project membership, lifecycle, parent/covered
  relationships, and session policy;
- each affected project keeps its own PAP authority where the client-wide
  decision materially changes that project.

Do not add `BUSINESS_PAP.md`, an umbrella project charter, or a mega-project to
represent the client. The portfolio Adam owner coordinates the projects but
does not absorb their execution authority.

For cross-project changes, record a compact impact matrix using
`update_required`, `already_current`, `not_applicable`, or `blocked`. Apply the
existing PAP delta receipt contract only to materially affected projects.
Cross-project reports remain evidence; accepted truth belongs in the client or
owning project authority named above.

## Optional split docs

Split out companion files only when the content is substantial, independently
updated, separately reviewed, or needed for external handoff.

### BUILD_PACKET.md
Use when the current bounded build slice needs its own operational artifact.

Should include:
- build objective
- in scope
- out of scope
- files likely affected
- acceptance criteria
- validation gate

### IMPLEMENTATION_PLAN.md
Use when execution sequencing is detailed enough to outgrow the charter.

Should include:
- task list
- dependencies
- owner/stage if relevant
- validation per task
- next action

### DECISIONS.md
Use when durable decisions are numerous, frequently updated, or need audit
history.

Should include:
- dated decisions
- rationale
- superseded decisions when relevant

### PRODUCT_UIUX_DESIGN_AUTHORITY.md
Use for product UI/UX projects when repeated UI/UX jobs, high-fidelity boards,
or design-to-build handoffs need one persistent app design authority.

Should include:
- document control and read order
- protected app design authority section
- product UI/UX plan and screen/state map
- component grammar
- visual direction and anti-patterns
- copy, proof, safety, and free/paid UX rules
- design override log
- generated artifact policy
- operational receipt pointers
- update rule separating design-law updates from operational ledger updates

Generated images, Figma review boards, screenshots, and implementation previews
should stay evidence until promoted in this file. The authority owns the current
generation-ready prompt pack, active low-fi/high-fi state, and declared Figma
target. Large batch ledgers, generated outputs, screenshots, validation
receipts, approvals, and run gates remain in run manifests, asset manifests,
batch contracts, ledgers, workspace-control records, or stage contracts, with
current pointers from the authority.

### UX_GUIDELINES.md
Use for lightweight UI, product, creative, or interaction guidance when the
content is reused across work but does not need a full UI/UX production
authority. For product/UIUX projects with Imagen or Figma production lanes,
prefer `PRODUCT_UIUX_DESIGN_AUTHORITY.md` and keep this file only as an alias or
legacy compatibility note when needed.

### AUDIT_BRIEF.md
Use for external review or handoff.

### VALIDATION_LOG.md
Use when repeated checks/builds/screenshots matter.

### REFERENCE_INDEX.md
Use when source material is spread across many docs/assets/APIs.

## Compatibility note

Existing project-specific names may remain in place when renaming would create churn. In that case, add a short alias note rather than forcing migration.

When the operator explicitly retires an old charter name, this general
compatibility allowance ends after a bounded migration: create and confirm
`PROJECT_CHARTER.md`, update active references, validate them, and retain only a
short retirement pointer if a live consumer still requires it. A retired file
must not remain a second authority.
