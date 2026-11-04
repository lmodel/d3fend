---
type: Dataset
id: https://w3id.org/lmodel/d3fend/knowledge/datasets/catalogue
genre: reference
title: The catalogue
description: "`src/d3fend/data/d3fend-1.6.0.yaml`: every class and individual of D3FEND 1.6.0, 5,419 in all, as one record each with its IRI as `id`, its kind as `type`, and its text and relations as slots."
resource: src/d3fend/data/d3fend-1.6.0.yaml
derivedFrom:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/upstream-copy
references:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/entries-module
sources:
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_each_file_that_copies_the_text_carries_the_designation
  - id: index.md
    resource: docs/index.md
    title: What was checked
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_the_json_ld_projection_reproduces_the_turtle
  - resource: src/d3fend/data/d3fend-1.6.0.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# The catalogue

The converter writes the file from the Turtle, and its header reproduces MITRE's designation and licence.[^test_upstream.py]

All 5,419 records pass the committed JSON Schema, `linkml-validate` and the rules on a whole catalogue, and load into the generated models.[^index.md]

A relation's values come from the Turtle's direct triples and its class restrictions. Through the JSON-LD context the catalogue gives back every triple the Turtle states about a term.[^test_catalogue.py]

[^test_upstream.py]: tests/test_upstream.py, test_each_file_that_copies_the_text_carries_the_designation
[^index.md]: docs/index.md, What was checked
[^test_catalogue.py]: tests/test_catalogue.py, test_the_json_ld_projection_reproduces_the_turtle
