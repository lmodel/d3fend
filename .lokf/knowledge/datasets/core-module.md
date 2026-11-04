---
type: Dataset
id: https://w3id.org/lmodel/d3fend/knowledge/datasets/core-module
genre: reference
title: Core module
description: "`src/d3fend/schema/d3fend_core.yaml`, the module with the schema's two value types, `d3fend_date_time` and `d3fend_uri`, and the one list, `D3fendOwlKind`."
resource: src/d3fend/schema/d3fend_core.yaml
isPartOf:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/d3fend-linkml-schema
sources:
  - id: d3fend_core.yaml
    resource: src/d3fend/schema/d3fend_core.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Core module

The module imports only the LinkML types.[^d3fend_core.yaml]

`d3fend_date_time` admits a date and time with no time zone, which LinkML's `datetime` asks a format checker to refuse, and most of D3FEND's values have none. `d3fend_uri` is typed `xsd:anyURI` and admits the three empty `has-link` values of this edition, which LinkML's `uri` would refuse.[^d3fend_core.yaml]

`D3fendOwlKind` says whether the ontology declares a term a class, an individual or both.[^d3fend_core.yaml]

[^d3fend_core.yaml]: src/d3fend/schema/d3fend_core.yaml
