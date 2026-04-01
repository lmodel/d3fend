"""Data tests for example YAML payloads and mappings JSON artifacts."""
import glob
import json
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
MAPPINGS_FILE = Path(__file__).parent / "data" / "d3fend" / "d3fend-full-mappings-1.3.0.json"

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


def _validate_mappings_payload(payload: dict) -> None:
    """Validate the expected high-level structure of D3FEND mappings JSON."""
    assert isinstance(payload, dict)
    assert "head" in payload
    assert "results" in payload

    head = payload["head"]
    results = payload["results"]
    assert isinstance(head, dict)
    assert isinstance(results, dict)

    assert "vars" in head
    assert isinstance(head["vars"], list)
    assert head["vars"], "head.vars must not be empty"

    assert "bindings" in results
    assert isinstance(results["bindings"], list)
    assert results["bindings"], "results.bindings must not be empty"

    expected_vars = set(head["vars"])
    for binding in results["bindings"]:
        assert isinstance(binding, dict)
        # Each binding should include at least the declared vars from head.
        missing = expected_vars - set(binding.keys())
        assert not missing, f"binding missing variables: {sorted(missing)}"
        for variable in expected_vars:
            entry = binding[variable]
            assert isinstance(entry, dict)
            assert "type" in entry
            assert "value" in entry


def test_mappings_file_exists():
    """The expected mappings artifact is present in the test data folder."""
    assert MAPPINGS_FILE.exists(), f"missing mappings file: {MAPPINGS_FILE}"


def test_mappings_file_valid_structure():
    """Validate structure of tests/data/d3fend/d3fend-full-mappings-1.3.0.json."""
    payload = json.loads(MAPPINGS_FILE.read_text(encoding="utf-8"))
    _validate_mappings_payload(payload)


@pytest.mark.parametrize(
    "invalid_payload",
    [
        {},
        {"head": {}, "results": {}},
        {"head": {"vars": []}, "results": {"bindings": []}},
        {
            "head": {"vars": ["a"]},
            "results": {"bindings": [{"b": {"type": "literal", "value": "x"}}]},
        },
        {
            "head": {"vars": ["a"]},
            "results": {"bindings": [{"a": {"type": "literal"}}]},
        },
    ],
)
def test_mappings_invalid_structures(invalid_payload):
    """Invalid mappings payloads should fail schema-level structure validation."""
    with pytest.raises(AssertionError):
        _validate_mappings_payload(invalid_payload)
