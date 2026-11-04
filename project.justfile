## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Rewrite the slots, the kinds and the catalogue from upstream/d3fend.ttl.
[group('model development')]
gen-schema:
  uv run scripts/d3fend_to_linkml.py --schema --catalogue
