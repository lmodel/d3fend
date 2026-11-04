---
type: Playbook
id: https://w3id.org/lmodel/d3fend/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test
description: "How to change the schema: edit the converter or a hand-written module, run `just gen-schema`, `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated files are never edited by hand."
references:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/d3fend-linkml-schema
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/generated-artefacts
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: project.justfile
    resource: project.justfile
    title: gen-schema
  - id: main.yaml
    resource: .github/workflows/main.yaml
    title: the lint step
  - id: justfile
    resource: justfile
    title: the test recipe
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Regenerate and test

1. Edit `scripts/d3fend_to_linkml.py`, `src/d3fend/schema/d3fend.yaml` or `src/d3fend/schema/d3fend_core.yaml`.[^contributing.md]
2. Run `just gen-schema`, which writes the slots, the kinds and the catalogue from the Turtle.[^project.justfile]
3. Run `just lint`. A warning fails it.[^main.yaml]
4. Run `just gen-project` and `just gen-doc`, then `just lokf-adapt`.[^contributing.md]
5. Run `just test`, which generates into `tmp/`, runs `pytest` and runs the example runner.[^justfile]
6. Commit the output.[^contributing.md]

[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
[^project.justfile]: project.justfile, gen-schema
[^main.yaml]: .github/workflows/main.yaml, the lint step
[^justfile]: justfile, the test recipe
