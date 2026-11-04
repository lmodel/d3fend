"""Checks each mapping against its source, and the prefixes it needs.

Each mapping names its target by a CURIE whose prefix the schema binds. A target in an
lmodel neighbour's namespace is held to that neighbour's released copy under
tests/neighbours/. The two others are the terms the ontology itself names as rdfs:isDefinedBy.
The schema is the one home for mappings: no SSSOM file sits beside it.
"""

from functools import cache
from pathlib import Path

import pytest
import yaml
from linkml_runtime import SchemaView

from tests import conversion
from tests.conversion import CONVERTER as C

ROOT = Path(__file__).parent.parent
SCHEMA_DIR = ROOT / "src" / "d3fend" / "schema"
NEIGHBOURS = ROOT / "tests" / "neighbours"
MAPPING_KEYS = (
    "exact_mappings",
    "close_mappings",
    "narrow_mappings",
    "broad_mappings",
    "related_mappings",
    "mappings",
)

# The targets outside the lmodel family, by the property that names them.
STATED_BY_THE_ONTOLOGY = {
    "skos:related": C.D3F.related,
    "IAO:0000115": C.D3F.definition,
}


def _mappings(node):
    if isinstance(node, dict):
        for key, value in node.items():
            if key in MAPPING_KEYS:
                yield from value if isinstance(value, list) else [value]
            else:
                yield from _mappings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _mappings(item)


def _meanings(node):
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "meaning":
                yield value
            else:
                yield from _meanings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _meanings(item)


MODULES = {
    path.name: yaml.safe_load(path.read_text(encoding="utf-8"))
    for path in sorted(SCHEMA_DIR.glob("*.yaml"))
}
TARGETS = sorted(
    {(name, curie) for name, doc in MODULES.items() for curie in _mappings(doc)}
)


@cache
def neighbour_iris():
    """Each IRI the neighbours' released copies declare."""
    found = set()
    for path in NEIGHBOURS.glob("*.yaml"):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        prefixes = doc.get("prefixes") or {}
        default = doc.get("default_prefix")

        def expand(curie):
            prefix, _, local = curie.partition(":")
            return prefixes[prefix] + local if prefix in prefixes else curie

        def add(kind, uri_key):
            for name, element in (doc.get(kind) or {}).items():
                element = element or {}
                found.add(expand(element.get(uri_key) or f"{default}:{name}"))

        add("classes", "class_uri")
        add("slots", "slot_uri")
        add("enums", "enum_uri")
        for cls in (doc.get("classes") or {}).values():
            for name, slot in ((cls or {}).get("attributes") or {}).items():
                found.add(expand((slot or {}).get("slot_uri") or f"{default}:{name}"))
    return found


def expand(module, curie):
    prefix, _, local = curie.partition(":")
    return MODULES[module]["prefixes"][prefix] + local


def test_mappings_exist():
    """The parametrized tests below pass on an empty list, so this one does not."""
    assert len(TARGETS) >= 12, len(TARGETS)


@pytest.mark.parametrize(("module", "curie"), TARGETS)
def test_each_target_has_a_bound_prefix(module, curie):
    """Every mapping names its target by a CURIE whose prefix its module binds, so a
    projection of the adapt copy raises no warning."""
    prefix, separator, _ = curie.partition(":")
    assert separator and prefix in MODULES[module]["prefixes"], curie


@pytest.mark.parametrize(("module", "curie"), TARGETS)
def test_each_target_is_read_at_its_source(module, curie):
    """Every target is a term a released neighbour copy declares, or a term the ontology
    itself names."""
    if curie in STATED_BY_THE_ONTOLOGY:
        stated = conversion.graph().objects(
            STATED_BY_THE_ONTOLOGY[curie], C.RDFS.isDefinedBy
        )
        assert expand(module, curie) in {str(o) for o in stated}, curie
    else:
        assert expand(module, curie) in neighbour_iris(), curie


def test_every_enum_meaning_is_owls():
    """The one list's meanings are OWL's own two terms."""
    for name, doc in MODULES.items():
        assert set(_meanings(doc)) <= {"owl:Class", "owl:NamedIndividual"}, name


def test_a_mapped_identifier_is_held_by_the_kind_it_names():
    """The ids that cross to another catalogue sit where the mapping says: every weakness
    but the root holds a CWE id, and no entry of another kind does."""
    entries = conversion.catalogue()["entries"]
    with_cwe = [e for e in entries if "cwe_id" in e]
    assert len(with_cwe) == 943
    assert {e["type"] for e in with_cwe} == {"D3fendWeakness"}
    assert all(e["cwe_id"].startswith("CWE-") for e in with_cwe)
    with_capec = [e for e in entries if "capec_id" in e]
    assert [e["capec_id"] for e in with_capec] == ["CAPEC-553"]
    with_attack = {e["type"] for e in entries if "attack_id" in e}
    assert with_attack == {
        "D3fendOffensiveTechnique",
        "D3fendOffensiveTactic",
        "D3fendThreatModelTechnique",
    }


def test_no_sssom_file_sits_beside_the_schema():
    """The schema is the one home for mappings, each held by a test here."""
    assert not list(ROOT.glob("src/**/*.sssom.*"))


def test_the_module_imports_are_the_contract():
    """d3fend_core imports only the LinkML types, d3fend_entries only it, and the umbrella
    takes both and holds only the tree root."""
    assert MODULES["d3fend_core.yaml"]["imports"] == ["linkml:types"]
    assert MODULES["d3fend_entries.yaml"]["imports"] == [
        "linkml:types",
        "./d3fend_core",
    ]
    assert MODULES["d3fend.yaml"]["imports"] == [
        "linkml:types",
        "./d3fend_core",
        "./d3fend_entries",
    ]
    assert set(MODULES["d3fend.yaml"]["classes"]) == {"D3fendCatalog"}
    assert (
        MODULES["d3fend_core.yaml"]["id"]
        == "https://w3id.org/lmodel/d3fend/d3fend_core"
    )


def test_each_module_loads_on_its_own():
    """Each module can be taken alone, with no import cycle."""
    for name in MODULES:
        view = SchemaView(str(SCHEMA_DIR / name))
        assert view.all_types(), name
