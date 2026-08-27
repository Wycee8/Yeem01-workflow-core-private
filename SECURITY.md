# Security Policy

## Public Access

This repository is publicly readable. There is no subscriber password, JSON
key or private download link. Anyone can retain a public clone; access cannot
be revoked from copies already downloaded.

## Trusted Installation

- Install only from `Wycee8/Yeem01-workflow-core-private`.
- Pin to an immutable release tag such as `v0.7.0`; do not install a
  production workflow from mutable `main`.
- Review release notes and checksums before rollout.
- Protect maintainer accounts with strong GitHub authentication and least
  privilege outside this repository.

## Data And Secret Boundary

The pack must contain no API keys, tokens, private keys, connector credentials,
client data, raw sessions, task history, sensitive personal data or employee
telemetry. Never place a secret in a prompt, feedback note, issue, skill file,
manifest or example.

## Reporting A Vulnerability

Do not open a public issue containing exploit details, credentials, client data
or personal information. Use GitHub private vulnerability reporting when it is
enabled for the repository; otherwise contact the maintainer through a private
BM/YEEM channel. Include only the minimum reproduction, affected version and
impact, with sensitive values removed.

## Endpoint Limits

Removing a checkout or the adapter-managed installation is an endpoint action.
The repository cannot remotely erase a clone, provider cache or copied skill.
