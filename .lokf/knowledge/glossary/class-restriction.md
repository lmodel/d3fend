---
type: GlossaryTerm
id: https://w3id.org/lmodel/d3fend/knowledge/glossary/class-restriction
title: Class restriction
description: "A class restriction: an OWL axiom such as `d3f:FileAnalysis rdfs:subClassOf [ owl:onProperty d3f:analyzes ; owl:someValuesFrom d3f:File ]`, which a record holds as a value of its slot."
relatedTo:
  - https://w3id.org/lmodel/d3fend/knowledge/explanations/terms-as-records
sources:
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: test_every_named_restriction_lands_in_its_record
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_the_json_ld_projection_reproduces_the_turtle
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Class restriction

The Turtle holds 1,954 such restrictions with `owl:someValuesFrom`. 1,939 of them name a term, and each is a value of a record's slot. The other 15 name a datatype. Of the 1,939 that name a term, 23 have no direct triple in the Turtle.[^test_coverage.py][^test_catalogue.py]

[^test_coverage.py]: tests/test_coverage.py, test_every_named_restriction_lands_in_its_record
[^test_catalogue.py]: tests/test_catalogue.py, test_the_json_ld_projection_reproduces_the_turtle
