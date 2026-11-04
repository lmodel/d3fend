---
type: Playbook
id: https://w3id.org/lmodel/d3fend/knowledge/playbooks/release
genre: how-to
title: Release
description: "How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off."
references:
  - https://w3id.org/lmodel/d3fend/knowledge/workflows/semantic-release
  - https://w3id.org/lmodel/d3fend/knowledge/workflows/knowledge-release
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Releasing (maintainers)
  - id: security.md
    resource: SECURITY.md
    title: What this repository releases
  - resource: .releaserc.json
  - resource: .github/release
  - resource: .github/scripts
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Release

1. Write `## [Unreleased]` in `CHANGELOG.md` as you go. The release job refuses an empty one.[^contributing.md]
2. Type each commit for what the change is. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release.[^contributing.md]
3. Before the first releasing merge, push the `v0.0.0` baseline tag on `main`, which then releases 0.1.0.[^contributing.md]
4. On merge, `semantic-release.yml` retitles the section, commits `CHANGELOG.md`, tags and publishes the GitHub Release.[^contributing.md]

Nothing is published to PyPI.[^security.md]

[^contributing.md]: CONTRIBUTING.md, Releasing (maintainers)
[^security.md]: SECURITY.md, What this repository releases
