# Trigger Tests

Use these fixtures to verify charter/PAP routing without creating or refreshing
project authority files.

| Case | Expected route |
| --- | --- |
| "Inspect whether this project's charter is current and complete." | `inspect`; return gaps and recommendation without writing. |
| "Capture this as the project charter." | `create` or `refresh`; default to one `PROJECT_CHARTER.md`. |
| "Refresh the current project PAP after this approved scope decision." | `refresh`; inspect affected project authorities and record PAP impact. |
| "Prepare a read-order package for an external project audit." | `audit-pack`; link source truth rather than copying authority. |
| "Create durable context so this plan survives session drift." | Use this skill; apply the one-file-first necessity gate. |
| "Set up one PAP for the whole client and all projects." | Refuse an umbrella PAP; use client authority plus affected project PAPs. |
| "Update the most recent project because I did not name one." | Resolve scope; do not silently bind a multi-project request. |
| "Add these tasks to the canonical backlog." | Route to `backlog-item-adder`; charter docs are not task state. |
| "Break this approved plan into executable implementation tasks." | Route to `workspace-implementation-planning`. |
| "Build the feature described by the existing charter." | Route to implementation/execution; charter creation is not build authority. |
| "Create a dashboard copy of the charter as the new source of truth." | Refuse source inversion; use `charter-session-viewer` as a projection only. |
| "Delete all old charter evidence while cleaning the docs." | Preserve/archive evidence by default; destructive deletion needs explicit approval. |
| `-pap design` | Inspect the current project's design-authority facet read-only; report sources, locks, gaps and conflicts. |
| Bound-project `-dap` | Normalize to `-pap design`; use the bounded DAP fast path, ignore `active/*` compatibility projections and unrelated workspace state, avoid recursive discovery/full long-file reads, keep cumulative initial project-authority output to 250 lines or fewer, project only the selected registry run fields, and do not create or require a DAP skill or file. |
| `-dap update the selected visual direction` | Treat as a material PAP/design-authority change; preview the owning-source delta and preserve approval gates before writing. |
| `-dap` when charter and UI/UX authority conflict | Fail closed, name both sources and remain read-only. |
| `-design make this better` | Route to Design after resolving DAP; PAP inspection does not own design action. |
