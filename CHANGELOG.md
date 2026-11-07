# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

## [0.2.0] - 2026-11-07

### Added

- **The schema as RDF Turtle and the merged schema**, in `project/rdf/` and `project/linkml/`, from `just gen-rdf` and `just gen-merged-schema`.

### Changed

- **The bundle's schema files sit in `.lokf/schema/`**: `lokf.yaml` and the `lokf adapt` copy `d3fend.yaml`, as KTL v0.62.0 lays them out.

## [0.1.0] - 2026-11-05

### Added

- **A LinkML model of MITRE D3FEND 1.6.0 as a catalogue with typed relations**, as an umbrella over `d3fend_core` and `d3fend_entries`. The 22 kinds of entry are classes under the abstract `D3fendEntry`, every property of the ontology is a slot under its own IRI, and all 5,419 terms are records in `src/d3fend/data/d3fend-1.6.0.yaml`. The catalogue leaves out the 340 abstracts of cited sources, which stay in MITRE's file alone.
- **`scripts/d3fend_to_linkml.py`**, the one fixed step from MITRE's Turtle file to the slots, the kinds and the catalogue. It stops on a predicate it does not know.
- **The relations that make D3FEND what it is.** Each of the 1,939 class restrictions that names a term is a value of its record's slot. The old schema held none of them.
- **A test that walks the Turtle in both directions**, a test that the whole catalogue validates and gives back the Turtle's triples through JSON-LD, and `tests/d3fend_rules.py` for what JSON Schema cannot state.
- **A weekly upstream watch** that reports a new edition, a changed file, a changed licence, or changed Terms of Use.
- **Mappings to lmodel/attack, lmodel/stix, lmodel/cwe, lmodel/capec and lmodel/nist-sp-800-53**, each held by a test to a released copy, and to the ten SKOS, IAO, BFO and Common Core Ontologies properties the ontology itself names as `rdfs:isDefinedBy`.
- **`.lokf/d3fend.yaml`, the schema's `lokf adapt` copy, rooted on `D3fendEntry` and `D3fendCatalog`.** The knowledge release attaches it as `schema-<tag>-d3fend.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.

### Changed

- **The schema moves from D3FEND 1.3.0's files to edition 1.6.0**, under the identifier `https://w3id.org/lmodel/d3fend`, with `d3f:` bound to D3FEND's own namespace for every class and slot that has a term there.
- **A class of the ontology is a record, not a LinkML class**, and an individual is a record, not an enum value. So 4,366 classes and 33 enums become 22 kinds and one enum.
- **Slots take snake_case names and keep their IRIs**, and a relation ranges over the entry base or a narrower kind, not over strings.
- **The template moves to linkml-project-copier v0.5.0**, linkml and linkml-runtime are locked at 1.12.1, and the Python project is named `d3fend-linkml`. PyPI publishing and the docs preview are off.
- **The generators' settings move to `.linkml/generators.yaml`**, and the SQL generator is off, since it would write about 4,800 join tables.

### Removed

- **The 44 MB `d3fend-full-mappings` file**, a query result at edition 1.3.0.
- **`build_schema.py`, `d3fend-protege.ttl` and the ABox fixtures.**
- **The hand-kept SSSOM file and the mappings on each class.** No source confirmed them, and several named prefixes that did not resolve. The schema is now the one home for mappings.
- **The mkdocs site.** The knowledge website replaces it.
