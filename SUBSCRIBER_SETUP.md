# Subscribe A Will Device

This guide is for a device authenticated to the private owner repository. The
repository must remain private and must not have collaborators unless Will
later makes a separate audience decision.

## First-time access

After the private remote exists, add its Git URL as the marketplace source:

```sh
codex plugin marketplace add <PRIVATE_GIT_REPOSITORY> --ref main
codex plugin marketplace list
codex plugin add will-workflow-core@will-private --json
codex plugin list --json
```

Start a fresh task and enter:

```text
-onboarding
```

Then run the read-only canary in the current handoff packet before relying on
the plugin for real work.

## Refresh

```sh
codex plugin marketplace upgrade will-private --json
codex plugin list --marketplace will-private --available --json
codex plugin add will-workflow-core@will-private --json
```

Start a fresh task after reinstalling. Marketplace refresh does not inherit
credentials, connectors, project authority, or another device's settings.

## Rollback

If discovery or canary behavior fails, stop using the candidate and restore the
previous verified version from the Yeem01 release handoff. Do not patch the
installed copy.

## Access boundary

- Repository visibility: private.
- Initial audience: repository owner only.
- Collaborators and associate devices: none.
- Credentials and connectors: configured separately per device.
- Feedback: use the redacted improvement-note contract; never submit raw
  transcripts or client/personal data.
