---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/d3fend/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: d3fend Knowledge Bundle
description: MITRE D3FEND Knowledge Graph 1.6.0 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/d3fend/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# d3fend Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for d3fend. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code, schema and documents.

# Datasets

* [d3fend LinkML schema](datasets/d3fend-linkml-schema.md) - The LinkML model of MITRE D3FEND 1.6.0, `src/d3fend/schema/d3fend.yaml` (schema id `https://w3id.org/lmodel/d3fend`): an umbrella over a core and an entries module, whose tree root `D3fendCatalog` holds every term of the edition as a record.
* [Core module](datasets/core-module.md) - `src/d3fend/schema/d3fend_core.yaml`, the module with the schema's two value types, `d3fend_date_time` and `d3fend_uri`, and the one list, `D3fendOwlKind`.
* [Entries module](datasets/entries-module.md) - `src/d3fend/schema/d3fend_entries.yaml`, which `scripts/d3fend_to_linkml.py` writes from the Turtle: the abstract `D3fendEntry`, its 22 kinds, and one slot for each of the ontology's 292 properties a record can hold, under the property's own IRI.
* [The catalogue](datasets/catalogue.md) - `src/d3fend/data/d3fend-1.6.0.yaml`: every class and individual of D3FEND 1.6.0, 5,419 in all, as one record each with its IRI as `id`, its kind as `type`, and its text and relations as slots.
* [Generated artefacts](datasets/generated-artefacts.md) - What `just gen-project` and `just gen-doc` generate from the schema: the projections in `project/`, the Python models in `src/d3fend/datamodel/`, and the merged schema and pages under `docs/`. None is edited by hand, and the SQL generator is off.
* [Example data](datasets/example-data.md) - The examples `tests/test_data.py` checks: a valid example of each class, most of them real records of D3FEND 1.6.0, a counter-example for each constraint, and a counter-example for each rule on a whole catalogue.
* [Copy of the upstream](datasets/upstream-copy.md) - `upstream/`: D3FEND 1.6.0's Turtle file, the licence file at tag 1.6.0, and the Terms of Use, unchanged. `scripts/check_upstream_release.py` pins each by its git object hash, and a test holds the folder to that list.
* [The schema's adapt copy](datasets/adapt-copy.md) - `.lokf/d3fend.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: rooted on `D3fendEntry` and `D3fendCatalog`, with `id`, `type` and `rdf_type` dropped for LOKF's, and six keys renamed with a `d3fend_` prefix.
* [Neighbours' adapt copies](datasets/neighbour-copies.md) - The adapt copies of fourteen released lmodel repositories in `tests/neighbours/`, among them attack, cwe, capec and nist-sp-800-53, each pinned by its SHA-256, against which `tests/test_schema_rules.py` holds this schema's copy apart and `tests/test_mappings.py` holds the mappings.
* [File Analysis](datasets/example-defensive-technique.md) - The defensive technique `d3f:FileAnalysis` of D3FEND 1.6.0, written as a concept of type `D3fendDefensiveTechnique` in the adapt copy's keys. It shows that the domain schema admits a technique as a concept, with its relations to D3FEND's own terms.

# Explanations

* [Why a term is a record](explanations/terms-as-records.md) - Why D3FEND's terms are records and not LinkML classes: D3FEND's own conventions pun its techniques as instances, its distribution states each class restriction again as a direct triple between terms, and most of its 4,465 classes are not types anyone instantiates.
* [How the kinds are chosen](explanations/kinds-of-entry.md) - How a term gets its kind: the first in the converter's table whose branch it sits under, the deeper before its parent and D3FEND's own branches before the external ones, so that a term with two parents has one kind.
* [What a slot may hold](explanations/what-a-slot-may-hold.md) - Which kinds hold which slots, and why most may hold any: the ontology states a domain for few of its properties, so no domain is invented. A literal slot holds one value where no term of this edition holds two.
* [Mappings](explanations/mappings.md) - What the schema maps to and how each mapping is held: lmodel/attack, stix, cwe, capec and nist-sp-800-53 by their released copies, and SKOS and IAO because the ontology itself names them. The earlier guessed mappings are gone.
* [RDF from the catalogue](explanations/rdf.md) - How the catalogue becomes RDF: every identifier is a CURIE, so both the JSON-LD context and LinkML's own dumper give a record's IRI and its relations as D3FEND's own. `rdfs:seeAlso` and `rdfs:isDefinedBy` project as text.
* [What the schema does not cover](explanations/scope.md) - What the schema leaves out on purpose: D3FEND's classes as LinkML classes, the restrictions the edition does not obey, two leftover subjects of WebProtege, the SQL form, and any claim about whether what an entry says is true.

# Glossary

* [Entry](glossary/entry.md) - An entry: one term of the D3FEND graph, a class or an individual, as a record with its IRI, its kind, its text and its relations.
* [Kind of entry](glossary/kind-of-entry.md) - A kind of entry: one of the 22 classes under `D3fendEntry`, each a branch of D3FEND's tree, which a record names in `type`.
* [Defensive technique](glossary/defensive-technique.md) - A defensive technique: a countermeasure, a method that makes a system harder to attack, related to the artifacts it acts on and to the tactic it enables. `D3fendDefensiveTechnique` holds 273 in this edition.
* [Offensive technique](glossary/offensive-technique.md) - An offensive technique: a way an adversary acts, drawn from ATT&CK Enterprise, related to the artifacts it touches and to the tactic it serves. The techniques of other frameworks are `D3fendThreatModelTechnique`.
* [Digital artifact](glossary/digital-artifact.md) - A digital artifact: something that carries information for a digital system, such as a file, a process or a packet, where offensive and defensive techniques meet.
* [Class restriction](glossary/class-restriction.md) - A class restriction: an OWL axiom such as `d3f:FileAnalysis rdfs:subClassOf [ owl:onProperty d3f:analyzes ; owl:someValuesFrom d3f:File ]`, which a record holds as a value of its slot.
* [Punning](glossary/punning.md) - Punning: declaring one IRI both an `owl:Class` and an `owl:NamedIndividual`. D3FEND's conventions pun defensive techniques, and `owl_kind` records it as `class_and_individual`.
* [Adapt copy](glossary/adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`.

# References

* [MITRE D3FEND ontology](references/d3fend-ontology.md) - D3FEND's distribution: the ontology at `https://d3fend.mitre.org/ontologies/d3fend/1.6.0/d3fend.ttl`, edition 1.6.0 of 2026-08-31, built from tag 1.6.0 of `d3fend/d3fend-ontology`. `upstream/` holds the Turtle file.
* [D3FEND Terms of Use](references/d3fend-terms-of-use.md) - MITRE's terms for using D3FEND: a non-exclusive, royalty-free licence for research, development and commercial purposes, on condition that a copy reproduces MITRE's copyright designation and the licence. `upstream/TERMS.txt` holds the text, and the watch compares it.
* [d3fend-ontology repository](references/d3fend-repository.md) - `d3fend/d3fend-ontology`, the repository that builds D3FEND's distribution, under the MIT licence. This project reads its licence file at tag 1.6.0, and pins that tag's commit in the schema header. It is the place to report a problem in D3FEND.

# Policies

* [Licence and attribution](policies/license-and-attribution.md) - Whose work each part is: the code and the schema under Apache-2.0, the bundle under CC BY 4.0, D3FEND under MITRE's Terms of Use with the designation and licence those terms ask each copy to reproduce, and the third-party text inside D3FEND under its own terms.
* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work here: whoever submits owns the contribution, an element says what the ontology says, a rule states only what the upstream states, a mapping is read at its source, and no commit carries an AI co-authorship trailer.
* [Security policy](policies/security-policy.md) - How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in D3FEND itself belongs with the D3FEND project.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/d3fend`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.

# Playbooks

* [Regenerate and test](playbooks/regenerate-and-test.md) - How to change the schema: edit the converter or a hand-written module, run `just gen-schema`, `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated files are never edited by hand.
* [Validate a catalogue](playbooks/validate-a-catalogue.md) - How to validate a catalogue: run `linkml-validate` with `D3fendCatalog` as the target class, and `tests/d3fend_rules.py` for what JSON Schema cannot state. `project/jsonschema/d3fend.schema.json` serves anyone without LinkML.
* [Release](playbooks/release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
* [Move to another edition](playbooks/update-upstream-pins.md) - How to move the schema to another edition when the watch reports one: read what changed, then move `upstream/`, the pins in `scripts/check_upstream_release.py`, the schema headers and the catalogue's name together, and let the tests show what the new Turtle changed.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow: on every pull request and push to `main`, it runs `just test` on Python 3.10 to 3.14, and lints the schema and checks the adapt copy on 3.13.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The static checks on pull requests, on `main` and every Monday: ShellCheck, actionlint, the word budgets of CONTRIBUTING.md and SECURITY.md, markdownlint, lychee and codespell.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The workflow that computes the next version from Conventional Commits on `main`, promotes the changelog, tags and publishes a GitHub Release, and dispatches the knowledge release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: another edition of D3FEND, a changed file, a changed licence or changed Terms of Use fails the run and opens or updates an issue.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate on the bundle: it validates the bundle on each pull request that touches it and weekly, and checks that each new `human:` event in a pull request is backed by an approval or a signature. It never judges whether content is true.
* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The sidecar's scheduled agent run that keeps the bundle in step with the repository and opens a pull request for a person to review. It is inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the bundle, a Copilot skill and the schema's adapt copy to a GitHub release, each with a checksum. It runs when dispatched, and on each release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, by one pull request.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds `website/` on each pull request that touches its inputs, and deploys the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
