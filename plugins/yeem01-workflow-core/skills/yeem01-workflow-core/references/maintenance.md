# Yeem01-Backed Maintenance

This pack has one editable source and many immutable generated releases.

## Source And Output

Canonical command-front-door source:

```text
starter_workspace/plugins/yeem01-workflow-core
```

Canonical portable owners live under
`starter_workspace/skills/<skill-name>`. Release control and the deterministic
builder live in the Yeem01 distribution project. The generated repository is a
projection, not a second editable authority.

Edit the smallest owning Yeem01 source. Never patch an installed device copy,
generated projection or old release. The builder materializes the front door
plus allowlisted skill trees, applies declared public-portability exclusions
and text replacements, records source and packaged inventories/hashes, and
emits subscriber docs, marketplace metadata, provenance, checksums and a
deterministic archive.

The public profile excludes executable local-session and fleet scanners. A
host may provide its own explicitly authorized analysis, but the shared pack
collects no sessions or employee telemetry.

## Normal Update Flow

1. receive a minimal redacted friction note through a private BM/YEEM channel;
2. confirm the issue is recurring and belongs in the shared core;
3. update the smallest owning Yeem01 skill rule;
4. add or revise a regression fixture;
5. bump semantic version in `.codex-plugin/plugin.json` and the source manifest;
6. run the contract, every bundled skill and plugin validators;
7. generate a new immutable release with the project builder;
8. verify subscriber docs, security/contribution surfaces and safe adapter;
9. QA source, candidate, clean extraction and provider-layout canaries;
10. publish one immutable `vX.Y.Z` tag; and
11. run a fresh-task canary on each materially new host cohort.

Use a patch version for corrections that preserve behaviour, a minor version
for new commands or material workflow behaviour, and a major version for a
breaking invocation or packaging change.

## Simple Feedback Contract

Feedback contains only:

```text
pack version and provider/scope
role or audience class
command and intended outcome
friction observed and recurrence count
observable effect
confirmation that client, personal, credential and employee-sensitive data was removed
suggested smallest rule, if any
```

Do not centralize raw transcripts, credentials, client data, sensitive personal
information or employee scoring. `-improve` produces a proposal; a maintainer
owns source changes and releases.

## Central Public Distribution

The generated projection is published to the public repository:

```text
Wycee8/Yeem01-workflow-core-private
```

The repository name has a legacy suffix; visibility is public. Public read
requires no individual GitHub authorization, password or shared JSON
credential. Codex adds marketplace `yeem01` pinned to an immutable release tag.
Cursor and documented Agent Skills hosts clone the same tag and use the
generated adapter; project scope is the associate default. The remote carries
only the generated channel, while the full Yeem01 workspace, release workbench,
credentials, client data and raw feedback remain excluded.

Maintainer account security, branch/tag protection and publication are
host-owned controls. A public clone cannot be revoked or remotely erased. If
future distribution must be identity-restricted, use a private repository or
fork outside this core.

## Release Rule

An immutable release is ready for handoff only when:

- source manifest, plugin and release versions match;
- every declared source input exists and has a recorded SHA-256;
- public-portability exclusions/replacements are recorded and scanner
  executables are absent;
- contract, skill, plugin, privacy, inventory and documentation checks pass;
- all ten skills and public/no-password/version-pinning boundaries are explained;
- Codex marketplace wiring and isolated Cursor/generic Agent Skills
  install/check/update/uninstall canaries pass;
- candidate, projection and clean extraction match;
- candidate and archive checksums pass and the repeat archive is identical;
- a previous release remains available for technical rollback; and
- commit, tag, push, publication, receiver install and runtime canary remain
  unperformed unless separately recorded.
