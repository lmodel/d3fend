#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["rdflib>=7", "pyyaml>=6"]
# ///
"""Turn MITRE's D3FEND Turtle file into this project's schema module and catalogue.

D3FEND's distribution holds one graph: its classes, its individuals and, as a direct
triple between them, each relation a class restriction states. So a D3FEND term reads as
a record with typed relations. This script writes the two files that say so:

- ``--schema`` writes ``src/d3fend/schema/d3fend_entries.yaml``: one slot for each OWL
  property, keeping its IRI, and one class for each kind of entry.
- ``--catalogue`` writes ``src/d3fend/data/d3fend-1.6.0.yaml``: one record for each class
  and each individual, keeping its IRI as a CURIE under ``d3f:``.

The script makes no judgement of its own beyond the table of kinds below, and it stops on
a predicate it does not know, so a new edition cannot lose a fact silently.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

import rdflib
import yaml
from rdflib import OWL, RDF, RDFS, BNode, Graph, Literal, Namespace, URIRef
from rdflib.collection import Collection

# Keep each literal's lexical form as MITRE writes it.
rdflib.NORMALIZE_LITERALS = False

ROOT = Path(__file__).resolve().parent.parent
TURTLE = ROOT / "upstream" / "d3fend.ttl"
SCHEMA_OUT = ROOT / "src" / "d3fend" / "schema" / "d3fend_entries.yaml"
CATALOGUE_OUT = ROOT / "src" / "d3fend" / "data" / "d3fend-1.6.0.yaml"

D3F = Namespace("http://d3fend.mitre.org/ontologies/d3fend.owl#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
DCTERMS = Namespace("http://purl.org/dc/terms/")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
ONTOLOGY = URIRef("http://d3fend.mitre.org/ontologies/d3fend.owl")

# Each kind of entry, its parent kind, and the D3FEND classes whose branch it holds. An
# entry takes the first kind in this order whose branch it sits under, so the deeper kind
# comes before its parent, and D3FEND's own branches come before the external ones. That
# order settles the entries with two parents: an ATT&CK Enterprise technique is an
# offensive technique first, and a tactic of any framework an offensive tactic first.
KINDS = (
    ("D3fendDefensiveTactic", "D3fendGoal", ("DefensiveTactic",)),
    ("D3fendOffensiveTactic", "D3fendGoal", ("OffensiveTactic",)),
    ("D3fendGoal", "D3fendEntry", ("Goal",)),
    ("D3fendDefensiveTechnique", "D3fendTechnique", ("DefensiveTechnique",)),
    ("D3fendOffensiveTechnique", "D3fendTechnique", ("OffensiveTechnique",)),
    ("D3fendAnalyticTechnique", "D3fendTechnique", ("AnalyticTechnique",)),
    ("D3fendTechnique", "D3fendEntry", ("Technique",)),
    ("D3fendWeakness", "D3fendEntry", ("Weakness",)),
    ("D3fendDigitalArtifact", "D3fendArtifact", ("DigitalArtifact",)),
    ("D3fendArtifact", "D3fendEntry", ("Artifact",)),
    ("D3fendEvent", "D3fendEntry", ("Event",)),
    ("D3fendAgent", "D3fendEntry", ("Agent",)),
    ("D3fendTechniqueReference", "D3fendEntry", ("TechniqueReference",)),
    ("D3fendNistControl", "D3fendExternalControl", ("NISTControl",)),
    ("D3fendCciControl", "D3fendExternalControl", ("CCIControl",)),
    ("D3fendExternalControl", "D3fendEntry", ("ExternalControl",)),
    ("D3fendControlCatalog", "D3fendEntry", ("ControlCatalog",)),
    (
        "D3fendAttackMitigation",
        "D3fendThreatModelThing",
        ("ATTACKEnterpriseMitigation",),
    ),
    (
        "D3fendAttackDataSource",
        "D3fendThreatModelThing",
        ("ATTACKEnterpriseDataSource",),
    ),
    (
        "D3fendThreatModelTechnique",
        "D3fendThreatModelThing",
        (
            "ATTACKMobileTechnique",
            "ATTACKICSTechnique",
            "ATLASTechnique",
            "SPARTATechnique",
        ),
    ),
    ("D3fendThreatModelThing", "D3fendEntry", ("ExternalThreatModelThing",)),
    ("D3fendThing", "D3fendEntry", ()),
)

# What the class says about itself, in this project's words. The class_uri is D3FEND's
# class where one means the same; D3fendThing and D3fendThreatModelTechnique group several
# of D3FEND's branches, so they keep this project's namespace.
KIND_TEXT = {
    "D3fendGoal": ("Goal", "d3f:Goal", "An aim that a tactic or a technique serves."),
    "D3fendDefensiveTactic": (
        "Defensive Tactic",
        "d3f:DefensiveTactic",
        "One of D3FEND's seven defensive aims, such as Detect or Harden, which a defensive "
        "technique enables.",
    ),
    "D3fendOffensiveTactic": (
        "Offensive Tactic",
        "d3f:OffensiveTactic",
        "A tactic of an adversary, from the ATT&CK, ATLAS or SPARTA framework, which an "
        "offensive technique enables.",
    ),
    "D3fendTechnique": (
        "Technique",
        "d3f:Technique",
        "A way of doing something in or to a computer system. Its narrower kinds say whose "
        "way it is.",
    ),
    "D3fendDefensiveTechnique": (
        "Defensive Technique",
        "d3f:DefensiveTechnique",
        "A countermeasure: a method that makes a system harder to attack, related to the "
        "artifacts it acts on and to the tactic it enables.",
    ),
    "D3fendOffensiveTechnique": (
        "Offensive Technique",
        "d3f:OffensiveTechnique",
        "A way an adversary acts, drawn from ATT&CK Enterprise, related to the artifacts it "
        "touches and to the tactic it serves.",
    ),
    "D3fendAnalyticTechnique": (
        "Analytic Technique",
        "d3f:AnalyticTechnique",
        "A mathematical method a defensive technique can use to find patterns in data, such "
        "as a form of machine learning or a statistical measure.",
    ),
    "D3fendWeakness": (
        "Weakness",
        "d3f:Weakness",
        "A condition in a system component that can contribute to a vulnerability. Nearly "
        "all of these entries name a CWE entry.",
    ),
    "D3fendArtifact": (
        "Artifact",
        "d3f:Artifact",
        "A man-made thing that techniques act on. Those that are not digital, such as "
        "a physical lock, stay here.",
    ),
    "D3fendDigitalArtifact": (
        "Digital Artifact",
        "d3f:DigitalArtifact",
        "An artifact that carries information for a digital system, such as a file, a process "
        "or a network packet: the common ground where offensive and defensive techniques meet.",
    ),
    "D3fendEvent": (
        "Event",
        "d3f:Event",
        "Something that happens in a system over a finite span of time, with the artifacts "
        "that take part in it.",
    ),
    "D3fendAgent": (
        "Agent",
        "d3f:Agent",
        "Something capable of intentional action, such as a person, an organization or an "
        "attacker.",
    ),
    "D3fendTechniqueReference": (
        "Technique Reference",
        "d3f:TechniqueReference",
        "A source behind a knowledge base article, such as a patent or a paper. rdf_type says "
        "which of D3FEND's reference types it is, since all of them hold the same fields.",
    ),
    "D3fendExternalControl": (
        "External Control",
        "d3f:ExternalControl",
        "A control another catalogue defines, which D3FEND relates to its techniques.",
    ),
    "D3fendNistControl": (
        "NIST Control",
        "d3f:NISTControl",
        "A control or control enhancement of a revision of NIST SP 800-53.",
    ),
    "D3fendCciControl": (
        "CCI Control",
        "d3f:CCIControl",
        "An item of the Control Correlation Identifier list that DISA publishes.",
    ),
    "D3fendControlCatalog": (
        "Control Catalog",
        "d3f:ControlCatalog",
        "A published list of controls, one edition of which holds D3FEND's control entries as "
        "members.",
    ),
    "D3fendThreatModelThing": (
        "Threat Model Thing",
        "d3f:ExternalThreatModelThing",
        "A term from a threat model outside D3FEND, such as ATT&CK, ATLAS, SPARTA or CAPEC, "
        "with no narrower kind here.",
    ),
    "D3fendThreatModelTechnique": (
        "Threat Model Technique",
        None,
        "A technique of ATT&CK Mobile, ATT&CK ICS, ATLAS or SPARTA. D3FEND places these under "
        "their frameworks and not under its own offensive technique.",
    ),
    "D3fendAttackMitigation": (
        "ATT&CK Enterprise Mitigation",
        "d3f:ATTACKEnterpriseMitigation",
        "A mitigation of ATT&CK Enterprise, which D3FEND relates to its defensive techniques.",
    ),
    "D3fendAttackDataSource": (
        "ATT&CK Enterprise Data Source",
        "d3f:ATTACKEnterpriseDataSource",
        "A data source of ATT&CK Enterprise, which D3FEND relates to its digital artifacts.",
    ),
    "D3fendThing": (
        "Thing",
        None,
        "An entry with no narrower kind here: a root of D3FEND's tree, or a term such as a "
        "plan, a step, a group, a time or a condition.",
    ),
}

# Mappings read at the target: each is held to a released copy under tests/neighbours/.
# D3FEND names the terms of these catalogues by their identifiers, so the kinds that hold
# one catalogue's terms are close to its class, and those that hold several are related.
KIND_MAPPINGS = {
    "D3fendWeakness": {"close_mappings": ["cwe:CweWeakness"]},
    "D3fendOffensiveTechnique": {"close_mappings": ["attack:AttackTechnique"]},
    "D3fendThreatModelTechnique": {"related_mappings": ["attack:AttackTechnique"]},
    "D3fendOffensiveTactic": {"related_mappings": ["attack:AttackTactic"]},
    "D3fendAttackMitigation": {"close_mappings": ["attack:AttackMitigation"]},
    "D3fendAttackDataSource": {"close_mappings": ["attack:AttackDataSource"]},
    "D3fendNistControl": {
        "related_mappings": [
            "nist_sp_800_53:Control",
            "nist_sp_800_53:ControlEnhancement",
        ]
    },
}
# The identifiers name the same things in another form: CWE-79 is 79 there, and an ATT&CK
# id is one external reference among several. So each is related. The two terms outside
# the lmodel family are the ones the ontology itself names as rdfs:isDefinedBy.
SLOT_MAPPINGS = {
    "attack_id": {"related_mappings": ["stix:external_id"]},
    "cwe_id": {"related_mappings": ["cwe:CWE_ID"]},
    "capec_id": {"related_mappings": ["capec:CAPEC_ID"]},
    "related": {"close_mappings": ["skos:related"]},
    "definition": {"close_mappings": ["IAO:0000115"]},
}
MAPPING_PREFIXES = {
    "IAO": "http://purl.obolibrary.org/obo/IAO_",
    "attack": "https://w3id.org/lmodel/attack/",
    "capec": "https://w3id.org/lmodel/capec/",
    "cwe": "https://w3id.org/lmodel/cwe/",
    "nist_sp_800_53": "https://w3id.org/lmodel/nist-sp-800-53/",
    "stix": "https://w3id.org/lmodel/stix/",
}

# What a class restriction with a literal filler states and this edition obeys, for the
# entries that are individuals. Those the edition does not obey stay out: tests/
# test_coverage.py lists them with the count that keeps them out.
KIND_RULES = {
    "D3fendTechniqueReference": ("has_link", "kb_reference_title"),
    "D3fendCciControl": ("published",),
    "D3fendControlCatalog": ("version",),
}

# A property's slot name, where the plain conversion would clash. d3f:date would shadow
# LinkML's date type in the generated Python, and d3f:label and d3f:pref-label share a
# name with the RDFS and SKOS terms of the same word.
EXTERNAL_SLOTS = {
    RDFS.label: "label",
    RDFS.comment: "comment",
    RDFS.seeAlso: "see_also",
    RDFS.isDefinedBy: "is_defined_by",
    SKOS.prefLabel: "skos_pref_label",
    SKOS.altLabel: "alt_label",
    SKOS.example: "example",
    OWL.deprecated: "deprecated",
    OWL.disjointWith: "disjoint_with",
}
RENAMED = {"date": "date_value", "label": "d3f_label"}

# The IRI each external slot is written under, for the schema's slot_uri.
EXTERNAL_CURIES = {
    RDFS.label: "rdfs:label",
    RDFS.comment: "rdfs:comment",
    RDFS.seeAlso: "rdfs:seeAlso",
    RDFS.isDefinedBy: "rdfs:isDefinedBy",
    SKOS.prefLabel: "skos:prefLabel",
    SKOS.altLabel: "skos:altLabel",
    SKOS.example: "skos:example",
    OWL.deprecated: "owl:deprecated",
    OWL.disjointWith: "owl:disjointWith",
}

# The ontology's own header: predicates of the ontology node, under the catalogue's keys.
HEADER = {
    OWL.versionInfo: "version_info",
    OWL.versionIRI: "version_iri",
    D3F["release-date"]: "release_date",
    RDFS.comment: "comment",
    DCTERMS.title: "ontology_title",
    DCTERMS.description: "ontology_description",
    DCTERMS.license: "ontology_license",
}

# A property with no use in this edition whose name says it only groups others. Each stays
# a slot, so its children keep their parent, but no class lists it.
GROUPING = re.compile(r"(-property|-annotation)$")

# The predicates of an entry that are not one of the ontology's declared properties, and
# which the script handles apart from them.
STRUCTURAL = {RDF.type, RDFS.subClassOf}


def local(iri) -> str:
    """The part of an IRI after the namespace."""
    text = str(iri)
    return text.split("#", 1)[1] if "#" in text else text.rsplit("/", 1)[-1]


def curie(iri) -> str:
    """The CURIE of a D3FEND term."""
    return f"d3f:{local(iri)}"


def is_d3f(iri) -> bool:
    """Whether a node is a term of D3FEND's own namespace."""
    return isinstance(iri, URIRef) and str(iri).startswith(str(D3F))


def load(path: Path = TURTLE) -> Graph:
    """Parse the Turtle file."""
    graph = Graph()
    graph.parse(path, format="turtle")
    return graph


def declared_properties(graph: Graph) -> dict[URIRef, str]:
    """Each property the ontology declares, with its OWL type."""
    found: dict[URIRef, str] = {}
    for owl_type, name in (
        (OWL.ObjectProperty, "object"),
        (OWL.DatatypeProperty, "data"),
        (OWL.AnnotationProperty, "annotation"),
    ):
        for prop in graph.subjects(RDF.type, owl_type):
            if isinstance(prop, URIRef):
                found[prop] = name
    return found


def slot_name(prop: URIRef) -> str:
    """The slot that carries a property."""
    if prop in EXTERNAL_SLOTS:
        return EXTERNAL_SLOTS[prop]
    name = local(prop)
    return RENAMED.get(name, name.replace("-", "_").lower())


def entry_subjects(graph: Graph) -> set[URIRef]:
    """Every D3FEND class and individual, each of which becomes one record."""
    found = set()
    for owl_type in (OWL.Class, OWL.NamedIndividual):
        found |= {s for s in graph.subjects(RDF.type, owl_type) if is_d3f(s)}
    return found


def parents(graph: Graph, entry: URIRef) -> set[URIRef]:
    """What an entry sits under: its named superclasses and its named types."""
    found = {o for o in graph.objects(entry, RDFS.subClassOf) if is_d3f(o)}
    found |= {o for o in graph.objects(entry, RDF.type) if is_d3f(o)}
    found.discard(entry)
    return found


def branches(graph: Graph, entries: set[URIRef]) -> dict[URIRef, set[URIRef]]:
    """Each entry with itself and everything above it."""
    direct = {entry: parents(graph, entry) for entry in entries}
    closed: dict[URIRef, set[URIRef]] = {}

    def above(entry: URIRef, trail: frozenset) -> set[URIRef]:
        if entry in closed:
            return closed[entry]
        found = {entry}
        for parent in direct.get(entry, ()):
            if parent not in trail:
                found |= above(parent, trail | {parent})
        closed[entry] = found
        return found

    for entry in sorted(entries):
        above(entry, frozenset({entry}))
    return closed


def kind_of(branch: set[URIRef]) -> str:
    """The first kind whose branch an entry sits under."""
    for kind, _parent, roots in KINDS:
        if any(D3F[root] in branch for root in roots):
            return kind
    return "D3fendThing"


def kind_tree() -> dict[str, set[str]]:
    """Each kind with its descendants and itself."""
    below: dict[str, set[str]] = defaultdict(set)
    for kind, parent, _roots in KINDS:
        below[kind].add(kind)
        below["D3fendEntry"].add(kind)
        walk = parent
        while walk != "D3fendEntry":
            below[walk].add(kind)
            walk = next(p for k, p, _ in KINDS if k == walk)
    return below


def scalar(node):
    """A literal as the value a record holds: integers and booleans stay typed."""
    if isinstance(node, Literal):
        if node.datatype == XSD.integer:
            return int(str(node))
        if node.datatype == XSD.boolean:
            return str(node).lower() == "true"
        return str(node)
    return str(node)


def restrictions(graph: Graph, entry: URIRef):
    """Each named relation a class restriction states, as (property, target)."""
    for node in graph.objects(entry, RDFS.subClassOf):
        if not isinstance(node, BNode):
            continue
        prop = graph.value(node, OWL.onProperty)
        target = graph.value(node, OWL.someValuesFrom)
        if prop is not None and is_d3f(target):
            yield prop, target


def relation_targets(
    graph: Graph, entries: set[URIRef], props: dict[URIRef, str]
) -> dict:
    """For each entry, each relation slot's targets: direct triples and restrictions."""
    found: dict[URIRef, dict[URIRef, set[URIRef]]] = defaultdict(
        lambda: defaultdict(set)
    )
    for entry in entries:
        for pred, obj in graph.predicate_objects(entry):
            if pred in props and props[pred] == "object" and is_d3f(obj):
                found[entry][pred].add(obj)
        for prop, target in restrictions(graph, entry):
            found[entry][prop].add(target)
    return found


def multivalued_props(
    graph: Graph, entries: set[URIRef], props: dict[URIRef, str]
) -> set[URIRef]:
    """The literal-valued properties an entry of this edition holds more than once."""
    counts: dict[URIRef, dict[URIRef, set]] = defaultdict(lambda: defaultdict(set))
    for entry in entries:
        for pred, obj in graph.predicate_objects(entry):
            if pred in props or pred in EXTERNAL_SLOTS:
                counts[pred][entry].add(str(obj))
    return {
        pred
        for pred, per_entry in counts.items()
        if any(len(v) > 1 for v in per_entry.values())
        or _objects_are_terms(graph, pred)
    }


def catalogue(graph: Graph) -> dict:
    """The whole graph as one catalogue document."""
    props = declared_properties(graph)
    entries = entry_subjects(graph)
    tree = branches(graph, entries)
    relations = relation_targets(graph, entries, props)
    many = multivalued_props(graph, entries, props)
    records = []
    for entry in sorted(entries, key=str):
        records.append(
            _record(graph, entry, tree[entry], relations[entry], props, many)
        )
    document = {"ontology_iri": str(ONTOLOGY)}
    for pred, key in HEADER.items():
        value = graph.value(ONTOLOGY, pred)
        if value is not None:
            document[key] = [str(value)] if key == "comment" else str(value)
    document["disjoint_groups"] = _disjoint_groups(graph)
    document["entries"] = records
    return document


def _owl_kind(graph: Graph, entry: URIRef) -> str:
    is_class = (entry, RDF.type, OWL.Class) in graph
    is_individual = (entry, RDF.type, OWL.NamedIndividual) in graph
    if is_class and is_individual:
        return "class_and_individual"
    return "class" if is_class else "individual"


def _record(graph, entry, branch, relations, props, many) -> dict:
    record: dict = {
        "id": curie(entry),
        "type": kind_of(branch),
        "owl_kind": _owl_kind(graph, entry),
    }
    types = sorted(curie(o) for o in graph.objects(entry, RDF.type) if is_d3f(o))
    if types:
        record["rdf_type"] = types
    supers = sorted(
        curie(o) for o in graph.objects(entry, RDFS.subClassOf) if is_d3f(o)
    )
    if supers:
        record["subclass_of"] = supers
    literals: dict[str, list] = defaultdict(list)
    for pred, obj in graph.predicate_objects(entry):
        if pred in STRUCTURAL or (
            pred in props and props[pred] == "object" and is_d3f(obj)
        ):
            continue
        if pred == OWL.disjointWith:
            literals["disjoint_with"].append(curie(obj))
            continue
        if pred not in props and pred not in EXTERNAL_SLOTS:
            raise SystemExit(f"{local(entry)}: no slot for the predicate {pred}")
        value = curie(obj) if _objects_are_terms(graph, pred) else scalar(obj)
        literals[slot_name(pred)].append((pred, value))
    for name in sorted(literals):
        pairs = literals[name]
        if name == "disjoint_with":
            record[name] = sorted(pairs)
            continue
        pred = pairs[0][0]
        values = sorted({v for _p, v in pairs}, key=str)
        record[name] = values if pred in many else values[0]
    for prop in sorted(relations, key=slot_name):
        record[slot_name(prop)] = sorted(curie(t) for t in relations[prop])
    return record


def _disjoint_groups(graph: Graph) -> list[dict]:
    groups = []
    for node in graph.subjects(RDF.type, OWL.AllDisjointClasses):
        members = Collection(graph, graph.value(node, OWL.members))
        groups.append({"members": sorted(curie(m) for m in members)})
    return sorted(groups, key=lambda g: g["members"])


class _Dumper(yaml.SafeDumper):
    """Writes block lists indented, and text with line breaks as a block."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def _text(dumper, value):
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


_Dumper.add_representer(str, _text)


def dump(document, handle) -> None:
    """Write YAML in the project's style."""
    yaml.dump(
        document, handle, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=100
    )


def _text_values(graph: Graph, subject, pred) -> list[str]:
    return sorted(str(o) for o in graph.objects(subject, pred))


def _xsd_range(graph: Graph, prop: URIRef) -> dict:
    """The slot's range for a literal-valued property, from what the ontology declares."""
    declared = graph.value(prop, RDFS.range)
    if isinstance(declared, BNode):
        union = graph.value(declared, OWL.unionOf)
        if union is not None:
            return {
                "any_of": [
                    {"range": local(member)} for member in Collection(graph, union)
                ],
            }
        if graph.value(declared, OWL.onDatatype) == XSD.integer:
            facets = {}
            for item in Collection(graph, graph.value(declared, OWL.withRestrictions)):
                for facet, limit in graph.predicate_objects(item):
                    key = {
                        "minInclusive": "minimum_value",
                        "maxInclusive": "maximum_value",
                    }
                    facets[key[local(facet)]] = int(str(limit))
            return {"range": "integer", **facets}
    if declared == XSD.dateTime:
        return {"range": "d3fend_date_time"}
    if declared == XSD.anyURI:
        return {"range": "d3fend_uri"}
    literals = {o for o in graph.objects(None, prop) if isinstance(o, Literal)}
    if literals and all(o.datatype == XSD.integer for o in literals):
        return {"range": "integer"}
    return {"range": "string"}


def _is_used(graph: Graph, prop: URIRef, entries: set[URIRef]) -> bool:
    if any(s in entries for s in graph.subjects(prop, None)):
        return True
    return any(
        graph.value(node, OWL.onProperty) == prop
        for node in graph.subjects(OWL.onProperty, prop)
        if any(s in entries for s in graph.subjects(RDFS.subClassOf, node))
    )


def _kind_of_class(tree, iri: URIRef) -> str | None:
    """The kind whose branch holds every descendant of a D3FEND class, if one does."""
    if iri not in tree:
        return None
    kind = kind_of(tree[iri])
    below = kind_tree()[kind]
    held = {kind_of(branch) for branch in tree.values() if iri in branch}
    return kind if held <= below and kind != "D3fendThing" else None


def _property_slot(
    graph, prop, owl_type, tree, relations, entries, many
) -> tuple[dict, str | None]:
    """One property's slot, and the kind that holds it when not the base class."""
    name = slot_name(prop)
    slot: dict = {}
    labels = _text_values(graph, prop, RDFS.label)
    slot["title"] = labels[0] if labels else local(prop)
    definitions = _text_values(graph, prop, D3F.definition)
    if definitions:
        slot["description"] = " ".join(definitions[0].split())
    else:
        word = labels[0] if labels else local(prop)
        slot["description"] = (
            f'D3FEND\'s property "{word}", which the ontology does not define.'
        )
    slot["slot_uri"] = EXTERNAL_CURIES.get(prop, curie(prop))

    supers = sorted(
        (
            slot_name(o)
            for o in graph.objects(prop, RDFS.subPropertyOf)
            if _known_prop(graph, o)
        ),
    )
    if supers:
        slot["is_a"] = supers[0]
        if supers[1:]:
            slot["mixins"] = supers[1:]
    partner = _partner(graph, prop)
    if partner is not None:
        slot["inverse"] = slot_name(partner)
    if (prop, RDF.type, OWL.TransitiveProperty) in graph:
        slot["transitive"] = True
    if (prop, RDF.type, OWL.SymmetricProperty) in graph:
        slot["symmetric"] = True

    domain = graph.value(prop, RDFS.domain)
    target = graph.value(prop, RDFS.range)
    partner = _partner(graph, prop)
    if partner is not None:
        domain = domain if domain is not None else graph.value(partner, RDFS.range)
        target = target if target is not None else graph.value(partner, RDFS.domain)
    holder = None
    comments = []
    subjects = {s for s in graph.subjects(prop, None) if s in entries}
    subjects |= {s for s, per in relations.items() if prop in per}
    if domain is not None:
        kind = _kind_of_class(tree, domain)
        if kind is None:
            comments.append(
                f"D3FEND declares the domain {curie(domain)}, which no one kind here holds "
                "whole, so every kind may hold this slot."
            )
        elif all(kind_of(tree[s]) in kind_tree()[kind] for s in subjects):
            holder = kind
        else:
            comments.append(
                f"D3FEND declares the domain {curie(domain)}, but this edition also uses the "
                "property outside it, so every kind may hold this slot."
            )
    if owl_type == "object" or _objects_are_terms(graph, prop):
        range_kind = "D3fendEntry"
        if is_d3f(target):
            kind = _kind_of_class(tree, target)
            targets = {t for per in relations.values() for t in per.get(prop, ())}
            if kind and all(
                kind_of(tree[t]) in kind_tree()[kind] for t in targets if t in tree
            ):
                range_kind = kind
            else:
                comments.append(
                    f"D3FEND declares the range {curie(target)}, which no one kind here holds "
                    "whole, so a target may be any entry."
                )
        slot["range"] = range_kind
        slot["multivalued"] = True
        slot["inlined"] = False
    else:
        slot.update(_xsd_range(graph, prop))
        if prop in many:
            slot["multivalued"] = True

    aliases = sorted(
        {str(o) for p in (SKOS.altLabel, D3F.synonym) for o in graph.objects(prop, p)}
    )
    if aliases:
        slot["aliases"] = aliases
    seen = _text_values(graph, prop, RDFS.seeAlso)
    links = [v for v in seen if v.startswith(("http://", "https://"))]
    if links:
        slot["see_also"] = links
    comments.extend(
        " ".join(v.split()) for v in _text_values(graph, prop, RDFS.comment)
    )
    if comments:
        slot["comments"] = comments
    if name in SLOT_MAPPINGS:
        slot.update(SLOT_MAPPINGS[name])
    annotations = {"owl_property": owl_type}
    outside = sorted(
        str(o)
        for o in graph.objects(prop, RDFS.subPropertyOf)
        if not _known_prop(graph, o)
    )
    if outside:
        annotations["owl_subproperty_of"] = " ".join(outside)
    if domain is not None:
        annotations["owl_domain"] = curie(domain)
    if is_d3f(target):
        annotations["owl_range"] = curie(target)
    defined_by = _text_values(graph, prop, RDFS.isDefinedBy)
    if defined_by:
        annotations["is_defined_by"] = " ".join(defined_by)
    preferred = _text_values(graph, prop, D3F["pref-label"])
    if preferred:
        annotations["pref_label"] = preferred[0]
    chain = graph.value(prop, OWL.propertyChainAxiom)
    if chain is not None:
        steps = " ".join(curie(step) for step in Collection(graph, chain))
        annotations["property_chain"] = steps
    if (prop, RDF.type, OWL.FunctionalProperty) in graph:
        annotations["owl_functional"] = "true"
    slot["annotations"] = annotations
    if not _is_used(graph, prop, entries) and GROUPING.search(local(prop)):
        slot["abstract"] = True
    return {name: slot}, holder


def _partner(graph: Graph, prop: URIRef):
    """The property the ontology declares inverse to this one, on either side."""
    return graph.value(prop, OWL.inverseOf) or graph.value(None, OWL.inverseOf, prop)


def _known_prop(graph: Graph, node) -> bool:
    return is_d3f(node) or node in EXTERNAL_SLOTS


def _objects_are_terms(graph: Graph, prop: URIRef) -> bool:
    """Whether an annotation property's values all name D3FEND terms."""
    objects = list(graph.objects(None, prop))
    return bool(objects) and all(is_d3f(o) for o in objects)


def schema_module(graph: Graph) -> dict:
    """The module holding every property's slot and every kind's class."""
    props = declared_properties(graph)
    entries = entry_subjects(graph)
    tree = branches(graph, entries)
    relations = relation_targets(graph, entries, props)
    many = multivalued_props(graph, entries, props)

    slots: dict = {}
    on_base: list[str] = []
    on_kind: dict[str, list[str]] = defaultdict(list)
    for prop in sorted((p for p in props if _known_prop(graph, p)), key=slot_name):
        slot, holder = _property_slot(
            graph, prop, props[prop], tree, relations, entries, many
        )
        slots.update(slot)
        name = slot_name(prop)
        if slot[name].get("abstract"):
            continue
        (on_kind[holder] if holder else on_base).append(name)
    for pred in (RDFS.comment, OWL.deprecated, OWL.disjointWith):
        name = slot_name(pred)
        slots[name] = _structural_slot(pred)
        on_base.append(name)
    # LinkML's loader compares a slot's range with its inverse's stated domain and warns
    # on any difference, so each slot of an inverse pair states the other's range.
    for name, slot in slots.items():
        if "inverse" in slot:
            slots[slot["inverse"]]["domain"] = slot["range"]
    slots = dict(sorted(slots.items()))

    classes = {
        "D3fendEntry": {
            "title": "Entry",
            "abstract": True,
            "description": (
                "One term of the D3FEND graph, a class or an individual, as a record that holds "
                "its text and its relations to other terms."
            ),
            "comments": [
                "The ontology declares a domain for few of its properties, so this class lists "
                "every property that has none, and any kind of entry may hold it. A narrower "
                "kind lists a property only where the ontology declares that domain and this "
                "edition obeys it."
            ],
            "slots": [
                "id",
                "type",
                "owl_kind",
                "rdf_type",
                "subclass_of",
                *sorted(set(on_base)),
            ],
        }
    }
    for kind, parent, roots in KINDS:
        title, class_uri, text = KIND_TEXT[kind]
        body: dict = {"title": title, "is_a": parent, "description": text}
        if class_uri:
            body["class_uri"] = class_uri
        if roots:
            body["annotations"] = {
                "d3fend_branches": " ".join(f"d3f:{r}" for r in roots)
            }
        if on_kind.get(kind):
            body["slots"] = sorted(on_kind[kind])
        body.update(KIND_MAPPINGS.get(kind, {}))
        if kind in KIND_RULES:
            body["rules"] = [
                {
                    "title": f"An individual holds {' and '.join(KIND_RULES[kind])}",
                    "description": (
                        f"A class restriction on {roots[0]} states that its instances hold "
                        f"{' and '.join(KIND_RULES[kind])}, and every individual of this "
                        "edition does."
                    ),
                    "preconditions": {
                        "slot_conditions": {
                            "owl_kind": {
                                "required": True,
                                "equals_string": "individual",
                            }
                        }
                    },
                    "postconditions": {
                        "slot_conditions": {
                            name: {"required": True} for name in KIND_RULES[kind]
                        }
                    },
                }
            ]
        classes[kind] = body
    classes = {
        name: classes[name]
        for name in ["D3fendEntry", *[k for k, _p, _r in reversed(KINDS)]]
    }
    classes["D3fendDisjointGroup"] = {
        "title": "Disjoint Group",
        "description": "A set of D3FEND classes of which no two share an instance.",
        "annotations": {"owl_type": "owl:AllDisjointClasses"},
        "attributes": {
            "members": {
                "description": "The classes in the group.",
                "slot_uri": "owl:members",
                "required": True,
                "multivalued": True,
                "range": "D3fendEntry",
                "inlined": False,
            }
        },
    }
    return {
        "id": "https://w3id.org/lmodel/d3fend/d3fend_entries",
        "name": "d3fend_entries",
        "title": "D3FEND entries",
        "description": (
            "Every property of the D3FEND ontology as a slot under its own IRI, and the kinds "
            "of entry the D3FEND graph holds. scripts/d3fend_to_linkml.py writes this file "
            "from upstream/d3fend.ttl, so edit the script, not the file."
        ),
        "version": str(graph.value(ONTOLOGY, OWL.versionInfo)),
        "source": "https://d3fend.mitre.org/ontologies/d3fend/1.6.0/d3fend.ttl",
        "license": "Apache-2.0",
        "see_also": ["https://lmodel.github.io/d3fend", "https://d3fend.mitre.org/"],
        "annotations": {
            "upstream_copyright": "Copyright 2022 The MITRE Corporation",
            "upstream_terms": "https://d3fend.mitre.org/tou",
        },
        "prefixes": dict(
            sorted(
                {
                    "d3f": str(D3F),
                    "d3fend": "https://w3id.org/lmodel/d3fend/",
                    "linkml": "https://w3id.org/linkml/",
                    "owl": str(OWL),
                    "rdf": str(RDF),
                    "rdfs": str(RDFS),
                    "skos": str(SKOS),
                    "xsd": str(XSD),
                    **MAPPING_PREFIXES,
                }.items()
            )
        ),
        "default_prefix": "d3fend",
        "default_range": "string",
        "imports": ["linkml:types", "./d3fend_core"],
        "classes": classes,
        "slots": {
            "id": {
                "title": "ID",
                "description": "The term's IRI, as a CURIE under d3f:.",
                "identifier": True,
                "range": "uriorcurie",
                "pattern": r"^d3f:\S+$",
            },
            "type": {
                "title": "Type",
                "description": "The kind of entry, as the name of its class in this schema.",
                "designates_type": True,
                "required": True,
                "range": "string",
            },
            "owl_kind": {
                "title": "OWL Kind",
                "description": (
                    "Whether the ontology declares the term a class, an individual or both."
                ),
                "range": "D3fendOwlKind",
            },
            "rdf_type": {
                "title": "RDF Type",
                "description": (
                    "The D3FEND classes the ontology states the term is an instance of."
                ),
                "slot_uri": "rdf:type",
                "range": "D3fendEntry",
                "multivalued": True,
                "inlined": False,
            },
            "subclass_of": {
                "title": "Subclass Of",
                "description": "The D3FEND classes directly above the term.",
                "slot_uri": "rdfs:subClassOf",
                "range": "D3fendEntry",
                "multivalued": True,
                "inlined": False,
            },
            **slots,
        },
    }


def _structural_slot(pred) -> dict:
    texts = {
        RDFS.comment: ("Comment", "A note on the term, in MITRE's words."),
        OWL.deprecated: (
            "Deprecated",
            "Whether the ontology marks the term as deprecated.",
        ),
        OWL.disjointWith: (
            "Disjoint With",
            "A D3FEND class that shares no instance with this one.",
        ),
    }
    title, text = texts[pred]
    slot = {"title": title, "description": text, "slot_uri": EXTERNAL_CURIES[pred]}
    if pred == OWL.deprecated:
        slot["range"] = "boolean"
    elif pred == OWL.disjointWith:
        slot.update(range="D3fendEntry", multivalued=True, inlined=False)
    else:
        slot.update(range="string", multivalued=True)
    return slot


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--turtle", type=Path, default=TURTLE)
    parser.add_argument("--schema", type=Path, nargs="?", const=SCHEMA_OUT)
    parser.add_argument("--catalogue", type=Path, nargs="?", const=CATALOGUE_OUT)
    args = parser.parse_args(argv)
    if not (args.schema or args.catalogue):
        parser.error("name --schema, --catalogue or both")
    graph = load(args.turtle)
    if args.schema:
        args.schema.parent.mkdir(parents=True, exist_ok=True)
        with args.schema.open("w", encoding="utf-8") as handle:
            handle.write(SCHEMA_HEADER)
            dump(schema_module(graph), handle)
    if args.catalogue:
        args.catalogue.parent.mkdir(parents=True, exist_ok=True)
        with args.catalogue.open("w", encoding="utf-8") as handle:
            handle.write(CATALOGUE_HEADER)
            dump(catalogue(graph), handle)
    return 0


SCHEMA_HEADER = """\
---
# Written by scripts/d3fend_to_linkml.py from upstream/d3fend.ttl. Edit the script, not
# this file. A slot's title and description are D3FEND's own label and definition.
#
# Copyright 2022 The MITRE Corporation. NOTICE reproduces the licence these copies carry.
"""

CATALOGUE_HEADER = """\
---
# MITRE D3FEND 1.6.0, as one record per class and individual. scripts/d3fend_to_linkml.py
# writes this file from upstream/d3fend.ttl, so regenerate it, never edit it.
#
# Copyright 2022 The MITRE Corporation. MITRE D3FEND and the MITRE D3FEND logo are
# trademarks of The MITRE Corporation.
#
# LICENSE
# The MITRE Corporation (MITRE) hereby grants you a non-exclusive, royalty-free license to
# use D3FEND for research, development, and commercial purposes. Any copy you make for such
# purposes is authorized provided that you reproduce MITRE's copyright designation and this
# license in any such copy.
#
# upstream/TERMS.txt gives the Terms of Use whole, with their disclaimers. D3FEND carries
# text of MITRE ATT&CK, MITRE ATLAS, Aerospace SPARTA and CWE, each under its own terms,
# and abstracts of the sources it cites. NOTICE says which.
"""


if __name__ == "__main__":
    sys.exit(main())
