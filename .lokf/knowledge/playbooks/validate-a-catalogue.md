---
type: Playbook
id: https://w3id.org/lmodel/d3fend/knowledge/playbooks/validate-a-catalogue
genre: how-to
title: Validate a catalogue
description: "How to validate a catalogue: run `linkml-validate` with `D3fendCatalog` as the target class, and `tests/d3fend_rules.py` for what JSON Schema cannot state. `project/jsonschema/d3fend.schema.json` serves anyone without LinkML."
references:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/catalogue
sources:
  - id: index.md
    resource: docs/index.md
    title: Validating a catalogue
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Validate a catalogue

1. Run `uv run linkml-validate -s src/d3fend/schema/d3fend.yaml -C D3fendCatalog src/d3fend/data/d3fend-1.6.0.yaml`.[^index.md]
2. For every rule, also run `rule_errors` from `tests/d3fend_rules.py`, which checks that a relation names a record of the right kind and that no two records share an IRI.[^index.md]

`project/jsonschema/d3fend.schema.json` is the same schema for anyone without LinkML.[^index.md]

[^index.md]: docs/index.md, Validating a catalogue
