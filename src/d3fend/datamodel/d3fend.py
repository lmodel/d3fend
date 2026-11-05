# Auto generated from d3fend.yaml by pythongen.py version: 0.0.1
# Schema: d3fend
#
# id: https://w3id.org/lmodel/d3fend
# description: A LinkML model of MITRE D3FEND, the knowledge graph of cybersecurity countermeasures. It models the graph as a catalogue of records: each kind of entry is a class, each property of the ontology is a slot under its own IRI, and every term of D3FEND 1.6.0 is a record that validates against them.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE

metamodel_version = "1.12.0"
version = "1.6.0"

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
COMMONCOREONTOLOGY = CurieNamespace('COMMONCOREONTOLOGY', 'http://www.ontologyrepository.com/CommonCoreOntologies/')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
ATTACK = CurieNamespace('attack', 'https://w3id.org/lmodel/attack/')
CAPEC = CurieNamespace('capec', 'https://w3id.org/lmodel/capec/')
CCO = CurieNamespace('cco', 'https://www.commoncoreontologies.org/')
CWE = CurieNamespace('cwe', 'https://w3id.org/lmodel/cwe/')
D3F = CurieNamespace('d3f', 'http://d3fend.mitre.org/ontologies/d3fend.owl#')
D3FEND = CurieNamespace('d3fend', 'https://w3id.org/lmodel/d3fend/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_SP_800_53 = CurieNamespace('nist_sp_800_53', 'https://w3id.org/lmodel/nist-sp-800-53/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
STIX = CurieNamespace('stix', 'https://w3id.org/lmodel/stix/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = D3FEND


# Types
class D3fendDateTime(String):
    """ A date and time as the ontology writes it, which may carry no time zone. """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "d3fend_date_time"
    type_model_uri = D3FEND.D3fendDateTime


class D3fendUri(String):
    """ An address as the ontology writes it, typed xsd:anyURI. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "d3fend_uri"
    type_model_uri = D3FEND.D3fendUri


# Class references
class D3fendCatalogOntologyIri(URIorCURIE):
    pass


class D3fendEntryId(URIorCURIE):
    pass


class D3fendThingId(D3fendEntryId):
    pass


class D3fendThreatModelThingId(D3fendEntryId):
    pass


class D3fendThreatModelTechniqueId(D3fendThreatModelThingId):
    pass


class D3fendAttackDataSourceId(D3fendThreatModelThingId):
    pass


class D3fendAttackMitigationId(D3fendThreatModelThingId):
    pass


class D3fendControlCatalogId(D3fendEntryId):
    pass


class D3fendExternalControlId(D3fendEntryId):
    pass


class D3fendCciControlId(D3fendExternalControlId):
    pass


class D3fendNistControlId(D3fendExternalControlId):
    pass


class D3fendTechniqueReferenceId(D3fendEntryId):
    pass


class D3fendAgentId(D3fendEntryId):
    pass


class D3fendEventId(D3fendEntryId):
    pass


class D3fendArtifactId(D3fendEntryId):
    pass


class D3fendDigitalArtifactId(D3fendArtifactId):
    pass


class D3fendWeaknessId(D3fendEntryId):
    pass


class D3fendTechniqueId(D3fendEntryId):
    pass


class D3fendAnalyticTechniqueId(D3fendTechniqueId):
    pass


class D3fendOffensiveTechniqueId(D3fendTechniqueId):
    pass


class D3fendDefensiveTechniqueId(D3fendTechniqueId):
    pass


class D3fendGoalId(D3fendEntryId):
    pass


class D3fendOffensiveTacticId(D3fendGoalId):
    pass


class D3fendDefensiveTacticId(D3fendGoalId):
    pass


@dataclass(repr=False)
class D3fendCatalog(YAMLRoot):
    """
    One edition of the D3FEND ontology, with its header and all its entries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3FEND["D3fendCatalog"]
    class_class_curie: ClassVar[str] = "d3fend:D3fendCatalog"
    class_name: ClassVar[str] = "D3fendCatalog"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendCatalog

    ontology_iri: Union[str, D3fendCatalogOntologyIri] = None
    version_info: str = None
    entries: Union[dict[Union[str, D3fendEntryId], Union[dict, "D3fendEntry"]], list[Union[dict, "D3fendEntry"]]] = empty_dict()
    comment: Optional[Union[str, list[str]]] = empty_list()
    release_date: Optional[str] = None
    version_iri: Optional[Union[str, URI]] = None
    ontology_title: Optional[str] = None
    ontology_description: Optional[str] = None
    ontology_license: Optional[str] = None
    disjoint_groups: Optional[Union[Union[dict, "D3fendDisjointGroup"], list[Union[dict, "D3fendDisjointGroup"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ontology_iri):
            self.MissingRequiredField("ontology_iri")
        if not isinstance(self.ontology_iri, D3fendCatalogOntologyIri):
            self.ontology_iri = D3fendCatalogOntologyIri(self.ontology_iri)

        if self._is_empty(self.version_info):
            self.MissingRequiredField("version_info")
        if not isinstance(self.version_info, str):
            self.version_info = str(self.version_info)

        if self._is_empty(self.entries):
            self.MissingRequiredField("entries")
        self._normalize_inlined_as_list(slot_name="entries", slot_type=D3fendEntry, key_name="id", keyed=True)

        if not isinstance(self.comment, list):
            self.comment = [self.comment] if self.comment is not None else []
        self.comment = [v if isinstance(v, str) else str(v) for v in self.comment]

        if self.release_date is not None and not isinstance(self.release_date, str):
            self.release_date = str(self.release_date)

        if self.version_iri is not None and not isinstance(self.version_iri, URI):
            self.version_iri = URI(self.version_iri)

        if self.ontology_title is not None and not isinstance(self.ontology_title, str):
            self.ontology_title = str(self.ontology_title)

        if self.ontology_description is not None and not isinstance(self.ontology_description, str):
            self.ontology_description = str(self.ontology_description)

        if self.ontology_license is not None and not isinstance(self.ontology_license, str):
            self.ontology_license = str(self.ontology_license)

        if not isinstance(self.disjoint_groups, list):
            self.disjoint_groups = [self.disjoint_groups] if self.disjoint_groups is not None else []
        self.disjoint_groups = [v if isinstance(v, D3fendDisjointGroup) else D3fendDisjointGroup(**as_dict(v)) for v in self.disjoint_groups]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class D3fendEntry(YAMLRoot):
    """
    One term of the D3FEND graph, a class or an individual, as a record that holds its text and its relations to other
    terms.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3FEND["D3fendEntry"]
    class_class_curie: ClassVar[str] = "d3fend:D3fendEntry"
    class_name: ClassVar[str] = "D3fendEntry"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendEntry

    id: Union[str, D3fendEntryId] = None
    type: str = None
    owl_kind: Optional[Union[str, "D3fendOwlKind"]] = None
    rdf_type: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    subclass_of: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    abuses: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    access_mediated_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    accessed_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    accesses: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    addressed_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    addresses: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    adds: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    alt_label: Optional[Union[str, list[str]]] = empty_list()
    analyzes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    archived_at: Optional[Union[str, D3fendUri]] = None
    associated_with: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    attached_to: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    attack_id: Optional[str] = None
    attack_may_be_countered_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    authenticates: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    authorizes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    available: Optional[Union[str, D3fendDateTime]] = None
    blocks: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    broader: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    broader_transitive: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    capec_id: Optional[str] = None
    carried_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    carries: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    caused_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    causes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    comment: Optional[Union[str, list[str]]] = empty_list()
    comments: Optional[str] = None
    communicates_with: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    confidence: Optional[str] = None
    configures: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    connected_to: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    connects: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    contained_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    contains: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    contributor: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    control_name: Optional[str] = None
    controlled_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    controls: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    copies: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    copy_of: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    corrupts: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    counters: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    created: Optional[Union[str, D3fendDateTime]] = None
    created_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    creates: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    cwe_id: Optional[str] = None
    d3f_label: Optional[Union[str, list[str]]] = empty_list()
    d3fend_annotation: Optional[str] = None
    d3fend_comment: Optional[str] = None
    d3fend_id: Optional[str] = None
    date_value: Optional[Union[str, D3fendDateTime]] = None
    deceives: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    deceives_with: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    decodes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    definition: Optional[Union[str, list[str]]] = empty_list()
    deletes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    dependent: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    depends_on: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    deprecated: Optional[Union[bool, Bool]] = None
    derived_from: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    description: Optional[str] = None
    detects: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    disables: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    disjoint_with: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    display_baseurl: Optional[str] = None
    display_order: Optional[int] = None
    display_priority: Optional[int] = None
    drives: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    employed_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    employs: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    enabled_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    enables: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    encodes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    encrypts: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    end: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    enforces: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    enumerates: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    erases: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    evaluated_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    evaluates: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    evicts: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    exactly: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    example: Optional[str] = None
    excises: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    executed_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    executes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    expectation_rating: Optional[str] = None
    extends: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    filters: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    forges: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    fork: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    hardens: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_account: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_agent: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_audience: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_contribution: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_contributor: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_dependent: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_goal: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_link: Optional[Union[str, D3fendUri]] = None
    has_location: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_mediator: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_member: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_operating_mode: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_participant: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_prerequisite: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_procedure: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_recipient: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_sender: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    has_weakness: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    hides: Optional[Union[Union[str, D3fendDigitalArtifactId], list[Union[str, D3fendDigitalArtifactId]]]] = empty_list()
    identified_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    identifier: Optional[str] = None
    identifies: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    impairs: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    implemented_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    implements: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    initiates: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    injects: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    installs: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    instructed_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    instructs: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    interprets: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    inventoried_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    inventories: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    invoked_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    invokes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    is_defined_by: Optional[Union[str, list[str]]] = empty_list()
    isolates: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    issued: Optional[Union[str, D3fendDateTime]] = None
    jams: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    kb_abstract: Optional[str] = None
    kb_article: Optional[Union[str, list[str]]] = empty_list()
    kb_organization: Optional[str] = None
    kb_reference_of: Optional[Union[Union[str, D3fendTechniqueId], list[Union[str, D3fendTechniqueId]]]] = empty_list()
    kb_reference_title: Optional[str] = None
    label: Optional[Union[str, list[str]]] = empty_list()
    limits: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    loaded_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    loads: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    manages: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    mapped_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    maps: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_access: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_add: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_be_accessed_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_be_associated_with: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_be_contained_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_be_created_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_be_deceived_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_be_detected_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_be_evicted_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_be_hardened_against_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_be_invoked_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_be_isolated_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_be_modified_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_be_tactically_associated_with: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_block: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_contain: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_corrupt: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_counter: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_counter_attack: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_create: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_deceive: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_detect: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_disable: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_evaluate: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_evict: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_execute: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_harden: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_interpret: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_invoke: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_isolate: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_map: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_modify: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_produce: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_query: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_run: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    may_transfer: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    mediates_access_to: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    member_of: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    modified: Optional[Union[str, D3fendDateTime]] = None
    modified_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    modifies: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    modifies_part: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    monitors: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    name: Optional[str] = None
    narrower: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    narrower_transitive: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    neutralizes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    next: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    obfuscates: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    operates: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    operating_system: Optional[str] = None
    originates_from: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    owns: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    participates_in: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    powered_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    powers: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    preceded_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    precedes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    pref_label: Optional[str] = None
    prescribed_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    prescribes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    process_ancestor: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    process_command_line_arguments: Optional[str] = None
    process_environmental_variables: Optional[str] = None
    process_identifier: Optional[str] = None
    process_image_path: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    process_parent: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    process_user: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    produced_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    produces: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    provider: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    published: Optional[Union[str, D3fendDateTime]] = None
    quarantines: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    queries: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    rating: Optional[str] = None
    reads: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    receives: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    recorded_in: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    records: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    regenerates: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    related: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    release_date: Optional[str] = None
    restores: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    restricted_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    restricts: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    resumes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    risk_impact: Optional[int] = None
    risk_likelihood: Optional[int] = None
    runs: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    see_also: Optional[Union[str, list[str]]] = empty_list()
    semantic_relation: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    signed_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    signs: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    skos_pref_label: Optional[Union[str, list[str]]] = empty_list()
    spoofs: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    stage: Optional[str] = None
    start: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    strengthens: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    summarizes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    suspends: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    synonym: Optional[Union[str, list[str]]] = empty_list()
    terminates: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    text: Optional[str] = None
    title: Optional[str] = None
    transmits: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    unloads: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    unmounts: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    updates: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    use_limits: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    used_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    uses: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    valid: Optional[Union[str, D3fendDateTime]] = None
    validated_by: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    validates: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    verifies: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    version: Optional[Union[int, str]] = None
    weakness_of: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()
    windows_registry_key: Optional[str] = None
    windows_registry_value: Optional[str] = None
    writes: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendEntryId):
            self.id = D3fendEntryId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)

        if self.owl_kind is not None and not isinstance(self.owl_kind, D3fendOwlKind):
            self.owl_kind = D3fendOwlKind(self.owl_kind)

        if not isinstance(self.rdf_type, list):
            self.rdf_type = [self.rdf_type] if self.rdf_type is not None else []
        self.rdf_type = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.rdf_type]

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.subclass_of]

        if not isinstance(self.abuses, list):
            self.abuses = [self.abuses] if self.abuses is not None else []
        self.abuses = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.abuses]

        if not isinstance(self.access_mediated_by, list):
            self.access_mediated_by = [self.access_mediated_by] if self.access_mediated_by is not None else []
        self.access_mediated_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.access_mediated_by]

        if not isinstance(self.accessed_by, list):
            self.accessed_by = [self.accessed_by] if self.accessed_by is not None else []
        self.accessed_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.accessed_by]

        if not isinstance(self.accesses, list):
            self.accesses = [self.accesses] if self.accesses is not None else []
        self.accesses = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.accesses]

        if not isinstance(self.addressed_by, list):
            self.addressed_by = [self.addressed_by] if self.addressed_by is not None else []
        self.addressed_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.addressed_by]

        if not isinstance(self.addresses, list):
            self.addresses = [self.addresses] if self.addresses is not None else []
        self.addresses = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.addresses]

        if not isinstance(self.adds, list):
            self.adds = [self.adds] if self.adds is not None else []
        self.adds = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.adds]

        if not isinstance(self.alt_label, list):
            self.alt_label = [self.alt_label] if self.alt_label is not None else []
        self.alt_label = [v if isinstance(v, str) else str(v) for v in self.alt_label]

        if not isinstance(self.analyzes, list):
            self.analyzes = [self.analyzes] if self.analyzes is not None else []
        self.analyzes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.analyzes]

        if self.archived_at is not None and not isinstance(self.archived_at, D3fendUri):
            self.archived_at = D3fendUri(self.archived_at)

        if not isinstance(self.associated_with, list):
            self.associated_with = [self.associated_with] if self.associated_with is not None else []
        self.associated_with = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.associated_with]

        if not isinstance(self.attached_to, list):
            self.attached_to = [self.attached_to] if self.attached_to is not None else []
        self.attached_to = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.attached_to]

        if self.attack_id is not None and not isinstance(self.attack_id, str):
            self.attack_id = str(self.attack_id)

        if not isinstance(self.attack_may_be_countered_by, list):
            self.attack_may_be_countered_by = [self.attack_may_be_countered_by] if self.attack_may_be_countered_by is not None else []
        self.attack_may_be_countered_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.attack_may_be_countered_by]

        if not isinstance(self.authenticates, list):
            self.authenticates = [self.authenticates] if self.authenticates is not None else []
        self.authenticates = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.authenticates]

        if not isinstance(self.authorizes, list):
            self.authorizes = [self.authorizes] if self.authorizes is not None else []
        self.authorizes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.authorizes]

        if self.available is not None and not isinstance(self.available, D3fendDateTime):
            self.available = D3fendDateTime(self.available)

        if not isinstance(self.blocks, list):
            self.blocks = [self.blocks] if self.blocks is not None else []
        self.blocks = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.blocks]

        if not isinstance(self.broader, list):
            self.broader = [self.broader] if self.broader is not None else []
        self.broader = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.broader]

        if not isinstance(self.broader_transitive, list):
            self.broader_transitive = [self.broader_transitive] if self.broader_transitive is not None else []
        self.broader_transitive = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.broader_transitive]

        if self.capec_id is not None and not isinstance(self.capec_id, str):
            self.capec_id = str(self.capec_id)

        if not isinstance(self.carried_by, list):
            self.carried_by = [self.carried_by] if self.carried_by is not None else []
        self.carried_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.carried_by]

        if not isinstance(self.carries, list):
            self.carries = [self.carries] if self.carries is not None else []
        self.carries = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.carries]

        if not isinstance(self.caused_by, list):
            self.caused_by = [self.caused_by] if self.caused_by is not None else []
        self.caused_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.caused_by]

        if not isinstance(self.causes, list):
            self.causes = [self.causes] if self.causes is not None else []
        self.causes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.causes]

        if not isinstance(self.comment, list):
            self.comment = [self.comment] if self.comment is not None else []
        self.comment = [v if isinstance(v, str) else str(v) for v in self.comment]

        if self.comments is not None and not isinstance(self.comments, str):
            self.comments = str(self.comments)

        if not isinstance(self.communicates_with, list):
            self.communicates_with = [self.communicates_with] if self.communicates_with is not None else []
        self.communicates_with = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.communicates_with]

        if self.confidence is not None and not isinstance(self.confidence, str):
            self.confidence = str(self.confidence)

        if not isinstance(self.configures, list):
            self.configures = [self.configures] if self.configures is not None else []
        self.configures = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.configures]

        if not isinstance(self.connected_to, list):
            self.connected_to = [self.connected_to] if self.connected_to is not None else []
        self.connected_to = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.connected_to]

        if not isinstance(self.connects, list):
            self.connects = [self.connects] if self.connects is not None else []
        self.connects = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.connects]

        if not isinstance(self.contained_by, list):
            self.contained_by = [self.contained_by] if self.contained_by is not None else []
        self.contained_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.contained_by]

        if not isinstance(self.contains, list):
            self.contains = [self.contains] if self.contains is not None else []
        self.contains = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.contains]

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.contributor]

        if self.control_name is not None and not isinstance(self.control_name, str):
            self.control_name = str(self.control_name)

        if not isinstance(self.controlled_by, list):
            self.controlled_by = [self.controlled_by] if self.controlled_by is not None else []
        self.controlled_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.controlled_by]

        if not isinstance(self.controls, list):
            self.controls = [self.controls] if self.controls is not None else []
        self.controls = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.controls]

        if not isinstance(self.copies, list):
            self.copies = [self.copies] if self.copies is not None else []
        self.copies = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.copies]

        if not isinstance(self.copy_of, list):
            self.copy_of = [self.copy_of] if self.copy_of is not None else []
        self.copy_of = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.copy_of]

        if not isinstance(self.corrupts, list):
            self.corrupts = [self.corrupts] if self.corrupts is not None else []
        self.corrupts = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.corrupts]

        if not isinstance(self.counters, list):
            self.counters = [self.counters] if self.counters is not None else []
        self.counters = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.counters]

        if self.created is not None and not isinstance(self.created, D3fendDateTime):
            self.created = D3fendDateTime(self.created)

        if not isinstance(self.created_by, list):
            self.created_by = [self.created_by] if self.created_by is not None else []
        self.created_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.created_by]

        if not isinstance(self.creates, list):
            self.creates = [self.creates] if self.creates is not None else []
        self.creates = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.creates]

        if self.cwe_id is not None and not isinstance(self.cwe_id, str):
            self.cwe_id = str(self.cwe_id)

        if not isinstance(self.d3f_label, list):
            self.d3f_label = [self.d3f_label] if self.d3f_label is not None else []
        self.d3f_label = [v if isinstance(v, str) else str(v) for v in self.d3f_label]

        if self.d3fend_annotation is not None and not isinstance(self.d3fend_annotation, str):
            self.d3fend_annotation = str(self.d3fend_annotation)

        if self.d3fend_comment is not None and not isinstance(self.d3fend_comment, str):
            self.d3fend_comment = str(self.d3fend_comment)

        if self.d3fend_id is not None and not isinstance(self.d3fend_id, str):
            self.d3fend_id = str(self.d3fend_id)

        if self.date_value is not None and not isinstance(self.date_value, D3fendDateTime):
            self.date_value = D3fendDateTime(self.date_value)

        if not isinstance(self.deceives, list):
            self.deceives = [self.deceives] if self.deceives is not None else []
        self.deceives = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.deceives]

        if not isinstance(self.deceives_with, list):
            self.deceives_with = [self.deceives_with] if self.deceives_with is not None else []
        self.deceives_with = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.deceives_with]

        if not isinstance(self.decodes, list):
            self.decodes = [self.decodes] if self.decodes is not None else []
        self.decodes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.decodes]

        if not isinstance(self.definition, list):
            self.definition = [self.definition] if self.definition is not None else []
        self.definition = [v if isinstance(v, str) else str(v) for v in self.definition]

        if not isinstance(self.deletes, list):
            self.deletes = [self.deletes] if self.deletes is not None else []
        self.deletes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.deletes]

        if not isinstance(self.dependent, list):
            self.dependent = [self.dependent] if self.dependent is not None else []
        self.dependent = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.dependent]

        if not isinstance(self.depends_on, list):
            self.depends_on = [self.depends_on] if self.depends_on is not None else []
        self.depends_on = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.depends_on]

        if self.deprecated is not None and not isinstance(self.deprecated, Bool):
            self.deprecated = Bool(self.deprecated)

        if not isinstance(self.derived_from, list):
            self.derived_from = [self.derived_from] if self.derived_from is not None else []
        self.derived_from = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.derived_from]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.detects, list):
            self.detects = [self.detects] if self.detects is not None else []
        self.detects = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.detects]

        if not isinstance(self.disables, list):
            self.disables = [self.disables] if self.disables is not None else []
        self.disables = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.disables]

        if not isinstance(self.disjoint_with, list):
            self.disjoint_with = [self.disjoint_with] if self.disjoint_with is not None else []
        self.disjoint_with = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.disjoint_with]

        if self.display_baseurl is not None and not isinstance(self.display_baseurl, str):
            self.display_baseurl = str(self.display_baseurl)

        if self.display_order is not None and not isinstance(self.display_order, int):
            self.display_order = int(self.display_order)

        if self.display_priority is not None and not isinstance(self.display_priority, int):
            self.display_priority = int(self.display_priority)

        if not isinstance(self.drives, list):
            self.drives = [self.drives] if self.drives is not None else []
        self.drives = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.drives]

        if not isinstance(self.employed_by, list):
            self.employed_by = [self.employed_by] if self.employed_by is not None else []
        self.employed_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.employed_by]

        if not isinstance(self.employs, list):
            self.employs = [self.employs] if self.employs is not None else []
        self.employs = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.employs]

        if not isinstance(self.enabled_by, list):
            self.enabled_by = [self.enabled_by] if self.enabled_by is not None else []
        self.enabled_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.enabled_by]

        if not isinstance(self.enables, list):
            self.enables = [self.enables] if self.enables is not None else []
        self.enables = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.enables]

        if not isinstance(self.encodes, list):
            self.encodes = [self.encodes] if self.encodes is not None else []
        self.encodes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.encodes]

        if not isinstance(self.encrypts, list):
            self.encrypts = [self.encrypts] if self.encrypts is not None else []
        self.encrypts = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.encrypts]

        if not isinstance(self.end, list):
            self.end = [self.end] if self.end is not None else []
        self.end = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.end]

        if not isinstance(self.enforces, list):
            self.enforces = [self.enforces] if self.enforces is not None else []
        self.enforces = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.enforces]

        if not isinstance(self.enumerates, list):
            self.enumerates = [self.enumerates] if self.enumerates is not None else []
        self.enumerates = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.enumerates]

        if not isinstance(self.erases, list):
            self.erases = [self.erases] if self.erases is not None else []
        self.erases = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.erases]

        if not isinstance(self.evaluated_by, list):
            self.evaluated_by = [self.evaluated_by] if self.evaluated_by is not None else []
        self.evaluated_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.evaluated_by]

        if not isinstance(self.evaluates, list):
            self.evaluates = [self.evaluates] if self.evaluates is not None else []
        self.evaluates = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.evaluates]

        if not isinstance(self.evicts, list):
            self.evicts = [self.evicts] if self.evicts is not None else []
        self.evicts = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.evicts]

        if not isinstance(self.exactly, list):
            self.exactly = [self.exactly] if self.exactly is not None else []
        self.exactly = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.exactly]

        if self.example is not None and not isinstance(self.example, str):
            self.example = str(self.example)

        if not isinstance(self.excises, list):
            self.excises = [self.excises] if self.excises is not None else []
        self.excises = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.excises]

        if not isinstance(self.executed_by, list):
            self.executed_by = [self.executed_by] if self.executed_by is not None else []
        self.executed_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.executed_by]

        if not isinstance(self.executes, list):
            self.executes = [self.executes] if self.executes is not None else []
        self.executes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.executes]

        if self.expectation_rating is not None and not isinstance(self.expectation_rating, str):
            self.expectation_rating = str(self.expectation_rating)

        if not isinstance(self.extends, list):
            self.extends = [self.extends] if self.extends is not None else []
        self.extends = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.extends]

        if not isinstance(self.filters, list):
            self.filters = [self.filters] if self.filters is not None else []
        self.filters = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.filters]

        if not isinstance(self.forges, list):
            self.forges = [self.forges] if self.forges is not None else []
        self.forges = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.forges]

        if not isinstance(self.fork, list):
            self.fork = [self.fork] if self.fork is not None else []
        self.fork = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.fork]

        if not isinstance(self.hardens, list):
            self.hardens = [self.hardens] if self.hardens is not None else []
        self.hardens = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.hardens]

        if not isinstance(self.has_account, list):
            self.has_account = [self.has_account] if self.has_account is not None else []
        self.has_account = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_account]

        if not isinstance(self.has_agent, list):
            self.has_agent = [self.has_agent] if self.has_agent is not None else []
        self.has_agent = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_agent]

        if not isinstance(self.has_audience, list):
            self.has_audience = [self.has_audience] if self.has_audience is not None else []
        self.has_audience = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_audience]

        if not isinstance(self.has_contribution, list):
            self.has_contribution = [self.has_contribution] if self.has_contribution is not None else []
        self.has_contribution = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_contribution]

        if not isinstance(self.has_contributor, list):
            self.has_contributor = [self.has_contributor] if self.has_contributor is not None else []
        self.has_contributor = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_contributor]

        if not isinstance(self.has_dependent, list):
            self.has_dependent = [self.has_dependent] if self.has_dependent is not None else []
        self.has_dependent = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_dependent]

        if not isinstance(self.has_goal, list):
            self.has_goal = [self.has_goal] if self.has_goal is not None else []
        self.has_goal = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_goal]

        if self.has_link is not None and not isinstance(self.has_link, D3fendUri):
            self.has_link = D3fendUri(self.has_link)

        if not isinstance(self.has_location, list):
            self.has_location = [self.has_location] if self.has_location is not None else []
        self.has_location = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_location]

        if not isinstance(self.has_mediator, list):
            self.has_mediator = [self.has_mediator] if self.has_mediator is not None else []
        self.has_mediator = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_mediator]

        if not isinstance(self.has_member, list):
            self.has_member = [self.has_member] if self.has_member is not None else []
        self.has_member = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_member]

        if not isinstance(self.has_operating_mode, list):
            self.has_operating_mode = [self.has_operating_mode] if self.has_operating_mode is not None else []
        self.has_operating_mode = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_operating_mode]

        if not isinstance(self.has_participant, list):
            self.has_participant = [self.has_participant] if self.has_participant is not None else []
        self.has_participant = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_participant]

        if not isinstance(self.has_prerequisite, list):
            self.has_prerequisite = [self.has_prerequisite] if self.has_prerequisite is not None else []
        self.has_prerequisite = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_prerequisite]

        if not isinstance(self.has_procedure, list):
            self.has_procedure = [self.has_procedure] if self.has_procedure is not None else []
        self.has_procedure = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_procedure]

        if not isinstance(self.has_recipient, list):
            self.has_recipient = [self.has_recipient] if self.has_recipient is not None else []
        self.has_recipient = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_recipient]

        if not isinstance(self.has_sender, list):
            self.has_sender = [self.has_sender] if self.has_sender is not None else []
        self.has_sender = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_sender]

        if not isinstance(self.has_weakness, list):
            self.has_weakness = [self.has_weakness] if self.has_weakness is not None else []
        self.has_weakness = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.has_weakness]

        if not isinstance(self.hides, list):
            self.hides = [self.hides] if self.hides is not None else []
        self.hides = [v if isinstance(v, D3fendDigitalArtifactId) else D3fendDigitalArtifactId(v) for v in self.hides]

        if not isinstance(self.identified_by, list):
            self.identified_by = [self.identified_by] if self.identified_by is not None else []
        self.identified_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.identified_by]

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if not isinstance(self.identifies, list):
            self.identifies = [self.identifies] if self.identifies is not None else []
        self.identifies = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.identifies]

        if not isinstance(self.impairs, list):
            self.impairs = [self.impairs] if self.impairs is not None else []
        self.impairs = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.impairs]

        if not isinstance(self.implemented_by, list):
            self.implemented_by = [self.implemented_by] if self.implemented_by is not None else []
        self.implemented_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.implemented_by]

        if not isinstance(self.implements, list):
            self.implements = [self.implements] if self.implements is not None else []
        self.implements = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.implements]

        if not isinstance(self.initiates, list):
            self.initiates = [self.initiates] if self.initiates is not None else []
        self.initiates = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.initiates]

        if not isinstance(self.injects, list):
            self.injects = [self.injects] if self.injects is not None else []
        self.injects = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.injects]

        if not isinstance(self.installs, list):
            self.installs = [self.installs] if self.installs is not None else []
        self.installs = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.installs]

        if not isinstance(self.instructed_by, list):
            self.instructed_by = [self.instructed_by] if self.instructed_by is not None else []
        self.instructed_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.instructed_by]

        if not isinstance(self.instructs, list):
            self.instructs = [self.instructs] if self.instructs is not None else []
        self.instructs = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.instructs]

        if not isinstance(self.interprets, list):
            self.interprets = [self.interprets] if self.interprets is not None else []
        self.interprets = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.interprets]

        if not isinstance(self.inventoried_by, list):
            self.inventoried_by = [self.inventoried_by] if self.inventoried_by is not None else []
        self.inventoried_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.inventoried_by]

        if not isinstance(self.inventories, list):
            self.inventories = [self.inventories] if self.inventories is not None else []
        self.inventories = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.inventories]

        if not isinstance(self.invoked_by, list):
            self.invoked_by = [self.invoked_by] if self.invoked_by is not None else []
        self.invoked_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.invoked_by]

        if not isinstance(self.invokes, list):
            self.invokes = [self.invokes] if self.invokes is not None else []
        self.invokes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.invokes]

        if not isinstance(self.is_defined_by, list):
            self.is_defined_by = [self.is_defined_by] if self.is_defined_by is not None else []
        self.is_defined_by = [v if isinstance(v, str) else str(v) for v in self.is_defined_by]

        if not isinstance(self.isolates, list):
            self.isolates = [self.isolates] if self.isolates is not None else []
        self.isolates = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.isolates]

        if self.issued is not None and not isinstance(self.issued, D3fendDateTime):
            self.issued = D3fendDateTime(self.issued)

        if not isinstance(self.jams, list):
            self.jams = [self.jams] if self.jams is not None else []
        self.jams = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.jams]

        if self.kb_abstract is not None and not isinstance(self.kb_abstract, str):
            self.kb_abstract = str(self.kb_abstract)

        if not isinstance(self.kb_article, list):
            self.kb_article = [self.kb_article] if self.kb_article is not None else []
        self.kb_article = [v if isinstance(v, str) else str(v) for v in self.kb_article]

        if self.kb_organization is not None and not isinstance(self.kb_organization, str):
            self.kb_organization = str(self.kb_organization)

        if not isinstance(self.kb_reference_of, list):
            self.kb_reference_of = [self.kb_reference_of] if self.kb_reference_of is not None else []
        self.kb_reference_of = [v if isinstance(v, D3fendTechniqueId) else D3fendTechniqueId(v) for v in self.kb_reference_of]

        if self.kb_reference_title is not None and not isinstance(self.kb_reference_title, str):
            self.kb_reference_title = str(self.kb_reference_title)

        if not isinstance(self.label, list):
            self.label = [self.label] if self.label is not None else []
        self.label = [v if isinstance(v, str) else str(v) for v in self.label]

        if not isinstance(self.limits, list):
            self.limits = [self.limits] if self.limits is not None else []
        self.limits = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.limits]

        if not isinstance(self.loaded_by, list):
            self.loaded_by = [self.loaded_by] if self.loaded_by is not None else []
        self.loaded_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.loaded_by]

        if not isinstance(self.loads, list):
            self.loads = [self.loads] if self.loads is not None else []
        self.loads = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.loads]

        if not isinstance(self.manages, list):
            self.manages = [self.manages] if self.manages is not None else []
        self.manages = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.manages]

        if not isinstance(self.mapped_by, list):
            self.mapped_by = [self.mapped_by] if self.mapped_by is not None else []
        self.mapped_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.mapped_by]

        if not isinstance(self.maps, list):
            self.maps = [self.maps] if self.maps is not None else []
        self.maps = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.maps]

        if not isinstance(self.may_access, list):
            self.may_access = [self.may_access] if self.may_access is not None else []
        self.may_access = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_access]

        if not isinstance(self.may_add, list):
            self.may_add = [self.may_add] if self.may_add is not None else []
        self.may_add = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_add]

        if not isinstance(self.may_be_accessed_by, list):
            self.may_be_accessed_by = [self.may_be_accessed_by] if self.may_be_accessed_by is not None else []
        self.may_be_accessed_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_be_accessed_by]

        if not isinstance(self.may_be_associated_with, list):
            self.may_be_associated_with = [self.may_be_associated_with] if self.may_be_associated_with is not None else []
        self.may_be_associated_with = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_be_associated_with]

        if not isinstance(self.may_be_contained_by, list):
            self.may_be_contained_by = [self.may_be_contained_by] if self.may_be_contained_by is not None else []
        self.may_be_contained_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_be_contained_by]

        if not isinstance(self.may_be_created_by, list):
            self.may_be_created_by = [self.may_be_created_by] if self.may_be_created_by is not None else []
        self.may_be_created_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_be_created_by]

        if not isinstance(self.may_be_deceived_by, list):
            self.may_be_deceived_by = [self.may_be_deceived_by] if self.may_be_deceived_by is not None else []
        self.may_be_deceived_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_be_deceived_by]

        if not isinstance(self.may_be_detected_by, list):
            self.may_be_detected_by = [self.may_be_detected_by] if self.may_be_detected_by is not None else []
        self.may_be_detected_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_be_detected_by]

        if not isinstance(self.may_be_evicted_by, list):
            self.may_be_evicted_by = [self.may_be_evicted_by] if self.may_be_evicted_by is not None else []
        self.may_be_evicted_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_be_evicted_by]

        if not isinstance(self.may_be_hardened_against_by, list):
            self.may_be_hardened_against_by = [self.may_be_hardened_against_by] if self.may_be_hardened_against_by is not None else []
        self.may_be_hardened_against_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_be_hardened_against_by]

        if not isinstance(self.may_be_invoked_by, list):
            self.may_be_invoked_by = [self.may_be_invoked_by] if self.may_be_invoked_by is not None else []
        self.may_be_invoked_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_be_invoked_by]

        if not isinstance(self.may_be_isolated_by, list):
            self.may_be_isolated_by = [self.may_be_isolated_by] if self.may_be_isolated_by is not None else []
        self.may_be_isolated_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_be_isolated_by]

        if not isinstance(self.may_be_modified_by, list):
            self.may_be_modified_by = [self.may_be_modified_by] if self.may_be_modified_by is not None else []
        self.may_be_modified_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_be_modified_by]

        if not isinstance(self.may_be_tactically_associated_with, list):
            self.may_be_tactically_associated_with = [self.may_be_tactically_associated_with] if self.may_be_tactically_associated_with is not None else []
        self.may_be_tactically_associated_with = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_be_tactically_associated_with]

        if not isinstance(self.may_block, list):
            self.may_block = [self.may_block] if self.may_block is not None else []
        self.may_block = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_block]

        if not isinstance(self.may_contain, list):
            self.may_contain = [self.may_contain] if self.may_contain is not None else []
        self.may_contain = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_contain]

        if not isinstance(self.may_corrupt, list):
            self.may_corrupt = [self.may_corrupt] if self.may_corrupt is not None else []
        self.may_corrupt = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_corrupt]

        if not isinstance(self.may_counter, list):
            self.may_counter = [self.may_counter] if self.may_counter is not None else []
        self.may_counter = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_counter]

        if not isinstance(self.may_counter_attack, list):
            self.may_counter_attack = [self.may_counter_attack] if self.may_counter_attack is not None else []
        self.may_counter_attack = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_counter_attack]

        if not isinstance(self.may_create, list):
            self.may_create = [self.may_create] if self.may_create is not None else []
        self.may_create = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_create]

        if not isinstance(self.may_deceive, list):
            self.may_deceive = [self.may_deceive] if self.may_deceive is not None else []
        self.may_deceive = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_deceive]

        if not isinstance(self.may_detect, list):
            self.may_detect = [self.may_detect] if self.may_detect is not None else []
        self.may_detect = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_detect]

        if not isinstance(self.may_disable, list):
            self.may_disable = [self.may_disable] if self.may_disable is not None else []
        self.may_disable = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_disable]

        if not isinstance(self.may_evaluate, list):
            self.may_evaluate = [self.may_evaluate] if self.may_evaluate is not None else []
        self.may_evaluate = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_evaluate]

        if not isinstance(self.may_evict, list):
            self.may_evict = [self.may_evict] if self.may_evict is not None else []
        self.may_evict = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_evict]

        if not isinstance(self.may_execute, list):
            self.may_execute = [self.may_execute] if self.may_execute is not None else []
        self.may_execute = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_execute]

        if not isinstance(self.may_harden, list):
            self.may_harden = [self.may_harden] if self.may_harden is not None else []
        self.may_harden = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_harden]

        if not isinstance(self.may_interpret, list):
            self.may_interpret = [self.may_interpret] if self.may_interpret is not None else []
        self.may_interpret = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_interpret]

        if not isinstance(self.may_invoke, list):
            self.may_invoke = [self.may_invoke] if self.may_invoke is not None else []
        self.may_invoke = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_invoke]

        if not isinstance(self.may_isolate, list):
            self.may_isolate = [self.may_isolate] if self.may_isolate is not None else []
        self.may_isolate = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_isolate]

        if not isinstance(self.may_map, list):
            self.may_map = [self.may_map] if self.may_map is not None else []
        self.may_map = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_map]

        if not isinstance(self.may_modify, list):
            self.may_modify = [self.may_modify] if self.may_modify is not None else []
        self.may_modify = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_modify]

        if not isinstance(self.may_produce, list):
            self.may_produce = [self.may_produce] if self.may_produce is not None else []
        self.may_produce = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_produce]

        if not isinstance(self.may_query, list):
            self.may_query = [self.may_query] if self.may_query is not None else []
        self.may_query = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_query]

        if not isinstance(self.may_run, list):
            self.may_run = [self.may_run] if self.may_run is not None else []
        self.may_run = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_run]

        if not isinstance(self.may_transfer, list):
            self.may_transfer = [self.may_transfer] if self.may_transfer is not None else []
        self.may_transfer = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.may_transfer]

        if not isinstance(self.mediates_access_to, list):
            self.mediates_access_to = [self.mediates_access_to] if self.mediates_access_to is not None else []
        self.mediates_access_to = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.mediates_access_to]

        if not isinstance(self.member_of, list):
            self.member_of = [self.member_of] if self.member_of is not None else []
        self.member_of = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.member_of]

        if self.modified is not None and not isinstance(self.modified, D3fendDateTime):
            self.modified = D3fendDateTime(self.modified)

        if not isinstance(self.modified_by, list):
            self.modified_by = [self.modified_by] if self.modified_by is not None else []
        self.modified_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.modified_by]

        if not isinstance(self.modifies, list):
            self.modifies = [self.modifies] if self.modifies is not None else []
        self.modifies = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.modifies]

        if not isinstance(self.modifies_part, list):
            self.modifies_part = [self.modifies_part] if self.modifies_part is not None else []
        self.modifies_part = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.modifies_part]

        if not isinstance(self.monitors, list):
            self.monitors = [self.monitors] if self.monitors is not None else []
        self.monitors = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.monitors]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.narrower, list):
            self.narrower = [self.narrower] if self.narrower is not None else []
        self.narrower = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.narrower]

        if not isinstance(self.narrower_transitive, list):
            self.narrower_transitive = [self.narrower_transitive] if self.narrower_transitive is not None else []
        self.narrower_transitive = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.narrower_transitive]

        if not isinstance(self.neutralizes, list):
            self.neutralizes = [self.neutralizes] if self.neutralizes is not None else []
        self.neutralizes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.neutralizes]

        if not isinstance(self.next, list):
            self.next = [self.next] if self.next is not None else []
        self.next = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.next]

        if not isinstance(self.obfuscates, list):
            self.obfuscates = [self.obfuscates] if self.obfuscates is not None else []
        self.obfuscates = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.obfuscates]

        if not isinstance(self.operates, list):
            self.operates = [self.operates] if self.operates is not None else []
        self.operates = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.operates]

        if self.operating_system is not None and not isinstance(self.operating_system, str):
            self.operating_system = str(self.operating_system)

        if not isinstance(self.originates_from, list):
            self.originates_from = [self.originates_from] if self.originates_from is not None else []
        self.originates_from = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.originates_from]

        if not isinstance(self.owns, list):
            self.owns = [self.owns] if self.owns is not None else []
        self.owns = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.owns]

        if not isinstance(self.participates_in, list):
            self.participates_in = [self.participates_in] if self.participates_in is not None else []
        self.participates_in = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.participates_in]

        if not isinstance(self.powered_by, list):
            self.powered_by = [self.powered_by] if self.powered_by is not None else []
        self.powered_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.powered_by]

        if not isinstance(self.powers, list):
            self.powers = [self.powers] if self.powers is not None else []
        self.powers = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.powers]

        if not isinstance(self.preceded_by, list):
            self.preceded_by = [self.preceded_by] if self.preceded_by is not None else []
        self.preceded_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.preceded_by]

        if not isinstance(self.precedes, list):
            self.precedes = [self.precedes] if self.precedes is not None else []
        self.precedes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.precedes]

        if self.pref_label is not None and not isinstance(self.pref_label, str):
            self.pref_label = str(self.pref_label)

        if not isinstance(self.prescribed_by, list):
            self.prescribed_by = [self.prescribed_by] if self.prescribed_by is not None else []
        self.prescribed_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.prescribed_by]

        if not isinstance(self.prescribes, list):
            self.prescribes = [self.prescribes] if self.prescribes is not None else []
        self.prescribes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.prescribes]

        if not isinstance(self.process_ancestor, list):
            self.process_ancestor = [self.process_ancestor] if self.process_ancestor is not None else []
        self.process_ancestor = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.process_ancestor]

        if self.process_command_line_arguments is not None and not isinstance(self.process_command_line_arguments, str):
            self.process_command_line_arguments = str(self.process_command_line_arguments)

        if self.process_environmental_variables is not None and not isinstance(self.process_environmental_variables, str):
            self.process_environmental_variables = str(self.process_environmental_variables)

        if self.process_identifier is not None and not isinstance(self.process_identifier, str):
            self.process_identifier = str(self.process_identifier)

        if not isinstance(self.process_image_path, list):
            self.process_image_path = [self.process_image_path] if self.process_image_path is not None else []
        self.process_image_path = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.process_image_path]

        if not isinstance(self.process_parent, list):
            self.process_parent = [self.process_parent] if self.process_parent is not None else []
        self.process_parent = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.process_parent]

        if not isinstance(self.process_user, list):
            self.process_user = [self.process_user] if self.process_user is not None else []
        self.process_user = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.process_user]

        if not isinstance(self.produced_by, list):
            self.produced_by = [self.produced_by] if self.produced_by is not None else []
        self.produced_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.produced_by]

        if not isinstance(self.produces, list):
            self.produces = [self.produces] if self.produces is not None else []
        self.produces = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.produces]

        if not isinstance(self.provider, list):
            self.provider = [self.provider] if self.provider is not None else []
        self.provider = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.provider]

        if self.published is not None and not isinstance(self.published, D3fendDateTime):
            self.published = D3fendDateTime(self.published)

        if not isinstance(self.quarantines, list):
            self.quarantines = [self.quarantines] if self.quarantines is not None else []
        self.quarantines = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.quarantines]

        if not isinstance(self.queries, list):
            self.queries = [self.queries] if self.queries is not None else []
        self.queries = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.queries]

        if self.rating is not None and not isinstance(self.rating, str):
            self.rating = str(self.rating)

        if not isinstance(self.reads, list):
            self.reads = [self.reads] if self.reads is not None else []
        self.reads = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.reads]

        if not isinstance(self.receives, list):
            self.receives = [self.receives] if self.receives is not None else []
        self.receives = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.receives]

        if not isinstance(self.recorded_in, list):
            self.recorded_in = [self.recorded_in] if self.recorded_in is not None else []
        self.recorded_in = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.recorded_in]

        if not isinstance(self.records, list):
            self.records = [self.records] if self.records is not None else []
        self.records = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.records]

        if not isinstance(self.regenerates, list):
            self.regenerates = [self.regenerates] if self.regenerates is not None else []
        self.regenerates = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.regenerates]

        if not isinstance(self.related, list):
            self.related = [self.related] if self.related is not None else []
        self.related = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.related]

        if self.release_date is not None and not isinstance(self.release_date, str):
            self.release_date = str(self.release_date)

        if not isinstance(self.restores, list):
            self.restores = [self.restores] if self.restores is not None else []
        self.restores = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.restores]

        if not isinstance(self.restricted_by, list):
            self.restricted_by = [self.restricted_by] if self.restricted_by is not None else []
        self.restricted_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.restricted_by]

        if not isinstance(self.restricts, list):
            self.restricts = [self.restricts] if self.restricts is not None else []
        self.restricts = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.restricts]

        if not isinstance(self.resumes, list):
            self.resumes = [self.resumes] if self.resumes is not None else []
        self.resumes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.resumes]

        if self.risk_impact is not None and not isinstance(self.risk_impact, int):
            self.risk_impact = int(self.risk_impact)

        if self.risk_likelihood is not None and not isinstance(self.risk_likelihood, int):
            self.risk_likelihood = int(self.risk_likelihood)

        if not isinstance(self.runs, list):
            self.runs = [self.runs] if self.runs is not None else []
        self.runs = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.runs]

        if not isinstance(self.see_also, list):
            self.see_also = [self.see_also] if self.see_also is not None else []
        self.see_also = [v if isinstance(v, str) else str(v) for v in self.see_also]

        if not isinstance(self.semantic_relation, list):
            self.semantic_relation = [self.semantic_relation] if self.semantic_relation is not None else []
        self.semantic_relation = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.semantic_relation]

        if not isinstance(self.signed_by, list):
            self.signed_by = [self.signed_by] if self.signed_by is not None else []
        self.signed_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.signed_by]

        if not isinstance(self.signs, list):
            self.signs = [self.signs] if self.signs is not None else []
        self.signs = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.signs]

        if not isinstance(self.skos_pref_label, list):
            self.skos_pref_label = [self.skos_pref_label] if self.skos_pref_label is not None else []
        self.skos_pref_label = [v if isinstance(v, str) else str(v) for v in self.skos_pref_label]

        if not isinstance(self.spoofs, list):
            self.spoofs = [self.spoofs] if self.spoofs is not None else []
        self.spoofs = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.spoofs]

        if self.stage is not None and not isinstance(self.stage, str):
            self.stage = str(self.stage)

        if not isinstance(self.start, list):
            self.start = [self.start] if self.start is not None else []
        self.start = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.start]

        if not isinstance(self.strengthens, list):
            self.strengthens = [self.strengthens] if self.strengthens is not None else []
        self.strengthens = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.strengthens]

        if not isinstance(self.summarizes, list):
            self.summarizes = [self.summarizes] if self.summarizes is not None else []
        self.summarizes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.summarizes]

        if not isinstance(self.suspends, list):
            self.suspends = [self.suspends] if self.suspends is not None else []
        self.suspends = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.suspends]

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, str) else str(v) for v in self.synonym]

        if not isinstance(self.terminates, list):
            self.terminates = [self.terminates] if self.terminates is not None else []
        self.terminates = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.terminates]

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.transmits, list):
            self.transmits = [self.transmits] if self.transmits is not None else []
        self.transmits = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.transmits]

        if not isinstance(self.unloads, list):
            self.unloads = [self.unloads] if self.unloads is not None else []
        self.unloads = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.unloads]

        if not isinstance(self.unmounts, list):
            self.unmounts = [self.unmounts] if self.unmounts is not None else []
        self.unmounts = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.unmounts]

        if not isinstance(self.updates, list):
            self.updates = [self.updates] if self.updates is not None else []
        self.updates = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.updates]

        if not isinstance(self.use_limits, list):
            self.use_limits = [self.use_limits] if self.use_limits is not None else []
        self.use_limits = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.use_limits]

        if not isinstance(self.used_by, list):
            self.used_by = [self.used_by] if self.used_by is not None else []
        self.used_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.used_by]

        if not isinstance(self.uses, list):
            self.uses = [self.uses] if self.uses is not None else []
        self.uses = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.uses]

        if self.valid is not None and not isinstance(self.valid, D3fendDateTime):
            self.valid = D3fendDateTime(self.valid)

        if not isinstance(self.validated_by, list):
            self.validated_by = [self.validated_by] if self.validated_by is not None else []
        self.validated_by = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.validated_by]

        if not isinstance(self.validates, list):
            self.validates = [self.validates] if self.validates is not None else []
        self.validates = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.validates]

        if not isinstance(self.verifies, list):
            self.verifies = [self.verifies] if self.verifies is not None else []
        self.verifies = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.verifies]

        if self.version is not None and not isinstance(self.version, (int, str)):
            value = self.version
            for _coerce in (lambda: int(value), lambda: str(value)):
                try:
                    self.version = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[int, str] could be constructed from {value!r} for slot version")

        if not isinstance(self.weakness_of, list):
            self.weakness_of = [self.weakness_of] if self.weakness_of is not None else []
        self.weakness_of = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.weakness_of]

        if self.windows_registry_key is not None and not isinstance(self.windows_registry_key, str):
            self.windows_registry_key = str(self.windows_registry_key)

        if self.windows_registry_value is not None and not isinstance(self.windows_registry_value, str):
            self.windows_registry_value = str(self.windows_registry_value)

        if not isinstance(self.writes, list):
            self.writes = [self.writes] if self.writes is not None else []
        self.writes = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.writes]

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class D3fendThing(D3fendEntry):
    """
    An entry with no narrower kind here: a root of D3FEND's tree, or a term such as a plan, a step, a group, a time or
    a condition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3FEND["D3fendThing"]
    class_class_curie: ClassVar[str] = "d3fend:D3fendThing"
    class_name: ClassVar[str] = "D3fendThing"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendThing

    id: Union[str, D3fendThingId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendThingId):
            self.id = D3fendThingId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendThreatModelThing(D3fendEntry):
    """
    A term from a threat model outside D3FEND, such as ATT&CK, ATLAS, SPARTA or CAPEC, with no narrower kind here.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["ExternalThreatModelThing"]
    class_class_curie: ClassVar[str] = "d3f:ExternalThreatModelThing"
    class_name: ClassVar[str] = "D3fendThreatModelThing"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendThreatModelThing

    id: Union[str, D3fendThreatModelThingId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendThreatModelThingId):
            self.id = D3fendThreatModelThingId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendThreatModelTechnique(D3fendThreatModelThing):
    """
    A technique of ATT&CK Mobile, ATT&CK ICS, ATLAS or SPARTA. D3FEND places these under their frameworks and not
    under its own offensive technique.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3FEND["D3fendThreatModelTechnique"]
    class_class_curie: ClassVar[str] = "d3fend:D3fendThreatModelTechnique"
    class_name: ClassVar[str] = "D3fendThreatModelTechnique"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendThreatModelTechnique

    id: Union[str, D3fendThreatModelTechniqueId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendThreatModelTechniqueId):
            self.id = D3fendThreatModelTechniqueId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendAttackDataSource(D3fendThreatModelThing):
    """
    A data source of ATT&CK Enterprise, which D3FEND relates to its digital artifacts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["ATTACKEnterpriseDataSource"]
    class_class_curie: ClassVar[str] = "d3f:ATTACKEnterpriseDataSource"
    class_name: ClassVar[str] = "D3fendAttackDataSource"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendAttackDataSource

    id: Union[str, D3fendAttackDataSourceId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendAttackDataSourceId):
            self.id = D3fendAttackDataSourceId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendAttackMitigation(D3fendThreatModelThing):
    """
    A mitigation of ATT&CK Enterprise, which D3FEND relates to its defensive techniques.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["ATTACKEnterpriseMitigation"]
    class_class_curie: ClassVar[str] = "d3f:ATTACKEnterpriseMitigation"
    class_name: ClassVar[str] = "D3fendAttackMitigation"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendAttackMitigation

    id: Union[str, D3fendAttackMitigationId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendAttackMitigationId):
            self.id = D3fendAttackMitigationId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendControlCatalog(D3fendEntry):
    """
    A published list of controls, one edition of which holds D3FEND's control entries as members.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["ControlCatalog"]
    class_class_curie: ClassVar[str] = "d3f:ControlCatalog"
    class_name: ClassVar[str] = "D3fendControlCatalog"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendControlCatalog

    id: Union[str, D3fendControlCatalogId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendControlCatalogId):
            self.id = D3fendControlCatalogId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendExternalControl(D3fendEntry):
    """
    A control another catalogue defines, which D3FEND relates to its techniques.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["ExternalControl"]
    class_class_curie: ClassVar[str] = "d3f:ExternalControl"
    class_name: ClassVar[str] = "D3fendExternalControl"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendExternalControl

    id: Union[str, D3fendExternalControlId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendExternalControlId):
            self.id = D3fendExternalControlId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendCciControl(D3fendExternalControl):
    """
    An item of the Control Correlation Identifier list that DISA publishes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["CCIControl"]
    class_class_curie: ClassVar[str] = "d3f:CCIControl"
    class_name: ClassVar[str] = "D3fendCciControl"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendCciControl

    id: Union[str, D3fendCciControlId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendCciControlId):
            self.id = D3fendCciControlId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendNistControl(D3fendExternalControl):
    """
    A control or control enhancement of a revision of NIST SP 800-53.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["NISTControl"]
    class_class_curie: ClassVar[str] = "d3f:NISTControl"
    class_name: ClassVar[str] = "D3fendNistControl"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendNistControl

    id: Union[str, D3fendNistControlId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendNistControlId):
            self.id = D3fendNistControlId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendTechniqueReference(D3fendEntry):
    """
    A source behind a knowledge base article, such as a patent or a paper. rdf_type says which of D3FEND's reference
    types it is, since all of them hold the same fields.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["TechniqueReference"]
    class_class_curie: ClassVar[str] = "d3f:TechniqueReference"
    class_name: ClassVar[str] = "D3fendTechniqueReference"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendTechniqueReference

    id: Union[str, D3fendTechniqueReferenceId] = None
    type: str = None
    kb_author: Optional[str] = None
    kb_mitre_analysis: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendTechniqueReferenceId):
            self.id = D3fendTechniqueReferenceId(self.id)

        if self.kb_author is not None and not isinstance(self.kb_author, str):
            self.kb_author = str(self.kb_author)

        if self.kb_mitre_analysis is not None and not isinstance(self.kb_mitre_analysis, str):
            self.kb_mitre_analysis = str(self.kb_mitre_analysis)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendAgent(D3fendEntry):
    """
    Something capable of intentional action, such as a person, an organization or an attacker.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["Agent"]
    class_class_curie: ClassVar[str] = "d3f:Agent"
    class_name: ClassVar[str] = "D3fendAgent"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendAgent

    id: Union[str, D3fendAgentId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendAgentId):
            self.id = D3fendAgentId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendEvent(D3fendEntry):
    """
    Something that happens in a system over a finite span of time, with the artifacts that take part in it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["Event"]
    class_class_curie: ClassVar[str] = "d3f:Event"
    class_name: ClassVar[str] = "D3fendEvent"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendEvent

    id: Union[str, D3fendEventId] = None
    type: str = None
    has_input: Optional[Union[Union[str, D3fendArtifactId], list[Union[str, D3fendArtifactId]]]] = empty_list()
    has_output: Optional[Union[Union[str, D3fendArtifactId], list[Union[str, D3fendArtifactId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendEventId):
            self.id = D3fendEventId(self.id)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, D3fendArtifactId) else D3fendArtifactId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, D3fendArtifactId) else D3fendArtifactId(v) for v in self.has_output]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendArtifact(D3fendEntry):
    """
    A man-made thing that techniques act on. Those that are not digital, such as a physical lock, stay here.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["Artifact"]
    class_class_curie: ClassVar[str] = "d3f:Artifact"
    class_name: ClassVar[str] = "D3fendArtifact"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendArtifact

    id: Union[str, D3fendArtifactId] = None
    type: str = None
    input_of: Optional[Union[Union[str, D3fendEventId], list[Union[str, D3fendEventId]]]] = empty_list()
    may_have_weakness: Optional[Union[Union[str, D3fendWeaknessId], list[Union[str, D3fendWeaknessId]]]] = empty_list()
    output_of: Optional[Union[Union[str, D3fendEventId], list[Union[str, D3fendEventId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendArtifactId):
            self.id = D3fendArtifactId(self.id)

        if not isinstance(self.input_of, list):
            self.input_of = [self.input_of] if self.input_of is not None else []
        self.input_of = [v if isinstance(v, D3fendEventId) else D3fendEventId(v) for v in self.input_of]

        if not isinstance(self.may_have_weakness, list):
            self.may_have_weakness = [self.may_have_weakness] if self.may_have_weakness is not None else []
        self.may_have_weakness = [v if isinstance(v, D3fendWeaknessId) else D3fendWeaknessId(v) for v in self.may_have_weakness]

        if not isinstance(self.output_of, list):
            self.output_of = [self.output_of] if self.output_of is not None else []
        self.output_of = [v if isinstance(v, D3fendEventId) else D3fendEventId(v) for v in self.output_of]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendDigitalArtifact(D3fendArtifact):
    """
    An artifact that carries information for a digital system, such as a file, a process or a network packet: the
    common ground where offensive and defensive techniques meet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["DigitalArtifact"]
    class_class_curie: ClassVar[str] = "d3f:DigitalArtifact"
    class_name: ClassVar[str] = "D3fendDigitalArtifact"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendDigitalArtifact

    id: Union[str, D3fendDigitalArtifactId] = None
    type: str = None
    process_security_context: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendDigitalArtifactId):
            self.id = D3fendDigitalArtifactId(self.id)

        if self.process_security_context is not None and not isinstance(self.process_security_context, str):
            self.process_security_context = str(self.process_security_context)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendWeakness(D3fendEntry):
    """
    A condition in a system component that can contribute to a vulnerability. Nearly all of these entries name a CWE
    entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["Weakness"]
    class_class_curie: ClassVar[str] = "d3f:Weakness"
    class_name: ClassVar[str] = "D3fendWeakness"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendWeakness

    id: Union[str, D3fendWeaknessId] = None
    type: str = None
    may_be_weakness_of: Optional[Union[Union[str, D3fendArtifactId], list[Union[str, D3fendArtifactId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendWeaknessId):
            self.id = D3fendWeaknessId(self.id)

        if not isinstance(self.may_be_weakness_of, list):
            self.may_be_weakness_of = [self.may_be_weakness_of] if self.may_be_weakness_of is not None else []
        self.may_be_weakness_of = [v if isinstance(v, D3fendArtifactId) else D3fendArtifactId(v) for v in self.may_be_weakness_of]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendTechnique(D3fendEntry):
    """
    A way of doing something in or to a computer system. Its narrower kinds say whose way it is.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["Technique"]
    class_class_curie: ClassVar[str] = "d3f:Technique"
    class_name: ClassVar[str] = "D3fendTechnique"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendTechnique

    id: Union[str, D3fendTechniqueId] = None
    type: str = None
    kb_reference: Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendTechniqueId):
            self.id = D3fendTechniqueId(self.id)

        if not isinstance(self.kb_reference, list):
            self.kb_reference = [self.kb_reference] if self.kb_reference is not None else []
        self.kb_reference = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.kb_reference]

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendAnalyticTechnique(D3fendTechnique):
    """
    A mathematical method a defensive technique can use to find patterns in data, such as a form of machine learning
    or a statistical measure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["AnalyticTechnique"]
    class_class_curie: ClassVar[str] = "d3f:AnalyticTechnique"
    class_name: ClassVar[str] = "D3fendAnalyticTechnique"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendAnalyticTechnique

    id: Union[str, D3fendAnalyticTechniqueId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendAnalyticTechniqueId):
            self.id = D3fendAnalyticTechniqueId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendOffensiveTechnique(D3fendTechnique):
    """
    A way an adversary acts, drawn from ATT&CK Enterprise, related to the artifacts it touches and to the tactic it
    serves.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["OffensiveTechnique"]
    class_class_curie: ClassVar[str] = "d3f:OffensiveTechnique"
    class_name: ClassVar[str] = "D3fendOffensiveTechnique"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendOffensiveTechnique

    id: Union[str, D3fendOffensiveTechniqueId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendOffensiveTechniqueId):
            self.id = D3fendOffensiveTechniqueId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendDefensiveTechnique(D3fendTechnique):
    """
    A countermeasure: a method that makes a system harder to attack, related to the artifacts it acts on and to the
    tactic it enables.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["DefensiveTechnique"]
    class_class_curie: ClassVar[str] = "d3f:DefensiveTechnique"
    class_name: ClassVar[str] = "D3fendDefensiveTechnique"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendDefensiveTechnique

    id: Union[str, D3fendDefensiveTechniqueId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendDefensiveTechniqueId):
            self.id = D3fendDefensiveTechniqueId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendGoal(D3fendEntry):
    """
    An aim that a tactic or a technique serves.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["Goal"]
    class_class_curie: ClassVar[str] = "d3f:Goal"
    class_name: ClassVar[str] = "D3fendGoal"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendGoal

    id: Union[str, D3fendGoalId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendGoalId):
            self.id = D3fendGoalId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendOffensiveTactic(D3fendGoal):
    """
    A tactic of an adversary, from the ATT&CK, ATLAS or SPARTA framework, which an offensive technique enables.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["OffensiveTactic"]
    class_class_curie: ClassVar[str] = "d3f:OffensiveTactic"
    class_name: ClassVar[str] = "D3fendOffensiveTactic"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendOffensiveTactic

    id: Union[str, D3fendOffensiveTacticId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendOffensiveTacticId):
            self.id = D3fendOffensiveTacticId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendDefensiveTactic(D3fendGoal):
    """
    One of D3FEND's seven defensive aims, such as Detect or Harden, which a defensive technique enables.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3F["DefensiveTactic"]
    class_class_curie: ClassVar[str] = "d3f:DefensiveTactic"
    class_name: ClassVar[str] = "D3fendDefensiveTactic"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendDefensiveTactic

    id: Union[str, D3fendDefensiveTacticId] = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, D3fendDefensiveTacticId):
            self.id = D3fendDefensiveTacticId(self.id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class D3fendDisjointGroup(YAMLRoot):
    """
    A set of D3FEND classes of which no two share an instance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = D3FEND["D3fendDisjointGroup"]
    class_class_curie: ClassVar[str] = "d3fend:D3fendDisjointGroup"
    class_name: ClassVar[str] = "D3fendDisjointGroup"
    class_model_uri: ClassVar[URIRef] = D3FEND.D3fendDisjointGroup

    members: Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.members):
            self.MissingRequiredField("members")
        if not isinstance(self.members, list):
            self.members = [self.members] if self.members is not None else []
        self.members = [v if isinstance(v, D3fendEntryId) else D3fendEntryId(v) for v in self.members]

        super().__post_init__(**kwargs)


# Enumerations
class D3fendOwlKind(EnumDefinitionImpl):
    """
    How the ontology declares a term.
    """
    individual = PermissibleValue(
        text="individual",
        title="Individual",
        description="The term is an owl:NamedIndividual only.",
        meaning=OWL["NamedIndividual"])
    class_and_individual = PermissibleValue(
        text="class_and_individual",
        title="Class and Individual",
        description="The term is punned, both an owl:Class and an owl:NamedIndividual.")

    _defn = EnumDefinition(
        name="D3fendOwlKind",
        description="How the ontology declares a term.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "class",
            PermissibleValue(
                text="class",
                title="Class",
                description="The term is an owl:Class only.",
                meaning=OWL["Class"]))

# Slots
class slots:
    pass

slots.id = Slot(uri=D3FEND.id, name="id", curie=D3FEND.curie('id'),
                   model_uri=D3FEND.id, domain=None, range=URIRef,
                   pattern=re.compile(r'^d3f:\S+$'))

slots.type = Slot(uri=D3FEND.type, name="type", curie=D3FEND.curie('type'),
                   model_uri=D3FEND.type, domain=None, range=str)

slots.owl_kind = Slot(uri=D3FEND.owl_kind, name="owl_kind", curie=D3FEND.curie('owl_kind'),
                   model_uri=D3FEND.owl_kind, domain=None, range=Optional[Union[str, "D3fendOwlKind"]])

slots.rdf_type = Slot(uri=RDF.type, name="rdf_type", curie=RDF.curie('type'),
                   model_uri=D3FEND.rdf_type, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.subclass_of = Slot(uri=RDFS.subClassOf, name="subclass_of", curie=RDFS.curie('subClassOf'),
                   model_uri=D3FEND.subclass_of, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.abuses = Slot(uri=D3F.abuses, name="abuses", curie=D3F.curie('abuses'),
                   model_uri=D3FEND.abuses, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.access_mediated_by = Slot(uri=D3F['access-mediated-by'], name="access_mediated_by", curie=D3F.curie('access-mediated-by'),
                   model_uri=D3FEND.access_mediated_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.accessed_by = Slot(uri=D3F['accessed-by'], name="accessed_by", curie=D3F.curie('accessed-by'),
                   model_uri=D3FEND.accessed_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.accesses = Slot(uri=D3F.accesses, name="accesses", curie=D3F.curie('accesses'),
                   model_uri=D3FEND.accesses, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.addressed_by = Slot(uri=D3F['addressed-by'], name="addressed_by", curie=D3F.curie('addressed-by'),
                   model_uri=D3FEND.addressed_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.addresses = Slot(uri=D3F.addresses, name="addresses", curie=D3F.curie('addresses'),
                   model_uri=D3FEND.addresses, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.adds = Slot(uri=D3F.adds, name="adds", curie=D3F.curie('adds'),
                   model_uri=D3FEND.adds, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.alt_label = Slot(uri=SKOS.altLabel, name="alt_label", curie=SKOS.curie('altLabel'),
                   model_uri=D3FEND.alt_label, domain=None, range=Optional[Union[str, list[str]]])

slots.analyzes = Slot(uri=D3F.analyzes, name="analyzes", curie=D3F.curie('analyzes'),
                   model_uri=D3FEND.analyzes, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.archived_at = Slot(uri=D3F['archived-at'], name="archived_at", curie=D3F.curie('archived-at'),
                   model_uri=D3FEND.archived_at, domain=None, range=Optional[Union[str, D3fendUri]])

slots.associated_with = Slot(uri=D3F['associated-with'], name="associated_with", curie=D3F.curie('associated-with'),
                   model_uri=D3FEND.associated_with, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.attached_to = Slot(uri=D3F['attached-to'], name="attached_to", curie=D3F.curie('attached-to'),
                   model_uri=D3FEND.attached_to, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.attack_id = Slot(uri=D3F['attack-id'], name="attack_id", curie=D3F.curie('attack-id'),
                   model_uri=D3FEND.attack_id, domain=None, range=Optional[str])

slots.attack_kb_annotation = Slot(uri=D3F['attack-kb-annotation'], name="attack_kb_annotation", curie=D3F.curie('attack-kb-annotation'),
                   model_uri=D3FEND.attack_kb_annotation, domain=None, range=Optional[str])

slots.attack_kb_data_property = Slot(uri=D3F['attack-kb-data-property'], name="attack_kb_data_property", curie=D3F.curie('attack-kb-data-property'),
                   model_uri=D3FEND.attack_kb_data_property, domain=None, range=Optional[str])

slots.attack_may_be_countered_by = Slot(uri=D3F['attack-may-be-countered-by'], name="attack_may_be_countered_by", curie=D3F.curie('attack-may-be-countered-by'),
                   model_uri=D3FEND.attack_may_be_countered_by, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.authenticates = Slot(uri=D3F.authenticates, name="authenticates", curie=D3F.curie('authenticates'),
                   model_uri=D3FEND.authenticates, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.authorizes = Slot(uri=D3F.authorizes, name="authorizes", curie=D3F.curie('authorizes'),
                   model_uri=D3FEND.authorizes, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.available = Slot(uri=D3F.available, name="available", curie=D3F.curie('available'),
                   model_uri=D3FEND.available, domain=None, range=Optional[Union[str, D3fendDateTime]])

slots.blocks = Slot(uri=D3F.blocks, name="blocks", curie=D3F.curie('blocks'),
                   model_uri=D3FEND.blocks, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.broader = Slot(uri=D3F.broader, name="broader", curie=D3F.curie('broader'),
                   model_uri=D3FEND.broader, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.broader_transitive = Slot(uri=D3F['broader-transitive'], name="broader_transitive", curie=D3F.curie('broader-transitive'),
                   model_uri=D3FEND.broader_transitive, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.capec_id = Slot(uri=D3F['capec-id'], name="capec_id", curie=D3F.curie('capec-id'),
                   model_uri=D3FEND.capec_id, domain=None, range=Optional[str])

slots.carried_by = Slot(uri=D3F['carried-by'], name="carried_by", curie=D3F.curie('carried-by'),
                   model_uri=D3FEND.carried_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.carries = Slot(uri=D3F.carries, name="carries", curie=D3F.curie('carries'),
                   model_uri=D3FEND.carries, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.caused_by = Slot(uri=D3F['caused-by'], name="caused_by", curie=D3F.curie('caused-by'),
                   model_uri=D3FEND.caused_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.causes = Slot(uri=D3F.causes, name="causes", curie=D3F.curie('causes'),
                   model_uri=D3FEND.causes, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.comment = Slot(uri=RDFS.comment, name="comment", curie=RDFS.curie('comment'),
                   model_uri=D3FEND.comment, domain=None, range=Optional[Union[str, list[str]]])

slots.comments = Slot(uri=D3F.comments, name="comments", curie=D3F.curie('comments'),
                   model_uri=D3FEND.comments, domain=None, range=Optional[str])

slots.communicates_with = Slot(uri=D3F['communicates-with'], name="communicates_with", curie=D3F.curie('communicates-with'),
                   model_uri=D3FEND.communicates_with, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.confidence = Slot(uri=D3F.confidence, name="confidence", curie=D3F.curie('confidence'),
                   model_uri=D3FEND.confidence, domain=None, range=Optional[str])

slots.configures = Slot(uri=D3F.configures, name="configures", curie=D3F.curie('configures'),
                   model_uri=D3FEND.configures, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.connected_to = Slot(uri=D3F['connected-to'], name="connected_to", curie=D3F.curie('connected-to'),
                   model_uri=D3FEND.connected_to, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.connects = Slot(uri=D3F.connects, name="connects", curie=D3F.curie('connects'),
                   model_uri=D3FEND.connects, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.contained_by = Slot(uri=D3F['contained-by'], name="contained_by", curie=D3F.curie('contained-by'),
                   model_uri=D3FEND.contained_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.contains = Slot(uri=D3F.contains, name="contains", curie=D3F.curie('contains'),
                   model_uri=D3FEND.contains, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.contributor = Slot(uri=D3F.contributor, name="contributor", curie=D3F.curie('contributor'),
                   model_uri=D3FEND.contributor, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.control_name = Slot(uri=D3F['control-name'], name="control_name", curie=D3F.curie('control-name'),
                   model_uri=D3FEND.control_name, domain=None, range=Optional[str])

slots.controlled_by = Slot(uri=D3F['controlled-by'], name="controlled_by", curie=D3F.curie('controlled-by'),
                   model_uri=D3FEND.controlled_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.controls = Slot(uri=D3F.controls, name="controls", curie=D3F.curie('controls'),
                   model_uri=D3FEND.controls, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.copies = Slot(uri=D3F.copies, name="copies", curie=D3F.curie('copies'),
                   model_uri=D3FEND.copies, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.copy_of = Slot(uri=D3F['copy-of'], name="copy_of", curie=D3F.curie('copy-of'),
                   model_uri=D3FEND.copy_of, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.corrupts = Slot(uri=D3F.corrupts, name="corrupts", curie=D3F.curie('corrupts'),
                   model_uri=D3FEND.corrupts, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.counters = Slot(uri=D3F.counters, name="counters", curie=D3F.curie('counters'),
                   model_uri=D3FEND.counters, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.created = Slot(uri=D3F.created, name="created", curie=D3F.curie('created'),
                   model_uri=D3FEND.created, domain=None, range=Optional[Union[str, D3fendDateTime]])

slots.created_by = Slot(uri=D3F['created-by'], name="created_by", curie=D3F.curie('created-by'),
                   model_uri=D3FEND.created_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.creates = Slot(uri=D3F.creates, name="creates", curie=D3F.curie('creates'),
                   model_uri=D3FEND.creates, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.cwe_id = Slot(uri=D3F['cwe-id'], name="cwe_id", curie=D3F.curie('cwe-id'),
                   model_uri=D3FEND.cwe_id, domain=None, range=Optional[str])

slots.cwe_kb_annotation = Slot(uri=D3F['cwe-kb-annotation'], name="cwe_kb_annotation", curie=D3F.curie('cwe-kb-annotation'),
                   model_uri=D3FEND.cwe_kb_annotation, domain=None, range=Optional[str])

slots.d3f_label = Slot(uri=D3F.label, name="d3f_label", curie=D3F.curie('label'),
                   model_uri=D3FEND.d3f_label, domain=None, range=Optional[Union[str, list[str]]])

slots.d3fend_annotation = Slot(uri=D3F['d3fend-annotation'], name="d3fend_annotation", curie=D3F.curie('d3fend-annotation'),
                   model_uri=D3FEND.d3fend_annotation, domain=None, range=Optional[str])

slots.d3fend_artifact_data_property = Slot(uri=D3F['d3fend-artifact-data-property'], name="d3fend_artifact_data_property", curie=D3F.curie('d3fend-artifact-data-property'),
                   model_uri=D3FEND.d3fend_artifact_data_property, domain=None, range=Optional[str])

slots.d3fend_catalog_annotation_property = Slot(uri=D3F['d3fend-catalog-annotation-property'], name="d3fend_catalog_annotation_property", curie=D3F.curie('d3fend-catalog-annotation-property'),
                   model_uri=D3FEND.d3fend_catalog_annotation_property, domain=None, range=Optional[str])

slots.d3fend_catalog_data_property = Slot(uri=D3F['d3fend-catalog-data-property'], name="d3fend_catalog_data_property", curie=D3F.curie('d3fend-catalog-data-property'),
                   model_uri=D3FEND.d3fend_catalog_data_property, domain=None, range=Optional[str])

slots.d3fend_comment = Slot(uri=D3F['d3fend-comment'], name="d3fend_comment", curie=D3F.curie('d3fend-comment'),
                   model_uri=D3FEND.d3fend_comment, domain=None, range=Optional[str])

slots.d3fend_data_property = Slot(uri=D3F['d3fend-data-property'], name="d3fend_data_property", curie=D3F.curie('d3fend-data-property'),
                   model_uri=D3FEND.d3fend_data_property, domain=None, range=Optional[str])

slots.d3fend_display_annotation = Slot(uri=D3F['d3fend-display-annotation'], name="d3fend_display_annotation", curie=D3F.curie('d3fend-display-annotation'),
                   model_uri=D3FEND.d3fend_display_annotation, domain=None, range=Optional[str])

slots.d3fend_display_property = Slot(uri=D3F['d3fend-display-property'], name="d3fend_display_property", curie=D3F.curie('d3fend-display-property'),
                   model_uri=D3FEND.d3fend_display_property, domain=None, range=Optional[str])

slots.d3fend_external_control_data_property = Slot(uri=D3F['d3fend-external-control-data-property'], name="d3fend_external_control_data_property", curie=D3F.curie('d3fend-external-control-data-property'),
                   model_uri=D3FEND.d3fend_external_control_data_property, domain=None, range=Optional[str])

slots.d3fend_general_object_property = Slot(uri=D3F['d3fend-general-object-property'], name="d3fend_general_object_property", curie=D3F.curie('d3fend-general-object-property'),
                   model_uri=D3FEND.d3fend_general_object_property, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.d3fend_id = Slot(uri=D3F['d3fend-id'], name="d3fend_id", curie=D3F.curie('d3fend-id'),
                   model_uri=D3FEND.d3fend_id, domain=None, range=Optional[str])

slots.d3fend_kb_annotation_property = Slot(uri=D3F['d3fend-kb-annotation-property'], name="d3fend_kb_annotation_property", curie=D3F.curie('d3fend-kb-annotation-property'),
                   model_uri=D3FEND.d3fend_kb_annotation_property, domain=None, range=Optional[str])

slots.d3fend_kb_data_property = Slot(uri=D3F['d3fend-kb-data-property'], name="d3fend_kb_data_property", curie=D3F.curie('d3fend-kb-data-property'),
                   model_uri=D3FEND.d3fend_kb_data_property, domain=None, range=Optional[str])

slots.d3fend_kb_object_property = Slot(uri=D3F['d3fend-kb-object-property'], name="d3fend_kb_object_property", curie=D3F.curie('d3fend-kb-object-property'),
                   model_uri=D3FEND.d3fend_kb_object_property, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.d3fend_kb_reference_annotation = Slot(uri=D3F['d3fend-kb-reference-annotation'], name="d3fend_kb_reference_annotation", curie=D3F.curie('d3fend-kb-reference-annotation'),
                   model_uri=D3FEND.d3fend_kb_reference_annotation, domain=None, range=Optional[str])

slots.d3fend_object_property = Slot(uri=D3F['d3fend-object-property'], name="d3fend_object_property", curie=D3F.curie('d3fend-object-property'),
                   model_uri=D3FEND.d3fend_object_property, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.d3fend_process_object_property = Slot(uri=D3F['d3fend-process-object-property'], name="d3fend_process_object_property", curie=D3F.curie('d3fend-process-object-property'),
                   model_uri=D3FEND.d3fend_process_object_property, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.d3fend_tactical_verb_property = Slot(uri=D3F['d3fend-tactical-verb-property'], name="d3fend_tactical_verb_property", curie=D3F.curie('d3fend-tactical-verb-property'),
                   model_uri=D3FEND.d3fend_tactical_verb_property, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.d3fend_use_case_object_property = Slot(uri=D3F['d3fend-use-case-object-property'], name="d3fend_use_case_object_property", curie=D3F.curie('d3fend-use-case-object-property'),
                   model_uri=D3FEND.d3fend_use_case_object_property, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.date_value = Slot(uri=D3F.date, name="date_value", curie=D3F.curie('date'),
                   model_uri=D3FEND.date_value, domain=None, range=Optional[Union[str, D3fendDateTime]])

slots.deceives = Slot(uri=D3F.deceives, name="deceives", curie=D3F.curie('deceives'),
                   model_uri=D3FEND.deceives, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.deceives_with = Slot(uri=D3F['deceives-with'], name="deceives_with", curie=D3F.curie('deceives-with'),
                   model_uri=D3FEND.deceives_with, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.decodes = Slot(uri=D3F.decodes, name="decodes", curie=D3F.curie('decodes'),
                   model_uri=D3FEND.decodes, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.definition = Slot(uri=D3F.definition, name="definition", curie=D3F.curie('definition'),
                   model_uri=D3FEND.definition, domain=None, range=Optional[Union[str, list[str]]])

slots.deletes = Slot(uri=D3F.deletes, name="deletes", curie=D3F.curie('deletes'),
                   model_uri=D3FEND.deletes, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.dependent = Slot(uri=D3F.dependent, name="dependent", curie=D3F.curie('dependent'),
                   model_uri=D3FEND.dependent, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.depends_on = Slot(uri=D3F['depends-on'], name="depends_on", curie=D3F.curie('depends-on'),
                   model_uri=D3FEND.depends_on, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.deprecated = Slot(uri=OWL.deprecated, name="deprecated", curie=OWL.curie('deprecated'),
                   model_uri=D3FEND.deprecated, domain=None, range=Optional[Union[bool, Bool]])

slots.derived_from = Slot(uri=D3F['derived-from'], name="derived_from", curie=D3F.curie('derived-from'),
                   model_uri=D3FEND.derived_from, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.description = Slot(uri=D3F.description, name="description", curie=D3F.curie('description'),
                   model_uri=D3FEND.description, domain=None, range=Optional[str])

slots.detects = Slot(uri=D3F.detects, name="detects", curie=D3F.curie('detects'),
                   model_uri=D3FEND.detects, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.disables = Slot(uri=D3F.disables, name="disables", curie=D3F.curie('disables'),
                   model_uri=D3FEND.disables, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.disjoint_with = Slot(uri=OWL.disjointWith, name="disjoint_with", curie=OWL.curie('disjointWith'),
                   model_uri=D3FEND.disjoint_with, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.display_baseurl = Slot(uri=D3F['display-baseurl'], name="display_baseurl", curie=D3F.curie('display-baseurl'),
                   model_uri=D3FEND.display_baseurl, domain=None, range=Optional[str])

slots.display_order = Slot(uri=D3F['display-order'], name="display_order", curie=D3F.curie('display-order'),
                   model_uri=D3FEND.display_order, domain=None, range=Optional[int])

slots.display_priority = Slot(uri=D3F['display-priority'], name="display_priority", curie=D3F.curie('display-priority'),
                   model_uri=D3FEND.display_priority, domain=None, range=Optional[int])

slots.drives = Slot(uri=D3F.drives, name="drives", curie=D3F.curie('drives'),
                   model_uri=D3FEND.drives, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.employed_by = Slot(uri=D3F['employed-by'], name="employed_by", curie=D3F.curie('employed-by'),
                   model_uri=D3FEND.employed_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.employs = Slot(uri=D3F.employs, name="employs", curie=D3F.curie('employs'),
                   model_uri=D3FEND.employs, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.enabled_by = Slot(uri=D3F['enabled-by'], name="enabled_by", curie=D3F.curie('enabled-by'),
                   model_uri=D3FEND.enabled_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.enables = Slot(uri=D3F.enables, name="enables", curie=D3F.curie('enables'),
                   model_uri=D3FEND.enables, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.encodes = Slot(uri=D3F.encodes, name="encodes", curie=D3F.curie('encodes'),
                   model_uri=D3FEND.encodes, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.encrypts = Slot(uri=D3F.encrypts, name="encrypts", curie=D3F.curie('encrypts'),
                   model_uri=D3FEND.encrypts, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.end = Slot(uri=D3F.end, name="end", curie=D3F.curie('end'),
                   model_uri=D3FEND.end, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.enforces = Slot(uri=D3F.enforces, name="enforces", curie=D3F.curie('enforces'),
                   model_uri=D3FEND.enforces, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.enumerates = Slot(uri=D3F.enumerates, name="enumerates", curie=D3F.curie('enumerates'),
                   model_uri=D3FEND.enumerates, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.erases = Slot(uri=D3F.erases, name="erases", curie=D3F.curie('erases'),
                   model_uri=D3FEND.erases, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.evaluated_by = Slot(uri=D3F['evaluated-by'], name="evaluated_by", curie=D3F.curie('evaluated-by'),
                   model_uri=D3FEND.evaluated_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.evaluates = Slot(uri=D3F.evaluates, name="evaluates", curie=D3F.curie('evaluates'),
                   model_uri=D3FEND.evaluates, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.evicts = Slot(uri=D3F.evicts, name="evicts", curie=D3F.curie('evicts'),
                   model_uri=D3FEND.evicts, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.exactly = Slot(uri=D3F.exactly, name="exactly", curie=D3F.curie('exactly'),
                   model_uri=D3FEND.exactly, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.example = Slot(uri=SKOS.example, name="example", curie=SKOS.curie('example'),
                   model_uri=D3FEND.example, domain=None, range=Optional[str])

slots.excises = Slot(uri=D3F.excises, name="excises", curie=D3F.curie('excises'),
                   model_uri=D3FEND.excises, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.executed_by = Slot(uri=D3F['executed-by'], name="executed_by", curie=D3F.curie('executed-by'),
                   model_uri=D3FEND.executed_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.executes = Slot(uri=D3F.executes, name="executes", curie=D3F.curie('executes'),
                   model_uri=D3FEND.executes, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.expectation_rating = Slot(uri=D3F['expectation-rating'], name="expectation_rating", curie=D3F.curie('expectation-rating'),
                   model_uri=D3FEND.expectation_rating, domain=None, range=Optional[str])

slots.extends = Slot(uri=D3F.extends, name="extends", curie=D3F.curie('extends'),
                   model_uri=D3FEND.extends, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.filters = Slot(uri=D3F.filters, name="filters", curie=D3F.curie('filters'),
                   model_uri=D3FEND.filters, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.forges = Slot(uri=D3F.forges, name="forges", curie=D3F.curie('forges'),
                   model_uri=D3FEND.forges, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.fork = Slot(uri=D3F.fork, name="fork", curie=D3F.curie('fork'),
                   model_uri=D3FEND.fork, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.hardens = Slot(uri=D3F.hardens, name="hardens", curie=D3F.curie('hardens'),
                   model_uri=D3FEND.hardens, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_account = Slot(uri=D3F['has-account'], name="has_account", curie=D3F.curie('has-account'),
                   model_uri=D3FEND.has_account, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_agent = Slot(uri=D3F['has-agent'], name="has_agent", curie=D3F.curie('has-agent'),
                   model_uri=D3FEND.has_agent, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_audience = Slot(uri=D3F['has-audience'], name="has_audience", curie=D3F.curie('has-audience'),
                   model_uri=D3FEND.has_audience, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_contribution = Slot(uri=D3F['has-contribution'], name="has_contribution", curie=D3F.curie('has-contribution'),
                   model_uri=D3FEND.has_contribution, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_contributor = Slot(uri=D3F['has-contributor'], name="has_contributor", curie=D3F.curie('has-contributor'),
                   model_uri=D3FEND.has_contributor, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_dependent = Slot(uri=D3F['has-dependent'], name="has_dependent", curie=D3F.curie('has-dependent'),
                   model_uri=D3FEND.has_dependent, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_goal = Slot(uri=D3F['has-goal'], name="has_goal", curie=D3F.curie('has-goal'),
                   model_uri=D3FEND.has_goal, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_input = Slot(uri=D3F['has-input'], name="has_input", curie=D3F.curie('has-input'),
                   model_uri=D3FEND.has_input, domain=D3fendEvent, range=Optional[Union[Union[str, D3fendArtifactId], list[Union[str, D3fendArtifactId]]]])

slots.has_link = Slot(uri=D3F['has-link'], name="has_link", curie=D3F.curie('has-link'),
                   model_uri=D3FEND.has_link, domain=None, range=Optional[Union[str, D3fendUri]])

slots.has_location = Slot(uri=D3F['has-location'], name="has_location", curie=D3F.curie('has-location'),
                   model_uri=D3FEND.has_location, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_mediator = Slot(uri=D3F['has-mediator'], name="has_mediator", curie=D3F.curie('has-mediator'),
                   model_uri=D3FEND.has_mediator, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_member = Slot(uri=D3F['has-member'], name="has_member", curie=D3F.curie('has-member'),
                   model_uri=D3FEND.has_member, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_operating_mode = Slot(uri=D3F['has-operating-mode'], name="has_operating_mode", curie=D3F.curie('has-operating-mode'),
                   model_uri=D3FEND.has_operating_mode, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_output = Slot(uri=D3F['has-output'], name="has_output", curie=D3F.curie('has-output'),
                   model_uri=D3FEND.has_output, domain=D3fendEvent, range=Optional[Union[Union[str, D3fendArtifactId], list[Union[str, D3fendArtifactId]]]])

slots.has_participant = Slot(uri=D3F['has-participant'], name="has_participant", curie=D3F.curie('has-participant'),
                   model_uri=D3FEND.has_participant, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_prerequisite = Slot(uri=D3F['has-prerequisite'], name="has_prerequisite", curie=D3F.curie('has-prerequisite'),
                   model_uri=D3FEND.has_prerequisite, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_procedure = Slot(uri=D3F['has-procedure'], name="has_procedure", curie=D3F.curie('has-procedure'),
                   model_uri=D3FEND.has_procedure, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_recipient = Slot(uri=D3F['has-recipient'], name="has_recipient", curie=D3F.curie('has-recipient'),
                   model_uri=D3FEND.has_recipient, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_sender = Slot(uri=D3F['has-sender'], name="has_sender", curie=D3F.curie('has-sender'),
                   model_uri=D3FEND.has_sender, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.has_weakness = Slot(uri=D3F['has-weakness'], name="has_weakness", curie=D3F.curie('has-weakness'),
                   model_uri=D3FEND.has_weakness, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.hides = Slot(uri=D3F.hides, name="hides", curie=D3F.curie('hides'),
                   model_uri=D3FEND.hides, domain=None, range=Optional[Union[Union[str, D3fendDigitalArtifactId], list[Union[str, D3fendDigitalArtifactId]]]])

slots.identified_by = Slot(uri=D3F['identified-by'], name="identified_by", curie=D3F.curie('identified-by'),
                   model_uri=D3FEND.identified_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.identifier = Slot(uri=D3F.identifier, name="identifier", curie=D3F.curie('identifier'),
                   model_uri=D3FEND.identifier, domain=None, range=Optional[str])

slots.identifies = Slot(uri=D3F.identifies, name="identifies", curie=D3F.curie('identifies'),
                   model_uri=D3FEND.identifies, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.impairs = Slot(uri=D3F.impairs, name="impairs", curie=D3F.curie('impairs'),
                   model_uri=D3FEND.impairs, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.implemented_by = Slot(uri=D3F['implemented-by'], name="implemented_by", curie=D3F.curie('implemented-by'),
                   model_uri=D3FEND.implemented_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.implements = Slot(uri=D3F.implements, name="implements", curie=D3F.curie('implements'),
                   model_uri=D3FEND.implements, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.initiates = Slot(uri=D3F.initiates, name="initiates", curie=D3F.curie('initiates'),
                   model_uri=D3FEND.initiates, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.injects = Slot(uri=D3F.injects, name="injects", curie=D3F.curie('injects'),
                   model_uri=D3FEND.injects, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.input_of = Slot(uri=D3F['input-of'], name="input_of", curie=D3F.curie('input-of'),
                   model_uri=D3FEND.input_of, domain=D3fendArtifact, range=Optional[Union[Union[str, D3fendEventId], list[Union[str, D3fendEventId]]]])

slots.installs = Slot(uri=D3F.installs, name="installs", curie=D3F.curie('installs'),
                   model_uri=D3FEND.installs, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.instructed_by = Slot(uri=D3F['instructed-by'], name="instructed_by", curie=D3F.curie('instructed-by'),
                   model_uri=D3FEND.instructed_by, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.instructs = Slot(uri=D3F.instructs, name="instructs", curie=D3F.curie('instructs'),
                   model_uri=D3FEND.instructs, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.interprets = Slot(uri=D3F.interprets, name="interprets", curie=D3F.curie('interprets'),
                   model_uri=D3FEND.interprets, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.inventoried_by = Slot(uri=D3F['inventoried-by'], name="inventoried_by", curie=D3F.curie('inventoried-by'),
                   model_uri=D3FEND.inventoried_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.inventories = Slot(uri=D3F.inventories, name="inventories", curie=D3F.curie('inventories'),
                   model_uri=D3FEND.inventories, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.invoked_by = Slot(uri=D3F['invoked-by'], name="invoked_by", curie=D3F.curie('invoked-by'),
                   model_uri=D3FEND.invoked_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.invokes = Slot(uri=D3F.invokes, name="invokes", curie=D3F.curie('invokes'),
                   model_uri=D3FEND.invokes, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.is_defined_by = Slot(uri=RDFS.isDefinedBy, name="is_defined_by", curie=RDFS.curie('isDefinedBy'),
                   model_uri=D3FEND.is_defined_by, domain=None, range=Optional[Union[str, list[str]]])

slots.isolates = Slot(uri=D3F.isolates, name="isolates", curie=D3F.curie('isolates'),
                   model_uri=D3FEND.isolates, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.issued = Slot(uri=D3F.issued, name="issued", curie=D3F.curie('issued'),
                   model_uri=D3FEND.issued, domain=None, range=Optional[Union[str, D3fendDateTime]])

slots.jams = Slot(uri=D3F.jams, name="jams", curie=D3F.curie('jams'),
                   model_uri=D3FEND.jams, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.kb_abstract = Slot(uri=D3F['kb-abstract'], name="kb_abstract", curie=D3F.curie('kb-abstract'),
                   model_uri=D3FEND.kb_abstract, domain=None, range=Optional[str])

slots.kb_article = Slot(uri=D3F['kb-article'], name="kb_article", curie=D3F.curie('kb-article'),
                   model_uri=D3FEND.kb_article, domain=None, range=Optional[Union[str, list[str]]])

slots.kb_author = Slot(uri=D3F['kb-author'], name="kb_author", curie=D3F.curie('kb-author'),
                   model_uri=D3FEND.kb_author, domain=None, range=Optional[str])

slots.kb_mitre_analysis = Slot(uri=D3F['kb-mitre-analysis'], name="kb_mitre_analysis", curie=D3F.curie('kb-mitre-analysis'),
                   model_uri=D3FEND.kb_mitre_analysis, domain=None, range=Optional[str])

slots.kb_organization = Slot(uri=D3F['kb-organization'], name="kb_organization", curie=D3F.curie('kb-organization'),
                   model_uri=D3FEND.kb_organization, domain=None, range=Optional[str])

slots.kb_reference = Slot(uri=D3F['kb-reference'], name="kb_reference", curie=D3F.curie('kb-reference'),
                   model_uri=D3FEND.kb_reference, domain=D3fendTechnique, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.kb_reference_of = Slot(uri=D3F['kb-reference-of'], name="kb_reference_of", curie=D3F.curie('kb-reference-of'),
                   model_uri=D3FEND.kb_reference_of, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendTechniqueId], list[Union[str, D3fendTechniqueId]]]])

slots.kb_reference_title = Slot(uri=D3F['kb-reference-title'], name="kb_reference_title", curie=D3F.curie('kb-reference-title'),
                   model_uri=D3FEND.kb_reference_title, domain=None, range=Optional[str])

slots.label = Slot(uri=RDFS.label, name="label", curie=RDFS.curie('label'),
                   model_uri=D3FEND.label, domain=None, range=Optional[Union[str, list[str]]])

slots.limits = Slot(uri=D3F.limits, name="limits", curie=D3F.curie('limits'),
                   model_uri=D3FEND.limits, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.loaded_by = Slot(uri=D3F['loaded-by'], name="loaded_by", curie=D3F.curie('loaded-by'),
                   model_uri=D3FEND.loaded_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.loads = Slot(uri=D3F.loads, name="loads", curie=D3F.curie('loads'),
                   model_uri=D3FEND.loads, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.manages = Slot(uri=D3F.manages, name="manages", curie=D3F.curie('manages'),
                   model_uri=D3FEND.manages, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.mapped_by = Slot(uri=D3F['mapped-by'], name="mapped_by", curie=D3F.curie('mapped-by'),
                   model_uri=D3FEND.mapped_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.maps = Slot(uri=D3F.maps, name="maps", curie=D3F.curie('maps'),
                   model_uri=D3FEND.maps, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_access = Slot(uri=D3F['may-access'], name="may_access", curie=D3F.curie('may-access'),
                   model_uri=D3FEND.may_access, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_add = Slot(uri=D3F['may-add'], name="may_add", curie=D3F.curie('may-add'),
                   model_uri=D3FEND.may_add, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_be_accessed_by = Slot(uri=D3F['may-be-accessed-by'], name="may_be_accessed_by", curie=D3F.curie('may-be-accessed-by'),
                   model_uri=D3FEND.may_be_accessed_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_be_associated_with = Slot(uri=D3F['may-be-associated-with'], name="may_be_associated_with", curie=D3F.curie('may-be-associated-with'),
                   model_uri=D3FEND.may_be_associated_with, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_be_contained_by = Slot(uri=D3F['may-be-contained-by'], name="may_be_contained_by", curie=D3F.curie('may-be-contained-by'),
                   model_uri=D3FEND.may_be_contained_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_be_created_by = Slot(uri=D3F['may-be-created-by'], name="may_be_created_by", curie=D3F.curie('may-be-created-by'),
                   model_uri=D3FEND.may_be_created_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_be_deceived_by = Slot(uri=D3F['may-be-deceived-by'], name="may_be_deceived_by", curie=D3F.curie('may-be-deceived-by'),
                   model_uri=D3FEND.may_be_deceived_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_be_detected_by = Slot(uri=D3F['may-be-detected-by'], name="may_be_detected_by", curie=D3F.curie('may-be-detected-by'),
                   model_uri=D3FEND.may_be_detected_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_be_evicted_by = Slot(uri=D3F['may-be-evicted-by'], name="may_be_evicted_by", curie=D3F.curie('may-be-evicted-by'),
                   model_uri=D3FEND.may_be_evicted_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_be_hardened_against_by = Slot(uri=D3F['may-be-hardened-against-by'], name="may_be_hardened_against_by", curie=D3F.curie('may-be-hardened-against-by'),
                   model_uri=D3FEND.may_be_hardened_against_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_be_invoked_by = Slot(uri=D3F['may-be-invoked-by'], name="may_be_invoked_by", curie=D3F.curie('may-be-invoked-by'),
                   model_uri=D3FEND.may_be_invoked_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_be_isolated_by = Slot(uri=D3F['may-be-isolated-by'], name="may_be_isolated_by", curie=D3F.curie('may-be-isolated-by'),
                   model_uri=D3FEND.may_be_isolated_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_be_modified_by = Slot(uri=D3F['may-be-modified-by'], name="may_be_modified_by", curie=D3F.curie('may-be-modified-by'),
                   model_uri=D3FEND.may_be_modified_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_be_tactically_associated_with = Slot(uri=D3F['may-be-tactically-associated-with'], name="may_be_tactically_associated_with", curie=D3F.curie('may-be-tactically-associated-with'),
                   model_uri=D3FEND.may_be_tactically_associated_with, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_be_weakness_of = Slot(uri=D3F['may-be-weakness-of'], name="may_be_weakness_of", curie=D3F.curie('may-be-weakness-of'),
                   model_uri=D3FEND.may_be_weakness_of, domain=D3fendWeakness, range=Optional[Union[Union[str, D3fendArtifactId], list[Union[str, D3fendArtifactId]]]])

slots.may_block = Slot(uri=D3F['may-block'], name="may_block", curie=D3F.curie('may-block'),
                   model_uri=D3FEND.may_block, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_contain = Slot(uri=D3F['may-contain'], name="may_contain", curie=D3F.curie('may-contain'),
                   model_uri=D3FEND.may_contain, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_corrupt = Slot(uri=D3F['may-corrupt'], name="may_corrupt", curie=D3F.curie('may-corrupt'),
                   model_uri=D3FEND.may_corrupt, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_counter = Slot(uri=D3F['may-counter'], name="may_counter", curie=D3F.curie('may-counter'),
                   model_uri=D3FEND.may_counter, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_counter_attack = Slot(uri=D3F['may-counter-attack'], name="may_counter_attack", curie=D3F.curie('may-counter-attack'),
                   model_uri=D3FEND.may_counter_attack, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_create = Slot(uri=D3F['may-create'], name="may_create", curie=D3F.curie('may-create'),
                   model_uri=D3FEND.may_create, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_deceive = Slot(uri=D3F['may-deceive'], name="may_deceive", curie=D3F.curie('may-deceive'),
                   model_uri=D3FEND.may_deceive, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_detect = Slot(uri=D3F['may-detect'], name="may_detect", curie=D3F.curie('may-detect'),
                   model_uri=D3FEND.may_detect, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_disable = Slot(uri=D3F['may-disable'], name="may_disable", curie=D3F.curie('may-disable'),
                   model_uri=D3FEND.may_disable, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_evaluate = Slot(uri=D3F['may-evaluate'], name="may_evaluate", curie=D3F.curie('may-evaluate'),
                   model_uri=D3FEND.may_evaluate, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_evict = Slot(uri=D3F['may-evict'], name="may_evict", curie=D3F.curie('may-evict'),
                   model_uri=D3FEND.may_evict, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_execute = Slot(uri=D3F['may-execute'], name="may_execute", curie=D3F.curie('may-execute'),
                   model_uri=D3FEND.may_execute, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_harden = Slot(uri=D3F['may-harden'], name="may_harden", curie=D3F.curie('may-harden'),
                   model_uri=D3FEND.may_harden, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_have_weakness = Slot(uri=D3F['may-have-weakness'], name="may_have_weakness", curie=D3F.curie('may-have-weakness'),
                   model_uri=D3FEND.may_have_weakness, domain=D3fendArtifact, range=Optional[Union[Union[str, D3fendWeaknessId], list[Union[str, D3fendWeaknessId]]]])

slots.may_interpret = Slot(uri=D3F['may-interpret'], name="may_interpret", curie=D3F.curie('may-interpret'),
                   model_uri=D3FEND.may_interpret, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_invoke = Slot(uri=D3F['may-invoke'], name="may_invoke", curie=D3F.curie('may-invoke'),
                   model_uri=D3FEND.may_invoke, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_isolate = Slot(uri=D3F['may-isolate'], name="may_isolate", curie=D3F.curie('may-isolate'),
                   model_uri=D3FEND.may_isolate, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_map = Slot(uri=D3F['may-map'], name="may_map", curie=D3F.curie('may-map'),
                   model_uri=D3FEND.may_map, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_modify = Slot(uri=D3F['may-modify'], name="may_modify", curie=D3F.curie('may-modify'),
                   model_uri=D3FEND.may_modify, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_produce = Slot(uri=D3F['may-produce'], name="may_produce", curie=D3F.curie('may-produce'),
                   model_uri=D3FEND.may_produce, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_query = Slot(uri=D3F['may-query'], name="may_query", curie=D3F.curie('may-query'),
                   model_uri=D3FEND.may_query, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_run = Slot(uri=D3F['may-run'], name="may_run", curie=D3F.curie('may-run'),
                   model_uri=D3FEND.may_run, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.may_transfer = Slot(uri=D3F['may-transfer'], name="may_transfer", curie=D3F.curie('may-transfer'),
                   model_uri=D3FEND.may_transfer, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.mediates_access_to = Slot(uri=D3F['mediates-access-to'], name="mediates_access_to", curie=D3F.curie('mediates-access-to'),
                   model_uri=D3FEND.mediates_access_to, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.member_of = Slot(uri=D3F['member-of'], name="member_of", curie=D3F.curie('member-of'),
                   model_uri=D3FEND.member_of, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.modified = Slot(uri=D3F.modified, name="modified", curie=D3F.curie('modified'),
                   model_uri=D3FEND.modified, domain=None, range=Optional[Union[str, D3fendDateTime]])

slots.modified_by = Slot(uri=D3F['modified-by'], name="modified_by", curie=D3F.curie('modified-by'),
                   model_uri=D3FEND.modified_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.modifies = Slot(uri=D3F.modifies, name="modifies", curie=D3F.curie('modifies'),
                   model_uri=D3FEND.modifies, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.modifies_part = Slot(uri=D3F['modifies-part'], name="modifies_part", curie=D3F.curie('modifies-part'),
                   model_uri=D3FEND.modifies_part, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.monitors = Slot(uri=D3F.monitors, name="monitors", curie=D3F.curie('monitors'),
                   model_uri=D3FEND.monitors, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.name = Slot(uri=D3F.name, name="name", curie=D3F.curie('name'),
                   model_uri=D3FEND.name, domain=None, range=Optional[str])

slots.narrower = Slot(uri=D3F.narrower, name="narrower", curie=D3F.curie('narrower'),
                   model_uri=D3FEND.narrower, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.narrower_transitive = Slot(uri=D3F['narrower-transitive'], name="narrower_transitive", curie=D3F.curie('narrower-transitive'),
                   model_uri=D3FEND.narrower_transitive, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.neutralizes = Slot(uri=D3F.neutralizes, name="neutralizes", curie=D3F.curie('neutralizes'),
                   model_uri=D3FEND.neutralizes, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.next = Slot(uri=D3F.next, name="next", curie=D3F.curie('next'),
                   model_uri=D3FEND.next, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.obfuscates = Slot(uri=D3F.obfuscates, name="obfuscates", curie=D3F.curie('obfuscates'),
                   model_uri=D3FEND.obfuscates, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.operates = Slot(uri=D3F.operates, name="operates", curie=D3F.curie('operates'),
                   model_uri=D3FEND.operates, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.operating_system = Slot(uri=D3F['operating-system'], name="operating_system", curie=D3F.curie('operating-system'),
                   model_uri=D3FEND.operating_system, domain=None, range=Optional[str])

slots.originates_from = Slot(uri=D3F['originates-from'], name="originates_from", curie=D3F.curie('originates-from'),
                   model_uri=D3FEND.originates_from, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.output_of = Slot(uri=D3F['output-of'], name="output_of", curie=D3F.curie('output-of'),
                   model_uri=D3FEND.output_of, domain=D3fendArtifact, range=Optional[Union[Union[str, D3fendEventId], list[Union[str, D3fendEventId]]]])

slots.owns = Slot(uri=D3F.owns, name="owns", curie=D3F.curie('owns'),
                   model_uri=D3FEND.owns, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.participates_in = Slot(uri=D3F['participates-in'], name="participates_in", curie=D3F.curie('participates-in'),
                   model_uri=D3FEND.participates_in, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.powered_by = Slot(uri=D3F['powered-by'], name="powered_by", curie=D3F.curie('powered-by'),
                   model_uri=D3FEND.powered_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.powers = Slot(uri=D3F.powers, name="powers", curie=D3F.curie('powers'),
                   model_uri=D3FEND.powers, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.preceded_by = Slot(uri=D3F['preceded-by'], name="preceded_by", curie=D3F.curie('preceded-by'),
                   model_uri=D3FEND.preceded_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.precedes = Slot(uri=D3F.precedes, name="precedes", curie=D3F.curie('precedes'),
                   model_uri=D3FEND.precedes, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.pref_label = Slot(uri=D3F['pref-label'], name="pref_label", curie=D3F.curie('pref-label'),
                   model_uri=D3FEND.pref_label, domain=None, range=Optional[str])

slots.prescribed_by = Slot(uri=D3F['prescribed-by'], name="prescribed_by", curie=D3F.curie('prescribed-by'),
                   model_uri=D3FEND.prescribed_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.prescribes = Slot(uri=D3F.prescribes, name="prescribes", curie=D3F.curie('prescribes'),
                   model_uri=D3FEND.prescribes, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.process_ancestor = Slot(uri=D3F['process-ancestor'], name="process_ancestor", curie=D3F.curie('process-ancestor'),
                   model_uri=D3FEND.process_ancestor, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.process_command_line_arguments = Slot(uri=D3F['process-command-line-arguments'], name="process_command_line_arguments", curie=D3F.curie('process-command-line-arguments'),
                   model_uri=D3FEND.process_command_line_arguments, domain=None, range=Optional[str])

slots.process_data_property = Slot(uri=D3F['process-data-property'], name="process_data_property", curie=D3F.curie('process-data-property'),
                   model_uri=D3FEND.process_data_property, domain=None, range=Optional[str])

slots.process_environmental_variables = Slot(uri=D3F['process-environmental-variables'], name="process_environmental_variables", curie=D3F.curie('process-environmental-variables'),
                   model_uri=D3FEND.process_environmental_variables, domain=None, range=Optional[str])

slots.process_identifier = Slot(uri=D3F['process-identifier'], name="process_identifier", curie=D3F.curie('process-identifier'),
                   model_uri=D3FEND.process_identifier, domain=None, range=Optional[str])

slots.process_image_path = Slot(uri=D3F['process-image-path'], name="process_image_path", curie=D3F.curie('process-image-path'),
                   model_uri=D3FEND.process_image_path, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.process_parent = Slot(uri=D3F['process-parent'], name="process_parent", curie=D3F.curie('process-parent'),
                   model_uri=D3FEND.process_parent, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.process_property = Slot(uri=D3F['process-property'], name="process_property", curie=D3F.curie('process-property'),
                   model_uri=D3FEND.process_property, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.process_security_context = Slot(uri=D3F['process-security-context'], name="process_security_context", curie=D3F.curie('process-security-context'),
                   model_uri=D3FEND.process_security_context, domain=None, range=Optional[str])

slots.process_user = Slot(uri=D3F['process-user'], name="process_user", curie=D3F.curie('process-user'),
                   model_uri=D3FEND.process_user, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.produced_by = Slot(uri=D3F['produced-by'], name="produced_by", curie=D3F.curie('produced-by'),
                   model_uri=D3FEND.produced_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.produces = Slot(uri=D3F.produces, name="produces", curie=D3F.curie('produces'),
                   model_uri=D3FEND.produces, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.provider = Slot(uri=D3F.provider, name="provider", curie=D3F.curie('provider'),
                   model_uri=D3FEND.provider, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.published = Slot(uri=D3F.published, name="published", curie=D3F.curie('published'),
                   model_uri=D3FEND.published, domain=None, range=Optional[Union[str, D3fendDateTime]])

slots.quarantines = Slot(uri=D3F.quarantines, name="quarantines", curie=D3F.curie('quarantines'),
                   model_uri=D3FEND.quarantines, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.queries = Slot(uri=D3F.queries, name="queries", curie=D3F.curie('queries'),
                   model_uri=D3FEND.queries, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.rating = Slot(uri=D3F.rating, name="rating", curie=D3F.curie('rating'),
                   model_uri=D3FEND.rating, domain=None, range=Optional[str])

slots.reads = Slot(uri=D3F.reads, name="reads", curie=D3F.curie('reads'),
                   model_uri=D3FEND.reads, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.receives = Slot(uri=D3F.receives, name="receives", curie=D3F.curie('receives'),
                   model_uri=D3FEND.receives, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.recorded_in = Slot(uri=D3F['recorded-in'], name="recorded_in", curie=D3F.curie('recorded-in'),
                   model_uri=D3FEND.recorded_in, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.records = Slot(uri=D3F.records, name="records", curie=D3F.curie('records'),
                   model_uri=D3FEND.records, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.regenerates = Slot(uri=D3F.regenerates, name="regenerates", curie=D3F.curie('regenerates'),
                   model_uri=D3FEND.regenerates, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.related = Slot(uri=D3F.related, name="related", curie=D3F.curie('related'),
                   model_uri=D3FEND.related, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.release_date = Slot(uri=D3F['release-date'], name="release_date", curie=D3F.curie('release-date'),
                   model_uri=D3FEND.release_date, domain=None, range=Optional[str])

slots.restores = Slot(uri=D3F.restores, name="restores", curie=D3F.curie('restores'),
                   model_uri=D3FEND.restores, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.restricted_by = Slot(uri=D3F['restricted-by'], name="restricted_by", curie=D3F.curie('restricted-by'),
                   model_uri=D3FEND.restricted_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.restricts = Slot(uri=D3F.restricts, name="restricts", curie=D3F.curie('restricts'),
                   model_uri=D3FEND.restricts, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.resumes = Slot(uri=D3F.resumes, name="resumes", curie=D3F.curie('resumes'),
                   model_uri=D3FEND.resumes, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.risk_impact = Slot(uri=D3F['risk-impact'], name="risk_impact", curie=D3F.curie('risk-impact'),
                   model_uri=D3FEND.risk_impact, domain=None, range=Optional[int])

slots.risk_likelihood = Slot(uri=D3F['risk-likelihood'], name="risk_likelihood", curie=D3F.curie('risk-likelihood'),
                   model_uri=D3FEND.risk_likelihood, domain=None, range=Optional[int])

slots.runs = Slot(uri=D3F.runs, name="runs", curie=D3F.curie('runs'),
                   model_uri=D3FEND.runs, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.see_also = Slot(uri=RDFS.seeAlso, name="see_also", curie=RDFS.curie('seeAlso'),
                   model_uri=D3FEND.see_also, domain=None, range=Optional[Union[str, list[str]]])

slots.semantic_relation = Slot(uri=D3F['semantic-relation'], name="semantic_relation", curie=D3F.curie('semantic-relation'),
                   model_uri=D3FEND.semantic_relation, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.signed_by = Slot(uri=D3F['signed-by'], name="signed_by", curie=D3F.curie('signed-by'),
                   model_uri=D3FEND.signed_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.signs = Slot(uri=D3F.signs, name="signs", curie=D3F.curie('signs'),
                   model_uri=D3FEND.signs, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.skos_pref_label = Slot(uri=SKOS.prefLabel, name="skos_pref_label", curie=SKOS.curie('prefLabel'),
                   model_uri=D3FEND.skos_pref_label, domain=None, range=Optional[Union[str, list[str]]])

slots.spoofs = Slot(uri=D3F.spoofs, name="spoofs", curie=D3F.curie('spoofs'),
                   model_uri=D3FEND.spoofs, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.stage = Slot(uri=D3F.stage, name="stage", curie=D3F.curie('stage'),
                   model_uri=D3FEND.stage, domain=None, range=Optional[str])

slots.start = Slot(uri=D3F.start, name="start", curie=D3F.curie('start'),
                   model_uri=D3FEND.start, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.strengthens = Slot(uri=D3F.strengthens, name="strengthens", curie=D3F.curie('strengthens'),
                   model_uri=D3FEND.strengthens, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.summarizes = Slot(uri=D3F.summarizes, name="summarizes", curie=D3F.curie('summarizes'),
                   model_uri=D3FEND.summarizes, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.suspends = Slot(uri=D3F.suspends, name="suspends", curie=D3F.curie('suspends'),
                   model_uri=D3FEND.suspends, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.synonym = Slot(uri=D3F.synonym, name="synonym", curie=D3F.curie('synonym'),
                   model_uri=D3FEND.synonym, domain=None, range=Optional[Union[str, list[str]]])

slots.terminates = Slot(uri=D3F.terminates, name="terminates", curie=D3F.curie('terminates'),
                   model_uri=D3FEND.terminates, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.text = Slot(uri=D3F.text, name="text", curie=D3F.curie('text'),
                   model_uri=D3FEND.text, domain=None, range=Optional[str])

slots.title = Slot(uri=D3F.title, name="title", curie=D3F.curie('title'),
                   model_uri=D3FEND.title, domain=None, range=Optional[str])

slots.transmits = Slot(uri=D3F.transmits, name="transmits", curie=D3F.curie('transmits'),
                   model_uri=D3FEND.transmits, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.unloads = Slot(uri=D3F.unloads, name="unloads", curie=D3F.curie('unloads'),
                   model_uri=D3FEND.unloads, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.unmounts = Slot(uri=D3F.unmounts, name="unmounts", curie=D3F.curie('unmounts'),
                   model_uri=D3FEND.unmounts, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.updates = Slot(uri=D3F.updates, name="updates", curie=D3F.curie('updates'),
                   model_uri=D3FEND.updates, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.use_limits = Slot(uri=D3F['use-limits'], name="use_limits", curie=D3F.curie('use-limits'),
                   model_uri=D3FEND.use_limits, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.used_by = Slot(uri=D3F['used-by'], name="used_by", curie=D3F.curie('used-by'),
                   model_uri=D3FEND.used_by, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.uses = Slot(uri=D3F.uses, name="uses", curie=D3F.curie('uses'),
                   model_uri=D3FEND.uses, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.valid = Slot(uri=D3F.valid, name="valid", curie=D3F.curie('valid'),
                   model_uri=D3FEND.valid, domain=None, range=Optional[Union[str, D3fendDateTime]])

slots.validated_by = Slot(uri=D3F['validated-by'], name="validated_by", curie=D3F.curie('validated-by'),
                   model_uri=D3FEND.validated_by, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.validates = Slot(uri=D3F.validates, name="validates", curie=D3F.curie('validates'),
                   model_uri=D3FEND.validates, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.verifies = Slot(uri=D3F.verifies, name="verifies", curie=D3F.curie('verifies'),
                   model_uri=D3FEND.verifies, domain=None, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.version = Slot(uri=D3F.version, name="version", curie=D3F.curie('version'),
                   model_uri=D3FEND.version, domain=None, range=Optional[Union[int, str]])

slots.weakness_of = Slot(uri=D3F['weakness-of'], name="weakness_of", curie=D3F.curie('weakness-of'),
                   model_uri=D3FEND.weakness_of, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.windows_registry_data_property = Slot(uri=D3F['windows-registry-data-property'], name="windows_registry_data_property", curie=D3F.curie('windows-registry-data-property'),
                   model_uri=D3FEND.windows_registry_data_property, domain=None, range=Optional[str])

slots.windows_registry_key = Slot(uri=D3F['windows-registry-key'], name="windows_registry_key", curie=D3F.curie('windows-registry-key'),
                   model_uri=D3FEND.windows_registry_key, domain=None, range=Optional[str])

slots.windows_registry_value = Slot(uri=D3F['windows-registry-value'], name="windows_registry_value", curie=D3F.curie('windows-registry-value'),
                   model_uri=D3FEND.windows_registry_value, domain=None, range=Optional[str])

slots.writes = Slot(uri=D3F.writes, name="writes", curie=D3F.curie('writes'),
                   model_uri=D3FEND.writes, domain=D3fendEntry, range=Optional[Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]]])

slots.d3fendCatalog__ontology_iri = Slot(uri=D3FEND.ontology_iri, name="d3fendCatalog__ontology_iri", curie=D3FEND.curie('ontology_iri'),
                   model_uri=D3FEND.d3fendCatalog__ontology_iri, domain=None, range=URIRef)

slots.d3fendCatalog__version_info = Slot(uri=OWL.versionInfo, name="d3fendCatalog__version_info", curie=OWL.curie('versionInfo'),
                   model_uri=D3FEND.d3fendCatalog__version_info, domain=None, range=str)

slots.d3fendCatalog__version_iri = Slot(uri=OWL.versionIRI, name="d3fendCatalog__version_iri", curie=OWL.curie('versionIRI'),
                   model_uri=D3FEND.d3fendCatalog__version_iri, domain=None, range=Optional[Union[str, URI]])

slots.d3fendCatalog__ontology_title = Slot(uri=DCTERMS.title, name="d3fendCatalog__ontology_title", curie=DCTERMS.curie('title'),
                   model_uri=D3FEND.d3fendCatalog__ontology_title, domain=None, range=Optional[str])

slots.d3fendCatalog__ontology_description = Slot(uri=DCTERMS.description, name="d3fendCatalog__ontology_description", curie=DCTERMS.curie('description'),
                   model_uri=D3FEND.d3fendCatalog__ontology_description, domain=None, range=Optional[str])

slots.d3fendCatalog__ontology_license = Slot(uri=DCTERMS.license, name="d3fendCatalog__ontology_license", curie=DCTERMS.curie('license'),
                   model_uri=D3FEND.d3fendCatalog__ontology_license, domain=None, range=Optional[str])

slots.d3fendCatalog__disjoint_groups = Slot(uri=D3FEND.disjoint_groups, name="d3fendCatalog__disjoint_groups", curie=D3FEND.curie('disjoint_groups'),
                   model_uri=D3FEND.d3fendCatalog__disjoint_groups, domain=None, range=Optional[Union[Union[dict, D3fendDisjointGroup], list[Union[dict, D3fendDisjointGroup]]]])

slots.d3fendCatalog__entries = Slot(uri=D3FEND.entries, name="d3fendCatalog__entries", curie=D3FEND.curie('entries'),
                   model_uri=D3FEND.d3fendCatalog__entries, domain=None, range=Union[dict[Union[str, D3fendEntryId], Union[dict, D3fendEntry]], list[Union[dict, D3fendEntry]]])

slots.d3fendDisjointGroup__members = Slot(uri=OWL.members, name="d3fendDisjointGroup__members", curie=OWL.curie('members'),
                   model_uri=D3FEND.d3fendDisjointGroup__members, domain=None, range=Union[Union[str, D3fendEntryId], list[Union[str, D3fendEntryId]]])
