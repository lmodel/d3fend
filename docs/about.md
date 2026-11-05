# About d3fend

This page is for anyone reading the schema's elements: it says why D3FEND's terms are records here, how the kinds are chosen, and what the model leaves out.

## Why a term is a record

D3FEND is an OWL ontology of 4,465 classes, but most of those classes are not types anyone instantiates. `d3f:FileAnalysis` names one countermeasure, and `d3f:T1003` one technique of ATT&CK. D3FEND's own conventions say a defensive technique is punned as an instance of its parent class, and its distribution states all but 23 of its 1,939 class restrictions on terms again as direct triples between them, such as `d3f:FileAnalysis d3f:analyzes d3f:File`. So what D3FEND publishes reads as a catalogue of entries with typed relations, and that is what this schema models.

- **A kind of entry is a class.** `D3fendDefensiveTechnique` is one, with `d3f:DefensiveTechnique` as its class IRI. There are 22, each one or more branches of D3FEND's tree.
- **A property is a slot.** `analyzes` is one, with `d3f:analyzes` as its slot IRI. There are 292 for the ontology's properties, and the subproperty tree, the inverses, the transitive and symmetric flags and the stated domains and ranges come with them.
- **A term is a record.** `src/d3fend/data/d3fend-1.6.0.yaml` holds one for each class and each individual, with its IRI as `id`. This one is shown without its definition and its article:

  ```yaml
  - id: d3f:FileAnalysis
    type: D3fendDefensiveTechnique
    owl_kind: class_and_individual
    rdf_type:
      - d3f:FileAnalysis
    subclass_of:
      - d3f:DefensiveTechnique
    d3fend_id: D3-FA
    label:
      - File Analysis
    analyzes:
      - d3f:File
    enables:
      - d3f:Detect
  ```

The graph's point is the walk through an artifact. `d3f:FileAnalysis` analyzes `d3f:File`, and `d3f:T1070.004`, File Deletion, deletes `d3f:File`, so a reader can go from a technique of an adversary to the countermeasures that see what it touches. `tests/test_catalogue.py` holds this example. MITRE's own `d3fend-full-mappings` query result is that walk with the class tree inferred, and it stays MITRE's: this repository keeps the facts it is computed from.

## How the kinds are chosen

An entry takes the first kind in the converter's table whose branch it sits under, through `rdfs:subClassOf` and `rdf:type`. The deeper kind comes first, and D3FEND's own branches come before the external ones. So an entry with two parents has one kind. An ATT&CK Enterprise technique is under both `d3f:OffensiveTechnique` and `d3f:ATTACKEnterpriseTechnique`, and takes `D3fendOffensiveTechnique`. A tactic of any framework takes `D3fendOffensiveTactic`. `rdf_type` and `subclass_of` keep every parent the ontology states.

D3FEND places the techniques of ATT&CK Mobile, ATT&CK ICS, ATLAS and SPARTA under their frameworks and not under its own offensive technique, so they are `D3fendThreatModelTechnique`. The ten types of reference share their fields, so they are one kind, and `rdf_type` says which each is. An entry with no narrower kind, such as `d3f:Plan` or a root of the tree, is `D3fendThing`.

## What a slot may hold

The ontology declares a domain for few of its properties, so `D3fendEntry` lists each property that has none, and any kind may hold it. A narrower kind lists a property only where D3FEND declares that domain, or the range of its inverse, and this edition obeys it. So `has_input` is on `D3fendEvent` alone, and `attack_id`, whose stated domain of `d3f:OffensiveTechnique` this edition goes beyond, stays on the base. A comment on the slot says so, and an annotation keeps the stated domain and range either way.

A property whose values name terms ranges over `D3fendEntry`, or a narrower kind where D3FEND states it and the data obeys. Such a slot holds a list of CURIEs, and the record it names sits elsewhere in the catalogue. JSON Schema sees only text there, so `tests/d3fend_rules.py` checks the target. A property with literal values holds one value where no term of this edition holds two, which is the one bound on D3FEND's properties that the ontology does not state. A property whose name says it only groups others, and which no term uses, such as `d3fend_object_property`, is an abstract slot that no class lists.

The rules are the class restrictions with a literal filler that every individual of the edition obeys: a reference holds `has_link` and `kb_reference_title`, a CCI item `published`, and a catalog `version`. `tests/test_coverage.py` lists the other eleven with the numbers that keep them out, such as the 14 of 42 mitigations that hold a `d3fend_comment`.

## What the data shows

A catalogue renders the file as it stands, faults included. `tests/test_catalogue.py` records what a reader would not expect, so a later edition that fixes one fails there:

- `d3f:CAPEC-663` holds the CAPEC id `CAPEC-553`.
- 27 values of `d3fend_id`, all of the form `D3A-`, name more than one analytic technique, though the ontology calls the id unique.
- Three references hold an empty `has_link`.
- Four CWE entries hold two labels, and `d3f:CreateProcess` three definitions.
- 263 of the defensive techniques are typed as instances of themselves, not of their parents.

## RDF

Every identifier is a CURIE, so both routes to RDF work. Apply `project/jsonld/d3fend.context.jsonld` to the catalogue, or run LinkML's own dumper, and a record's IRI and its relations come out as D3FEND's own. `tests/test_catalogue.py` compares the first with the Turtle, and `tests/test_datamodel.py` runs the second on the small example.

`rdfs:seeAlso`, `rdfs:isDefinedBy` and `skos:example` hold text here, since D3FEND gives addresses and plain words in all three. An address among them projects as text where the Turtle has an IRI, and the comparison above compares their words. `project/owl/d3fend.owl.ttl` is the schema's own OWL, which names the slots and classes under this schema's namespace. D3FEND's ontology is `upstream/d3fend.ttl`.

## What is left out

D3FEND's classes are not LinkML classes, as above. A host that wants a concept of a technique uses a kind and names the term by its CURIE.

A record does not tell a class restriction from a direct triple: both are values of one slot. `upstream/d3fend.ttl` keeps the difference, and no reasoner ran, so a value is one the file states and not one it implies.

The 340 values of `kb_abstract` stay out of the catalogue. They quote the patents, papers, articles and manuals D3FEND cites, so those words are their authors', and `upstream/d3fend.ttl` alone holds them. The slot stays, so the schema renders the property and a host may hold an abstract of its own.

`tests/test_coverage.py` lists the rest:

- the eleven restrictions with a literal filler that the edition does not obey, and one `owl:allValuesFrom` and two anonymous unions, none of which names a target a record could hold;
- two subjects under `wptmp:entity#`, each with one literal, which are WebProtege's leftovers and which nothing names.

The SQL generator is off. Every kind may hold every relation, so it would write about 4,800 join tables, and the JSON-LD context is the way to a graph database. D3FEND's CSV file and its inferred mappings are MITRE's products of this same graph, and are not copied.

The schema says nothing about whether what an entry claims is true.
