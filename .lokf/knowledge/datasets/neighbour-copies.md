---
type: Dataset
id: https://w3id.org/lmodel/d3fend/knowledge/datasets/neighbour-copies
genre: reference
title: Neighbours' adapt copies
description: The adapt copies of fourteen released lmodel repositories in `tests/neighbours/`, among them attack, cwe, capec and nist-sp-800-53, each pinned by its SHA-256, against which `tests/test_schema_rules.py` holds this schema's copy apart and `tests/test_mappings.py` holds the mappings.
resource: tests/neighbours
references:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/adapt-copy
sources:
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: NEIGHBOURS and SHARED_WITH_NEIGHBOURS
  - id: test_mappings.py
    resource: tests/test_mappings.py
    title: neighbour_iris
  - resource: tests/neighbours
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Neighbours' adapt copies

Each file is the schema asset of a lmodel release, pinned in `tests/test_schema_rules.py` by its checksum.[^test_schema_rules.py]

The same test fails on any shared class, enum or type, and on a shared key the test does not list. D3FEND's properties are ordinary words, so it lists a few for oscal, attack, stix, nist-nvd, uco, spdx and slsa.[^test_schema_rules.py]

`tests/test_mappings.py` reads these copies to hold the mappings to attack, stix, cwe, capec and nist-sp-800-53.[^test_mappings.py]

[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and SHARED_WITH_NEIGHBOURS
[^test_mappings.py]: tests/test_mappings.py, neighbour_iris
