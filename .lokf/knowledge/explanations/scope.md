---
type: Explanation
id: https://w3id.org/lmodel/d3fend/knowledge/explanations/scope
genre: explanation
title: What the schema does not cover
description: "What the schema leaves out on purpose: D3FEND's classes as LinkML classes, the 340 abstracts of cited sources, the restrictions the edition does not obey, two leftover subjects of WebProtege, the SQL form, and any claim about whether what an entry says is true."
about:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/d3fend-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: What is left out
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: LITERAL_RESTRICTIONS and AXIOMS_LEFT_OUT
generated:
  by: process:ktl-librarian
  at: "2026-11-05T01:50:09Z"
status: draft
---

# What the schema does not cover

D3FEND's classes are not LinkML classes. A host that wants a concept of a technique uses a kind and names the term by its CURIE.[^about.md]

The 340 values of `kb_abstract` stay out of the catalogue. They quote the sources D3FEND cites, so those words are their authors', and `upstream/d3fend.ttl` alone holds them. The slot stays, so the schema renders the property.[^about.md]

`tests/test_coverage.py` lists what else stays out: eleven restrictions with a literal filler that the edition does not obey, one `owl:allValuesFrom`, two anonymous unions, and two subjects under `wptmp:entity#`.[^test_coverage.py]

The schema says nothing about whether what an entry claims is true.[^about.md]

[^about.md]: docs/about.md, What is left out
[^test_coverage.py]: tests/test_coverage.py, LITERAL_RESTRICTIONS and AXIOMS_LEFT_OUT
