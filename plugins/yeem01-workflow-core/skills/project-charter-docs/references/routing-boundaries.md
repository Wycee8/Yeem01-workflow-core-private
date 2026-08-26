# Routing Boundaries

## Use project-charter-docs when

The real need is durable context:
- why the project exists
- what it is trying to become
- current build slice
- durable decisions
- reusable validation logic
- audit/read-order clarity

## Do not use when

- The user only needs a one-turn brainstorm.
- The user asks for canonical backlog mutation.
- The user asks for stage-specific run execution.
- The project already has fresh charter docs and no capture/refresh is needed.

## Client and portfolio requests

- “Update this project's PAP” -> resolve exactly one project and use
  `project-charter-docs`.
- “Set up authority for this business and all its projects” -> inspect
  `CLIENT_BRIEF.md` plus `PROJECT_REGISTRY.json`; do not create a business PAP
  or bind the request to the most recent project.
- “Apply this client-wide decision” -> capture the client decision once, list
  affected projects, then update only the project PAP sources with material
  local impact.
- A covered workstream may rely on its parent project's authority and an
  explicit read-order pointer; it does not automatically need another charter.
- A temporary or completed campaign should be closed or re-briefed before a
  charter is created merely for structural consistency.
- Devices, Drive roots, repositories, tools, and execution sessions are not
  projects unless they have an independently approved durable outcome, owner,
  lifecycle, and evidence boundary.

## Related skills

- `workspace-implementation-planning`: execution checklist/build packet/backlog planning.
- `workspace-project-management`: ownership, visibility, approvals, handoff, backlog clarity.
- `adam-mode`: client/portfolio coordination and routing to affected project owners.
- `create-guide`: creation readiness and lane selection.
- `creative-workflow`: creative/product specialist hub.
- `yeem-skill`: skill creation/modification governance.
