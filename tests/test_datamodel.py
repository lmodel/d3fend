"""Checks what the generated models and the JSON-LD context do with real data.

The Pydantic models and the dataclasses load the whole catalogue, each record as the kind
its `type` names. RDF goes through JSON-LD with the generated context, which is how
tests/test_catalogue.py compares the catalogue with the Turtle. LinkML's own RDF dumper
also works, because every identifier is a CURIE. These tests hold those sentences.
"""

import json
from functools import cache
from pathlib import Path

import rdflib
import yaml
from linkml_runtime.dumpers import rdflib_dumper
from linkml_runtime.loaders import json_loader
from linkml_runtime.utils.schemaview import SchemaView

from d3fend.datamodel import d3fend as dataclasses_module
from d3fend.datamodel import d3fend_pydantic
from tests import conversion

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "d3fend" / "schema" / "d3fend.yaml"
SMALL = ROOT / "tests" / "data" / "valid" / "D3fendCatalog-small.yaml"
D3F = rdflib.Namespace("http://d3fend.mitre.org/ontologies/d3fend.owl#")


@cache
def small():
    return yaml.safe_load(SMALL.read_text(encoding="utf-8"))


def test_the_whole_catalogue_loads_into_the_pydantic_models():
    """Each record loads as its own kind, with its relations."""
    model = d3fend_pydantic.D3fendCatalog(**conversion.catalogue())
    assert len(model.entries) == 5419
    assert all(type(e).__name__ == e.type for e in model.entries)
    entry = next(e for e in model.entries if e.id == "d3f:FileAnalysis")
    assert type(entry).__name__ == "D3fendDefensiveTechnique"
    assert entry.analyzes == ["d3f:File"]
    assert entry.enables == ["d3f:Detect"]


def test_the_whole_catalogue_loads_into_the_dataclasses():
    """The designator chooses each record's class here too."""
    catalogue = json_loader.loads(
        json.dumps(conversion.catalogue()),
        target_class=dataclasses_module.D3fendCatalog,
    )
    assert len(catalogue.entries) == 5419
    assert all(type(e).__name__ == e.type for e in catalogue.entries)
    entry = next(e for e in catalogue.entries if e.id == "d3f:FileAnalysis")
    assert type(entry).__name__ == "D3fendDefensiveTechnique"
    assert list(entry.analyzes) == ["d3f:File"]


def test_linkmls_rdf_dumper_keeps_the_iris():
    """Every identifier is a CURIE, so LinkML's dumper expands records and relations to
    D3FEND's own IRIs, on the small example, as docs/about.md says."""
    catalogue = json_loader.loads(
        json.dumps(small()), target_class=dataclasses_module.D3fendCatalog
    )
    graph = rdflib.Graph()
    text = rdflib_dumper.dumps(catalogue, schemaview=SchemaView(str(SCHEMA)))
    graph.parse(data=text, format="turtle")
    assert (D3F.FileAnalysis, D3F.analyzes, D3F.File) in graph
    assert (D3F.FileAnalysis, rdflib.RDF.type, D3F.FileAnalysis) in graph
    assert (D3F.FileAnalysis, rdflib.RDFS.subClassOf, D3F.DefensiveTechnique) in graph
