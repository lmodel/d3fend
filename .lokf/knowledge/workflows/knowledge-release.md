---
type: Service
id: https://w3id.org/lmodel/d3fend/knowledge/workflows/knowledge-release
genre: reference
title: Knowledge release (knowledge-release.yaml)
description: The workflow that attaches the bundle, a Copilot skill and the schema's adapt copy to a GitHub release, each with a checksum. It runs when dispatched, and on each release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.
resource: .github/workflows/knowledge-release.yaml
references:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/adapt-copy
sources:
  - id: security.md
    resource: SECURITY.md
    title: What this repository releases
  - resource: .github/workflows/knowledge-release.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Knowledge release (knowledge-release.yaml)

The workflow attaches `schema-<tag>-d3fend.yaml`, the bundle zip and a Copilot skill zip, each with a `.sha256` and a build-provenance attestation, when the bundle or the schema has changed.[^security.md]

[^security.md]: SECURITY.md, What this repository releases
