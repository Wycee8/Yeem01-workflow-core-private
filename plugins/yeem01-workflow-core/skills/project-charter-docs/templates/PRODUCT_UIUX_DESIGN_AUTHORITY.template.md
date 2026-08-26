# Product UI/UX Design Authority

Status: `<draft | active | superseded>`
Last updated: `<YYYY-MM-DD>`
Client/project: `<client / project>`
Product: `<product name>`

DAP route: `-pap design` (canonical) / `-dap` (thin alias)

## Document Control

This file is the persistent **app design authority** for `<product name>`. It
owns product UI/UX truth: user journeys, information architecture, route/page
jobs, screen states, drawers, sheets, modals, proof labels, component grammar,
visual direction, copy rules, safety posture, and free/paid UX boundaries.

This file does **not** own operational state. Image-generation batches, Figma
placement history, screenshots, run gates, approval receipts, task claims, and validation
logs live in run manifests, asset manifests, batch contracts, ledgers, and
workspace-control records. Those artifacts may provide evidence, but they do not
become design law unless a named design decision is promoted into this file.

The authority must nevertheless declare the current design-production target
and point to its current external receipt. This prevents future design work from
reconstructing the destination from batch history while keeping large ledgers
and placement history outside the authority.

## Current Design Production Target

| Field | Current authority |
| --- | --- |
| Design state | `<FULL_APP_LOW_FI | FULL_APP_HIGH_FI>` |
| Figma file | `<file name>` |
| File key | `<file key>` |
| Canonical page/node | `<page/node ID>` |
| Canonical URL | `<direct target URL>` |
| Placement zone | `<named board/section/coordinates or creation rule>` |
| Board role | `<structural coverage | visual review | editable production | handoff>` |
| Allowed writes | `<explicit non-destructive scope>` |
| Excluded writes | `<destructive replacement and other hard gates>` |
| Current receipt | `<current placement/screenshot/metadata receipt>` |

## Current Project Plan

- Plan: `<project-specific implementation plan path>`
- Current design phase: `<phase / gate>`
- Next plan action: `<action>`

The plan owns execution decomposition and status. This authority owns design
truth and only points to the current plan.

Target resolution rule: resolve the declared page/node before inspecting or
writing child boards. Child review frames are content inside the target and do
not replace it as the canonical destination. Stop and reconcile conflicting
targets before writing.

## Read Order

For product and design decisions:

1. `PROJECT_CHARTER.md`
2. `PRODUCT_UIUX_DESIGN_AUTHORITY.md`
3. `<product-fit / research / pipeline packet when needed>`
4. `<active run manifest only when reading operational state>`

PAP / `-pap` means the wider Project Authority Pack: charter, this UI/UX
authority, active decisions, plan/build packets, reference index, and
validation/read-order docs. Use it as a read-order bundle label, not a separate
design authority.

DAP / `-dap` means the read-only design facet of that same PAP. It resolves
this file when applicable, declared brand authority, scoped task requirements
and current evidence pointers without copying them into another file. Use
`-design` when a recommendation or design action is required.

## Protected App Design Authority

Everything in this section is app design law.

### Product And User Frame

- Product promise:
- Primary user:
- First user job:
- Success signal:
- Non-goals:

### Priority Model

| Model | Meaning | Current value |
| --- | --- | --- |
| `UX Priority P0` | Must exist for a trusted product experience, first screen, top-level need, or mandatory component. | `<value>` |
| `UX Priority P1` | Important for MVP depth or repeat use. | `<value>` |
| `UX Priority P2` | Useful but not required for first validation. | `<value>` |
| `UX Priority P3` | Advanced, expert, paid, or commercial expansion. | `<value>` |
| `Execution P0` | Current buildable/product-fit slice. | `<value>` |
| `Execution P1+` | Build phases after validation. | `<value>` |

### Canonical Journey

```text
<Step 1>
-> <Step 2>
-> <Step 3>
```

### Screen / Route Map

| Screen / route | User job | Primary action | Proof/safety rule | Notes |
| --- | --- | --- | --- | --- |
| `<screen>` | `<job>` | `<action>` | `<rule>` | `<notes>` |

### App Shell And Navigation Rules

- Root destinations:
- Pre-trust or pre-auth navigation rule:
- Root vs nested back behavior:
- Drawer/sheet/modal return behavior:
- Forbidden route bleed:

### Component Grammar

| Canonical component | Alias | Owns | Required states |
| --- | --- | --- | --- |
| `<Component>` | `<Alias>` | `<job>` | `<states>` |

### Visual Direction

- Feeling target:
- Product posture:
- Palette roles:
- Typography posture:
- Density:
- Radius and elevation:
- Icon/image/material rules:
- Anti-patterns:

### Copy, Proof, And Safety Rules

- Preferred user-facing terms:
- Avoided terms:
- Proof/confidence language:
- Sensitive-data language:
- Destructive-action language:
- Required caveats:

### Free / Paid UX Boundary

- Free layer:
- Paid layer:
- Paywall timing:
- Paid preview rules:
- Forbidden monetization behavior:

## Current Generation-Ready Prompt Packet

Maintain this section after low-fi structure is accepted and generation is
useful. Preparing or auditing it does not authorize provider execution.

- Shared design intent:
- Screen inventory and stable IDs:
- Visual and component system:
- Per-screen instructions:
- Consistency rules:
- Negative constraints:
- Reference policy:
- Output and batch requirements:
- Figma placement target:
- Review rubric:
- External manifest pointer, when volume requires one:

## Design Override Log

Use this table when later work supersedes or clarifies prior design source
material.

| Conflict surface | Ruling | Production effect |
| --- | --- | --- |
| `<conflict>` | `<decision>` | `<effect>` |

## Generated Artifact Policy

Generated images, review boards, screenshots, and implementation previews are
evidence until promoted here. Exact UI copy, screen-state logic, source labels,
confidence rules, route/page ownership, tab behavior, and product behavior
remain deterministic and owned by this authority unless explicitly promoted.

### Review Surface Policy

For UI/UX image-generation lanes, Figma is the default review surface when this
authority declares the target and allowed non-destructive scope.

In that case, generated images must be persisted locally, placed into the
declared Figma review board or declared slots, captured with a proof screenshot,
and recorded in the operational Figma board receipt before the batch is called
review-ready. Chat attachments and media paths are delivery receipts, not the
primary review surface.

If no Figma review-board target is declared, use a local contact sheet
or local review surface instead of mutating Figma.

This policy authorizes review placement only. It does not authorize final Figma
lock, editable production capture, app implementation, external send,
deployment, destructive deletion, credential/payment changes, or client/
production mutation.

Promotion requires:

- explicit operator feedback, selection, or approval;
- named screen/component/direction being promoted;
- note of what remains reference-only;
- a design-law update here when the promotion changes product UI/UX behavior.

The authority declares the current target file/page/node and allowed scope.
Proof screenshots, large prompt manifests, batch ledgers, placement history,
run gates, and validation receipts belong in external run/asset/control
records.

## Operational Receipt Pointers

Use these only to locate execution state. They are not app design law.

- Product law:
- Active run manifest:
- Active run registry:
- Active asset manifest:
- Current next-action surface:
- Other receipt indexes:

If an operational receipt conflicts with this file, update this authority only
when the conflict is a product UI/UX decision. Otherwise update the relevant run,
asset, batch, or workspace-control record.

## Update Rule

Update this file when any of these change:

- user journey, IA, route/page ownership, or tab behavior;
- screen-state logic, drawer/sheet/modal behavior, or proof placement;
- component grammar or component state rules;
- selected visual direction or durable style rules;
- product copy rules, safety posture, or free/paid UX timing;
- promotion of generated or implementation evidence into app design law.

Update this authority and its receipt pointers when the current generation-ready
prompt pack, active generation scope, low-fi/high-fi state, declared Figma
target, review decision, or next design action changes.

Update operational records instead when any of these change:

- large batch ledgers, renderer settings, generated outputs, or output paths;
- placement receipts, screenshots, or proof exports;
- approval receipts, run gates, validation logs, task claims, or external-send
  boundaries.

Update `PROJECT_CHARTER.md` instead when the change alters product intent,
users, scope, non-goals, constraints, success, or durable product policy. Use a
bounded retirement pointer for explicitly retired charter names; do not keep a
retired file as a second authority.
