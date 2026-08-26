# Yeem01 Workflow Core Private Channel

This repository is the owner-only subscription surface for
`yeem01-workflow-core`. It exposes the current stable portable plugin without
publishing or cloning the Yeem01 workspace.

## Current channel

- Marketplace: `yeem01-private`
- Plugin: `yeem01-workflow-core`
- Stable version: `0.5.0`
- Audience: Will's authenticated devices only
- Private remote: `git@github.com:Wycee8/Yeem01-workflow-core-private.git`
- Source authority: Yeem01 canonical skills and release builder

Only the live marketplace projection is tracked here:

```text
.agents/plugins/marketplace.json
plugins/yeem01-workflow-core/
CHANNEL.json
SUBSCRIBER_SETUP.md
```

Local immutable archives under `releases/` are intentionally excluded. Git
history and version tags preserve the published channel history, while the
Yeem01 release project preserves full QA evidence and rollback packages.

`0.5.0` replaces the former `will-workflow-core` install identity with
`yeem01-workflow-core`. A device should keep only the new identity enabled
after completing the receiver canary.

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
