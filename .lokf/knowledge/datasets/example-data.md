---
type: Dataset
id: https://w3id.org/lmodel/d3fend/knowledge/datasets/example-data
genre: reference
title: Example data
description: "The examples `tests/test_data.py` checks: a valid example of each class, most of them real records of D3FEND 1.6.0, a counter-example for each constraint, and a counter-example for each rule on a whole catalogue."
resource: tests/data
references:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/d3fend-linkml-schema
sources:
  - id: test_data.py
    resource: tests/test_data.py
  - id: data-readme.md
    resource: tests/data/README.md
  - id: d3fend_rules.py
    resource: tests/d3fend_rules.py
  - resource: tests/data
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Example data

`tests/data/valid/` holds an example of each class, and a test fails when a concrete class has none.[^test_data.py] `tests/data/invalid/` holds a counter-example for each constraint, whose first line names the one place it fails.[^data-readme.md]

`tests/data/problem/invalid/` holds what JSON Schema cannot state: a relation that names no record, two records with one IRI, and a target of the wrong kind. `tests/d3fend_rules.py` checks those.[^d3fend_rules.py]

[^test_data.py]: tests/test_data.py
[^data-readme.md]: tests/data/README.md
[^d3fend_rules.py]: tests/d3fend_rules.py
