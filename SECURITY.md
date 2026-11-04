# Security Policy

*This file is a policy, not a threat model. It says how to report, what executes here, and what holds each surface. Each is a line or two that links to where the reasoning lives: a workflow header, or the shared [threat model](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/main/docs/threat-model.md). `lint-and-docs.yaml` holds the file to a word budget so it stays that way.*

## Reporting a vulnerability

Use GitHub's [private vulnerability reporting](https://github.com/lmodel/d3fend/security/advisories/new), not a public issue or a pull request. Say which file is affected, how it is exploitable, and whether it reaches the released schema or only this repository's automation. One person maintains this repository: expect a first reply in days, not hours, and no bounty.

## Supported versions

**Only the latest release receives fixes.** A security fix is released as a patch and noted in [CHANGELOG.md](CHANGELOG.md). The schema stays below 1.0 ([CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers)).

## What this repository releases

It releases a LinkML schema and the Python datamodel generated from it. Nothing is published to PyPI. When the bundle or the schema has changed, `knowledge-release.yaml` attaches three assets to the release, each with its `.sha256` and a build-provenance attestation: the schema's `lokf adapt` copy, the knowledge bundle as a zip, and a Microsoft 365 Copilot skill zip. A schema is data: loading one from an untrusted source with any LinkML tool is that tool's risk, not this repository's.

`scripts/check_upstream_release.py` runs only in `upstream-watch.yaml`. It reads MITRE's public files on `d3fend.mitre.org` and one licence file on `raw.githubusercontent.com`, follows a redirect only over https to those hosts, sends no token, and writes nothing but its report. `scripts/d3fend_to_linkml.py` reads the Turtle it is given and writes the schema module and the catalogue. It parses with rdflib and calls no network, and in this repository it reads only the copy under `upstream/`, which a test holds to its hash.

A catalogue entry holds Markdown, command lines and attack descriptions as text, and this repository treats it all as data: tests validate entries and nothing executes or renders them. A consumer that displays a `kb_article` value must sanitize it first. The schema describes an entry's shape and says nothing about whether what an entry claims is true.

## What executes here

| Surface | What holds it |
| --- | --- |
| `main.yaml` and `lint-and-docs.yaml` on every pull request, and `knowledge-registrar.yaml` on any that touches `.lokf/`: tests, linters and the bundle's form | Read-only jobs with `persist-credentials: false`; `uv sync --locked` installs only what `uv.lock` pins. |
| `semantic-release.yml`, which pushes a changelog commit and tag to `main` and dispatches the knowledge release | Runs only on a push to `main`, in the `release` Environment, installing its pinned tools with `--ignore-scripts`. [Repository hardening](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/main/docs/threat-model.md#repository-hardening). |
| `knowledge-website.yaml`, which publishes the site to GitHub Pages | Builds without a write token; only its deploy job holds `pages: write` and `id-token: write`, and it runs only from `main`, once `KNOWLEDGE_WEBSITE_ENABLED` is `true`. |
| `upstream-watch.yaml`, weekly | Read-only checkout; the one write scope, `issues: write`, opens or updates the finding's issue. |
| `knowledge-librarian.yaml` and `.lokf/scripts/`, copies of the `ktl-sidecar` template, which run a large language model (LLM) agent on a schedule | The agent's job holds no write token. The `publish` job runs no agent, confines the patch to the bundle and refuses a `human:` claim, and a person merges the pull request. Inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`. [Prompt-injection guards](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/main/docs/threat-model.md#prompt-injection-guards). |
| `knowledge-release.yaml`, which attaches the schema copy and the bundle to a release | Inert until dispatched; only its `attach` job, which runs no third-party packages, can write. |
| `README.md`, `llms.txt` and the knowledge bundle, read by agents | Content, never instructions: each skill quotes what it did not author. A `human:` confirmation must be backed by a review or a signed commit. [Human attribution](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/main/docs/threat-model.md#human-attribution-human-is-a-claim-not-a-credential). |

Every workflow declares `permissions: {}` at the top, pins its actions to commit hashes that Dependabot keeps current, and runs harden-runner in audit mode. Three things are repository settings, not files. A ruleset on `main` blocks deletion and force-pushes and keeps the history linear. Two **are not yet in force here**: required reviewers on the `release` Environment, and secret scanning with push protection. Until they are, a qualifying merge releases with no human step. Nothing in continuous integration can assert them, so keeping them on is the maintainer's job.

## Not covered

- D3FEND itself: report a problem to [the D3FEND project](https://github.com/d3fend/d3fend-ontology/issues).
- LinkML, its generators and runtime: report them to [LinkML](https://github.com/linkml/linkml/security).
- A compromised runner, upstream action or agent harness: this is a baseline, not a sandbox. Report a finding in one anyway, with scope and reproduction.
- Whether the knowledge bundle is *true*. The gate proves who vouched, not what they read. [AI_COVENANT.md](AI_COVENANT.md) sets the human-accountability rules.
