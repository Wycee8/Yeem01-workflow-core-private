# Yeem01-Backed Maintenance

This pack has one editable source and many immutable generated releases.

## Source And Output

Canonical command-front-door source:

```text
starter_workspace/plugins/will-workflow-core
```

Release control and builder:

```text
starter_workspace/client_cases/marketing_ai_optimisation/projects/
workspace_optimisation/will_private_skill_distribution
```

Generated local marketplace and releases:

```text
private_distribution/will-private-marketplace
```

The allowlisted portable owners remain canonical under
`starter_workspace/skills/<skill-name>`. Edit only those Yeem01 sources. Never
patch an installed device copy, generated projection, or old release. The
builder materializes the front door plus complete allowlisted skill trees,
normalizes workspace-only frontmatter keys in the generated copies for portable
Codex compatibility, records source and packaged inventories/hashes, and emits
the marketplace packet, provenance, checksums, handoff guide, and deterministic
archive. Skill instructions, references, scripts and templates are otherwise
copied intact.

## Normal Update Flow

1. collect a minimal redacted friction note;
2. confirm the issue is recurring and belongs in the shared core;
3. update the smallest owning Yeem01 skill rule;
4. add or revise a regression fixture;
5. bump semantic versioning in `.codex-plugin/plugin.json`;
6. run the contract, every bundled skill, and plugin validators;
7. generate a new immutable release with the project builder;
8. QA the cleanly extracted package; and
9. distribute through the chosen private channel and run a fresh-task canary.

Use a patch version for corrections that preserve command behavior, a minor
version for new commands or material workflow behavior, and a major version
for a breaking invocation or packaging change.

## Simple Feedback Contract

Feedback should contain only:

```text
role or audience class
command and intended outcome
friction observed
recurrence count
observable effect
confirmation that client, personal and credential data was removed
suggested rule, if any
```

Do not centralize raw transcripts, credentials, client data, sensitive personal
information, or employee scoring. `-improve` produces a proposal; a maintainer
owns the Yeem01 source change.

## Future Central Distribution

The generated marketplace directory can later become a private Git-backed
marketplace. A compatible device would add that private marketplace once and
install or update the named plugin version. This improves access and updates
without cloning the full Yeem01 workspace.

The initial AT-Will handoff remains an offline, checksum-verified archive. A
remote, push, collaborator setup, connector, or device install is outside this
core and must be handled by the surrounding workspace process.

## Release Rule

An immutable release is ready for handoff only when:

- the source version and release version match;
- every declared Yeem01 source input exists and has a recorded SHA-256;
- contract, skill, plugin, privacy, and inventory checks pass;
- candidate, marketplace projection, and clean extraction match the generated
  allowlisted bundle;
- candidate and archive checksums pass;
- a previous accepted release remains available for rollback; and
- transfer, install, runtime canary, external rollout, credentials, and push
  remain unperformed unless separately in scope.
