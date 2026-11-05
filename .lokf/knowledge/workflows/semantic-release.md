---
type: Service
id: https://w3id.org/lmodel/d3fend/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: The workflow that computes the next version from Conventional Commits on `main`, promotes the changelog, tags and publishes a GitHub Release, and dispatches the knowledge release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.
resource: .github/workflows/semantic-release.yml
references:
  - https://w3id.org/lmodel/d3fend/knowledge/playbooks/release
sources:
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
    title: the header comment
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Semantic release (semantic-release.yml)

The workflow computes the next version, promotes `CHANGELOG.md`'s `## [Unreleased]` section and publishes the release. The `v0.0.0` baseline tag keeps the first release at 0.1.0, and a breaking change bumps the minor version.[^semantic-release.yml]

[^semantic-release.yml]: .github/workflows/semantic-release.yml, the header comment
