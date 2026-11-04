"""Checks the copy of the upstream, and that the schema names the same edition.

upstream/ holds D3FEND's Turtle file as MITRE publishes it. These tests hold it to the git
object hashes that scripts/check_upstream_release.py pins, and the schema's headers to the
edition that script watches. They run offline.
"""

import importlib.util
from pathlib import Path

import pytest
import yaml
from rdflib import OWL

from tests import conversion

ROOT = Path(__file__).parent.parent
UPSTREAM = ROOT / "upstream"
SCHEMA_DIR = ROOT / "src" / "d3fend" / "schema"
WATCH = ROOT / "scripts" / "check_upstream_release.py"
MODULES = {
    path.stem: yaml.safe_load(path.read_text(encoding="utf-8"))
    for path in SCHEMA_DIR.glob("*.yaml")
}


def _watch():
    spec = importlib.util.spec_from_file_location("watch_pins", WATCH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PINS = _watch()


def test_upstream_holds_exactly_the_pinned_files():
    """Nothing is added to the copy, and nothing is missing from it."""
    held = {
        p.relative_to(UPSTREAM).as_posix() for p in UPSTREAM.rglob("*") if p.is_file()
    }
    assert held == set(PINS.PINNED_BLOBS)


@pytest.mark.parametrize("name", sorted(PINS.PINNED_BLOBS))
def test_each_copy_is_the_pinned_blob(name):
    """Each file is byte for byte what was read from MITRE."""
    assert PINS.blob((UPSTREAM / name).read_bytes()) == PINS.PINNED_BLOBS[name]


def test_every_module_names_the_pinned_edition():
    """Each module's version is the edition the watch pins, and each names its source."""
    assert MODULES.keys() == {"d3fend", "d3fend_core", "d3fend_entries"}
    for name, doc in MODULES.items():
        assert doc["version"] == PINS.PINNED_EDITION, name
        assert doc["source"] == PINS.PINNED_SOURCE, name
        assert doc["license"] == "Apache-2.0", name


def test_the_umbrella_names_the_tag():
    annotations = MODULES["d3fend"]["annotations"]
    assert annotations["upstream_tag"] == PINS.PINNED_EDITION
    assert annotations["upstream_commit"] == PINS.PINNED_TAG_COMMIT
    assert annotations["upstream_release_date"] == PINS.PINNED_DATE


def test_the_turtle_is_the_edition_the_pins_name():
    graph = conversion.graph()
    ontology = conversion.CONVERTER.ONTOLOGY
    assert str(graph.value(ontology, OWL.versionInfo)) == PINS.PINNED_EDITION
    release = graph.value(ontology, conversion.CONVERTER.D3F["release-date"])
    assert str(release).startswith(PINS.PINNED_DATE)
    assert str(graph.value(ontology, OWL.versionIRI)).endswith(
        f"/{PINS.PINNED_EDITION}/d3fend.owl"
    )


def test_the_catalogue_names_the_edition_it_holds():
    assert conversion.catalogue()["version_info"] == PINS.PINNED_EDITION
    assert conversion.CATALOGUE_FILE.name == f"d3fend-{PINS.PINNED_EDITION}.yaml"


def _one_line(path):
    return " ".join(path.read_text(encoding="utf-8").split())


def test_notice_reproduces_the_designation_and_the_licence():
    """The Terms of Use ask each copy to reproduce them."""
    notice = _one_line(ROOT / "NOTICE")
    terms = _one_line(UPSTREAM / "TERMS.txt")
    assert "Copyright 2022 The MITRE Corporation." in notice
    assert "endorse" in notice
    grant = (
        "hereby grants you a non-exclusive, royalty-free license to use D3FEND for research, "
        "development, and commercial purposes. Any copy you make for such purposes is "
        "authorized provided that you reproduce MITRE's copyright designation and this "
        "license in any such copy."
    )
    assert grant in notice
    assert grant in terms


def test_the_terms_designation_stands_in_the_turtle():
    """The designation NOTICE gives is the one the ontology's own header gives."""
    comment = str(
        conversion.graph().value(
            conversion.CONVERTER.ONTOLOGY, conversion.CONVERTER.RDFS.comment
        )
    )
    assert "Copyright 2022 The MITRE Corporation" in comment
    assert "W56KGU-18-D0004" in comment


def test_each_file_that_copies_the_text_carries_the_designation():
    """The catalogue and the slots hold MITRE's words, so each says whose they are."""
    catalogue_head = conversion.CATALOGUE_FILE.read_text(encoding="utf-8")[:1200]
    assert "Copyright 2022 The MITRE Corporation" in catalogue_head
    assert "hereby grants you a non-exclusive, royalty-free license" in catalogue_head
    module_head = conversion.ENTRIES_MODULE.read_text(encoding="utf-8")[:600]
    assert "Copyright 2022 The MITRE Corporation" in module_head


def test_a_released_copy_keeps_the_designation_and_the_licence():
    """The schema asset of a release is the adapt copy, and it travels alone, so its header
    says whose words its slots hold and on what terms."""
    copy = yaml.safe_load((ROOT / ".lokf" / "d3fend.yaml").read_text(encoding="utf-8"))
    annotations = copy["annotations"]
    assert annotations["upstream_copyright"] == "Copyright 2022 The MITRE Corporation"
    assert (
        "Any copy you make for such purposes is authorized"
        in annotations["upstream_license"]
    )
    assert annotations["upstream_terms"] == "https://d3fend.mitre.org/tou"


def test_notice_counts_the_abstracts():
    """NOTICE says how many values of kb_abstract quote another party's source."""
    held = sum("kb_abstract" in e for e in conversion.catalogue()["entries"])
    assert held == 340
    assert f"kb_abstract ({held} in this edition)" in _one_line(ROOT / "NOTICE")


def test_a_kinds_description_is_this_projects_own():
    """A class is described in this project's words: no description shares a run of six
    words with any definition in the Turtle. A slot's are D3FEND's, and say so."""
    graph = conversion.graph()
    converter = conversion.CONVERTER

    def runs(text):
        words = text.lower().split()
        return {tuple(words[i : i + 6]) for i in range(len(words) - 5)}

    upstream = set()
    for obj in graph.objects(None, converter.D3F.definition):
        upstream |= runs(str(obj))
    for name, cls in conversion.module()["classes"].items():
        assert not runs(cls["description"]) & upstream, name
