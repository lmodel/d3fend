import re
from pathlib import Path

import yaml
from rdflib import Graph, Namespace, RDF, OWL, URIRef


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "src" / "d3fend" / "schema" / "d3fend.yaml"
TTL_PATHS = [
    ROOT / "src" / "d3fend" / "schema" / "d3fend.ttl",
    ROOT / "src" / "d3fend" / "schema" / "d3fend-protege.ttl",
]

D3F = Namespace("http://d3fend.mitre.org/ontologies/d3fend.owl#")
_VALUE_LOCAL_RE = re.compile(r"^n[0-9a-f]{8,}b\d+$")


def _local_name(uri) -> str:
    value = str(uri)
    if "#" in value:
        return value.rsplit("#", 1)[1]
    return value.rsplit("/", 1)[-1]


def _load_schema() -> dict:
    return yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))


def _load_merged_graph() -> Graph:
    graph = Graph()
    for ttl_path in TTL_PATHS:
        graph.parse(ttl_path)
    return graph


def _is_d3f_uri(uri) -> bool:
    return isinstance(uri, URIRef) and str(uri).startswith(str(D3F))


def _is_VALUE_d3f_uri(uri) -> bool:
    if not _is_d3f_uri(uri):
        return False
    return _VALUE_LOCAL_RE.fullmatch(_local_name(uri)) is not None


def test_schema_license_matches_ontology_metadata():
    schema = _load_schema()
    graph = _load_merged_graph()

    ontology = next(graph.subjects(RDF.type, OWL.Ontology))
    assert schema["license"] == str(graph.value(ontology, Namespace("http://purl.org/dc/terms/").license))


def test_all_d3f_classes_from_both_ttls_are_emitted():
    schema = _load_schema()
    graph = _load_merged_graph()

    schema_class_uris = {
        spec["class_uri"].split(":", 1)[1]
        for spec in schema.get("classes", {}).values()
        if isinstance(spec, dict) and isinstance(spec.get("class_uri"), str) and spec["class_uri"].startswith("d3f:")
    }
    ttl_classes = {
        _local_name(subject)
        for subject in graph.subjects(RDF.type, OWL.Class)
        if _is_d3f_uri(subject) and not _is_VALUE_d3f_uri(subject)
    }

    missing = sorted(ttl_classes - schema_class_uris)
    assert not missing, missing


def test_all_native_d3f_properties_are_emitted_as_slots():
    schema = _load_schema()
    graph = _load_merged_graph()

    schema_slot_uris = {
        spec["slot_uri"].split(":", 1)[1]
        for spec in schema.get("slots", {}).values()
        if isinstance(spec, dict) and isinstance(spec.get("slot_uri"), str) and spec["slot_uri"].startswith("d3f:")
    }
    ttl_properties = {
        _local_name(subject)
        for owl_type in (OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)
        for subject in graph.subjects(RDF.type, owl_type)
        if str(subject).startswith(str(D3F))
    }

    missing = sorted(ttl_properties - schema_slot_uris)
    assert not missing, missing


def test_schema_does_not_invent_native_slot_uris():
    schema = _load_schema()
    graph = _load_merged_graph()

    ttl_properties = {
        _local_name(subject)
        for owl_type in (OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)
        for subject in graph.subjects(RDF.type, owl_type)
        if str(subject).startswith(str(D3F))
    }

    invented = {}
    for slot_name, spec in schema.get("slots", {}).items():
        if not isinstance(spec, dict):
            continue
        slot_uri = spec.get("slot_uri")
        if isinstance(slot_uri, str) and slot_uri.startswith("d3f:"):
            local_name = slot_uri.split(":", 1)[1]
            if local_name not in ttl_properties:
                invented[slot_name] = slot_uri

    assert not invented, invented


def test_schema_includes_protege_only_class_marker():
    """Guard that regeneration reflects content unique to d3fend-protege.ttl."""
    schema = _load_schema()
    atomic_clock = schema.get("classes", {}).get("AtomicClock")
    assert isinstance(atomic_clock, dict)
    assert atomic_clock.get("class_uri") == "d3f:AtomicClock"


def test_schema_includes_mappings_artifact_enrichment():
    """Guard that defensive->offensive mappings are emitted into class mappings."""
    schema = _load_schema()
    token_binding = schema.get("classes", {}).get("TokenBinding")
    assert isinstance(token_binding, dict)
    related = token_binding.get("related_mappings") or []
    assert "attack:T1528" in related


def test_schema_has_mapping_aggregate_coverage():
    """Guard against silent mapping degradation in generated classes."""
    schema = _load_schema()
    classes = schema.get("classes", {})

    related_count = sum(
        1
        for class_spec in classes.values()
        if isinstance(class_spec, dict) and class_spec.get("related_mappings")
    )
    broad_count = sum(
        1
        for class_spec in classes.values()
        if isinstance(class_spec, dict) and class_spec.get("broad_mappings")
    )

    # Conservative floors based on current generated output to detect major regressions.
    assert related_count >= 100, related_count
    assert broad_count >= 100, broad_count