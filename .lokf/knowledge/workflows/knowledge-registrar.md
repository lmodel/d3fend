---
type: Service
id: https://w3id.org/lmodel/d3fend/knowledge/workflows/knowledge-registrar
genre: reference
title: Knowledge registrar (knowledge-registrar.yaml)
description: "The gate on the bundle: it validates the bundle on each pull request that touches it and weekly, and checks that each new `human:` event in a pull request is backed by an approval or a signature. It never judges whether content is true."
resource: .github/workflows/knowledge-registrar.yaml
references:
  - https://w3id.org/lmodel/d3fend/knowledge/playbooks/knowledge-sources
sources:
  - id: knowledge-registrar.yaml
    resource: .github/workflows/knowledge-registrar.yaml
    title: the header comment
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Knowledge registrar (knowledge-registrar.yaml)

The workflow keeps the bundle's records well-formed. It runs `lokf validate --check-refs` and the conventions script.[^knowledge-registrar.yaml]

[^knowledge-registrar.yaml]: .github/workflows/knowledge-registrar.yaml, the header comment
