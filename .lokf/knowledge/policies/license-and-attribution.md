---
type: Policy
id: https://w3id.org/lmodel/d3fend/knowledge/policies/license-and-attribution
genre: reference
title: Licence and attribution
description: "Whose work each part is: the code and the schema under Apache-2.0, the bundle under CC BY 4.0, D3FEND under MITRE's Terms of Use with the designation and licence those terms ask each copy to reproduce, and the third-party text inside D3FEND under its own terms."
resource: NOTICE
references:
  - https://w3id.org/lmodel/d3fend/knowledge/references/d3fend-terms-of-use
sources:
  - id: notice
    resource: NOTICE
  - id: readme.md
    resource: README.md
    title: License
  - resource: LICENSE
generated:
  by: process:ktl-librarian
  at: "2026-11-05T01:50:09Z"
status: draft
---

# Licence and attribution

The code in this repository is under the Apache License 2.0.[^notice] The knowledge bundle is under CC BY 4.0.[^readme.md]

`upstream/` holds the ontology as MITRE publishes it, and the catalogue and the slots hold its words. The Terms of Use allow such copies on condition that each reproduces MITRE's copyright designation and the licence, and `NOTICE` and the files' headers do.[^notice]

D3FEND carries text of ATT&CK, ATLAS, SPARTA and CWE under their own terms. The 340 values of `kb_abstract` quote the sources it cites, and those words stay their authors', so the catalogue leaves them out and only `upstream/d3fend.ttl` holds them. Some definitions also quote a source, and those stay as part of MITRE's text.[^notice]

D3FEND is a trademark of The MITRE Corporation, and the project implies no endorsement by it.[^notice]

[^notice]: NOTICE
[^readme.md]: README.md, License
