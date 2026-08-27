# Yeem01 Workflow Core Private Channel

`yeem01-workflow-core` is Will's private, versioned workflow pack for using the
same core audit, discussion, planning, QA, evaluation, improvement, research,
pipeline and project-context methods on another device without cloning the
Yeem01 workspace.

- Current stable version: `0.6.2`
- Rollback: `0.5.0`
- Marketplace: `yeem01-private`

## Fast Start

Codex on an authorized device:

```sh
codex plugin marketplace add git@github.com:Wycee8/Yeem01-workflow-core-private.git --ref main --json
codex plugin add yeem01-workflow-core@yeem01-private --json
```

Open a fresh task and enter:

```text
-onboarding
```

Cursor on an authorized device:

```sh
git clone git@github.com:Wycee8/Yeem01-workflow-core-private.git
cd Yeem01-workflow-core-private
python3 scripts/install_agent_skills.py --provider cursor --scope user --action install
```

Start a new Cursor chat after installation. For Cursor cloud or remote workers,
use project scope or a prepared worker image; a local user-level install is not
automatically copied to a remote worker.

## What Is Included

The plugin contains `10` actual skill directories:

- `yeem01-workflow-core` — command front door, onboarding, composition and host boundaries
- `audit-check` — direction audit and impact evaluation
- `workspace-implementation-planning` — current-slice, milestone and full planning
- `artifact-lane-output-defaults` — operator artifact and summary contracts
- `quality-check` — post-build quality assurance
- `improve` — evidence-backed improvement proposals
- `pipeline` — portable reusable workflow and Double Diamond routing
- `research` — evidence-backed research workflows
- `project-charter-docs` — durable project charter and authority context
- `user-skill` — user-first durable skill/change gate

`-discuss`, `-explore`, `-suggest`, `-ask`, and bounded `proceed` are front-door
behaviours, not extra skill directories.

## Read Next

- `USE_MANUAL.md` — skill list, command map, examples, workflow and boundaries.
- `SUBSCRIBER_SETUP.md` — authentication, install, update, rollback and
  troubleshooting.
- `IMPROVEMENT_NOTE_TEMPLATE.md` — minimal redacted feedback for a maintainer.

## Security In One Minute

- The repository is private; GitHub identity controls who can fetch it.
- There is no shared JSON key. `.agents/plugins/marketplace.json` is public-style
  package metadata inside a private repository, not a credential.
- Each person or device uses its own GitHub identity or device key.
- The pack contains no API keys, private keys, tokens, connectors, client data,
  task history, raw transcripts or employee telemetry.
- Removing repository access prevents future fetches but cannot erase a clone or
  installed copy already retained on a device; endpoint offboarding is separate.

## Maintenance Law

Edit the canonical Yeem01 skill, add a regression case, bump the version, build
and QA a new immutable release, then publish the generated channel. Never patch
an installed copy or this generated projection directly.

This version is published through Will's private, identity-controlled GitHub
channel. Subscriber invitations and credential changes remain separate owner
actions, and every new version still requires a fresh-session receiver canary.
