---
type: Explanation
id: https://w3id.org/lmodel/d3fend/knowledge/explanations/rdf
genre: explanation
title: RDF from the catalogue
description: "How the catalogue becomes RDF: every identifier is a CURIE, so both the JSON-LD context and LinkML's own dumper give a record's IRI and its relations as D3FEND's own. `rdfs:seeAlso` and `rdfs:isDefinedBy` project as text."
about:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/catalogue
sources:
  - id: about.md
    resource: docs/about.md
    title: RDF
  - resource: tests/test_datamodel.py
  - resource: tests/test_catalogue.py
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# RDF from the catalogue

Apply `project/jsonld/d3fend.context.jsonld` to the catalogue, or run LinkML's own dumper, and a record's IRI and its relations come out as D3FEND's own.[^about.md]

`tests/test_catalogue.py` compares the first with the Turtle, and `tests/test_datamodel.py` runs the second on the small example.[^about.md]

`project/owl/d3fend.owl.ttl` is the schema's own OWL, which names slots and classes under this schema's namespace. D3FEND's ontology is `upstream/d3fend.ttl`.[^about.md]

[^about.md]: docs/about.md, RDF
