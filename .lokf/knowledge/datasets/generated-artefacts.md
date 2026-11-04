---
type: Dataset
id: https://w3id.org/lmodel/d3fend/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What `just gen-project` and `just gen-doc` generate from the schema: the projections in `project/`, the Python models in `src/d3fend/datamodel/`, and the merged schema and pages under `docs/`. None is edited by hand, and the SQL generator is off."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/d3fend-linkml-schema
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: What this project is
  - id: generators.yaml
    resource: .linkml/generators.yaml
  - id: test_generated_json_schema.py
    resource: tests/test_generated_json_schema.py
  - resource: project
  - resource: src/d3fend/datamodel
  - resource: docs/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# Generated artefacts

`project/` holds the JSON Schema, the JSON-LD context, OWL, SHACL, ShEx, GraphQL, Protobuf, Excel, Java and TypeScript forms of the schema, and `src/d3fend/datamodel/` the dataclasses and the Pydantic models.[^contributing.md]

`.linkml/generators.yaml` holds the generators' settings. It turns the SQL generator off, since it would write about 4,600 join tables, and has the JSON Schema offer each concrete kind for an entry.[^generators.yaml]

`tests/test_generated_json_schema.py` fails when the committed JSON Schema is not the generator's output.[^test_generated_json_schema.py]

[^contributing.md]: CONTRIBUTING.md, What this project is
[^generators.yaml]: .linkml/generators.yaml
[^test_generated_json_schema.py]: tests/test_generated_json_schema.py
