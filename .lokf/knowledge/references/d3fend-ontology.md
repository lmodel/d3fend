---
type: Reference
id: https://w3id.org/lmodel/d3fend/knowledge/references/d3fend-ontology
genre: reference
title: MITRE D3FEND ontology
description: "D3FEND's distribution: the ontology at `https://d3fend.mitre.org/ontologies/d3fend/1.6.0/d3fend.ttl`, edition 1.6.0 of 2026-08-31, built from tag 1.6.0 of `d3fend/d3fend-ontology`. `upstream/` holds the Turtle file."
resource: https://d3fend.mitre.org/resources/ontology/
references:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/upstream-copy
sources:
  - id: d3fend.ttl
    resource: upstream/d3fend.ttl
    title: the ontology header
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: check_latest and check_pinned
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# MITRE D3FEND ontology

The ontology's header names edition 1.6.0 and the release date, and its `dcterms:license` says MIT.[^d3fend.ttl]

The watch compares the file at the latest address and at the versioned one with the copy under `upstream/`.[^check_upstream_release.py]

[^d3fend.ttl]: upstream/d3fend.ttl, the ontology header
[^check_upstream_release.py]: scripts/check_upstream_release.py, check_latest and check_pinned
