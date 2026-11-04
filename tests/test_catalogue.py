"""Checks the whole catalogue against the Turtle it comes from.

src/d3fend/data/d3fend-1.6.0.yaml is every term of the edition as a record. These tests
hold it to the converter's output, to the validator the docs tell a user to run, to the
rules JSON Schema cannot state and, through the generated JSON-LD context, to the triples
of the Turtle itself.
"""

import collections
import json
from functools import cache
from pathlib import Path

import jsonschema
import rdflib
from linkml.validator import validate
from rdflib import OWL, RDF, BNode

from tests import conversion
from tests.d3fend_rules import rule_errors

ROOT = Path(__file__).parent.parent
JSON_SCHEMA = ROOT / "project" / "jsonschema" / "d3fend.schema.json"
CONTEXT = ROOT / "project" / "jsonld" / "d3fend.context.jsonld"
OWN_NAMESPACE = "https://w3id.org/lmodel/d3fend/"
C = conversion.CONVERTER

# What this edition holds, by kind. A change here is a change of edition, or of the table
# of kinds in the converter, and either should be looked at.
KIND_COUNTS = {
    "D3fendAgent": 23,
    "D3fendAnalyticTechnique": 227,
    "D3fendArtifact": 18,
    "D3fendAttackDataSource": 42,
    "D3fendAttackMitigation": 43,
    "D3fendCciControl": 300,
    "D3fendControlCatalog": 7,
    "D3fendDefensiveTactic": 8,
    "D3fendDefensiveTechnique": 273,
    "D3fendDigitalArtifact": 953,
    "D3fendEvent": 317,
    "D3fendExternalControl": 1,
    "D3fendGoal": 18,
    "D3fendNistControl": 118,
    "D3fendOffensiveTactic": 65,
    "D3fendOffensiveTechnique": 875,
    "D3fendTechnique": 2,
    "D3fendTechniqueReference": 408,
    "D3fendThing": 24,
    "D3fendThreatModelTechnique": 736,
    "D3fendThreatModelThing": 17,
    "D3fendWeakness": 944,
}


def test_the_catalogue_is_the_converters_output():
    """The committed catalogue is what the converter writes from the Turtle, so nothing
    was edited by hand and a change to the converter shows here."""
    assert conversion.catalogue() == C.catalogue(conversion.graph())


def test_the_module_is_the_converters_output():
    """The committed slots and kinds are what the converter writes from the Turtle."""
    assert conversion.module() == C.schema_module(conversion.graph())


def test_each_kind_holds_what_it_should():
    counts = collections.Counter(e["type"] for e in conversion.catalogue()["entries"])
    assert counts == KIND_COUNTS
    assert sum(counts.values()) == 5419


def test_the_catalogue_passes_the_committed_json_schema():
    """Every record passes project/jsonschema/d3fend.schema.json, the file a consumer
    without LinkML validates with."""
    schema = json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))
    validator = jsonschema.validators.validator_for(schema)(schema)
    errors = [
        (list(e.absolute_path)[:3], e.message[:120])
        for e in validator.iter_errors(conversion.catalogue())
    ]
    assert not errors, errors[:5]


def test_the_catalogue_passes_the_validator_the_docs_name():
    """linkml-validate runs a format checker the test above does not, so the whole
    catalogue goes through it too. This is the call behind the command in docs/index.md."""
    report = validate(conversion.catalogue(), conversion.SCHEMA, "D3fendCatalog")
    assert not report.results, [r.message[:200] for r in report.results[:5]]


def test_the_catalogue_keeps_the_rules():
    """Every relation's target is a record of the right kind, and each IRI is one record."""
    found = rule_errors(conversion.catalogue())
    assert not found, found[:10]


def test_a_record_holds_its_relations():
    """The walk docs/about.md describes: a defensive technique names the artifact it acts
    on and the tactic it enables, and an offensive technique names the same artifact."""
    entries = conversion.entries_by_id()
    file_analysis = entries["d3f:FileAnalysis"]
    assert file_analysis["type"] == "D3fendDefensiveTechnique"
    assert file_analysis["d3fend_id"] == "D3-FA"
    assert file_analysis["analyzes"] == ["d3f:File"]
    assert file_analysis["enables"] == ["d3f:Detect"]
    file_deletion = entries["d3f:T1070.004"]
    assert file_deletion["type"] == "D3fendOffensiveTechnique"
    assert "d3f:File" in file_deletion["deletes"]


def test_an_entry_under_two_branches_takes_the_stated_kind():
    """An entry under both D3FEND's own branch and a framework's takes D3FEND's, as the
    comment on the converter's table of kinds says. The numbers are the 874 ATT&CK
    Enterprise techniques and the 65 tactics."""
    graph = conversion.graph()
    tree = C.branches(graph, C.entry_subjects(graph))
    both = {
        entry: C.kind_of(branch)
        for entry, branch in tree.items()
        if C.D3F.ATTACKThing in branch and C.D3F.OffensiveTechnique in branch
    }
    assert len(both) == 874
    assert set(both.values()) == {"D3fendOffensiveTechnique"}
    tactics = [
        C.kind_of(branch)
        for branch in tree.values()
        if C.D3F.OffensiveTactic in branch and C.D3F.ExternalThreatModelThing in branch
    ]
    assert len(tactics) == 64
    assert set(tactics) == {"D3fendOffensiveTactic"}


@cache
def _projected():
    """The catalogue's triples, through the committed JSON-LD context."""
    context = json.loads(CONTEXT.read_text(encoding="utf-8"))["@context"]
    document = dict(conversion.catalogue(), **{"@context": context})
    graph = rdflib.Graph()
    graph.parse(data=json.dumps(document), format="json-ld")
    return graph


def _subject_triples(graph, subjects):
    """A graph's triples about the given subjects, each object by its lexical form. A
    blank node stands for a restriction, which test_coverage.py follows apart."""
    found = set()
    for subject in subjects:
        for predicate, obj in graph.predicate_objects(subject):
            if isinstance(obj, BNode) or str(predicate).startswith(OWN_NAMESPACE):
                continue
            if predicate == RDF.type and obj in (OWL.Class, OWL.NamedIndividual):
                continue
            found.add((subject, predicate, str(obj)))
    return found


def test_the_json_ld_projection_reproduces_the_turtle():
    """Each triple of the Turtle about a term comes back from the catalogue, and the
    only extra triples are the class restrictions that have no direct triple. Objects
    compare by their lexical form, since LinkML writes rdfs:seeAlso and rdfs:isDefinedBy
    as text."""
    graph = conversion.graph()
    entries = C.entry_subjects(graph)
    upstream = _subject_triples(graph, entries)
    projected = _subject_triples(_projected(), entries)
    assert upstream - projected == set()
    restrictions = {
        (entry, prop, str(target))
        for entry in entries
        for prop, target in C.restrictions(graph, entry)
    }
    extra = projected - upstream
    assert extra == restrictions - upstream
    assert len(extra) == 23
    assert len(upstream) > 30000


def test_a_relation_projects_as_an_iri():
    """A relation's target is a node of the graph, not a piece of text."""
    triple = (C.D3F.FileAnalysis, C.D3F.analyzes, C.D3F.File)
    assert triple in conversion.graph()
    assert triple in _projected()


def test_the_header_projects_as_the_ontologys_own():
    """The catalogue's header is the ontology node's own facts."""
    graph = conversion.graph()
    keep = (C.OWL.versionInfo, C.OWL.versionIRI, C.DCTERMS.title, C.DCTERMS.description)
    for predicate in (*keep, C.DCTERMS.license, C.RDFS.comment, C.D3F["release-date"]):
        assert str(graph.value(C.ONTOLOGY, predicate)) == str(
            _projected().value(C.ONTOLOGY, predicate)
        ), predicate
