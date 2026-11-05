"""Data tests: every example against the JSON Schema the validator generates, and
the rules on a whole catalogue that no generator carries."""

import json
from functools import cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.validator import validate
from linkml_runtime import SchemaView

from tests.d3fend_rules import rule_errors

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "d3fend" / "schema" / "d3fend.yaml"
DATA = Path(__file__).parent / "data"
VALID = sorted((DATA / "valid").glob("*.yaml"))
INVALID = sorted((DATA / "invalid").glob("*.yaml"))
PROBLEM_INVALID = sorted((DATA / "problem" / "invalid").glob("*.yaml"))


@cache
def definitions():
    """The class definitions of the JSON Schema that linkml-validate generates.
    Generating it once keeps the run short; test_validator_agrees checks that
    linkml-validate gives the same answers."""
    generator = JsonSchemaGenerator(
        str(SCHEMA), mergeimports=True, include_range_class_descendants=True
    )
    return json.loads(generator.serialize())["$defs"]


def errors(instance, class_name):
    schema = {"$ref": f"#/$defs/{class_name}", "$defs": definitions()}
    validator = jsonschema.validators.validator_for(schema)(schema)
    return list(validator.iter_errors(instance))


def pointer(error):
    return "/" + "/".join(str(part) for part in error.absolute_path)


def class_of(path):
    return path.stem.split("-")[0]


def fails_at(path):
    first = path.read_text(encoding="utf-8").splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{path.name}: the first line names where it fails"
    )
    return first.removeprefix("# Fails at: ").strip()


def places(error):
    """Where an error points: its own place, or, for an anyOf or oneOf that no branch
    met, the places inside each branch that could have been meant. An optional value's
    branches are the value and null, so its error points inside the value; the null
    branch is left aside. A choice whose branches are alternatives, such as the kinds
    an entry may be, stays at its own place."""
    if error.validator not in ("anyOf", "oneOf") or not error.context:
        return {pointer(error)}
    branches = {}
    for sub in error.context:
        branches.setdefault(sub.relative_schema_path[0], []).append(sub)
    real = [
        subs
        for subs in branches.values()
        if not any(s.validator == "type" and s.validator_value == "null" for s in subs)
    ]
    if len(real) != 1:
        return {pointer(error)}
    found = set()
    for sub in real[0]:
        found |= places(sub)
    return found or {pointer(error)}


def test_the_example_folders_hold_examples():
    """The parametrized tests below pass on an empty folder, so this one does not."""
    assert len(VALID) >= 25, len(VALID)
    assert len(INVALID) >= 40, len(INVALID)
    assert len(PROBLEM_INVALID) >= 6, len(PROBLEM_INVALID)


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.stem)
def test_valid_examples_validate(path):
    """Every valid example passes the JSON Schema."""
    instance = yaml.safe_load(path.read_text(encoding="utf-8"))
    found = errors(instance, class_of(path))
    assert not found, [f"{pointer(e)}: {e.message[:200]}" for e in found]


def test_the_small_catalogue_keeps_the_rules():
    """The valid tree root breaks none of the rules on a whole catalogue."""
    instance = yaml.safe_load(
        (DATA / "valid" / "D3fendCatalog-small.yaml").read_text(encoding="utf-8")
    )
    assert not rule_errors(instance)


@pytest.mark.parametrize("path", INVALID, ids=lambda p: p.stem)
def test_counter_examples_fail_where_they_say(path):
    """Every counter-example fails at the place its first line names, as
    `# Fails at: <JSON pointer>`, and nowhere else but on the way to it, so a
    file that starts failing for another reason fails this test."""
    where = fails_at(path)
    found = errors(yaml.safe_load(path.read_text(encoding="utf-8")), class_of(path))
    assert found, "it validates"
    reached = set().union(*(places(e) for e in found))
    report = [f"{pointer(e)}: {e.message[:200]}" for e in found]
    assert where in reached, (sorted(reached), report)
    on_the_way = {
        p for p in reached if where == p or where.startswith(p.rstrip("/") + "/")
    }
    assert reached == on_the_way, (sorted(reached - on_the_way), report)


@pytest.mark.parametrize("path", PROBLEM_INVALID, ids=lambda p: p.stem)
def test_rule_counter_examples_fail_where_they_say(path):
    """A counter-example under problem/invalid/ passes the JSON Schema, which cannot
    state its rule, and fails only the rule its first line points to."""
    where = fails_at(path)
    instance = yaml.safe_load(path.read_text(encoding="utf-8"))
    found = errors(instance, class_of(path))
    assert not found, [f"{pointer(e)}: {e.message[:200]}" for e in found]
    assert [p for p, _ in rule_errors(instance)] == [where]


def test_validator_agrees():
    """linkml-validate, which the docs tell a user to run, accepts a valid example and
    rejects a counter-example at the same place."""
    good = DATA / "valid" / "D3fendCatalog-small.yaml"
    report = validate(yaml.safe_load(good.read_text()), SCHEMA, "D3fendCatalog")
    assert not report.results, [r.message for r in report.results]
    bad = DATA / "invalid" / "D3fendThing-risk-impact-too-high.yaml"
    report = validate(yaml.safe_load(bad.read_text()), SCHEMA, "D3fendThing")
    assert any("/risk_impact" in r.message for r in report.results), [
        r.message for r in report.results
    ]


def test_every_concrete_class_has_an_example():
    """Each class a catalogue can hold has a valid example, and so does the root."""
    view = SchemaView(str(SCHEMA))
    concrete = {
        name
        for name, cls in view.all_classes().items()
        if not cls.abstract and not cls.mixin
    }
    examples = {class_of(path) for path in VALID}
    assert concrete == examples, sorted(concrete ^ examples)
