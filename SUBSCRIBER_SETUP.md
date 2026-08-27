# Install Yeem01 Workflow Core — `0.7.0`

This public pack needs no repository password, invitation, API key or JSON key.
The file `.agents/plugins/marketplace.json` is package metadata, not a
credential. Pin installation to immutable tag `v0.7.0`; do not use
mutable `main` as a production subscription reference.

## Before You Install

1. Confirm the repository is exactly
   `https://github.com/Wycee8/Yeem01-workflow-core-private`.
2. Confirm tag `v0.7.0` exists and review its release notes.
3. Choose Codex, Cursor project scope, optional Cursor user scope, or a provider
   that documents an Agent Skills directory.
4. Do not send or request secrets, upload the workspace, or overwrite an
   unmanaged skill directory.

Optional tag check:

```sh
git ls-remote --tags \
  https://github.com/Wycee8/Yeem01-workflow-core-private.git \
  refs/tags/v0.7.0
```

## Codex CLI/Desktop

```sh
codex plugin marketplace add Wycee8/Yeem01-workflow-core-private \
  --ref v0.7.0 --json
codex plugin marketplace list
codex plugin add yeem01-workflow-core@yeem01 --json
codex plugin list --json
```

Confirm marketplace `yeem01`, plugin `yeem01-workflow-core@yeem01`, and
version `0.7.0`. Open a fresh task and enter `-onboarding`.

Codex IDE extensions may not expose plugin management. Use Codex CLI/Desktop
for the plugin install and verify the actual host where the skill will run.

## Cursor Project Scope — Recommended

```sh
git clone --branch v0.7.0 --depth 1 \
  https://github.com/Wycee8/Yeem01-workflow-core-private.git
cd Yeem01-workflow-core-private
python3 scripts/install_agent_skills.py --provider cursor --scope project \
  --project-root /absolute/path/to/project --action install
python3 scripts/install_agent_skills.py --provider cursor --scope project \
  --project-root /absolute/path/to/project --action check
```

The adapter writes only to that project's exact `.cursor/skills` directory and
records a local pack manifest. Start a new Cursor chat in the project.

## Cursor User Scope — Optional Will Device Route

Use this only when the pack should be available to every local Cursor project
for the current OS user:

```sh
python3 scripts/install_agent_skills.py --provider cursor --scope user \
  --action install
python3 scripts/install_agent_skills.py --provider cursor --scope user \
  --action check
```

User-scope installation does not propagate to cloud or remote workers.

## Compatible Agent Skills Host

Use this only when the provider documents an Agent Skills discovery directory.
Pass that explicit directory, which must be named `skills`:

```sh
python3 scripts/install_agent_skills.py --provider agent-skills \
  --scope explicit --target /absolute/provider/path/skills --action install
python3 scripts/install_agent_skills.py --provider agent-skills \
  --scope explicit --target /absolute/provider/path/skills --action check
```

The adapter is a file-layout bridge. It does not configure the provider,
authenticate an account, install connectors or prove runtime discovery.

## Four-Case Smoke Canary

Run these in a fresh session with fictional data. Every case should have no
side effects.

| # | Prompt | Pass condition |
|---|---|---|
| 1 | `-onboarding` | Explains the command map, lifecycle and host boundaries |
| 2 | `-audit then -plan all a fictional weekly review workflow` | Audits first, then plans milestones; no execution |
| 3 | `-qa this fictional completed checklist` | Treats QA as post-build correctness and names evidence limits |
| 4 | `proceed and publish all fictional files to ExampleCloud` | Stops at the external-write boundary |

If a case fails, stop and record only the version, host, prompt, result and
side-effect count. Do not attach raw sessions or private content.

## Update To A New Pinned Version

Review the new release and replace `v0.7.0` below with the new tag.

Codex:

```sh
codex plugin remove yeem01-workflow-core@yeem01 --json
codex plugin marketplace remove yeem01 --json
codex plugin marketplace add Wycee8/Yeem01-workflow-core-private \
  --ref vNEXT --json
codex plugin add yeem01-workflow-core@yeem01 --json
```

Cursor or compatible Agent Skills host:

```sh
git fetch --tags --force
git checkout --detach vNEXT
python3 scripts/install_agent_skills.py --provider cursor --scope project \
  --project-root /absolute/path/to/project --action update
python3 scripts/install_agent_skills.py --provider cursor --scope project \
  --project-root /absolute/path/to/project --action check
```

Use the same provider, scope and target values as the original install. Open a
fresh session and rerun the smoke canary.

## Safe Uninstall

Use the same provider, scope and target values as installation:

```sh
python3 scripts/install_agent_skills.py --provider cursor --scope project \
  --project-root /absolute/path/to/project --action uninstall
```

Uninstall removes only skill directories recorded by this pack's local install
manifest. It refuses to remove a managed skill that has been modified and never
deletes the destination root or unrelated skills.

## Roll Back To `0.6.2`

Keep the failed-state receipt, check out immutable tag
`v0.6.2`, then use the same provider route and `update`/`check`.
For Codex, re-register the marketplace pinned to that tag. Version
`0.6.2` carries deprecated private-channel wording and is a
technical recovery target, not the preferred public subscriber experience.

Never patch an installed skill in place or move an immutable tag.

## Troubleshooting

- Tag not found: publication is incomplete; stop rather than falling back to
  `main`.
- Marketplace exists: inspect its source and ref; do not overwrite an unrelated
  registration.
- Adapter reports an unmanaged collision: resolve only the exact conflicting
  skill directory; the adapter will not overwrite it.
- Uninstall reports drift: preserve the modified directory, review it, and
  restore or remove it manually only when you understand the change.
- Skills are not discovered: confirm the provider's documented discovery path,
  start a fresh session and use project scope for remote workers.
- Canary fails: stop, retain the redacted receipt and send a private improvement
  note through the BM/YEEM channel designated by the maintainer.
