---
type: Explanation
id: https://w3id.org/lmodel/d3fend/knowledge/explanations/terms-as-records
genre: explanation
title: Why a term is a record
description: "Why D3FEND's terms are records and not LinkML classes: D3FEND's own conventions pun its techniques as instances, its distribution states nearly every class restriction again as a direct triple between terms, and most of its 4,465 classes are not types anyone instantiates."
about:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/d3fend-linkml-schema
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/catalogue
sources:
  - id: about.md
    resource: docs/about.md
    title: Why a term is a record
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: test_every_named_restriction_lands_in_its_record
generated:
  by: process:ktl-librarian
  at: "2026-11-04T23:03:24Z"
status: draft
---

# Why a term is a record

D3FEND is an OWL ontology of 4,465 classes, and most name one thing: `d3f:FileAnalysis` one countermeasure, `d3f:T1003` one technique of ATT&CK. D3FEND's conventions pun a defensive technique as an instance, and its distribution states all but 23 of its restrictions on terms again as direct triples, such as `d3f:FileAnalysis d3f:analyzes d3f:File`.[^about.md]

So the schema models the catalogue that the graph already is. A kind of entry is a class, a property is a slot, and a term is a record.[^about.md]

The Turtle states 1,939 class restrictions that name a term, and each is a value of its record's slot.[^test_coverage.py]

[^about.md]: docs/about.md, Why a term is a record
[^test_coverage.py]: tests/test_coverage.py, test_every_named_restriction_lands_in_its_record
