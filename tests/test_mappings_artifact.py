import json
import csv
from pathlib import Path

import pytest


MAPPINGS_FILE = Path(__file__).resolve().parents[1] / "src" / "d3fend" / "mappings" / "d3fend-full-mappings-1.3.0.json"
SSSOM_FILE = Path(__file__).resolve().parents[1] / "src" / "d3fend" / "mappings" / "stix_spdx_oscal_mappings.sssom.csv"


def _validate_mappings_payload(payload: dict) -> None:
    """Validate the expected high-level structure of the D3FEND mappings artifact."""
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
        missing = expected_vars - set(binding.keys())
        assert not missing, f"binding missing variables: {sorted(missing)}"
        for variable in expected_vars:
            entry = binding[variable]
            assert isinstance(entry, dict)
            assert "type" in entry
            assert "value" in entry


def test_mappings_file_exists():
    """The D3FEND mappings artifact is available from the package source tree."""
    assert MAPPINGS_FILE.exists(), f"missing mappings file: {MAPPINGS_FILE}"


def test_sssom_file_exists():
    """The SSSOM mapping artifact is available from the package source tree."""
    assert SSSOM_FILE.exists(), f"missing SSSOM file: {SSSOM_FILE}"


def test_mappings_file_valid_structure():
    """Validate structure of src/d3fend/mappings/d3fend-full-mappings-1.3.0.json."""
    payload = json.loads(MAPPINGS_FILE.read_text(encoding="utf-8"))
    _validate_mappings_payload(payload)


def test_sssom_file_valid_structure():
    """Validate minimal SSSOM CSV structure and required core columns."""
    rows = []
    with SSSOM_FILE.open(encoding="utf-8", newline="") as handle:
        for line in handle:
            if not line.startswith("#"):
                rows.append(line)

    reader = csv.DictReader(rows)
    assert reader.fieldnames is not None
    required = {
        "subject_id",
        "predicate_id",
        "object_id",
        "mapping_justification",
    }
    assert required.issubset(set(reader.fieldnames)), reader.fieldnames

    first = next(reader, None)
    assert first is not None, "SSSOM file has no mapping rows"


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
