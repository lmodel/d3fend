---
type: Explanation
id: https://w3id.org/lmodel/d3fend/knowledge/explanations/kinds-of-entry
genre: explanation
title: How the kinds are chosen
description: "How a term gets its kind: the first in the converter's table whose branch it sits under, the deeper before its parent and D3FEND's own branches before the external ones, so that a term with two parents has one kind."
about:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/entries-module
sources:
  - id: about.md
    resource: docs/about.md
    title: How the kinds are chosen
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_an_entry_under_two_branches_takes_the_stated_kind
  - resource: scripts/d3fend_to_linkml.py
    title: KINDS
generated:
  by: process:ktl-librarian
  at: "2026-11-04T23:03:24Z"
status: draft
---

# How the kinds are chosen

An entry takes the first kind in the converter's table whose branch it sits under, through `rdfs:subClassOf` and `rdf:type`. An ATT&CK Enterprise technique sits under both `d3f:OffensiveTechnique` and `d3f:ATTACKEnterpriseTechnique`, and takes `D3fendOffensiveTechnique`.[^about.md]

`rdf_type` and `subclass_of` keep every parent the ontology states. The 874 ATT&CK Enterprise techniques and the 64 framework tactics are the terms with two such parents, and a test holds the kind each takes.[^test_catalogue.py]

The ten types of reference share their fields, so they are one kind, and `rdf_type` says which each is.[^about.md]

[^about.md]: docs/about.md, How the kinds are chosen
[^test_catalogue.py]: tests/test_catalogue.py, test_an_entry_under_two_branches_takes_the_stated_kind
