# Improve Target Route Map

Use this map after identifying the target type and quality goal. When current
usage, target shape, user-flow, efficiency, or overbuild risk could change the
recommendation, read `improvement-passes.md` before ranking options.

| Target type | Default route | Notes |
|---|---|---|
| Skill, routing behavior, command mode | Skill Control Layer -> `yeem-skill`, `skill-audit`; `self-evolve` only as backend learning route | Use `self-evolve` only for repeated lessons, transcript-backed friction, or future behavior change. |
| Business plan, strategy, offer, startup idea | `audit-check`, `pipeline`, `research` when evidence would change the verdict | Diagnose before planning; research only for named evidence gaps. |
| UI/UX, Figma, visual surface, viewer | `design`, UI/UX design quality workflow, `ui-viewer` for rendered proof | Improvement is visual and task-fit first, not generic polish. |
| Workflow, workspace system, Control Room | `workspace-project-management`, `workspace-control-room`; `self-evolve` only for recurring lessons | Prefer absorption into existing routes over new controllers. |
| Marketing, content, creative, asset, campaign | `marketing-system`, `creative-workflow`, `design`, `boooom-market-analyser` when market reaction matters | Preserve audience, claim, channel, and approval gates. |
| Code/app implementation | Local code route, then `quality-check` after changes | Diagnose first; implementation only after explicit proceed. |
| Long-running improve-toward-goal loop | `adam-auto-loop` improve mode | Use only when governed repeated ticks are intended. |
| Completed implementation needing readiness check | `quality-check` | Post-build QA, not improvement diagnosis. |
| Recurring operating pattern or lesson | `self-evolve` | Use when the goal is future behavior change, not one artifact. |

## Usage evidence shortcut

- For skill/routing targets, inspect usage, trigger phrases, interaction
  patterns, wiring, registry/index visibility, near-miss collisions, and
  runtime caveats before recommending a patch.
- For surface/viewer targets, inspect the user-flow and first-screen question
  order before recommending visual or structural polish.
- For code/app targets, inspect callers, tests, logs, and local architecture
  before recommending implementation.
- For workflow/control targets, inspect source-of-truth files, handoff points,
  repeated manual steps, and approval/recovery gates before recommending a new
  artifact or view.

## Near-miss boundaries

- Use `quality-check` when the question is "is the completed thing done?"
- Use `audit-check` when the question is "is this direction right before
  building?"
- Use `adam-auto-loop` when Will wants repeated governed improvement over time.
- Use `self-evolve` behind `improve` when the source is repeated session
  friction, transcript evidence, or lessons that should change future behavior.
- Use `design` directly when the object is primarily visual quality.
- Use `user-skill` before durable new systems, major skills, or control layers.
