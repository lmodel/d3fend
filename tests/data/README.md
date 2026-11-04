# Example data for d3fend

- `valid/` holds an example of each class. Most are real records of D3FEND 1.6.0, each naming the term it comes from, and a few are written from the schema to show a slot no record of this edition uses. `linkml-run-examples` and `tests/test_data.py` read this folder.
- `invalid/` holds a counter-example for each constraint the validator can state. Each file's first line, `# Fails at: <JSON pointer>`, names its one failing place, and `tests/test_data.py` holds it there.
- `problem/invalid/` holds a counter-example for each rule the generated JSON Schema cannot state, which `tests/d3fend_rules.py` checks over a whole catalogue.

A file name is `ClassName-anything.yaml`, and the class is the part before the first hyphen. The whole catalogue is `src/d3fend/data/d3fend-1.6.0.yaml`, and `tests/test_catalogue.py` validates it.

The real records are copies under MITRE's Terms of Use: Copyright 2022 The MITRE Corporation. See [NOTICE](../../NOTICE).
