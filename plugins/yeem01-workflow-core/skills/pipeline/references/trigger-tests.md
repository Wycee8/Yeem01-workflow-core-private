# Pipeline Trigger Tests

Use these cases when updating `pipeline` routing, reusable workflow modes, or
Double Diamond shorthand.

| Operator phrase | Expected behavior |
|---|---|
| `-plan -dd this opportunity` | Use `pipeline` Double Diamond and artifact-lane plan output. |
| `-dd` with Discover/Define/Develop/Deliver context | Treat as Double Diamond shorthand. |
| `DD this market` with diligence context | Clarify whether `DD` means due diligence or Double Diamond. |
| `audit this startup idea` | Use `startup-pattern-audit`; do not start a product build. |
| `turn this into an MVP pipeline` | Use `product` mode with riskiest assumption and validation gate. |
| `build the app now` before validation gate | Stop at product slice approval; preserve hard gates. |
| `make a marketing campaign plan` | Route through `marketing-system` / `creative-workflow` unless a reusable marketing pipeline is explicitly requested. |
| `create a new workflow system` | Apply `user-skill` / PM necessity checks before creating durable structure. |
| `proceed all phases` on a selected pipeline plan | Execute safe local plan phases only until blocked or gated. |
| `-proceed all` on a visible selected pipeline plan | Treat as `proceed all phases`; ask if the selected plan is not visible. |
| `auto proceed all` on a pipeline goal without loop contract | Ask for scope or route to `adam-auto-loop` preflight; do not infer a queue by recency. |
