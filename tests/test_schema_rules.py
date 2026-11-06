"""Checks that the adapt copy can sit beside LOKF and the neighbours' copies."""

import hashlib
import json
import keyword
from functools import cache
from pathlib import Path

import jsonschema
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

ROOT = Path(__file__).parent.parent

# What a host may import beside this schema's adapt copy: LOKF's schema, pinned by the
# sidecar, and the adapt copies other lmodel repositories release. Each neighbour is the
# schema asset of a release, downloaded and checked against the release's .sha256, and
# pinned here by that checksum.
SOURCE_DIR = ROOT / "src" / "d3fend" / "schema"
COPY = ROOT / ".lokf" / "schema" / "d3fend.yaml"
LOKF = ROOT / ".lokf" / "schema" / "lokf.yaml"
NEIGHBOURS = {
    # lmodel/slsa v0.10.0, schema-v0.10.0-slsa.yaml
    "slsa.yaml": "9eeb68decc918565886794fe4eb6e32e1fee0620688cc699961c227242a2f4c2",
    # lmodel/github-actions v0.5.0, schema-v0.5.0-github-actions.yaml
    "github-actions.yaml": "375794f7343936ae8c555e8c060c2790346661e7d81fa84d15a761fd5a329969",
    # lmodel/in-toto v0.3.0, schema-v0.3.0-in-toto.yaml
    "in-toto.yaml": "b1d15be557adfbcd538ab75ec9d43f558027d4bcbd150d72d370e83c9602f25b",
    # lmodel/oscal v0.1.2, schema-v0.1.2-oscal.yaml
    "oscal.yaml": "4eb56d7d1106463ed0a2255a29af14b8d619741acc29863d1e86eb3f8923c710",
    # lmodel/spdx v0.1.1, schema-v0.1.1-spdx.yaml
    "spdx.yaml": "3411cf5d19b1955f0362988c542984e4c817417c7b7b7892647aba1adf1ddd4a",
    # lmodel/stix v0.1.0, schema-v0.1.0-stix.yaml
    "stix.yaml": "3837d097c0cd48e0d2a98d118003c099d1290333f5b973aee85a7017bae344c9",
    # lmodel/attack v0.1.1, schema-v0.1.1-attack.yaml
    "attack.yaml": "c2e436b0d8ab0e60a8d6557b3ba32894e0b0d23b866f1e0c0d608a97e9f5f08e",
    # lmodel/uco v0.3.0, schema-v0.3.0-uco.yaml
    "uco.yaml": "78bc3a266fa463ba380da7290adcbdfb1b8e1b7cef1ceb992bf8b1bed9b7b758",
    # lmodel/cve v0.1.0, schema-v0.1.0-cve.yaml
    "cve.yaml": "33e6086a81ac8e4cdc1e6143598cfcc961cbc1864ad9268773da9e863c652a73",
    # lmodel/kev-catalog v0.1.0, schema-v0.1.0-kev-catalog.yaml
    "kev-catalog.yaml": "76bdff7d02cc34ac6a14314692e316b005649a34f442eaf54c2846b1dac5396c",
    # lmodel/nist-nvd v0.1.0, schema-v0.1.0-nist-nvd.yaml
    "nist-nvd.yaml": "69dc8a9b34cc6646cf44515c121c8924c4e07232a9699e31065fb8930ed8be40",
    # lmodel/cwe v0.1.0, schema-v0.1.0-cwe.yaml
    "cwe.yaml": "1b2bb4c1beb089f031adc8861572b98ddf0b42f0ed3c6e5c3bfbc0f767b032cd",
    # lmodel/capec v0.1.0, schema-v0.1.0-capec.yaml
    "capec.yaml": "613164c0520384919de7d353ff87debb4e82938cec861158d151b41edd506d46",
    # lmodel/nist-sp-800-53 v0.1.0, schema-v0.1.0-nist-sp-800-53.yaml
    "nist-sp-800-53.yaml": "d32a989b5b855281cb45d707bf59cf52b125f05a09c54930e2b4d45c174c0d99",
}
NEIGHBOUR_DIR = ROOT / "tests" / "neighbours"
ELEMENT_KINDS = ("classes", "enums", "types", "subsets")

# Keys the copy shares with a neighbour, each under another IRI, since D3FEND's properties
# are ordinary words. LinkML merges a composite's imports into one namespace, so a host
# importing such a neighbour beside this copy projects these keys under one IRI, until
# lokf's adapt can rename what a neighbour copy defines (lokf #169). A new overlap fails
# this test. No class, enum or type is shared, since each carries the D3fend prefix.
SHARED_WITH_NEIGHBOURS = {name: set() for name in NEIGHBOURS}
SHARED_WITH_NEIGHBOURS |= {
    "attack.yaml": {"comment", "confidence", "end", "modified", "published", "start"},
    "nist-nvd.yaml": {"comment", "deprecated", "published"},
    "oscal.yaml": {
        "addresses",
        "adds",
        "controls",
        "depends_on",
        "end",
        "entries",
        "identifier",
        "label",
        "maps",
        "published",
        "start",
        "text",
    },
    "slsa.yaml": {"produced_by"},
    "spdx.yaml": {"comment", "identifier"},
    "stix.yaml": {"comment", "confidence", "end", "modified", "published", "start"},
    "uco.yaml": {"comment", "confidence", "text"},
}

# The classes `just lokf-adapt` re-roots on Concept, and the ones a concept can name, which
# the README lists for the plugins' Known LOKF types setting.
ROOTS = {"D3fendEntry", "D3fendCatalog"}
CONCEPT_EXAMPLES = {
    "D3fendAgent": "D3fendAgent-organization",
    "D3fendAnalyticTechnique": "D3fendAnalyticTechnique-mean",
    "D3fendArtifact": "D3fendArtifact-physical-lock",
    "D3fendAttackDataSource": "D3fendAttackDataSource-user-account",
    "D3fendAttackMitigation": "D3fendAttackMitigation-active-directory",
    "D3fendCciControl": "D3fendCciControl-account-management",
    "D3fendControlCatalog": "D3fendControlCatalog-revision-5",
    "D3fendDefensiveTactic": "D3fendDefensiveTactic-harden",
    "D3fendDefensiveTechnique": "D3fendDefensiveTechnique-decoy-environment",
    "D3fendDigitalArtifact": "D3fendDigitalArtifact-file",
    "D3fendEvent": "D3fendEvent-file-event",
    "D3fendExternalControl": "D3fendExternalControl-root",
    "D3fendGoal": "D3fendGoal-classifying",
    "D3fendNistControl": "D3fendNistControl-account-management",
    "D3fendOffensiveTactic": "D3fendOffensiveTactic-credential-access",
    "D3fendOffensiveTechnique": "D3fendOffensiveTechnique-credential-dumping",
    "D3fendTechnique": "D3fendTechnique-cyber-technique",
    "D3fendTechniqueReference": "D3fendTechniqueReference-patent",
    "D3fendThing": "D3fendThing-step",
    "D3fendThreatModelTechnique": "D3fendThreatModelTechnique-atlas-search",
    "D3fendThreatModelThing": "D3fendThreatModelThing-capec",
    "D3fendWeakness": "D3fendWeakness-cross-site-scripting",
}

# What the copy drops for LOKF's id and type, and the keys it renames because LOKF has a
# slot of that name under another IRI. Each renamed key keeps its IRI.
DROPPED = {"id", "type", "rdf_type"}
RENAMED = {
    "created": "d3fend_created",
    "definition": "d3fend_definition",
    "description": "d3fend_description",
    "name": "d3fend_name",
    "title": "d3fend_title",
    "version": "d3fend_version",
}

MAPPING_KEYS = (
    "mappings",
    "exact_mappings",
    "close_mappings",
    "related_mappings",
    "narrow_mappings",
    "broad_mappings",
)


@cache
def _load(path):
    """A schema file, parsed once: the tests read the copy and the neighbours many times
    and change nothing in them."""
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _expander(doc):
    """A function that expands a CURIE by the prefixes a schema file binds."""
    prefixes = doc.get("prefixes") or {}

    def expand(curie):
        prefix, _, local = curie.partition(":")
        return prefixes[prefix] + local if prefix in prefixes else curie

    return expand


@cache
def _names(path):
    """Each kind of element a schema file declares, and every slot and attribute name
    with the IRI it expands to."""
    doc = _load(path)
    expand = _expander(doc)
    default = doc.get("default_prefix")
    elements = {kind: set(doc.get(kind) or {}) for kind in ELEMENT_KINDS}
    slots = {}
    owners = [doc.get("slots") or {}]
    owners += [
        (cls or {}).get("attributes") or {}
        for cls in (doc.get("classes") or {}).values()
    ]
    for owner in owners:
        for name, slot in owner.items():
            uri = (slot or {}).get("slot_uri") or f"{default}:{name}"
            slots.setdefault(name, set()).add(expand(uri))
    return elements, slots


def _terms(doc):
    """The IRI of every class, slot, attribute, enum and type a schema file declares, each
    its own URI or the default prefix and its name."""
    expand = _expander(doc)
    default = doc.get("default_prefix")
    terms = set()
    for kind, uri_key in (
        ("classes", "class_uri"),
        ("slots", "slot_uri"),
        ("enums", "enum_uri"),
        ("types", "uri"),
    ):
        for name, element in (doc.get(kind) or {}).items():
            terms.add(expand((element or {}).get(uri_key) or f"{default}:{name}"))
    for cls in (doc.get("classes") or {}).values():
        for name, slot in ((cls or {}).get("attributes") or {}).items():
            terms.add(expand((slot or {}).get("slot_uri") or f"{default}:{name}"))
    return terms


def _mappings(node):
    """Every mapping value anywhere in a parsed schema file."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in MAPPING_KEYS:
                yield from value if isinstance(value, list) else [value]
            else:
                yield from _mappings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _mappings(item)


def _source():
    """The three modules of the source, merged by element kind."""
    merged = {"classes": {}, "slots": {}, "prefixes": {}, "enums": {}, "types": {}}
    for path in sorted(SOURCE_DIR.glob("*.yaml")):
        doc = _load(path)
        for kind, elements in merged.items():
            elements.update(doc.get(kind) or {})
    return merged


def test_neighbours_are_the_released_assets():
    """Each neighbour copy is byte for byte the file pinned above."""
    assert {p.name for p in NEIGHBOUR_DIR.iterdir()} == set(NEIGHBOURS)
    for name, sha256 in NEIGHBOURS.items():
        digest = hashlib.sha256((NEIGHBOUR_DIR / name).read_bytes()).hexdigest()
        assert digest == sha256, name


def test_names_apart_from_lokf():
    """No class, enum, type or subset name of the copy is LOKF's, and a slot name the two
    share carries LOKF's IRI."""
    elements, slots = _names(COPY)
    their_elements, their_slots = _names(LOKF)
    for kind in ELEMENT_KINDS:
        assert not elements[kind] & their_elements[kind], kind
    for name in slots.keys() & their_slots.keys():
        assert slots[name] == their_slots[name], name


def test_names_apart_from_neighbours():
    """A class, enum, type or subset name is the copy's alone, and the only keys it shares
    with a neighbour are the listed ones."""
    elements, slots = _names(COPY)
    for name in NEIGHBOURS:
        their_elements, their_slots = _names(NEIGHBOUR_DIR / name)
        for kind in ELEMENT_KINDS:
            assert not elements[kind] & their_elements[kind], (name, kind)
        assert slots.keys() & their_slots.keys() == SHARED_WITH_NEIGHBOURS[name], name


def test_a_key_shared_with_a_neighbour_has_another_iri():
    """The comment on SHARED_WITH_NEIGHBOURS and the README say so. A key under the same
    IRI would mean the same thing, and would need no listing."""
    _, slots = _names(COPY)
    for name, shared in SHARED_WITH_NEIGHBOURS.items():
        _, their_slots = _names(NEIGHBOUR_DIR / name)
        for key in shared:
            assert slots[key] != their_slots[key], (name, key)


def test_the_copy_drops_and_renames_only_what_is_named():
    """The copy keeps each class and slot of the source, but for the keys it drops for
    LOKF's id and type and the keys it renames, and a renamed key keeps its IRI."""
    source, copy = _source(), _load(COPY)
    assert set(copy["classes"]) == set(source["classes"])
    expected = {RENAMED.get(name, name) for name in source["slots"]} - DROPPED
    assert set(copy["slots"]) == expected
    expand_source = _expander({"prefixes": source["prefixes"]})
    expand_copy = _expander(copy)
    for old, new in RENAMED.items():
        assert expand_copy(copy["slots"][new]["slot_uri"]) == expand_source(
            source["slots"][old]["slot_uri"]
        ), old


def test_the_catalogue_keeps_its_iri_as_the_concepts_id():
    """The catalogue's identifier is an attribute, which the copy turns into LOKF's id."""
    copy = _load(COPY)
    catalogue = copy["classes"]["D3fendCatalog"]
    assert "ontology_iri" not in catalogue["attributes"]
    assert "id" in catalogue["slots"]


def test_copy_roots_the_concept_classes():
    """The copy re-roots exactly the classes with an identifier on Concept, keeps every
    kind under the base, and imports nothing but the LinkML types and LOKF."""
    doc = _load(COPY)
    rooted = {
        name for name, cls in doc["classes"].items() if cls.get("is_a") == "Concept"
    }
    assert rooted == ROOTS
    assert doc["imports"] == ["linkml:types", "lokf"]
    assert not doc["classes"]["D3fendCatalog"].get("tree_root")
    kinds = set(doc["classes"]) - ROOTS - {"D3fendDisjointGroup"}
    assert kinds == set(CONCEPT_EXAMPLES)
    for name in kinds:
        walk = name
        while doc["classes"][walk].get("is_a") != "Concept":
            walk = doc["classes"][walk]["is_a"]
        assert walk == "D3fendEntry", name


def test_the_readme_lists_the_concept_types():
    """The README's Known LOKF types block names each class a concept may use."""
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for name in CONCEPT_EXAMPLES:
        assert name in readme, name


def test_mappings_use_a_bound_prefix():
    """Every mapping in the copy is a CURIE whose prefix the copy binds. A full address that
    no prefix covers makes every `lokf convert --schema` over the copy warn that it has no
    namespace."""
    doc = _load(COPY)
    prefixes = doc.get("prefixes") or {}
    mappings = list(_mappings(doc))
    assert mappings
    for mapping in mappings:
        prefix, sep, _ = mapping.partition(":")
        assert sep and prefix in prefixes, mapping


def test_no_mapping_points_at_spdx():
    """LOKF binds `spdx:` to SPDX 2, so a mapping to it would project wrongly. None does."""
    assert not [m for m in _mappings(_load(COPY)) if m.startswith("spdx:")]


def _page_names(source):
    """The name of each page gen-doc writes for an element of the source."""
    names = set(source["classes"]) | set(source["enums"]) | set(source["slots"])
    names |= {
        "".join(part.title() for part in name.split("_")) for name in source["types"]
    }
    for cls in source["classes"].values():
        names |= set(cls.get("attributes") or {})
    return names


def test_no_two_pages_differ_only_by_case():
    """gen-doc writes a page per element, and two names that differ only by case are one
    file on a case-insensitive disk. A slot is snake_case and every class, enum and type
    carries this schema's prefix, so no two can."""
    lowered = {}
    for name in _page_names(_source()):
        lowered.setdefault(name.lower(), set()).add(name)
    assert not {key: found for key, found in lowered.items() if len(found) > 1}


def test_no_page_collides_with_linkmls_types():
    """A slot named date would share a page with LinkML's Date type, so d3f:date is
    date_value, and this holds the rest."""
    linkml_types = {
        "Boolean", "Curie", "Date", "DateOrDatetime", "Datetime", "Decimal", "Double",
        "Float", "Integer", "Jsonpath", "Jsonpointer", "Ncname", "Nodeidentifier",
        "Objectidentifier", "Sparqlpath", "String", "Time", "Uri", "Uriorcurie",
        "boolean", "curie", "date", "datetime", "decimal", "double", "float", "integer",
        "ncname", "string", "time", "uri", "uriorcurie",
    }  # fmt: skip
    assert not _page_names(_source()) & linkml_types


def test_no_page_overwrites_the_index():
    """A slot named index would overwrite the docs site's index page."""
    assert "index" not in {name.lower() for name in _page_names(_source())}


def test_no_slot_is_a_python_keyword():
    """A slot named after a Python keyword breaks the generated dataclasses."""
    source = _source()
    slots = set(source["slots"])
    for cls in source["classes"].values():
        slots |= set(cls.get("attributes") or {})
    assert not {name for name in slots if keyword.iskeyword(name)}


@cache
def _concept_schema():
    """The JSON Schema of the adapt copy, as `lokf validate` reads it beside LOKF.
    Generating it takes seconds, so the two tests that read it share one."""
    generator = JsonSchemaGenerator(str(COPY), mergeimports=True)
    return json.loads(generator.serialize())["$defs"]


def test_a_concept_of_each_type_validates_against_the_copy():
    """Each class a concept may name admits a real record, in the copy's keys: LOKF's id,
    type, title and description stand beside what the record holds."""
    definitions = _concept_schema()
    for class_name, example in CONCEPT_EXAMPLES.items():
        data = _load(ROOT / "tests" / "data" / "valid" / f"{example}.yaml")
        concept = {
            RENAMED.get(key, key): value
            for key, value in data.items()
            if key not in DROPPED
        }
        concept.update(
            type=class_name,
            id=f"https://example.org/knowledge/{class_name}",
            title="A title",
            description="A description.",
        )
        schema = {"$ref": f"#/$defs/{class_name}", "$defs": definitions}
        validator = jsonschema.validators.validator_for(schema)(schema)
        errors = [e.message[:160] for e in validator.iter_errors(concept)]
        assert not errors, (class_name, errors)
        concept["analyses"] = ["d3f:File"]
        assert list(validator.iter_errors(concept)), (class_name, "is closed")


def test_the_reference_rule_survives_in_the_copy():
    """A rule of the source reaches the copy, so a host's reference holds its link."""
    definitions = _concept_schema()
    concept = {
        "type": "D3fendTechniqueReference",
        "id": "https://example.org/knowledge/a-paper",
        "title": "A paper",
        "description": "A paper.",
        "owl_kind": "individual",
        "kb_reference_title": "A paper",
    }
    schema = {"$ref": "#/$defs/D3fendTechniqueReference", "$defs": definitions}
    validator = jsonschema.validators.validator_for(schema)(schema)
    assert list(validator.iter_errors(concept))
    concept["has_link"] = "https://example.org/a-paper"
    assert not list(validator.iter_errors(concept))
