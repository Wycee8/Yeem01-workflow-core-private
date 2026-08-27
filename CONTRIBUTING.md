# Contributing Improvements

Yeem01 Workflow Core grows from explicit, redacted evidence rather than passive
session collection.

## Subscriber Feedback

1. Copy `IMPROVEMENT_NOTE_TEMPLATE.md`.
2. Record the pack version, provider/scope, command, intended outcome, friction,
   recurrence and observable effect.
3. Remove client, personal, credential and employee-sensitive information.
4. Send the note through a private BM/YEEM channel designated by the
   maintainer. Do not place sensitive feedback in a public issue.

Do not send raw transcripts, workspace archives, credentials or employee
performance judgments.

## Maintainer Flow

```text
redacted note
-> reproduce and confirm ownership
-> choose the smallest shared rule
-> update canonical Yeem01 source
-> add a regression fixture
-> bump semantic version
-> build deterministic public projection
-> QA source, candidate and clean extraction
-> publish immutable tag
-> run clean-device canary
-> keep, iterate or roll back
```

Generated files, installed copies and old releases are not editable authority.
Do not accept changes that add credentials, client data, raw session collection,
employee scoring or project-specific permissions to the pack.
