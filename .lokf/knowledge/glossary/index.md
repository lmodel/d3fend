# Glossary

* [Entry](entry.md) - An entry: one term of the D3FEND graph, a class or an individual, as a record with its IRI, its kind, its text and its relations.
* [Kind of entry](kind-of-entry.md) - A kind of entry: one of the 22 classes under `D3fendEntry`, each a branch of D3FEND's tree, which a record names in `type`.
* [Defensive technique](defensive-technique.md) - A defensive technique: a countermeasure, a method that makes a system harder to attack, related to the artifacts it acts on and to the tactic it enables. `D3fendDefensiveTechnique` holds 273 in this edition.
* [Offensive technique](offensive-technique.md) - An offensive technique: a way an adversary acts, drawn from ATT&CK Enterprise, related to the artifacts it touches and to the tactic it serves. The techniques of other frameworks are `D3fendThreatModelTechnique`.
* [Digital artifact](digital-artifact.md) - A digital artifact: something that carries information for a digital system, such as a file, a process or a packet, where offensive and defensive techniques meet.
* [Class restriction](class-restriction.md) - A class restriction: an OWL axiom such as `d3f:FileAnalysis rdfs:subClassOf [ owl:onProperty d3f:analyzes ; owl:someValuesFrom d3f:File ]`, which a record holds as a value of its slot.
* [Punning](punning.md) - Punning: declaring one IRI both an `owl:Class` and an `owl:NamedIndividual`. D3FEND's conventions pun defensive techniques, and `owl_kind` records it as `class_and_individual`.
* [Adapt copy](adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`.
