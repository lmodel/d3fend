"""The Turtle and the catalogue, for the tests that read them.

scripts/d3fend_to_linkml.py is not a package, so it is loaded by its path. Parsing the
Turtle takes a few seconds and so does reading the catalogue, so each test module shares
one copy and must not change it.
"""

import importlib.util
import sys
from functools import cache
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "d3fend_to_linkml.py"
CATALOGUE_FILE = ROOT / "src" / "d3fend" / "data" / "d3fend-1.6.0.yaml"
ENTRIES_MODULE = ROOT / "src" / "d3fend" / "schema" / "d3fend_entries.yaml"
SCHEMA = ROOT / "src" / "d3fend" / "schema" / "d3fend.yaml"


def _load():
    spec = importlib.util.spec_from_file_location("d3fend_to_linkml", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


CONVERTER = _load()
# The C loader reads the catalogue in a fifth of the time, where the build has it.
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


@cache
def graph():
    """The Turtle, parsed once."""
    return CONVERTER.load()


@cache
def catalogue():
    """The committed catalogue, read once."""
    return yaml.load(CATALOGUE_FILE.read_text(encoding="utf-8"), Loader=LOADER)


@cache
def entries_by_id():
    """The catalogue's records by their CURIE."""
    return {entry["id"]: entry for entry in catalogue()["entries"]}


@cache
def module():
    """The committed module of slots and kinds, read once."""
    return yaml.load(ENTRIES_MODULE.read_text(encoding="utf-8"), Loader=LOADER)
