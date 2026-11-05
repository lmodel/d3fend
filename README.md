<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# d3fend

MITRE D3FEND Knowledge Graph 1.6.0 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/d3fend](https://lmodel.github.io/d3fend)

## What it models

The schema models [MITRE D3FEND](https://d3fend.mitre.org/), edition 1.6.0 of 31 August 2026, the knowledge graph of cybersecurity countermeasures: what each defensive technique acts on, what each offensive technique touches, and the digital artifacts where the two meet. Each kind of entry is a class, each property of the ontology is a slot under its own IRI, and every term of the edition is a record in `src/d3fend/data/d3fend-1.6.0.yaml`, under its own IRI too.

`upstream/` holds MITRE's Turtle file, pinned by hash, and `scripts/d3fend_to_linkml.py` writes the slots and the catalogue from it. `tests/test_coverage.py` walks the file in both directions, and `tests/test_catalogue.py` shows that the catalogue validates and projects back to the file's own triples. A weekly workflow opens an issue when a new edition appears, a pinned file changes, or the Terms of Use change. [docs/index.md](docs/index.md) says how to validate a catalogue, and [docs/about.md](docs/about.md) why terms are records and what stays out.

## Mappings

The schema is the one home for mappings. The hand-kept SSSOM file and the guessed mappings on each class are gone, since no source confirmed them.

* **[lmodel/attack](https://github.com/lmodel/attack)**: `close_mappings` on the offensive technique, the mitigation and the data source, and `related_mappings` on the tactic and on the techniques of other frameworks. `tests/test_mappings.py` checks each against its released copy.
* **[lmodel/stix](https://github.com/lmodel/stix)**: `related_mappings` on `attack_id` to `external_id`. `tests/test_mappings.py` checks it against the released copy.
* **[lmodel/cwe](https://github.com/lmodel/cwe)**: `close_mappings` on the weakness, and `related_mappings` on `cwe_id`, since D3FEND writes the number with a `CWE-` prefix. `tests/test_mappings.py` checks both against the released copy.
* **[lmodel/capec](https://github.com/lmodel/capec)**: `related_mappings` on `capec_id`, for the same reason. `tests/test_mappings.py` checks it against the released copy.
* **[lmodel/nist-sp-800-53](https://github.com/lmodel/nist-sp-800-53)**: `related_mappings` on the NIST control to the control and the enhancement, since D3FEND names three revisions and the target one. `tests/test_mappings.py` checks both against the released copy.
* **[SKOS](https://www.w3.org/TR/skos-reference/), [IAO](https://obofoundry.org/ontology/iao.html), [BFO](https://obofoundry.org/ontology/bfo.html) and the [Common Core Ontologies](https://github.com/CommonCoreOntology/CommonCoreOntologies)**: `close_mappings` on the ten properties the ontology itself names as `rdfs:isDefinedBy`, such as `related` to `skos:related` and `has_participant` to `BFO:0000057`. `tests/test_mappings.py` reads each from the Turtle.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the converter from the Turtle and the upstream watch
* [src/d3fend/schema/](src/d3fend/schema): the LinkML schema, `d3fend.yaml`, `d3fend_core.yaml` and `d3fend_entries.yaml`, which the converter writes
* [src/d3fend/data/](src/d3fend/data): the catalogue, which the converter writes
* [src/d3fend/datamodel/](src/d3fend/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream/): the ontology at the pinned edition and its terms, unchanged
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/d3fend.yaml`, is the copy `just lokf-adapt` writes from `src/d3fend/schema/d3fend.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-d3fend.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots `D3fendEntry` and `D3fendCatalog` on `Concept`, so a concept may be an entry of any kind. In Obsidian, add the kinds to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
D3fendAgent, D3fendAnalyticTechnique, D3fendArtifact, D3fendAttackDataSource, D3fendAttackMitigation, D3fendCciControl, D3fendControlCatalog, D3fendDefensiveTactic, D3fendDefensiveTechnique, D3fendDigitalArtifact, D3fendEvent, D3fendExternalControl, D3fendGoal, D3fendNistControl, D3fendOffensiveTactic, D3fendOffensiveTechnique, D3fendTechnique, D3fendTechniqueReference, D3fendThing, D3fendThreatModelTechnique, D3fendThreatModelThing, D3fendWeakness
```

The copy drops `id`, `type` and `rdf_type` for LOKF's `id` and `type`. It renames `created`, `definition`, `description`, `name`, `title` and `version` with a `d3fend_` prefix, keeping their IRIs, because LOKF has slots of those names. A concept names a D3FEND term in a relation by its CURIE, such as `analyzes: [d3f:File]`.

No class, enum or type is a neighbour's, since each carries the `D3fend` prefix. D3FEND's properties are ordinary words, so the copy shares a few keys with oscal, attack, stix, nist-nvd, uco, spdx and slsa, under other IRIs, which `tests/test_schema_rules.py` lists. A composite projects each under one IRI until `lokf adapt` can rename what a neighbour copy defines (lokf #169).

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

D3FEND is under its Terms of Use and its repository's MIT licence, and `upstream/`, the catalogue and the slots reproduce MITRE's designation and licence as those terms ask. D3FEND also carries text of ATT&CK, ATLAS, SPARTA and CWE under their own terms, and abstracts of the sources it cites, which stay their authors' and which the catalogue leaves out: see [NOTICE](NOTICE). This is not a project of MITRE, and its use implies no endorsement by it. MITRE D3FEND is a trademark of The MITRE Corporation.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
