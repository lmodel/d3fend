---
type: Service
id: https://w3id.org/lmodel/d3fend/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, by one pull request.
resource: .github/workflows/knowledge-sync.yaml
references:
  - https://w3id.org/lmodel/d3fend/knowledge/playbooks/knowledge-sources
sources:
  - id: knowledge-sync.yaml
    resource: .github/workflows/knowledge-sync.yaml
    title: the header comment
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Knowledge sync (knowledge-sync.yaml)

The workflow compares the sidecar's copies with the newest release of the skills repository, and opens one pull request when they differ.[^knowledge-sync.yaml]

[^knowledge-sync.yaml]: .github/workflows/knowledge-sync.yaml, the header comment
