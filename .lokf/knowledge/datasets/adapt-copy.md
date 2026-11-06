---
type: Dataset
id: https://w3id.org/lmodel/d3fend/knowledge/datasets/adapt-copy
genre: reference
title: The schema's adapt copy
description: "`.lokf/schema/d3fend.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: rooted on `D3fendEntry` and `D3fendCatalog`, with `id`, `type` and `rdf_type` dropped for LOKF's, and six keys renamed with a `d3fend_` prefix."
resource: .lokf/schema/d3fend.yaml
derivedFrom:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/d3fend-linkml-schema
about:
  - https://w3id.org/lmodel/d3fend/knowledge/glossary/adapt-copy
sources:
  - id: project.justfile
    resource: project.justfile
    title: the comment above the recipes
  - id: readme.md
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: DROPPED and RENAMED
  - resource: .lokf/schema/d3fend.yaml
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the schema setting
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:18:57Z"
status: draft
---

# The schema's adapt copy

`just lokf-adapt` writes `.lokf/schema/d3fend.yaml` from `src/d3fend/schema/d3fend.yaml`, and `just lokf-adapt-check` fails when it is stale. CI runs the check.[^project.justfile]

A concept names one of the 22 kinds as its `type`, and names a D3FEND term in a relation by its CURIE.[^readme.md]

The copy renames `created`, `definition`, `description`, `name`, `title` and `version`, each keeping its IRI, because LOKF has slots of those names. `rdfs:isDefinedBy` keeps its own key, because LOKF's `definedBy` names a concept and D3FEND's values are text.[^test_schema_rules.py]

A release attaches the copy as `schema-<tag>-d3fend.yaml`.[^readme.md]

[^project.justfile]: project.justfile, the comment above the recipes
[^readme.md]: README.md, Knowledge Trust Ladder (KTL)
[^test_schema_rules.py]: tests/test_schema_rules.py, DROPPED and RENAMED
