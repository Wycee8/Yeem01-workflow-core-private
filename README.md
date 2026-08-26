# Will Core Private Channel

This repository is the owner-only subscription surface for
`will-workflow-core`. It exposes the current stable portable plugin without
publishing or cloning the Yeem01 workspace.

## Current channel

- Marketplace: `will-private`
- Plugin: `will-workflow-core`
- Stable version: `0.4.1`
- Audience: Will's authenticated devices only
- Source authority: Yeem01 canonical skills and release builder

Only the live marketplace projection is tracked here:

```text
.agents/plugins/marketplace.json
plugins/will-workflow-core/
CHANNEL.json
SUBSCRIBER_SETUP.md
```

Local immutable archives under `releases/` are intentionally excluded. Git
history and version tags preserve the published channel history, while the
Yeem01 release project preserves full QA evidence and rollback packages.

## Maintenance law

1. Change the owning canonical skill in Yeem01.
2. Build and QA a new immutable release.
3. Refresh this generated marketplace projection.
4. Verify `CHANNEL.json`, plugin structure, privacy and clean installation.
5. Commit and tag the stable version.
6. Push only to the private owner-controlled remote.
7. Refresh and explicitly update subscribed devices.

Do not edit packaged skills here. Do not add credentials, client data,
workspace state, task history, raw feedback, or employee telemetry.
