---
type: Dataset
id: https://w3id.org/lmodel/d3fend/knowledge/datasets/d3fend-linkml-schema
genre: reference
title: d3fend LinkML schema
description: "The LinkML model of MITRE D3FEND 1.6.0, `src/d3fend/schema/d3fend.yaml` (schema id `https://w3id.org/lmodel/d3fend`): an umbrella over a core and an entries module, whose tree root `D3fendCatalog` holds every term of the edition as a record."
resource: src/d3fend/schema/d3fend.yaml
sources:
  - id: d3fend.yaml
    resource: src/d3fend/schema/d3fend.yaml
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_every_module_names_the_pinned_edition
  - id: about.md
    resource: docs/about.md
    title: Why a term is a record
  - id: pyproject.toml
    resource: pyproject.toml
    title: the project's name
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# d3fend LinkML schema

The umbrella imports the LinkML types, `d3fend_core` and `d3fend_entries`, and holds only the tree root.[^d3fend.yaml] `D3fendCatalog` holds the ontology's header, its disjoint groups and its entries.[^d3fend.yaml]

The header carries the edition in `version`, the Turtle file's address in `source`, and the tag and commit in annotations. `tests/test_upstream.py` holds them equal to the watch's pins.[^test_upstream.py]

Each kind of entry is a class, each property a slot under its own IRI, and each term a record.[^about.md]

The Python project is `d3fend-linkml`, and PyPI publishing is off.[^pyproject.toml]

[^d3fend.yaml]: src/d3fend/schema/d3fend.yaml
[^test_upstream.py]: tests/test_upstream.py, test_every_module_names_the_pinned_edition
[^about.md]: docs/about.md, Why a term is a record
[^pyproject.toml]: pyproject.toml, the project's name
