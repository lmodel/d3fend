---
type: Service
id: https://w3id.org/lmodel/d3fend/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website in `website/`, a Hugo site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/d3fend`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.
resource: website
dependsOn:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/generated-artefacts
references:
  - https://w3id.org/lmodel/d3fend/knowledge/workflows/knowledge-website
sources:
  - id: website-readme.md
    resource: website/README.md
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:04:48Z"
status: draft
---

# Documentation site

`website/` holds a Hugo site with a page per concept, a health page, a graph, the schema's pages and the docs. Each schema page is also at `elements/<Name>/`, where the schema's w3id rules point.[^website-readme.md]

`website/site.toml` sends two old addresses on: `about` to the page built from `docs/about.md`, and each address under `schema/` to the schema's page of the same name.[^site.toml]

[^website-readme.md]: website/README.md
[^site.toml]: website/site.toml, the site's address, title and redirects
