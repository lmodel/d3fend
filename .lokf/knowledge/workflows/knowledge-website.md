---
type: Service
id: https://w3id.org/lmodel/d3fend/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: The workflow that builds `website/` on each pull request that touches its inputs, and deploys the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
resource: .github/workflows/knowledge-website.yaml
references:
  - https://w3id.org/lmodel/d3fend/knowledge/services/documentation-site
sources:
  - id: security.md
    resource: SECURITY.md
    title: What executes here
  - resource: .github/workflows/knowledge-website.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

The workflow builds the site without a write token, and only its deploy job holds `pages: write` and `id-token: write`.[^security.md]

[^security.md]: SECURITY.md, What executes here
