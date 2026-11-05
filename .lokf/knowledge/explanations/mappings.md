---
type: Explanation
id: https://w3id.org/lmodel/d3fend/knowledge/explanations/mappings
genre: explanation
title: Mappings
description: "What the schema maps to and how each mapping is held: lmodel/attack, stix, cwe, capec and nist-sp-800-53 by their released copies, and SKOS, IAO, BFO and the Common Core Ontologies because the ontology itself names their terms. The earlier guessed mappings are gone."
about:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/d3fend-linkml-schema
references:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/neighbour-copies
sources:
  - id: test_mappings.py
    resource: tests/test_mappings.py
  - id: readme.md
    resource: README.md
    title: Mappings
generated:
  by: process:ktl-librarian
  at: "2026-11-05T01:50:09Z"
status: draft
---

# Mappings

The schema is the one home for mappings. Each names its target by a CURIE whose prefix the module binds, and a target is a term a released neighbour copy declares, or one the ontology names as `rdfs:isDefinedBy`.[^test_mappings.py]

D3FEND names CWE and CAPEC entries with a prefix, such as `CWE-79`, where those catalogues hold `79`, so the identifier slots are `related_mappings`.[^readme.md]

Ten properties carry a `close_mappings` to the SKOS, IAO, BFO or Common Core Ontologies term the ontology names as `rdfs:isDefinedBy`, such as `related` to `skos:related` and `has_participant` to `BFO:0000057`.[^readme.md]

[^test_mappings.py]: tests/test_mappings.py
[^readme.md]: README.md, Mappings
