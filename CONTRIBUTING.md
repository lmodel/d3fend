# Contributing to d3fend

*This file is a checklist, not a design log. Each rule is a line or two that links to where its reasoning lives. `lint-and-docs.yaml` holds it to a word budget.*

## What this project is

A LinkML schema of MITRE D3FEND 1.6.0, the knowledge graph of countermeasures: each kind of entry a class, each property a slot under its own IRI, and every term a record. [NOTICE](NOTICE) says whose work each part is.

| Path | Holds |
| --- | --- |
| `src/d3fend/schema/` | The LinkML schema: `d3fend_core` and the umbrella `d3fend`, which you edit, and `d3fend_entries`, which the script below writes. |
| `src/d3fend/data/` | The catalogue: every term of the edition as a record, written by the script below. |
| `src/d3fend/datamodel/`, `project/`, `docs/schema/` | Artefacts generated from the schema. |
| `upstream/` | MITRE's Turtle file of the pinned edition, unchanged, with its terms. |
| `scripts/d3fend_to_linkml.py` | The one fixed step from the Turtle to the slots, the kinds and the catalogue. |
| `docs/` | The website's own pages. |
| `tests/` | Python tests and example data. |
| `.lokf/knowledge/` | This repository's knowledge bundle. |

## Development setup

You need Python 3.10+, [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just).

```bash
git clone https://github.com/lmodel/d3fend.git
cd d3fend
uv sync --group dev
just --list
```

### Agent skills (optional, only for this repo's `.lokf/` bundle)

The bundle is maintained with the Knowledge Trust Ladder (KTL) skills, **installed, never committed**. Continuous integration (CI) installs the librarian skill at run time, pinned to a release. [The install page](https://w3id.org/ktl/docs/install/) lists every route. With npm:

```bash
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-librarian --yes   # derive concepts
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-curator --yes     # confirm them as a person
```

## Before opening a pull request

- **Edit the source, then regenerate.** Edit `scripts/d3fend_to_linkml.py` or the two hand-written schema files, run `just gen-schema`, `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit the output. `src/d3fend/schema/d3fend_entries.yaml`, `src/d3fend/data/`, `project/`, `src/d3fend/datamodel/`, `docs/schema/` and `.lokf/schema/d3fend.yaml` are generated.
- **Keep the ontology's IRIs.** A slot carries its property's IRI as `slot_uri`, and a record its term's IRI as `id`. `tests/test_coverage.py` walks the Turtle in `upstream/` and fails on anything it does not render, unless it is listed there with its reason.
- **State only what the upstream states.** No bound or rule of your own. What JSON Schema cannot check is in `tests/d3fend_rules.py`, and what the data merely shows stays in `tests/test_catalogue.py`.
- **A mapping is read at its source.** `tests/test_mappings.py` holds each one to a neighbour copy or to what the ontology itself states. A term with no sure match stays unmapped.
- **Render the pinned edition.** `tests/test_upstream.py` holds the schema header, `scripts/check_upstream_release.py` and `upstream/` equal.
- **Keep names apart.** A host imports this adapt copy beside the Linked Open Knowledge Format (LOKF) schema and the released copies in `tests/neighbours/`. `tests/test_schema_rules.py` checks this.
- **Run the tests**: `just test` (schema generation, `pytest` and the examples under `tests/data/`). Example data goes in `tests/data/valid/` and `tests/data/invalid/`, named `ClassName-suffix.yaml`. An invalid example's first line, `# Fails at: <pointer>`, names where it fails.
- **Follow the schema's conventions**: PascalCase classes and enums with the `D3fend` prefix, snake_case slots, and a short description on every element. `just lint` checks, under `.linkmllint.yaml`.
- **Run the pre-commit hooks** on what you staged (`uvx pre-commit run`).
- **Lock files are part of the change.** CI installs with `uv sync --locked`, so an edit without its `uv.lock` (or `.lokf/uv.lock`) fails.
- **Knowledge-bundle changes**: `cd .lokf && just lokf-validate` must pass, and `knowledge-registrar.yaml` runs on any `.lokf/**` change.
- **`lint-and-docs.yaml`** runs ShellCheck, actionlint, markdownlint, lychee and codespell.
- **Actions are pinned to commit hashes**; Dependabot bumps them.
- **The skills pin moves with the sidecar copies.** When moving `TRUST_LADDER_SKILLS_REF` in `.github/workflows/knowledge-librarian.yaml`, copy the other `knowledge-*.yaml` workflows and `.lokf/scripts/` and `.lokf/m365/` from that release's `skills/ktl-sidecar/templates/` in the same pull request.
- **If your change alters behaviour**, add an entry under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).

## Code of conduct

Participation here is covered by the [Contributor Covenant](CODE_OF_CONDUCT.md).

## Using AI tools

Artificial intelligence (AI) assistance is welcome. [AI_COVENANT.md](AI_COVENANT.md) sets the rules, for people and the scheduled `knowledge-librarian` agent alike.

## Reporting issues

Use the [issue tracker](https://github.com/lmodel/d3fend/issues) for the schema. A problem in D3FEND itself belongs with [the D3FEND project](https://github.com/d3fend/d3fend-ontology/issues).

## Releasing (maintainers)

- Write `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md) as you go. The release job refuses an empty one (`.github/scripts/changelog-release.mjs check`).
- Type the commit ([Conventional Commits](https://www.conventionalcommits.org/)) for what the change *is*. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release. Other types leave their entries for the next release that does. A pull request that would release must carry a releasing type in its title too, since a squash merge takes its subject from it.
- On merge, [`semantic-release.yml`](.github/workflows/semantic-release.yml) retitles the section to `## [X.Y.Z] - YYYY-MM-DD`, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub Release. No file is bumped. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches `.github/workflows/knowledge-release.yaml`, which attaches the schema copy and the bundle when the bundle or the schema changed.
- That step runs behind the `release` GitHub Environment. Configure required reviewers on it in Settings → Environments, or every qualifying merge is released unattended.
- Below 1.0.0: push the `v0.0.0` baseline tag on `main` before the first releasing merge, which then releases 0.1.0. Both release jobs refuse to run without a `v*` tag, because semantic-release would otherwise start at 1.0.0. `.releaserc.json` maps `breaking: true` to `minor`, and reaching 1.0.0 means removing that rule in a pull request of its own.
- A branch rule requiring pull requests, status checks or signed commits would reject the release job's own push to `main`, so leave them off. [SECURITY.md](SECURITY.md) says what holds `main` instead, and the shared design is on [KTL's releasing page](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/main/docs/releasing.md).

## License

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE). The upstream's files are under their own terms, and [NOTICE](NOTICE) says what they allow. Update it when you add something from elsewhere.
