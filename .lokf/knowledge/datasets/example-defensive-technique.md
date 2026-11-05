---
type: D3fendDefensiveTechnique
id: https://w3id.org/lmodel/d3fend/knowledge/datasets/example-defensive-technique
genre: reference
title: File Analysis
description: The defensive technique `d3f:FileAnalysis` of D3FEND 1.6.0, written as a concept of type `D3fendDefensiveTechnique` in the adapt copy's keys. It shows that the domain schema admits a technique as a concept, with its relations to D3FEND's own terms.
resource: src/d3fend/data/d3fend-1.6.0.yaml
d3fend_id: D3-FA
analyzes:
  - d3f:File
enables:
  - d3f:Detect
derivedFrom:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/catalogue
sources:
  - id: readme.md
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_a_record_holds_its_relations
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# File Analysis

This concept shows how a host writes a D3FEND term in its bundle: its `type` is a kind, and its relations name D3FEND's terms by their CURIEs. `lokf validate` checks it against `.lokf/d3fend.yaml`.[^readme.md]

Its keys are the ones the record `d3f:FileAnalysis` holds in the catalogue.[^test_catalogue.py]

[^readme.md]: README.md, Knowledge Trust Ladder (KTL)
[^test_catalogue.py]: tests/test_catalogue.py, test_a_record_holds_its_relations
