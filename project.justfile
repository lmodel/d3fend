## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Regenerate LinkML schema from ontology sources and mapping artifacts.
[group('model development')]
regen-schema:
	uv run python src/d3fend/schema/build_schema.py

# Run targeted tests that validate fixture integrity and schema consistency.
[group('model development')]
test-schema-fixtures:
	uv run python -m pytest tests/test_schema_consistency.py tests/test_mappings_artifact.py

# Run all schema-related fixture tests, including ABox-to-LinkML symbol checks.
[group('model development')]
test-all-fixtures: test-schema-fixtures test-abox-fixtures

# Fast path: run targeted tests only (no schema regeneration step).
[group('model development')]
test-fast:
	uv run python -m pytest tests/test_schema_consistency.py tests/test_mappings_artifact.py tests/test_abox_fixtures.py

# End-to-end check for schema regeneration + fixture consistency.
[group('model development')]
check-schema: regen-schema test-all-fixtures

# Run ABox fixture tests in isolation from schema-generation checks.
[group('model development')]
test-abox-fixtures:
	uv run python -m pytest tests/test_abox_fixtures.py
