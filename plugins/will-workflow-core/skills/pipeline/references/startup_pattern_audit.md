# Startup Pattern Audit

Purpose: audit an idea, product, offer, or company direction through startup and
YC-derived pattern lenses before pipeline/build work.

Evidence home:
- `client_cases/marketing_ai_optimisation/projects/startup_intelligence/`
- Latest pilot run:
  `runs/20260622_052600_yc_startup_intelligence_pilot/`
- Pattern cards:
  `runs/20260622_052600_yc_startup_intelligence_pilot/patterns/PATTERN_INDEX.md`
- Skill packet source:
  `runs/20260622_052600_yc_startup_intelligence_pilot/skill_packets/startup_pattern_audit_skill_packet.md`

Inputs:
- idea or product thesis
- target customer / buyer / operator
- current offer or MVP shape
- existing proof or evidence
- constraints and non-goals

Lenses:
- category clarity
- customer pain intensity
- founder-market fit
- wedge strength
- MVP compression
- AI-native lifecycle stage
- distribution path
- venture-scale narrative
- trust/compliance burden
- pricing power
- cone of probability: base, upside, downside, cone width, and narrowing
  evidence
- pattern match and anti-patterns

Pattern families from the pilot:
- AI service replacement
- developer workflow compression
- vertical compliance automation
- data/API abstraction
- marketplace liquidity wedge
- regulated workflow software
- open-source to enterprise
- hardware/deeptech iteration

AI-native founder lifecycle check:

Use this when a founder/product idea is being built with coding agents,
workflow agents, or AI-native operating assumptions. Source basis:
`client_cases/marketing_ai_optimisation/projects/startup_intelligence/runs/20260704_054600_founder_playbook_ai_native_startup_ingestion/`.

| Stage | Core question | Proof expected | Failure mode |
|---|---|---|---|
| Idea | Is AI being used to validate the problem, or to skip validation by building fast? | Customer/problem evidence, disconfirming signals, competitor mapping | Impressive prototype for a weak problem |
| MVP | Is the MVP still a focused evidence system? | Scope, architecture context, PMF measurement, user feedback, security review | False product-market fit or uncontrolled feature sprawl |
| Launch | Has the founder moved from doing work to designing repeatable systems? | Workflow inventory, founder-bottleneck map, technical debt/security/compliance plan | Founder remains the hidden operating system |
| Scale | Is the company codifying domain knowledge and workflow value into defensibility? | Knowledge capture, integrations, switching-cost/user-value evidence, GTM infrastructure | Moat claim without workflow depth or user benefit |

Boundary: this checklist came from a vendor-authored Anthropic/Claude PDF. Use
it as a lifecycle audit lens, not as neutral market proof or a requirement to use
specific Claude products.

Output shape:

```text
Startup pattern audit
Intent read:
Category/customer/offer/wedge:
Pattern matches:
AI-native lifecycle check:
Cone of probability:
Missing proof:
Riskiest assumption:
Cheapest validation test:
Suggested MVP wedge:
Build gate:
Pipeline note:
```

Rules:
- Keep facts and inference separate.
- Do not claim a market is venture-scale without evidence.
- Do not recommend production build work until the riskiest assumption and
  cheapest test are named.
- If the audit exposes reusable friction, propose a pipeline improvement rather
  than creating a new skillhub immediately.
