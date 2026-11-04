## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Rewrite the slots, the kinds and the catalogue from upstream/d3fend.ttl.
[group('model development')]
gen-schema:
  uv run scripts/d3fend_to_linkml.py --schema --catalogue

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/d3fend.yaml` is the copy `lokf adapt` writes from the schema so that it can sit
# beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the moves). The roots are the two
# classes that carry the schema's identifiers: D3fendEntry, the abstract base of every kind
# of entry, and D3fendCatalog. A concept names one of the kinds as its `type`, and LOKF's
# `id` stands for the term's IRI, which adapt drops. rdfs:isDefinedBy keeps its own key,
# because LOKF's definedBy names a concept and D3FEND's values are text. The recipes run the
# `lokf` the sidecar's floor pins (0.9.0 or later); LOKF_CMD runs another, such as a
# checkout: LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root D3fendEntry --root D3fendCatalog --prefix d3fend --keep is_defined_by"

# Rewrite .lokf/d3fend.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/d3fend.yaml

# Fail when .lokf/d3fend.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/d3fend.yaml --check
