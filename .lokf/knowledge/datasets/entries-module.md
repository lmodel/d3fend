---
type: Dataset
id: https://w3id.org/lmodel/d3fend/knowledge/datasets/entries-module
genre: reference
title: Entries module
description: "`src/d3fend/schema/d3fend_entries.yaml`, which `scripts/d3fend_to_linkml.py` writes from the Turtle: the abstract `D3fendEntry`, its 22 kinds, and one slot for each of the ontology's 292 properties a record can hold, under the property's own IRI."
resource: src/d3fend/schema/d3fend_entries.yaml
isPartOf:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/d3fend-linkml-schema
derivedFrom:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/upstream-copy
sources:
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_the_module_is_the_converters_output
  - id: test_coverage.py
    resource: tests/test_coverage.py
  - id: about.md
    resource: docs/about.md
    title: What a slot may hold
  - resource: src/d3fend/schema/d3fend_entries.yaml
  - resource: scripts/d3fend_to_linkml.py
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Entries module

The converter writes this file, so a change goes in the script. `tests/test_catalogue.py` fails when the file is not the script's output.[^test_catalogue.py]

A slot's title and description are the property's own label and definition.[^test_coverage.py] Its `is_a` and `mixins` are the superproperties, `inverse` the declared inverse, and `transitive` and `symmetric` the declared flags. An annotation keeps a stated domain and range.[^test_coverage.py]

`D3fendEntry` lists each property with no stated domain. A narrower kind lists a property only where the ontology states that domain, or the range of its inverse, and this edition obeys it.[^about.md]

[^test_catalogue.py]: tests/test_catalogue.py, test_the_module_is_the_converters_output
[^test_coverage.py]: tests/test_coverage.py
[^about.md]: docs/about.md, What a slot may hold
