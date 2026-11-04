---
type: Explanation
id: https://w3id.org/lmodel/d3fend/knowledge/explanations/what-a-slot-may-hold
genre: explanation
title: What a slot may hold
description: "Which kinds hold which slots, and why most may hold any: the ontology states a domain for few of its properties, so no domain is invented. A literal slot holds one value where no term of this edition holds two."
about:
  - https://w3id.org/lmodel/d3fend/knowledge/datasets/entries-module
sources:
  - id: about.md
    resource: docs/about.md
    title: What a slot may hold
generated:
  by: process:ktl-librarian
  at: "2026-11-04T22:48:04Z"
status: draft
---

# What a slot may hold

`D3fendEntry` lists each property with no stated domain, so any kind may hold it. `has_input` is on `D3fendEvent` alone, because D3FEND states that domain and the edition obeys it. `attack_id` stays on the base, because the edition goes beyond its stated domain.[^about.md]

A relation holds a list of CURIEs, and JSON Schema sees only text there, so `tests/d3fend_rules.py` checks each target.[^about.md]

A property whose name says it only groups others, and which no term uses, is an abstract slot that no class lists.[^about.md]

[^about.md]: docs/about.md, What a slot may hold
