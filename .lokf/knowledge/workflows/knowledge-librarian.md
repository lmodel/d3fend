---
type: Service
id: https://w3id.org/lmodel/d3fend/knowledge/workflows/knowledge-librarian
genre: reference
title: Knowledge librarian (knowledge-librarian.yaml)
description: The sidecar's scheduled agent run that keeps the bundle in step with the repository and opens a pull request for a person to review. It is inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
resource: .github/workflows/knowledge-librarian.yaml
references:
  - https://w3id.org/lmodel/d3fend/knowledge/playbooks/knowledge-sources
sources:
  - id: knowledge-librarian.yaml
    resource: .github/workflows/knowledge-librarian.yaml
    title: the header comment and TRUST_LADDER_SKILLS_REF
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Knowledge librarian (knowledge-librarian.yaml)

The agent's job holds no write token. A separate `publish` job confines the patch to the bundle and opens the pull request. The workflow pins the skills at KTL v0.61.0.[^knowledge-librarian.yaml]

[^knowledge-librarian.yaml]: .github/workflows/knowledge-librarian.yaml, the header comment and TRUST_LADDER_SKILLS_REF
