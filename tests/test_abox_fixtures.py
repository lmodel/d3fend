"""ABox fixture tests mapped against generated LinkML schema.

These tests treat Turtle files as fixture input and verify that referenced
instance types and predicates exist as classes/slots in d3fend.yaml.
"""

from pathlib import Path

import pytest
import yaml
from rdflib import RDF, Graph, Namespace, URIRef

ABOX_VALID_DIR = Path(__file__).parent / "data" / "abox" / "valid"
ABOX_INVALID_DIR = Path(__file__).parent / "data" / "abox" / "invalid"
SCHEMA_PATH = Path(__file__).resolve().parents[1] / "src" / "d3fend" / "schema" / "d3fend.yaml"
D3F = Namespace("http://d3fend.mitre.org/ontologies/d3fend.owl#")

VALID_ABOX_FILES = sorted(ABOX_VALID_DIR.glob("*.ttl"))
INVALID_ABOX_UNKNOWN_SYMBOLS = ABOX_INVALID_DIR / "unknown-schema-symbols-001.ttl"


def _local_name(uri: URIRef) -> str:
    value = str(uri)
    if "#" in value:
        return value.rsplit("#", 1)[1]
    return value.rsplit("/", 1)[-1]


def _load_schema_symbols() -> tuple[set[str], set[str]]:
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))

    class_uris = {
        spec["class_uri"].split(":", 1)[1]
        for spec in schema.get("classes", {}).values()
        if isinstance(spec, dict)
        and isinstance(spec.get("class_uri"), str)
        and spec["class_uri"].startswith("d3f:")
    }
    slot_uris = {
        spec["slot_uri"].split(":", 1)[1]
        for spec in schema.get("slots", {}).values()
        if isinstance(spec, dict)
        and isinstance(spec.get("slot_uri"), str)
        and spec["slot_uri"].startswith("d3f:")
    }
    return class_uris, slot_uris


@pytest.mark.parametrize("filepath", VALID_ABOX_FILES)
def test_abox_fixtures_reference_declared_schema_symbols(filepath: Path):
    class_uris, slot_uris = _load_schema_symbols()

    graph = Graph()
    graph.parse(filepath, format="turtle")

    referenced_class_uris = {
        _local_name(obj)
        for _, _, obj in graph.triples((None, RDF.type, None))
        if isinstance(obj, URIRef) and str(obj).startswith(str(D3F))
    }
    referenced_slot_uris = {
        _local_name(pred)
        for _, pred, _ in graph
        if pred != RDF.type and str(pred).startswith(str(D3F))
    }

    assert referenced_class_uris, f"No d3f rdf:type assertions found in {filepath.name}"
    missing_classes = sorted(referenced_class_uris - class_uris)
    assert not missing_classes, f"Unknown d3f class_uri(s) in {filepath.name}: {missing_classes}"

    assert referenced_slot_uris, f"No d3f predicate assertions found in {filepath.name}"
    missing_slots = sorted(referenced_slot_uris - slot_uris)
    assert not missing_slots, f"Unknown d3f slot_uri(s) in {filepath.name}: {missing_slots}"


def test_abox_invalid_fixture_detects_unknown_schema_symbols():
    class_uris, slot_uris = _load_schema_symbols()

    graph = Graph()
    graph.parse(INVALID_ABOX_UNKNOWN_SYMBOLS, format="turtle")

    referenced_class_uris = {
        _local_name(obj)
        for _, _, obj in graph.triples((None, RDF.type, None))
        if isinstance(obj, URIRef) and str(obj).startswith(str(D3F))
    }
    referenced_slot_uris = {
        _local_name(pred)
        for _, pred, _ in graph
        if pred != RDF.type and str(pred).startswith(str(D3F))
    }

    missing_classes = sorted(referenced_class_uris - class_uris)
    missing_slots = sorted(referenced_slot_uris - slot_uris)

    assert missing_classes, "Expected at least one unknown d3f class symbol"
    assert missing_slots, "Expected at least one unknown d3f slot symbol"
