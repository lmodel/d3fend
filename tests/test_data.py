"""Data tests for example YAML payloads.

Valid fixture naming convention: ``<ClassName>-<seq>.yaml``
  The portion before the first hyphen is used as the Python class name to load
  against.  Every file under ``tests/data/valid/`` must parse and load cleanly.

Invalid fixture naming convention: ``<ClassName>-<reason>-<seq>.yaml``
  The portion before the first hyphen is used as the Python class name.  Every
  file under ``tests/data/invalid/`` must raise an exception when loaded.
  Three failure modes are covered:

  1. **YAML syntax errors** - unclosed flow sequences/mappings cause
     ``yaml.scanner.ScannerError`` before the datamodel is consulted.
  2. **Non-existent class names** - class names that do not exist in the
     generated module raise ``AttributeError`` at ``getattr()``.
  3. **Type mismatches** - slots with constrained ranges (e.g. ``integer``)
     receiving incompatible values raise ``ValueError`` during loading.

Valid fixtures cover:
  - D3FENDKBThing  - minimal KB entity (label + description)
  - DefensiveTechnique  - core technique with synonym multivalued slot
  - Detect  - DefensiveTactic with pref-label
  - NetworkTrafficAnalysis  - technique with d3fend-id, kb-article, analyzes
  - DigitalArtifact  - artifact with d3fend-artifact-data-property slot
  - File  - simple resource entity
  - DetectionEvent  - security event with definition
  - FileAnalysis  - inherited-slot resolution across DefensiveTechnique hierarchy
"""
import glob
import os
from pathlib import Path

import pytest
from linkml_runtime.loaders import yaml_loader

try:
    import d3fend.datamodel.d3fend as d3fend_model
except ModuleNotFoundError:
    d3fend_model = None

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    if d3fend_model is None:
        pytest.skip("Generated datamodel module d3fend.datamodel.d3fend is not available")
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        d3fend_model,
        target_class_name,
    )
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Test that all invalid data files fail to load against the datamodel."""
    if d3fend_model is None:
        pytest.skip("Generated datamodel module d3fend.datamodel.d3fend is not available")
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(d3fend_model, target_class_name)
    with pytest.raises(Exception):
        yaml_loader.load(filepath, target_class=tgt_class)

