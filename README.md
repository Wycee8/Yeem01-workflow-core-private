# Yeem01 Workflow Core

`yeem01-workflow-core` is YEEM's small, versioned workflow pack for using the
same core audit, discussion, planning, QA, evaluation, improvement, research,
pipeline and project-context methods on another device without cloning the full
Yeem01 workspace.

- Current release: `0.7.0`
- Previous technical rollback: `0.6.2`
- Marketplace: `yeem01` (display name `YEEM`)
- Public repository: `Wycee8/Yeem01-workflow-core-private`

The repository name retains a legacy `private` suffix, but repository
visibility controls access. When the repository is public, anyone can read and
clone it; there is no subscriber password or JSON key.

## Fast Start

These version-pinned commands work after tag `v0.7.0` is published.

Codex CLI/Desktop:

```sh
codex plugin marketplace add Wycee8/Yeem01-workflow-core-private --ref v0.7.0 --json
codex plugin add yeem01-workflow-core@yeem01 --json
```

Open a fresh task and enter:

```text
-onboarding
```

Cursor project scope (recommended for associates):

```sh
git clone --branch v0.7.0 --depth 1 \
  https://github.com/Wycee8/Yeem01-workflow-core-private.git
cd Yeem01-workflow-core-private
python3 scripts/install_agent_skills.py --provider cursor --scope project \
  --project-root /absolute/path/to/your/project --action install
python3 scripts/install_agent_skills.py --provider cursor --scope project \
  --project-root /absolute/path/to/your/project --action check
```

Start a new Cursor chat in that project and enter `-onboarding`. A local skill
install does not automatically propagate to Cursor cloud or another remote
worker; use project scope or a prepared worker image and verify a fresh session.

## Copyable New-Device Installation Prompt

```text
Install Yeem01 Workflow Core v0.7.0 from the public GitHub repository
Wycee8/Yeem01-workflow-core-private. Pin every fetch to tag v0.7.0. Use
the documented Codex plugin route, or for Cursor prefer project scope and run
the included install adapter followed by check. Do not request a password,
JSON key, credentials, Drive upload, or full Yeem01 workspace. Do not overwrite
unmanaged skills. After installation, open a fresh session, run -onboarding,
then run the four-case fictional smoke canary in SUBSCRIBER_SETUP.md. Report
commands, version, checks and side effects, and stop on any mismatch.
```

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

- `USE_MANUAL.md` — skill list, command map, examples and workflow boundaries.
- `SUBSCRIBER_SETUP.md` — install, update, uninstall, rollback and
  troubleshooting.
- `SECURITY.md` — public-access truth, trusted-release and disclosure rules.
- `CONTRIBUTING.md` — safe improvement feedback and maintainer release flow.
- `IMPROVEMENT_NOTE_TEMPLATE.md` — minimal redacted feedback form.

## Security In One Minute

- Public read access needs no password, token or shared JSON key.
- Install only from the named repository and an immutable `vX.Y.Z` tag.
- Maintainer GitHub security and release controls protect changes; they do not
  make public source private.
- The pack must contain no API keys, private keys, tokens, connectors, client
  data, raw sessions, task history or employee telemetry.
- A public clone cannot be revoked or remotely erased. Endpoint removal is a
  separate device-management responsibility.

## Maintenance Law

Edit the canonical Yeem01 skill, update the public-portability profile when
needed, add a regression case, bump the version, build and QA a new immutable
release, then publish the generated channel. Never patch an installed copy,
generated projection or old release directly.

Git commit, tag, push, publication and clean-device runtime proof are separate
owner actions from local package preparation.
