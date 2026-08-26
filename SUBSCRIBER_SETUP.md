# Subscribe A Will Device

This guide is for a device authenticated to the private owner repository. The
repository must remain private and must not have collaborators unless Will
later makes a separate audience decision.

## First-time access

Authenticate the device to Will's private GitHub repository, then run:

```sh
codex plugin marketplace add git@github.com:Wycee8/Yeem01-workflow-core-private.git --ref main --json
codex plugin marketplace list
codex plugin add yeem01-workflow-core@yeem01-private --json
codex plugin list --json
```

Confirm marketplace `yeem01-private`, plugin `yeem01-workflow-core`, and
version `0.5.0` before opening a new task.

Start a fresh task and enter:

```text
-onboarding
```

Then run the read-only canary in the current handoff packet before relying on
the plugin for real work.

## Rename Migration

If `codex plugin list --json` still shows the former
`will-workflow-core@will-private` installation, remove it only after the new
plugin passes the canary:

```sh
codex plugin remove will-workflow-core@will-private --json
```

The old identifier is not updated in place.

## Refresh

```sh
codex plugin marketplace upgrade yeem01-private --json
codex plugin list --marketplace yeem01-private --available --json
codex plugin add yeem01-workflow-core@yeem01-private --json
```

Start a fresh task after reinstalling. Marketplace refresh does not inherit
credentials, connectors, project authority, or another device's settings.

## Rollback

If discovery or canary behavior fails, remove the new plugin and restore the
previous verified `will-workflow-core` `0.4.1` package from the Yeem01 release
handoff. Do not patch an installed copy.

## Access boundary

- Repository visibility: private.
- Initial audience: repository owner only.
- Collaborators and associate devices: none.
- Credentials and connectors: configured separately per device.
- Feedback: use the redacted improvement-note contract; never submit raw
  transcripts or client/personal data.
