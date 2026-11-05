"""Walks the Turtle beside the schema and the catalogue, in both directions.

Every class, individual, property and restriction of upstream/d3fend.ttl is rendered as a
slot, a class or a value of a record, or is listed here with the reason it is not. The
schema renders nothing the Turtle does not state, beyond the few slots named here.
"""

import collections
from functools import cache

import pytest
from rdflib import OWL, RDF, RDFS, BNode, Literal, URIRef
from rdflib.collection import Collection

from tests import conversion
from tests.conversion import CONVERTER as C

D3F = C.D3F

# What a slot of the schema renders that no property of the ontology declares: the record's
# own keys, RDF's structure, and OWL's flags.
SLOTS_WITH_NO_DECLARED_PROPERTY = {
    "id",
    "type",
    "owl_kind",
    "rdf_type",
    "subclass_of",
    "comment",
    "deprecated",
    "disjoint_with",
}

# The three declared properties that only the ontology's header uses. They are rendered
# as attributes of the catalogue, not of a record.
HEADER_ONLY = {C.DCTERMS.title, C.DCTERMS.description, C.DCTERMS.license}

# Subjects that are neither a term, a property nor the ontology, and why they stay out.
# They are WebProtege's leftovers, each with a single literal and nothing naming them.
SUBJECTS_LEFT_OUT = {
    URIRef(
        "wptmp:entity#Reference%20-%20%20CAR-2016-04-004:%20Successful%20Local%20Account%20Login"
    ),
    URIRef(
        "wptmp:entity#Reference%20-%20DNS%20Whitelist%20(DNSWL)%20Email%20Authentication"
        "%20Method%20Extension"
    ),
}

# Each class restriction whose filler is a datatype, not a term, so that it names no target.
# The second value is the slot a rule in the schema holds to it for an individual, or None
# where this edition does not obey the restriction, with the count that shows why.
LITERAL_RESTRICTIONS = {
    # 14 of 42 mitigations hold a comment.
    ("ATTACKEnterpriseMitigation", "d3fend-comment"): None,
    # No CCI item holds a control name. The NIST controls do.
    ("CCIControl", "control-name"): None,
    ("CCIControl", "published"): "published",
    ("ControlCatalog", "version"): "version",
    # 271 of the 272 techniques below the root hold an id. ParticleRadiationHardening does not.
    ("DefensiveTechnique", "d3fend-id"): None,
    # No technique holds a date.
    ("DefensiveTechnique", "date"): None,
    # No person is an entry of this edition.
    ("Person", "name"): None,
    # None of the 23 process individuals holds any of these four.
    ("Process", "process-command-line-arguments"): None,
    ("Process", "process-environmental-variables"): None,
    ("Process", "process-identifier"): None,
    ("Process", "process-security-context"): None,
    ("TechniqueReference", "has-link"): "has_link",
    ("TechniqueReference", "kb-reference-title"): "kb_reference_title",
    # No entry is a registry key or value.
    ("WindowsRegistryKey", "windows-registry-key"): None,
    ("WindowsRegistryValue", "windows-registry-value"): None,
}

# What the graph states that names no term as a target, so a record cannot hold it. The
# upper limit on Procedure's start is the one owl:allValuesFrom of the edition, and the two
# events' parents are anonymous unions.
AXIOMS_LEFT_OUT = {
    ("Procedure", "allValuesFrom", "start", "Step"),
    ("DNSEvent", "unionOf", "TCPEvent", "UDPEvent"),
    ("RDPEvent", "unionOf", "TCPEvent", "UDPEvent"),
}

# Each predicate of a term's triples, and where it is rendered. test_every_predicate_lands
# reads this table with the declared properties, each rendered as the slot of its own name.
UNDECLARED_PREDICATES = {
    RDF.type: "rdf_type and owl_kind",
    RDFS.subClassOf: "subclass_of, and each relation slot for a restriction",
    RDFS.comment: "comment",
    OWL.deprecated: "deprecated",
    OWL.disjointWith: "disjoint_with",
}


def _slots():
    return conversion.module()["slots"]


@cache
def _terms():
    return C.entry_subjects(conversion.graph())


@cache
def _declared():
    return C.declared_properties(conversion.graph())


def _rendered_props():
    return [p for p in _declared() if p not in HEADER_ONLY]


def test_every_term_is_a_record_and_every_record_a_term():
    """The 4465 classes and the 954 individuals that are not classes are one record each."""
    graph = conversion.graph()
    classes = {s for s in graph.subjects(RDF.type, OWL.Class) if C.is_d3f(s)}
    individuals = {
        s for s in graph.subjects(RDF.type, OWL.NamedIndividual) if C.is_d3f(s)
    }
    assert (len(classes), len(individuals - classes)) == (4465, 954)
    records = {entry["id"] for entry in conversion.catalogue()["entries"]}
    assert records == {C.curie(term) for term in classes | individuals}


def test_each_record_says_how_the_ontology_declares_it():
    graph = conversion.graph()
    for entry in conversion.catalogue()["entries"]:
        iri = D3F[entry["id"].removeprefix("d3f:")]
        is_class = (iri, RDF.type, OWL.Class) in graph
        is_individual = (iri, RDF.type, OWL.NamedIndividual) in graph
        assert (
            entry["owl_kind"]
            == {
                (True, False): "class",
                (False, True): "individual",
                (True, True): "class_and_individual",
            }[(is_class, is_individual)]
        ), entry["id"]


def test_every_subject_of_the_graph_is_accounted_for():
    """Each named subject is a term, a property or the ontology, or is listed above."""
    graph = conversion.graph()
    named = {s for s in graph.subjects() if isinstance(s, URIRef)}
    known = _terms() | set(_declared()) | {C.ONTOLOGY}
    assert named - known == SUBJECTS_LEFT_OUT


def test_the_only_namespace_of_the_terms_is_d3fends():
    """A record's id says d3f: for every term, since every term is under D3FEND's IRI."""
    graph = conversion.graph()
    for owl_type in (OWL.Class, OWL.NamedIndividual):
        assert all(
            C.is_d3f(s)
            for s in graph.subjects(RDF.type, owl_type)
            if isinstance(s, URIRef)
        )


def test_every_predicate_lands():
    """Each predicate of a term's triples is rendered somewhere, so a new one fails here.
    The converter also stops on one it does not know."""
    graph = conversion.graph()
    used = {p for term in _terms() for p in graph.predicates(term)}
    assert used - set(_declared()) - set(UNDECLARED_PREDICATES) == set()


def test_every_declared_property_is_a_slot_under_its_own_iri():
    """All 295 properties are rendered, each once, and only the header's three as
    attributes."""
    declared = _declared()
    assert len(declared) == 295
    assert len(_rendered_props()) == 292
    by_uri = {}
    for name, slot in _slots().items():
        if "slot_uri" in slot:
            by_uri[slot["slot_uri"]] = name
    for prop in _rendered_props():
        curie = C.EXTERNAL_CURIES.get(prop, C.curie(prop))
        assert by_uri.get(curie) == C.slot_name(prop), prop
    module = conversion.module()
    header = module["slots"].keys() & {"ontology_title", "ontology_description"}
    assert not header


def test_nothing_is_a_slot_the_ontology_does_not_declare():
    """Each slot renders a declared property, or is one of the few listed above."""
    rendered = {C.slot_name(p) for p in _rendered_props()}
    assert set(_slots()) - rendered == SLOTS_WITH_NO_DECLARED_PROPERTY


def test_the_property_tree_is_the_ontologys():
    """A slot's is_a and mixins are its property's superproperties. Those outside the
    schema, such as owl:versionInfo, are kept in an annotation."""
    graph = conversion.graph()
    for prop in _rendered_props():
        slot = _slots()[C.slot_name(prop)]
        stated = {
            C.slot_name(o)
            for o in graph.objects(prop, RDFS.subPropertyOf)
            if C._known_prop(graph, o)
        }
        held = {slot["is_a"]} if "is_a" in slot else set()
        assert held | set(slot.get("mixins", ())) == stated, prop
        outside = {
            str(o)
            for o in graph.objects(prop, RDFS.subPropertyOf)
            if not C._known_prop(graph, o)
        }
        kept = slot["annotations"].get("owl_subproperty_of", "").split()
        assert set(kept) == outside, prop


def test_each_inverse_is_the_ontologys():
    """A slot's inverse is the property declared inverse to it, from either side. The
    ontology declares 45 pairs."""
    graph = conversion.graph()
    pairs = {
        (C.slot_name(a), C.slot_name(b))
        for a, b in graph.subject_objects(OWL.inverseOf)
    }
    assert len(pairs) == 45
    for one, other in pairs:
        assert _slots()[one]["inverse"] == other, one
        assert _slots()[other]["inverse"] == one, other
    held = {name for name, slot in _slots().items() if "inverse" in slot}
    assert held == {name for pair in pairs for name in pair}


@pytest.mark.parametrize(
    ("owl_type", "key"),
    [(OWL.TransitiveProperty, "transitive"), (OWL.SymmetricProperty, "symmetric")],
)
def test_each_logical_flag_is_the_ontologys(owl_type, key):
    graph = conversion.graph()
    stated = {C.slot_name(p) for p in graph.subjects(RDF.type, owl_type)}
    assert stated
    assert {name for name, slot in _slots().items() if slot.get(key)} == stated


def test_functional_properties_are_noted():
    graph = conversion.graph()
    stated = {C.slot_name(p) for p in graph.subjects(RDF.type, OWL.FunctionalProperty)}
    assert len(stated) == 4
    held = {
        n for n, s in _slots().items() if s.get("annotations", {}).get("owl_functional")
    }
    assert held == stated


def test_declared_domains_and_ranges_are_kept():
    """Each declared domain and term range stands in an annotation, or came from the
    inverse's declaration, whichever the slot took."""
    graph = conversion.graph()
    for prop in _rendered_props():
        annotations = _slots()[C.slot_name(prop)]["annotations"]
        for predicate, key in ((RDFS.domain, "owl_domain"), (RDFS.range, "owl_range")):
            stated = graph.value(prop, predicate)
            if C.is_d3f(stated):
                assert annotations[key] == C.curie(stated), prop


def test_a_slots_words_are_the_ontologys():
    """A slot's title and description are the property's own label and definition, with
    its white space made even, and a property with no definition says so."""
    graph = conversion.graph()
    for prop in _rendered_props():
        slot = _slots()[C.slot_name(prop)]
        labels = {str(o) for o in graph.objects(prop, RDFS.label)}
        assert slot["title"] in (labels or {C.local(prop)}), prop
        definitions = {
            " ".join(str(o).split()) for o in graph.objects(prop, D3F.definition)
        }
        if definitions:
            assert slot["description"] in definitions, prop
        else:
            assert "does not define" in slot["description"], prop


def test_a_property_with_a_datatype_range_keeps_it():
    """The bounds and the union the ontology declares reach the slots."""
    assert _slots()["risk_impact"]["minimum_value"] == 1
    assert _slots()["risk_impact"]["maximum_value"] == 5
    assert _slots()["risk_likelihood"]["minimum_value"] == 1
    assert _slots()["risk_likelihood"]["maximum_value"] == 5
    assert _slots()["version"]["any_of"] == [{"range": "integer"}, {"range": "string"}]
    assert _slots()["published"]["range"] == "d3fend_date_time"
    assert _slots()["has_link"]["range"] == "d3fend_uri"


def test_every_named_restriction_lands_in_its_record():
    """The 1954 restrictions are the domain: 1939 name a term, and every one of those is
    a value of its record's slot, whether or not the Turtle also states the direct triple."""
    graph = conversion.graph()
    entries = conversion.entries_by_id()
    found = 0
    for term in _terms():
        for prop, target in C.restrictions(graph, term):
            values = entries[C.curie(term)][C.slot_name(prop)]
            assert C.curie(target) in values, (term, prop, target)
            found += 1
    assert found == 1939


def test_every_other_restriction_is_listed():
    """What is not a named target is listed above with its reason: nothing else is left."""
    graph = conversion.graph()
    literal = set()
    other = set()
    for term in _terms():
        for node in graph.objects(term, RDFS.subClassOf):
            if not isinstance(node, BNode):
                continue
            prop = graph.value(node, OWL.onProperty)
            some = graph.value(node, OWL.someValuesFrom)
            every = graph.value(node, OWL.allValuesFrom)
            union = graph.value(node, OWL.unionOf)
            if union is not None:
                members = sorted(C.local(m) for m in Collection(graph, union))
                other.add((C.local(term), "unionOf", *members))
            elif every is not None:
                other.add(
                    (C.local(term), "allValuesFrom", C.local(prop), C.local(every))
                )
            elif not C.is_d3f(some):
                literal.add((C.local(term), C.local(prop)))
    assert literal == set(LITERAL_RESTRICTIONS)
    assert other == AXIOMS_LEFT_OUT


@cache
def _tree():
    """Each term with everything above it, computed once for the parametrized tests."""
    return C.branches(conversion.graph(), _terms())


def _individuals_below(class_name):
    graph = conversion.graph()
    return [
        term
        for term, branch in _tree().items()
        if D3F[class_name] in branch
        and term != D3F[class_name]
        and (term, RDF.type, OWL.NamedIndividual) in graph
    ]


@pytest.mark.parametrize(
    ("class_name", "local", "slot"),
    [(c, p, s) for (c, p), s in LITERAL_RESTRICTIONS.items()],
)
def test_a_literal_restriction_is_a_rule_only_where_the_edition_obeys_it(
    class_name, local, slot
):
    """A rule in the schema states a restriction only where each individual holds the
    property. A restriction the edition does not obey stays out of the schema."""
    graph = conversion.graph()
    below = _individuals_below(class_name)
    holds = [term for term in below if (term, D3F[local], None) in graph]
    if slot:
        assert below
        assert len(holds) == len(below), (class_name, local)
        kind = C.kind_of(_tree()[D3F[class_name]])
        assert slot in C.KIND_RULES[kind]
    else:
        assert len(holds) < len(below) or not below, (class_name, local)


def _held(class_name, local):
    """How many individuals below a class hold a property, out of how many there are."""
    graph = conversion.graph()
    below = _individuals_below(class_name)
    return sum((term, D3F[local], None) in graph for term in below), len(below)


@pytest.mark.parametrize(
    ("class_name", "local", "numbers"),
    [
        ("ATTACKEnterpriseMitigation", "d3fend-comment", (14, 42)),
        ("CCIControl", "control-name", (0, 299)),
        ("DefensiveTechnique", "d3fend-id", (271, 272)),
        ("DefensiveTechnique", "date", (0, 272)),
        ("Process", "process-identifier", (0, 23)),
    ],
)
def test_the_numbers_that_keep_a_restriction_out(class_name, local, numbers):
    """The numbers the comments above and docs/about.md give."""
    assert _held(class_name, local) == numbers


def test_a_narrow_slot_sits_on_its_kind_and_a_wide_one_on_the_base():
    """The two examples docs/about.md gives: has_input is on the event alone, since D3FEND
    states that domain and the edition obeys it. attack_id stays on the base, since the
    edition goes beyond its stated domain, and a comment says so."""
    classes = conversion.module()["classes"]
    assert "has_input" in classes["D3fendEvent"]["slots"]
    assert "has_input" not in classes["D3fendEntry"]["slots"]
    assert "attack_id" in classes["D3fendEntry"]["slots"]
    assert "outside" in _slots()["attack_id"]["comments"][0]


def test_each_rule_in_the_schema_is_one_listed_above():
    listed = {s for s in LITERAL_RESTRICTIONS.values() if s}
    assert listed == {slot for slots in C.KIND_RULES.values() for slot in slots}


def test_the_disjoint_axioms_land():
    """Each owl:AllDisjointClasses is a group of the catalogue, and each owl:disjointWith
    is a value of its record's slot."""
    graph = conversion.graph()
    groups = {
        tuple(
            sorted(
                C.curie(m) for m in Collection(graph, graph.value(node, OWL.members))
            )
        )
        for node in graph.subjects(RDF.type, OWL.AllDisjointClasses)
    }
    held = {
        tuple(group["members"]) for group in conversion.catalogue()["disjoint_groups"]
    }
    assert held == groups
    assert len(groups) == 6
    entries = conversion.entries_by_id()
    pairs = list(graph.subject_objects(OWL.disjointWith))
    assert len(pairs) == 3
    for one, other in pairs:
        assert C.curie(other) in entries[C.curie(one)]["disjoint_with"]


def test_a_single_valued_slot_holds_one_value_in_this_edition():
    """The ontology bounds few properties, so a literal slot is single-valued where no term
    of this edition holds two. A term that held two would fail here and in the schema."""
    graph = conversion.graph()
    counts = collections.defaultdict(collections.Counter)
    for term in _terms():
        for predicate, obj in graph.predicate_objects(term):
            if predicate in _declared():
                counts[predicate][(term, str(obj))] += 1
    for predicate, seen in counts.items():
        per_term = collections.Counter(term for term, _ in seen)
        slot = _slots()[C.slot_name(predicate)]
        if max(per_term.values()) > 1:
            assert slot.get("multivalued"), predicate


def test_no_record_loses_a_language_tag():
    """A record's text carries no language tag, and no term's text has one to lose. The
    tags D3FEND does write, all English, sit on property labels, which become titles."""
    graph = conversion.graph()
    tagged = [
        obj.language
        for term in _terms()
        for obj in graph.objects(term)
        if isinstance(obj, Literal) and obj.language
    ]
    assert not tagged
    labels = [
        obj.language
        for prop in _declared()
        for obj in graph.objects(prop)
        if isinstance(obj, Literal) and obj.language
    ]
    assert labels and set(labels) == {"en"}


def test_a_kind_keeps_the_branch_it_names():
    """A class_uri is the D3FEND class at the root of the kind's branch, and that class
    exists in the Turtle. The two kinds that group several branches keep this schema's IRI."""
    graph = conversion.graph()
    classes = conversion.module()["classes"]
    for kind, _parent, roots in C.KINDS:
        for root in roots:
            assert (D3F[root], RDF.type, OWL.Class) in graph, root
        uri = classes[kind].get("class_uri")
        if kind in {"D3fendThing", "D3fendThreatModelTechnique"}:
            assert uri is None, kind
        else:
            assert uri == f"d3f:{C.KIND_ROOTS[kind]}", kind


def test_the_abstracts_stay_out_of_the_catalogue_and_nothing_else_does():
    """The one property whose values the catalogue leaves out is kb-abstract, and the
    slot says so. Every other literal a term holds is a value of its record."""
    graph = conversion.graph()
    assert C.LEFT_OUT == {D3F["kb-abstract"]}
    entries = conversion.entries_by_id()
    for prop in C.LEFT_OUT:
        subjects = set(graph.subjects(prop, None))
        assert len(subjects) == 340
        assert not any(C.slot_name(prop) in entries[C.curie(s)] for s in subjects)
        assert any("leaves" in c for c in _slots()[C.slot_name(prop)]["comments"])
    for term in _terms():
        for predicate, obj in graph.predicate_objects(term):
            if predicate not in _declared() or predicate in C.LEFT_OUT:
                continue
            if isinstance(obj, Literal) and not C._objects_are_terms(graph, predicate):
                held = entries[C.curie(term)][C.slot_name(predicate)]
                values = held if isinstance(held, list) else [held]
                assert C.scalar(obj) in values, (term, predicate)
