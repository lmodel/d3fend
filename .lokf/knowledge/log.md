# Change Log

## 2026-11-05

* **Prose**: reworded 8 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: the catalogue leaves the 340 abstracts of cited sources out; NOTICE says so since 0b0ca57.
* **Changed**: the catalogue holds no `kb_abstract` value; `tests/test_catalogue.py` holds the 340 left out since 0b0ca57.
* **Changed**: the abstracts of cited sources are among what the schema leaves out; `docs/about.md` says so since 0b0ca57.
* **Changed**: the mappings to BFO and the Common Core Ontologies, which the ontology names as `rdfs:isDefinedBy`, are in since 9668280.

## 2026-11-04

* **Added**: What the data shows.
* **Changed**: the join tables the SQL generator would write number about 4,800.
* **Changed**: the Turtle states all but 23 of its restrictions as direct triples.
* **Changed**: the wording on the types of reference.
* **Added**: d3fend LinkML schema.
* **Added**: Core module.
* **Added**: Entries module.
* **Added**: The catalogue.
* **Added**: Generated artefacts.
* **Added**: Example data.
* **Added**: Copy of the upstream.
* **Added**: The schema's adapt copy.
* **Added**: Neighbours' adapt copies.
* **Added**: File Analysis.
* **Added**: Why a term is a record.
* **Added**: How the kinds are chosen.
* **Added**: What a slot may hold.
* **Added**: Mappings.
* **Added**: RDF from the catalogue.
* **Added**: What the schema does not cover.
* **Added**: Entry.
* **Added**: Kind of entry.
* **Added**: Defensive technique.
* **Added**: Offensive technique.
* **Added**: Digital artifact.
* **Added**: Class restriction.
* **Added**: Punning.
* **Added**: Adapt copy.
* **Added**: MITRE D3FEND ontology.
* **Added**: D3FEND Terms of Use.
* **Added**: d3fend-ontology repository.
* **Added**: Licence and attribution.
* **Added**: AI covenant.
* **Added**: Security policy.
* **Added**: Documentation site.
* **Added**: Regenerate and test.
* **Added**: Validate a catalogue.
* **Added**: Release.
* **Added**: Move to another edition.
* **Added**: Knowledge sources map.
* **Added**: Build and test (main.yaml).
* **Added**: Lint and docs (lint-and-docs.yaml).
* **Added**: Semantic release (semantic-release.yml).
* **Added**: Upstream watch (upstream-watch.yaml).
* **Added**: Knowledge registrar (knowledge-registrar.yaml).
* **Added**: Knowledge librarian (knowledge-librarian.yaml).
* **Added**: Knowledge release (knowledge-release.yaml).
* **Added**: Knowledge sync (knowledge-sync.yaml).
* **Added**: Knowledge website (knowledge-website.yaml).
* **Initialization**: Scaffolded the LOKF bundle for d3fend with placeholder
  services. Real concepts to follow.
