"""The rules on a whole catalogue that the generated JSON Schema cannot state.

JSON Schema looks at one value at a time. So it cannot say that a relation's target exists,
that the target is of the kind its slot ranges over, or that no two records share an IRI.
A consumer that wants every rule runs these too.
"""

from functools import cache
from pathlib import Path

import yaml

MODULE = (
    Path(__file__).parent.parent / "src" / "d3fend" / "schema" / "d3fend_entries.yaml"
)


@cache
def _module():
    return yaml.safe_load(MODULE.read_text(encoding="utf-8"))


@cache
def _reference_ranges():
    """Each slot whose values name a record, with the kind it ranges over."""
    classes = _module()["classes"]
    return {
        name: slot["range"]
        for name, slot in _module()["slots"].items()
        if slot.get("range") in classes
    }


@cache
def _kinds_under():
    """Each class with its descendants and itself."""
    classes = _module()["classes"]
    under = {name: {name} for name in classes}
    for name in classes:
        walk = classes[name].get("is_a")
        while walk:
            under[walk].add(name)
            walk = classes[walk].get("is_a")
    return under


def rule_errors(catalogue: dict) -> list[tuple[str, str]]:
    """Each break of a rule in a catalogue, as (JSON pointer, message)."""
    found = []
    entries = catalogue.get("entries") or []
    kinds = {}
    for index, entry in enumerate(entries):
        identifier = entry.get("id")
        if identifier in kinds:
            found.append((f"/entries/{index}/id", f"{identifier} is a second record"))
        kinds[identifier] = entry.get("type")
        if "owl_kind" not in entry:
            found.append((f"/entries/{index}", "a record states no owl_kind"))
    ranges = _reference_ranges()
    under = _kinds_under()
    for index, entry in enumerate(entries):
        for key, value in entry.items():
            if key not in ranges or not isinstance(value, list):
                continue
            for position, target in enumerate(value):
                where = f"/entries/{index}/{key}/{position}"
                if target not in kinds:
                    found.append((where, f"{target} names no record"))
                elif kinds[target] not in under[ranges[key]]:
                    found.append(
                        (where, f"{target} is a {kinds[target]}, not a {ranges[key]}")
                    )
    for index, group in enumerate(catalogue.get("disjoint_groups") or []):
        for position, member in enumerate(group.get("members") or []):
            if member not in kinds:
                where = f"/disjoint_groups/{index}/members/{position}"
                found.append((where, f"{member} names no record"))
    return found
