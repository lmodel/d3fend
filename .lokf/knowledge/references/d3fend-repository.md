---
type: Reference
id: https://w3id.org/lmodel/d3fend/knowledge/references/d3fend-repository
genre: reference
title: d3fend-ontology repository
description: "`d3fend/d3fend-ontology`, the repository that builds D3FEND's distribution, under the MIT licence. This project reads its licence file at tag 1.6.0, and pins that tag's commit in the schema header. It is the place to report a problem in D3FEND."
resource: https://github.com/d3fend/d3fend-ontology
references:
  - https://w3id.org/lmodel/d3fend/knowledge/references/d3fend-ontology
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: check_licence
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_the_umbrella_names_the_tag
  - resource: upstream/LICENSE.md
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# d3fend-ontology repository

`upstream/LICENSE.md` is the repository's licence file at tag 1.6.0, and the watch compares it.[^check_upstream_release.py]

The umbrella schema's `upstream_commit` annotation names the tag's commit.[^test_upstream.py]

[^check_upstream_release.py]: scripts/check_upstream_release.py, check_licence
[^test_upstream.py]: tests/test_upstream.py, test_the_umbrella_names_the_tag
