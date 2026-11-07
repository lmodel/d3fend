## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Rewrite the slots, the kinds and the catalogue from upstream/d3fend.ttl.
[group('model development')]
gen-schema:
  uv run scripts/d3fend_to_linkml.py --schema --catalogue

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/schema/d3fend.yaml` is the copy `lokf adapt` writes from the schema so that it can sit
# beside `.lokf/schema/lokf.yaml` (`lokf adapt --help` lists the moves). The roots are the two
# classes that carry the schema's identifiers: D3fendEntry, the abstract base of every kind
# of entry, and D3fendCatalog. A concept names one of the kinds as its `type`, and LOKF's
# `id` stands for the term's IRI, which adapt drops. rdfs:isDefinedBy keeps its own key,
# because LOKF's definedBy names a concept and D3FEND's values are text. The recipes run the
# `lokf` the sidecar's floor pins (0.9.0 or later); LOKF_CMD runs another, such as a
# checkout: LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root D3fendEntry --root D3fendCatalog --prefix d3fend --keep is_defined_by"

# Rewrite .lokf/schema/d3fend.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/schema/lokf.yaml -o .lokf/schema/d3fend.yaml

# Fail when .lokf/schema/d3fend.yaml is stale against the schema or .lokf/schema/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/schema/lokf.yaml -o .lokf/schema/d3fend.yaml --check

# ============ Artefacts gen-project does not write ============

# Write one LinkML YAML with every import merged, as the copier template's recipe does
[group('model development - extended')]
gen-merged-schema:
  mkdir -p {{dest}}/linkml
  uv run gen-linkml --mergeimports -o {{dest}}/linkml/{{schema_name}}.merged.linkml.yaml {{source_schema_path}}

# Write the schema as RDF Turtle; gen-project's rdf generator is switched off in LinkML
[group('model development - extended')]
gen-rdf:
  mkdir -p {{dest}}/rdf
  uv run gen-rdf --mergeimports {{source_schema_path}} > {{dest}}/rdf/{{schema_name}}.ttl
