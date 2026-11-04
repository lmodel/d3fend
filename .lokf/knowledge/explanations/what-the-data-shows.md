---
type: Explanation
id: https://w3id.org/lmodel/d3fend/knowledge/explanations/what-the-data-shows
genre: explanation
title: What the data shows
description: "What the catalogue holds as the file holds it, faults included: a CAPEC id that names another entry, 27 duplicated D3FEND ids, three empty links, and terms with two labels or three definitions. A test records each, so a later edition that fixes one fails."
about:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/catalogue
sources:
  - id: about.md
    resource: docs/about.md
    title: What the data shows
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_what_the_data_shows_and_the_ontology_does_not_say
generated:
  by: process:ktl-librarian
  at: "2026-11-04T23:03:24Z"
status: draft
---

# What the data shows

A catalogue renders the file as it stands. `d3f:CAPEC-663` holds the CAPEC id `CAPEC-553`, 27 values of `d3fend_id` name more than one analytic technique, and three references hold an empty `has_link`.[^about.md]

`tests/test_catalogue.py` records each of these, so a later edition that fixes one fails there.[^test_catalogue.py]

[^about.md]: docs/about.md, What the data shows
[^test_catalogue.py]: tests/test_catalogue.py, test_what_the_data_shows_and_the_ontology_does_not_say
