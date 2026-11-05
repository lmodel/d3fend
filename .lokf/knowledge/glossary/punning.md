---
type: GlossaryTerm
id: https://w3id.org/lmodel/d3fend/knowledge/glossary/punning
title: Punning
description: "Punning: declaring one IRI both an `owl:Class` and an `owl:NamedIndividual`. D3FEND's conventions pun defensive techniques, and `owl_kind` records it as `class_and_individual`."
relatedTo:
  - https://w3id.org/lmodel/d3fend/knowledge/explanations/terms-as-records
sources:
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: test_each_record_says_how_the_ontology_declares_it
  - resource: src/d3fend/schema/d3fend_core.yaml
    title: D3fendOwlKind
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Punning

A record's `owl_kind` says how the ontology declares its term. 2,070 of the 5,419 terms are punned.[^test_coverage.py]

[^test_coverage.py]: tests/test_coverage.py, test_each_record_says_how_the_ontology_declares_it
