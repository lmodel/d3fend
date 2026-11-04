# The D3FEND files this schema renders

This folder holds files of MITRE D3FEND as The MITRE Corporation publishes them, unchanged. `scripts/check_upstream_release.py` pins each by its git object hash, and `tests/test_upstream.py` holds the folder to that list.

| File | What it is | Read from |
| --- | --- | --- |
| `d3fend.ttl` | The D3FEND ontology, edition 1.6.0 of 2026-08-31 | <https://d3fend.mitre.org/ontologies/d3fend/1.6.0/d3fend.ttl> |
| `LICENSE.md` | The licence file of the repository that builds the ontology, at tag 1.6.0 | <https://github.com/d3fend/d3fend-ontology/blob/1.6.0/LICENSE.md> |
| `TERMS.txt` | The text of the Terms of Use | <https://d3fend.mitre.org/tou/> |

Copyright 2022 The MITRE Corporation. MITRE D3FEND and the MITRE D3FEND logo are trademarks of The MITRE Corporation. The Terms of Use authorise these copies on condition that each reproduces that designation and the licence in `TERMS.txt`. [NOTICE](../NOTICE) says more, and says which of the text the Turtle carries is another party's. MITRE has not endorsed this project.

`scripts/d3fend_to_linkml.py` turns the Turtle file into the schema's slots and into the catalogue that the schema describes.
