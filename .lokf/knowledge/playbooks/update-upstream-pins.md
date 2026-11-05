---
type: Playbook
id: https://w3id.org/lmodel/d3fend/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Move to another edition
description: "How to move the schema to another edition when the watch reports one: read what changed, then move `upstream/`, the pins in `scripts/check_upstream_release.py`, the schema headers and the catalogue's name together, and let the tests show what the new Turtle changed."
references:
  - https://w3id.org/lmodel/d3fend/knowledge/workflows/upstream-watch
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/upstream-copy
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the pins
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_every_module_names_the_pinned_edition
  - id: d3fend_to_linkml.py
    resource: scripts/d3fend_to_linkml.py
    title: the docstring
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Move to another edition

1. Read the watch's report and D3FEND's changelog. A person decides whether the schema moves.[^check_upstream_release.py]
2. Put the new Turtle in `upstream/`, and move the pins in `scripts/check_upstream_release.py`.[^check_upstream_release.py]
3. Move the `version`, `source` and annotations in each schema header. `tests/test_upstream.py` holds them equal to the pins.[^test_upstream.py]
4. Run `just gen-schema`. The script stops on a predicate it does not know.[^d3fend_to_linkml.py]
5. Run `just test`. `tests/test_coverage.py` fails on each new axiom, and `tests/test_catalogue.py` on each kind whose count moved.[^test_coverage.py]

[^check_upstream_release.py]: scripts/check_upstream_release.py, the pins
[^test_upstream.py]: tests/test_upstream.py, test_every_module_names_the_pinned_edition
[^d3fend_to_linkml.py]: scripts/d3fend_to_linkml.py, the docstring
[^test_coverage.py]: tests/test_coverage.py, the docstring
