# d3fend

This project is a LinkML model of MITRE D3FEND, edition 1.6.0, the knowledge graph of cybersecurity countermeasures. Each kind of entry is a class, each property of the ontology a slot under its own IRI, and every term of the edition a record under its own IRI.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): why terms are records, how the kinds are chosen and what stays out
- [`d3fend.yaml`](schema/d3fend.yaml): the schema, with its modules merged

## Validating a catalogue

```bash
uv run linkml-validate -s src/d3fend/schema/d3fend.yaml -C D3fendCatalog src/d3fend/data/d3fend-1.6.0.yaml
```

`project/jsonschema/d3fend.schema.json` is the same schema for anyone without LinkML. JSON Schema looks at one value at a time, so a consumer that wants every rule also runs `tests/d3fend_rules.py`, which checks that a relation names a record of the right kind and that no two records share an IRI.

To write the catalogue and the slots again from MITRE's Turtle file:

```bash
just gen-schema
```

## What was checked

All 5,419 records of D3FEND 1.6.0 pass the committed JSON Schema, `linkml-validate` and those rules with no departure, and load into the generated dataclasses and Pydantic models, each as its own kind. Through the generated JSON-LD context they give back every triple the Turtle states about a term, except the facts of `owl:Class` and `owl:NamedIndividual`, which each record holds as `owl_kind`, and add only the 23 class restrictions that have no direct triple. `tests/test_catalogue.py` holds this, and `tests/test_coverage.py` walks the Turtle in both directions and lists what stays out.
