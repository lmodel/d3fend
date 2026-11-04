"""Checks the JSON Schema this project commits, as a user of it would read it.

project/jsonschema/d3fend.schema.json is what a consumer without LinkML validates with.
It is read here under the draft it declares, and held to the generator's settings in
.linkml/generators.yaml.
"""

import json
from functools import cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

ROOT = Path(__file__).parent.parent
COMMITTED = ROOT / "project" / "jsonschema" / "d3fend.schema.json"
SCHEMA = ROOT / "src" / "d3fend" / "schema" / "d3fend.yaml"
DATA = ROOT / "tests" / "data"


@cache
def schema():
    return json.loads(COMMITTED.read_text(encoding="utf-8"))


def validator():
    return jsonschema.validators.validator_for(schema())(schema())


def _load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_the_schema_is_valid_under_the_draft_it_declares():
    jsonschema.validators.validator_for(schema()).check_schema(schema())


def test_the_committed_file_is_the_generators_output():
    """A schema edit without `just gen-project` fails here."""
    settings = yaml.safe_load((ROOT / ".linkml" / "generators.yaml").read_text())
    args = settings["generator_args"]["jsonschema"]
    generated = JsonSchemaGenerator(str(SCHEMA), **args).serialize()
    assert json.loads(generated) == schema()


def test_the_top_of_the_schema_is_the_catalogue():
    """The file's root takes a whole catalogue, and refuses any other key."""
    assert schema()["title"] == "d3fend"
    assert schema()["additionalProperties"] is False
    assert set(schema()["properties"]) == {
        "ontology_iri",
        "version_info",
        "version_iri",
        "release_date",
        "comment",
        "ontology_title",
        "ontology_description",
        "ontology_license",
        "disjoint_groups",
        "entries",
    }
    assert set(schema()["required"]) == {"ontology_iri", "version_info", "entries"}


def test_an_entry_is_one_of_the_concrete_kinds():
    """The list of entries offers each concrete kind and not the abstract base, which
    no record could pass."""
    offered = schema()["$defs"]["D3fendCatalog"]["properties"]["entries"]["items"][
        "anyOf"
    ]
    names = {branch["$ref"].rsplit("/", 1)[1] for branch in offered}
    assert "D3fendEntry" not in names
    assert {"D3fendDefensiveTechnique", "D3fendDigitalArtifact", "D3fendThing"} <= names
    assert len(names) == 22


def test_every_class_is_closed():
    """A key the ontology does not declare is refused everywhere."""
    for name, definition in schema()["$defs"].items():
        if definition.get("type") == "object":
            assert definition["additionalProperties"] is False, name


@pytest.mark.parametrize("name", ["D3fendCatalog-small"])
def test_a_catalogue_validates_against_the_file(name):
    assert not list(validator().iter_errors(_load(DATA / "valid" / f"{name}.yaml")))


def test_a_rule_reaches_the_file():
    """A rule in the schema is a condition in the committed file: a reference with no
    link is refused there too, inside a catalogue."""
    catalogue = _load(DATA / "valid" / "D3fendCatalog-small.yaml")
    catalogue["entries"][0] = {
        "id": "d3f:Reference-X",
        "type": "D3fendTechniqueReference",
        "owl_kind": "individual",
        "kb_reference_title": "A title",
    }
    assert list(validator().iter_errors(catalogue))


def test_a_kinds_own_slot_reaches_the_file():
    """A slot that only one kind holds is refused on another, inside a catalogue."""
    catalogue = _load(DATA / "valid" / "D3fendCatalog-small.yaml")
    catalogue["entries"][1]["has_input"] = ["d3f:File"]
    assert list(validator().iter_errors(catalogue))
