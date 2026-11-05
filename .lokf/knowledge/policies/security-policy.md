---
type: Policy
id: https://w3id.org/lmodel/d3fend/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in D3FEND itself belongs with the D3FEND project.
resource: SECURITY.md
references:
  - https://w3id.org/lmodel/d3fend/knowledge/workflows/upstream-watch
sources:
  - id: security.md
    resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Security policy

Report a vulnerability through GitHub's private vulnerability reporting. Only the latest release receives fixes.[^security.md]

The release carries the adapt copy, the bundle as a zip and a Copilot skill zip, each with a checksum and a build-provenance attestation.[^security.md]

A catalogue entry holds Markdown, command lines and attack descriptions as text, and this repository treats it all as data. Tests validate entries, and nothing executes or renders them.[^security.md]

The watch reads MITRE's public files on `d3fend.mitre.org` and sends no token.[^security.md]

[^security.md]: SECURITY.md
