---
type: Dataset
id: https://w3id.org/lmodel/d3fend/knowledge/datasets/upstream-copy
genre: reference
title: Copy of the upstream
description: "`upstream/`: D3FEND 1.6.0's Turtle file, the licence file at tag 1.6.0, and the Terms of Use, unchanged. `scripts/check_upstream_release.py` pins each by its git object hash, and a test holds the folder to that list."
resource: upstream
references:
  - https://w3id.org/lmodel/d3fend/knowledge/references/d3fend-ontology
  - https://w3id.org/lmodel/d3fend/knowledge/references/d3fend-terms-of-use
sources:
  - id: upstream-readme.md
    resource: upstream/README.md
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_upstream_holds_exactly_the_pinned_files
  - resource: upstream
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Copy of the upstream

The folder holds `d3fend.ttl`, read from MITRE's versioned address, `LICENSE.md` from the repository that builds the ontology, and `TERMS.txt`, the text of the Terms of Use.[^upstream-readme.md]

`tests/test_upstream.py` holds the folder to the pins, so nothing is added and nothing changes.[^test_upstream.py]

[^upstream-readme.md]: upstream/README.md
[^test_upstream.py]: tests/test_upstream.py, test_upstream_holds_exactly_the_pinned_files
