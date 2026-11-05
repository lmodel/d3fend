export type D3fendEntryId = string;
export type D3fendThingId = string;
export type D3fendThreatModelThingId = string;
export type D3fendThreatModelTechniqueId = string;
export type D3fendAttackDataSourceId = string;
export type D3fendAttackMitigationId = string;
export type D3fendControlCatalogId = string;
export type D3fendExternalControlId = string;
export type D3fendCciControlId = string;
export type D3fendNistControlId = string;
export type D3fendTechniqueReferenceId = string;
export type D3fendAgentId = string;
export type D3fendEventId = string;
export type D3fendArtifactId = string;
export type D3fendDigitalArtifactId = string;
export type D3fendWeaknessId = string;
export type D3fendTechniqueId = string;
export type D3fendAnalyticTechniqueId = string;
export type D3fendOffensiveTechniqueId = string;
export type D3fendDefensiveTechniqueId = string;
export type D3fendGoalId = string;
export type D3fendOffensiveTacticId = string;
export type D3fendDefensiveTacticId = string;
export type D3fendCatalogOntologyIri = string;
/**
* How the ontology declares a term.
*/
export enum D3fendOwlKind {
    
    /** The term is an owl:Class only. */
    Class = "class",
    /** The term is an owl:NamedIndividual only. */
    Individual = "individual",
    /** The term is punned, both an owl:Class and an owl:NamedIndividual. */
    Class_and_Individual = "class_and_individual",
};


/**
 * One term of the D3FEND graph, a class or an individual, as a record that holds its text and its relations to other terms.
 */
export interface D3fendEntry {
    /** The term's IRI, as a CURIE under d3f:. */
    id: string,
    /** The kind of entry, as the name of its class in this schema. */
    type: string,
    /** Whether the ontology declares the term a class, an individual or both. */
    owl_kind?: string,
    /** The D3FEND classes the ontology states the term is an instance of. */
    rdf_type?: D3fendEntryId[],
    /** The D3FEND classes directly above the term. */
    subclass_of?: D3fendEntryId[],
    /** x abuses y: The entity x applies an artifact y to a wrong thing or person; x applies y badly or incorrectly. */
    abuses?: D3fendEntryId[],
    /** x access-mediated-by y: The entity or resource x has its access regulated, controlled, or facilitated by entity y, which acts as an intermediary or gatekeeper to enforce access control policies. */
    access_mediated_by?: D3fendEntryId[],
    /** x accessed-by y: The entity or resource x is accessed by entity y. */
    accessed_by?: D3fendEntryId[],
    /** x accesses y: The subject x takes the action of reading from, writing into, or executing the stored information in the object y. Reads, writes, and executes are specific cases of accesses. */
    accesses?: D3fendEntryId[],
    /** x addressed-by y: Relates a resource x (e.g., network host, peripheral device, disk sector, a memory cell or other logical or physical entity) to a discrete address y in an address space that points to it. */
    addressed_by?: D3fendEntryId[],
    /** x addresses y: Relates a pointer x to a digital artifact y located in the address space to which x points. The address space is part of some digital store, whether it be in memory, an image, or a persistent storage device. */
    addresses?: D3fendEntryId[],
    /** x adds y: The subject x adds a data object y, such as a file, to some other digital artifact, such as a directory. Examples include an agent or technique adding a record to a database or a domain entry to a DNS server. */
    adds?: D3fendEntryId[],
    /** D3FEND's property "altLabel", which the ontology does not define. */
    alt_label?: string[],
    /** x analyzes y: The subject x breaks down object y into components or essential features, assessing y by quantitative methods, qualitative methods, or both. Usually the analysis is done in terms of some model or framework. */
    analyzes?: D3fendEntryId[],
    /** D3FEND's property "archived-at", which the ontology does not define. */
    archived_at?: string,
    /** x associated-with y: The subject x and object y are associated in some way. This is the most general definite relationship in d3fend (i.e., most general relationship that is not prefixed by 'may-'.) */
    associated_with?: D3fendEntryId[],
    /** x attached-to y: A subject x is joined in close association to an object y. */
    attached_to?: D3fendEntryId[],
    /** x attack-id y: The offensive technique x has the att&ck unique id of y. */
    attack_id?: string,
    /** D3FEND's property "attack-may-be-countered-by", which the ontology does not define. */
    attack_may_be_countered_by?: D3fendEntryId[],
    /** x authenticates y: The subject x establishes the authenticity of some y. This relation indicates an authentication event has occurred. */
    authenticates?: D3fendEntryId[],
    /** x authorizes y: A subject x grants authorization or clearance for an agent y to use an object. This relation indicates an authorization event has occurred. */
    authorizes?: D3fendEntryId[],
    /** Date that the resource became or will become available. */
    available?: string,
    /** x blocks y: The entity x blocks off the use of digital artifact y by reference to a block or allow list (or both.) */
    blocks?: D3fendEntryId[],
    /** x broader y: The entity x represents a more general or inclusive concept than entity y. */
    broader?: D3fendEntryId[],
    /** x broader-transitive y: The entity x represents a more general concept than entity y, including indirect or hierarchical relationships where x encompasses y through intermediate entities. */
    broader_transitive?: D3fendEntryId[],
    /** Unique identifier for a CAPEC technique, i.e. a common attack pattern identified by the pattern CAPEC-[number]. */
    capec_id?: string,
    /** x carried-by y: The information entity x is dependent upon the entity y for its storage, transport, or communication. Entity y serves as the necessary bearer or link from which x can be recovered or interpreted. */
    carried_by?: D3fendEntryId[],
    /** x carries y: The entity x serves as the bearer or link for information y, enabling y to be stored, transported, or communicated such that y can be recovered or interpreted from x */
    carries?: D3fendEntryId[],
    /** x caused-by y: The event or action x occurs as a consequence of event or action y. */
    caused_by?: D3fendEntryId[],
    /** x causes y: The event or action x brings about event or action y as a consequence. */
    causes?: D3fendEntryId[],
    /** A note on the term, in MITRE's words. */
    comment?: string[],
    /** x comments y: x claim has provider comments y. */
    comments?: string,
    /** x communicates-with y: x and y exchange signals or data bidirectionally, enabling mutual awareness, coordination, or interaction. */
    communicates_with?: D3fendEntryId[],
    /** D3FEND's property "confidence", which the ontology does not define. */
    confidence?: string,
    /** x configures y: The entity x sets the operational parameters of entity y, determining how y will operate. */
    configures?: D3fendEntryId[],
    /** x connected-to y: The subject x shares a direct physical or logical link with object y such that communication is possible between them without intermediate routing. */
    connected_to?: D3fendEntryId[],
    /** x connects y: The subject x joins system y by means of communication equipment (to some other system, typically the adversary-targeted host). */
    connects?: D3fendEntryId[],
    /** x contained-by y: The entity x exists within or is physically or logically enclosed by entity y. */
    contained_by?: D3fendEntryId[],
    /** x contains y: A core relation that holds between a whole x and its part y. Equivalent to relational concept 'has part' and thus transitive. */
    contains?: D3fendEntryId[],
    /** D3FEND's property "contributor", which the ontology does not define. */
    contributor?: D3fendEntryId[],
    /** The control (or control enhancement) name. */
    control_name?: string,
    /** x controlled-by y: x's operation or behavior is directed or regulated by y. */
    controlled_by?: D3fendEntryId[],
    /** x controls y: x directs or regulates y's operational state, behavior, or function. */
    controls?: D3fendEntryId[],
    /** x copies y: A technique or agent x reproduces or makes an exact copy of some digital artifact y. */
    copies?: D3fendEntryId[],
    /** x copy-of y: The subject x is a duplicate of the object y. */
    copy_of?: D3fendEntryId[],
    /** x corrupts y: The entity x causes y to enter an incorrect, inconsistent, or unintended state by modifying y's information-bearing content (e.g., a bit, symbol, word, configuration cell, or stored parameter) such that y's value no longer matches the expected or previously valid value. */
    corrupts?: D3fendEntryId[],
    /** D3FEND's property "counters", which the ontology does not define. */
    counters?: D3fendEntryId[],
    /** Date of creation of the resource. */
    created?: string,
    /** x created-by y: The entity x is brought into existence, developed, or generated by entity y. */
    created_by?: D3fendEntryId[],
    /** x creates y: The subject x brings into existence an object y. Some technique or agent x creates a persistent digital artifact y (as opposed to production of a consumable or transient object.); i.e., bring forth or generate. */
    creates?: D3fendEntryId[],
    /** D3FEND's property "cwe-id", which the ontology does not define. */
    cwe_id?: string,
    /** D3FEND's property "label", which the ontology does not define. */
    d3f_label?: string[],
    /** x d3fend-annotation y: The d3fend object x has the annotation y. */
    d3fend_annotation?: string,
    /** x d3fend-comment y: The entity x has an D3FEND team written a public note about entity y. */
    d3fend_comment?: string,
    /** Unique identifier for a D3FEND technique. D3-[Acronym]. */
    d3fend_id?: string,
    /** A point or period of time associated with an event in the lifecycle of the resource. */
    date_value?: string,
    /** D3FEND's property "deceives", which the ontology does not define. */
    deceives?: D3fendEntryId[],
    /** x deceives-with y: The entity x misleads or manipulates another entity using y as a tool, method, or mechanism to create false perceptions or understanding. */
    deceives_with?: D3fendEntryId[],
    /** x decodes y: The entity x transforms data y to a different form, usually through decompression. */
    decodes?: D3fendEntryId[],
    /** x definition y: The d3fend object x has the definition y. */
    definition?: string[],
    /** x deletes y: A technique or agent x wipes out the digitally or magnetically recorded information of digital object y. */
    deletes?: D3fendEntryId[],
    /** x dependent y: A dependent y is an entity that requires the fulfillment of the requirements specified in dependency x. */
    dependent?: D3fendEntryId[],
    /** x depends-on y: The entity x is contingent on y being available; x relies on y. */
    depends_on?: D3fendEntryId[],
    /** Whether the ontology marks the term as deprecated. */
    deprecated?: boolean,
    /** x derived-from y: The entity x is derived from or based on the value of y. */
    derived_from?: D3fendEntryId[],
    /** A statement that represents something in words. */
    description?: string,
    /** x detects y: The entity x discovers the presence, occurrence, or state of entity y through observation or measurement. */
    detects?: D3fendEntryId[],
    /** x disables y: The technique or agent x makes an entity y unable to perform its actions or capabilities. */
    disables?: D3fendEntryId[],
    /** A D3FEND class that shares no instance with this one. */
    disjoint_with?: D3fendEntryId[],
    /** A base string to use as prefix to create a full URL for an entity. The baseurl must end in a forward slash: / */
    display_baseurl?: string,
    /** x display-order y: An object x should be displayed in ordinal position y when placed or listed in a d3fend display with other objects of its kind. */
    display_order?: number,
    /** D3FEND's property "display-priority", which the ontology does not define. */
    display_priority?: number,
    /** x drives y: The device driver x causes a system component y to function by controlling it. */
    drives?: D3fendEntryId[],
    /** x employed-by y: An entity x is put into service by a technique or agent y. Inverse of y employs x. */
    employed_by?: D3fendEntryId[],
    /** x employs y: The entity x makes purposeful use of entity y to perform a function. */
    employs?: D3fendEntryId[],
    /** x enabled-by y: A top level technique y enables a tactic x, that is, the property indicates that a technique y is used to put a particular tactic x into action. In other words, y renders x capable or able for some task. Inverse of enables. */
    enabled_by?: D3fendEntryId[],
    /** x enables y: A top level technique x enables a tactic y, that is, the property indicates that a technique x is used to put a particular tactic y into action. In other words, x renders y capable or able for some task. */
    enables?: D3fendEntryId[],
    /** x encodes y: The entity x transforms data y to a different form, usually through compression. */
    encodes?: D3fendEntryId[],
    /** x encrypts y: The entity x converts the ordinary representation of a digital artifact y into a secret code. */
    encrypts?: D3fendEntryId[],
    /** D3FEND's property "end", which the ontology does not define. */
    end?: D3fendEntryId[],
    /** x enforces y: Technique x forces entity y to be compliant with a law, rule, or obligation. */
    enforces?: D3fendEntryId[],
    /** x enumerates y: The subject x takes the action of reading from a digital source y to acquire data and create a list of its contents. */
    enumerates?: D3fendEntryId[],
    /** x erases y: A technique x removes recorded data from storage device y creating space for new data. */
    erases?: D3fendEntryId[],
    /** x evaluated-by y: The entity x is assessed and analyzed by entity y. */
    evaluated_by?: D3fendEntryId[],
    /** x evaluates y: The entity x systematically assesses entity y to judge its state, quality, or risk. */
    evaluates?: D3fendEntryId[],
    /** x evicts y: The entity x forcibly removes entity y from the environment or resource where y was residing. */
    evicts?: D3fendEntryId[],
    /** x exactly y: The entity x is identical to or fully corresponds to entity y. */
    exactly?: D3fendEntryId[],
    /** D3FEND's property "example", which the ontology does not define. */
    example?: string,
    /** x excises y: Technique x removes a section of entity y. */
    excises?: D3fendEntryId[],
    /** x executed-by y: The entity or function x is carried out, performed, or run by entity y. */
    executed_by?: D3fendEntryId[],
    /** x executes y: The subject x takes the action of carrying out (executing) y, which is a single software module, function, or instruction. */
    executes?: D3fendEntryId[],
    /** D3FEND's property "expectation-rating", which the ontology does not define. */
    expectation_rating?: string,
    /** x extends y: The entity x extends the scope or range or area of entity y, especially in the sense of widening the range of applications. */
    extends?: D3fendEntryId[],
    /** x filters y: A technique or agent x removes some specified set of entities from the content of a digital artifact y, by passing an artifact's content through a filter. A filter is a device that removes something from whatever passes through it. */
    filters?: D3fendEntryId[],
    /** x forges y: An technique or agent x counterfeits a digital artifact y, such as a fake credential, with the intent to deceive. */
    forges?: D3fendEntryId[],
    /** D3FEND's property "fork", which the ontology does not define. */
    fork?: D3fendEntryId[],
    /** x hardens y: The entity x fortifies entity y to reduce its weaknesses so y can better withstand attack or failure. */
    hardens?: D3fendEntryId[],
    /** x has-account y: The subject x has ownership or possession of some account y. */
    has_account?: D3fendEntryId[],
    /** x has-agent y: The event x occurs because agent y actively carries it out. */
    has_agent?: D3fendEntryId[],
    /** D3FEND's property "has-audience", which the ontology does not define. */
    has_audience?: D3fendEntryId[],
    /** D3FEND's property "has-contribution", which the ontology does not define. */
    has_contribution?: D3fendEntryId[],
    /** D3FEND's property "has-contributor", which the ontology does not define. */
    has_contributor?: D3fendEntryId[],
    /** x has-dependent y: The entity x is relied upon or required by entity y. */
    has_dependent?: D3fendEntryId[],
    /** D3FEND's property "has-goal", which the ontology does not define. */
    has_goal?: D3fendEntryId[],
    /** x has-link y: The d3fend analysis x has the link y. */
    has_link?: string,
    /** x has-location y: The entity x is situated in a particular spot or position y. */
    has_location?: D3fendEntryId[],
    /** x has-mediator y: The entity x relies on or is facilitated by entity y. */
    has_mediator?: D3fendEntryId[],
    /** D3FEND's property "has-member", which the ontology does not define. */
    has_member?: D3fendEntryId[],
    /** x has-operating-mode y: The entity x is currently operating in or has the potential to be in operating mode y. */
    has_operating_mode?: D3fendEntryId[],
    /** x has-participant y: The event x involves an object y as a participant, indicating that y plays some role in the event, whether actively, passively, or otherwise. */
    has_participant?: D3fendEntryId[],
    /** D3FEND's property "has-prerequisite", which the ontology does not define. */
    has_prerequisite?: D3fendEntryId[],
    /** D3FEND's property "has-procedure", which the ontology does not define. */
    has_procedure?: D3fendEntryId[],
    /** x has-recipient y: An agent y is the intended recipient and decoder of the information contained in communication x. */
    has_recipient?: D3fendEntryId[],
    /** x has-sender y: An agent y is the sender and encoder of the information contained in communication x. */
    has_sender?: D3fendEntryId[],
    /** x has-weakness y: The entity x exhibits a condition y that could, in some circumstances, lead to a vulnerability. */
    has_weakness?: D3fendEntryId[],
    /** x hides y: A technique or operation x conceals the digital artifact y. */
    hides?: D3fendDigitalArtifactId[],
    /** x identified-by y: The entity x is recognized or described by entity y. */
    identified_by?: D3fendEntryId[],
    /** D3FEND's property "identifier", which the ontology does not define. */
    identifier?: string,
    /** x identifies y: The entity x recognizes or brings attention to entity y, making it distinct or clear through naming, description, or discovery. */
    identifies?: D3fendEntryId[],
    /** x impairs y: The entity or action x hinders entity y by reducing its normal function, capacity, or availability. */
    impairs?: D3fendEntryId[],
    /** x implemented-by y: The entity x is realized or brought into operation by entity y. */
    implemented_by?: D3fendEntryId[],
    /** x implements y: The entity x realizes entity y by putting its design or specification into effect. */
    implements?: D3fendEntryId[],
    /** x initiates y: The entity or action x starts or triggers entity or function y, bringing it into action. */
    initiates?: D3fendEntryId[],
    /** x injects y: The subject x takes the action of exploiting a security flaw by introducing (injecting) y, which is code or data that will change the course of execution or state of a computing process to an alternate course or state. Typically code injection is associated with adversaries intending the alternate course to facilitate a malevolent purpose; however, code injection can be unintentional or the intentions behind it may be good or benign. */
    injects?: D3fendEntryId[],
    /** x installs y: An entity x sets up digital artifact y for subsequent use. For example, an installation program can install application software. */
    installs?: D3fendEntryId[],
    /** x instructed-by y: A subject x takes machine instructions from object y. */
    instructed_by?: D3fendEntryId[],
    /** x instructs y: A subject x delivers machine instructions to object y. */
    instructs?: D3fendEntryId[],
    /** x interprets y: The subject x interprets the executable script y. The definition of interprets here is 'Parse the source code and perform its behavior directly.' */
    interprets?: D3fendEntryId[],
    /** x inventoried-by y: The entity x is cataloged, recorded, or tracked by entity y. */
    inventoried_by?: D3fendEntryId[],
    /** x inventories y: The entity x systematically discovers entity y and records its presence and key details for tracking. */
    inventories?: D3fendEntryId[],
    /** x invoked-by y: The entity x is called, triggered, or activated by entity y. */
    invoked_by?: D3fendEntryId[],
    /** x invokes y: The subject x invokes a system service by use of an instruction object y that interrupts the program being executed and passes control to the operating system to perform that operation. */
    invokes?: D3fendEntryId[],
    /** D3FEND's property "isDefinedBy", which the ontology does not define. */
    is_defined_by?: string[],
    /** x isolates y: The technique or agent x sets digital artifact y apart from other digital artifacts, sequestering y. */
    isolates?: D3fendEntryId[],
    /** Date of formal issuance of the resource. */
    issued?: string,
    /** x jams y: The entity x deliberately introduces interfering energy that degrades, disrupts, blocks, or masks the information-bearing capability of the target y. */
    jams?: D3fendEntryId[],
    /** x kb-abstract y: The reference x has the abstract y. */
    kb_abstract?: string,
    /** The technique x has the kb-article y, where y is written in Markdown. */
    kb_article?: string[],
    /** x kb-organization y: The reference x was created or owned by the organization y. */
    kb_organization?: string,
    /** x kb-is-example-of y: The reference x is an example of technique y. */
    kb_reference_of?: D3fendTechniqueId[],
    /** x kb-reference-title y: The d3fend knowledge base reference x has the reference title string y. */
    kb_reference_title?: string,
    /** D3FEND's property "label", which the ontology does not define. */
    label?: string[],
    /** x limits y: The entity x specifies a designated limit beyond which some entity y cannot function or must be terminated. */
    limits?: D3fendEntryId[],
    /** x loaded-by y: The entity x is brought into memory by entity y. */
    loaded_by?: D3fendEntryId[],
    /** x loads y: The technique or process x transfers a software from storage y to a computer's memory for subsequent execution. */
    loads?: D3fendEntryId[],
    /** x manages y: The technique or agent x watches and directs the use of digital artifact y. */
    manages?: D3fendEntryId[],
    /** x mapped-by y: The entity x is linked to another entity by entity y. */
    mapped_by?: D3fendEntryId[],
    /** x maps y: The entity x discovers and records how entity y is arranged and interconnected. */
    maps?: D3fendEntryId[],
    /** x may-access y: The entity x may access the thing y; that is, 'x accesses y' may be true. */
    may_access?: D3fendEntryId[],
    /** x may-add y: The entity x may add the thing y; that is, 'x adds y' may be true. */
    may_add?: D3fendEntryId[],
    /** D3FEND's property "may-be-accessed-by", which the ontology does not define. */
    may_be_accessed_by?: D3fendEntryId[],
    /** x may-be-associated-with y: The subject x and object y may be associated in some way. */
    may_be_associated_with?: D3fendEntryId[],
    /** D3FEND's property "may-be-contained-by", which the ontology does not define. */
    may_be_contained_by?: D3fendEntryId[],
    /** D3FEND's property "may-be-created-by", which the ontology does not define. */
    may_be_created_by?: D3fendEntryId[],
    /** D3FEND's property "may-be-deceived-by", which the ontology does not define. */
    may_be_deceived_by?: D3fendEntryId[],
    /** D3FEND's property "may-be-detected-by", which the ontology does not define. */
    may_be_detected_by?: D3fendEntryId[],
    /** D3FEND's property "may-be-evicted-by", which the ontology does not define. */
    may_be_evicted_by?: D3fendEntryId[],
    /** D3FEND's property "may-be-hardened-against-by", which the ontology does not define. */
    may_be_hardened_against_by?: D3fendEntryId[],
    /** D3FEND's property "may-be-invoked-by", which the ontology does not define. */
    may_be_invoked_by?: D3fendEntryId[],
    /** D3FEND's property "may-be-isolated-by", which the ontology does not define. */
    may_be_isolated_by?: D3fendEntryId[],
    /** D3FEND's property "may-be-modified-by", which the ontology does not define. */
    may_be_modified_by?: D3fendEntryId[],
    /** x may-be-tactically-associated-with y: the defensive action x may be a tactic that counters offensive action y. */
    may_be_tactically_associated_with?: D3fendEntryId[],
    /** x may-block y: The entity x may block the thing y; that is, 'x blocks y' may be true. */
    may_block?: D3fendEntryId[],
    /** to potentially have as contents or constituent parts; comprise; include. */
    may_contain?: D3fendEntryId[],
    /** x may-corrupt y: The entity x may corrupt y's information content; that is, 'x corrupts y' may be true. */
    may_corrupt?: D3fendEntryId[],
    /** D3FEND's property "may-counter", which the ontology does not define. */
    may_counter?: D3fendEntryId[],
    /** D3FEND's property "may-counter-attack", which the ontology does not define. */
    may_counter_attack?: D3fendEntryId[],
    /** x may-create y: The entity x may create the entity y; that is, 'x creates y' may be true. */
    may_create?: D3fendEntryId[],
    /** D3FEND's property "may-deceive", which the ontology does not define. */
    may_deceive?: D3fendEntryId[],
    /** D3FEND's property "may-detect", which the ontology does not define. */
    may_detect?: D3fendEntryId[],
    /** D3FEND's property "may-disable", which the ontology does not define. */
    may_disable?: D3fendEntryId[],
    /** D3FEND's property "may-evaluate", which the ontology does not define. */
    may_evaluate?: D3fendEntryId[],
    /** D3FEND's property "may-evict", which the ontology does not define. */
    may_evict?: D3fendEntryId[],
    /** x may-execute y: The subject x may take the action of carrying out (executing) y, which is a single software module, function, or instruction. */
    may_execute?: D3fendEntryId[],
    /** D3FEND's property "may-harden", which the ontology does not define. */
    may_harden?: D3fendEntryId[],
    /** x may-interpret y: The entity x may interpret the thing y; that is, 'x interprets y' may be true. */
    may_interpret?: D3fendEntryId[],
    /** x may-invoke y: The entity x may invoke the thing y; that is, 'x invokes y' may be true. */
    may_invoke?: D3fendEntryId[],
    /** D3FEND's property "may-isolate", which the ontology does not define. */
    may_isolate?: D3fendEntryId[],
    /** D3FEND's property "may-map", which the ontology does not define. */
    may_map?: D3fendEntryId[],
    /** x may-modify y: The entity x may modify the thing y; that is, 'x modifies y' may be true. */
    may_modify?: D3fendEntryId[],
    /** x may-produce y: The entity x may produce the thing y; that is, 'x produces y' may be true. */
    may_produce?: D3fendEntryId[],
    /** D3FEND's property "may-query", which the ontology does not define. */
    may_query?: D3fendEntryId[],
    /** x may-run y: The entity x may run the thing y; that is, 'x runs y' may be true. */
    may_run?: D3fendEntryId[],
    /** x may-transfer y: The entity x may send the thing y; that is, 'x transfers y' may be true. */
    may_transfer?: D3fendEntryId[],
    /** x mediates-access-to y: The entity x controls and brokers requests to reach entity y, enforcing the access rules that allow or deny it. */
    mediates_access_to?: D3fendEntryId[],
    /** D3FEND's property "member-of", which the ontology does not define. */
    member_of?: D3fendEntryId[],
    /** Date on which the resource was changed. */
    modified?: string,
    /** x modified-by y: The entity x is changed by entity y. */
    modified_by?: D3fendEntryId[],
    /** x modifies y: A technique or agent x causes a digital object y to change; become different; or undertake a transformation. Afterwards, the data or state held by a digital object is changed. */
    modifies?: D3fendEntryId[],
    /** x modifies-part y: The entity x modifies a part of y. [Note: This is a rolification property for the rule 'if one modifies a part of a whole, they modify the whole.' Reasoning for this and similar semantics to come are under evaluation and not part of current d3fend inferences.] */
    modifies_part?: D3fendEntryId[],
    /** x monitors y: The technique or agent x keep tabs on, keeps an eye on, or keeps the digital artifact y under surveillance. */
    monitors?: D3fendEntryId[],
    /** D3FEND's property "name", which the ontology does not define. */
    name?: string,
    /** x narrower y: The entity x represents a more specific or focused concept than entity y. */
    narrower?: D3fendEntryId[],
    /** x narrower-transitive y: The entity x represents a more specific concept than entity y, including indirect or hierarchical relationships where x is a subset of y through intermediate entities. */
    narrower_transitive?: D3fendEntryId[],
    /** x neutralizes y: The technique x makes the execution of actions of y ineffective by preventing or counterbalancing the effect of y. */
    neutralizes?: D3fendEntryId[],
    /** D3FEND's property "next", which the ontology does not define. */
    next?: D3fendEntryId[],
    /** x obfuscates y: The technique x makes the digital artifact y unclear or obscure. Typically obfuscation is a way to hide a digital artifact from discovery, use, or both. */
    obfuscates?: D3fendEntryId[],
    /** x operates y: The entity x enables, activates, or controls the functioning or behavior of object y (operated entity), typically in accordance with the design or intended use of the operated entity. */
    operates?: D3fendEntryId[],
    /** x operating-system y: The product x is supported on operating system y. */
    operating_system?: string,
    /** x originates-from y: The digital event or artifact x began its network transit from a physical location y. */
    originates_from?: D3fendEntryId[],
    /** x owns y: The subject x has ownership or possession of some object y. */
    owns?: D3fendEntryId[],
    /** x participates-in y: The object x takes part in the event y, signifying that x contributes to or is affected by the event's occurrence in some way. */
    participates_in?: D3fendEntryId[],
    /** x powered-by y: x obtains its essential energy or force from y to perform its function or remain active. */
    powered_by?: D3fendEntryId[],
    /** x powers y: x furnishes y with the energy or force required for y's functionality or operation. */
    powers?: D3fendEntryId[],
    /** x preceded-by y: The event or action x occurs after event or action y in time. */
    preceded_by?: D3fendEntryId[],
    /** x precedes y: The event or action x occurs before event or action y in time. */
    precedes?: D3fendEntryId[],
    /** x pref-label y: The preferred display value for x is y in d3fend tools. */
    pref_label?: string,
    /** x prescribed-by y: y provides a directive specification for x (i.e., y serves as a rule or guide for x). */
    prescribed_by?: D3fendEntryId[],
    /** x prescribes y: x provides a directive specification for y (i.e., x serves as a rule or guide for how y is intended to occur or be made). */
    prescribes?: D3fendEntryId[],
    /** x process-ancestor y: The process y is a process ancestor of process x, indicating one or more process creation events were conducted at process y and subsequently created process x. */
    process_ancestor?: D3fendEntryId[],
    /** x process-command-line-arguments y: The process x has the process command line arguments data y. */
    process_command_line_arguments?: string,
    /** x process-environment-variables y: The process x has the process environmental variables data y. */
    process_environmental_variables?: string,
    /** x process-identifier y: The process x has the process identifier y. */
    process_identifier?: string,
    /** x process-image-path y: The filepath y is the process image path for the process x, indicating the path to the resource from which the process's image was loaded. */
    process_image_path?: D3fendEntryId[],
    /** x process-parent y: The process y created the process x (directly) with a create process event. */
    process_parent?: D3fendEntryId[],
    /** x process-user y: The process x has been executed by the user y. */
    process_user?: D3fendEntryId[],
    /** x produced-by y: The entity x is created by entity y. */
    produced_by?: D3fendEntryId[],
    /** x produces y: The subject entity x or process produces a data object y, which may be discrete digital object or a stream (e.g., a stream such as network traffic.) */
    produces?: D3fendEntryId[],
    /** x provider y: A provider y is an entity that supplies a service, system, or data resources to a dependent entity x. */
    provider?: D3fendEntryId[],
    /** Date of publication of the resource. */
    published?: string,
    /** x quarantines y: Technique x moves entity y to a place of isolation. */
    quarantines?: D3fendEntryId[],
    /** x queries y: The entity x requests information or data from entity y. */
    queries?: D3fendEntryId[],
    /** D3FEND's property "rating", which the ontology does not define. */
    rating?: string,
    /** x reads y: The subject x takes the action of reading from a digital source y to acquire data and placing it into volatile memory for processing. */
    reads?: D3fendEntryId[],
    /** x receives y: The subject x acquires object y from a communication medium and transfers y into its local context for storage or processing. */
    receives?: D3fendEntryId[],
    /** x recorded-in y: The event x is documented, logged, or otherwise preserved within the digital artifact y, which stores or encodes relevant data about the event. */
    recorded_in?: D3fendEntryId[],
    /** x records y: The digital artifact x makes a record of events y; set down in permanent form. */
    records?: D3fendEntryId[],
    /** x regenerates y: The entity x discards the current digital artifact y and creates a new version that serves the same function. */
    regenerates?: D3fendEntryId[],
    /** x related y: x has a symmetric associative relation to y. */
    related?: D3fendEntryId[],
    /** x release-date y: The object x has the release-date y. */
    release_date?: string,
    /** x restores y: The entity x returns entity y to its known-good or previous state. */
    restores?: D3fendEntryId[],
    /** x restricted-by y: The entity x is limited, constrained, or regulated by entity y. */
    restricted_by?: D3fendEntryId[],
    /** x restricts y: The entity x bounds the use of entity y. */
    restricts?: D3fendEntryId[],
    /** x resumes y: The agent or technique x continues a previous action on entity y. Usually occurs after suspension on y. */
    resumes?: D3fendEntryId[],
    /** Risk impact rating, expressed on a numeric scale from 1 (lowest impact) to 5 (highest impact) in the context of a 5x5 risk matrix. Impact is used here as a synonym for consequence, another popular term used in risk analysis. */
    risk_impact?: number,
    /** Risk likelihood rating, expressed on a numeric scale from 1 (lowest likelihood) to 5 (highest likelihood) in the context of a 5x5 risk matrix. */
    risk_likelihood?: number,
    /** x runs y: To carry out a process or program y, as on a computer or a machine x; where y may be a large software assembly or a specific module or instruction. Examples: "run a new program on the Mac"; "the computer runs the application software". */
    runs?: D3fendEntryId[],
    /** D3FEND's property "seeAlso", which the ontology does not define. */
    see_also?: string[],
    /** x semantic-relation y: The entity x is conceptually or meaningfully connected to entity y. */
    semantic_relation?: D3fendEntryId[],
    /** x signed-by y: The digital artifact x includes a signature generated by the entity y, certifying the authenticity and integrity of x. This relationship indicates that x has undergone a validation process by y, using cryptographic measures to ensure that x is trustworthy and unaltered since the signing by y. */
    signed_by?: D3fendEntryId[],
    /** x signs y: The entity x applies a digital signature to the digital artifact y, thereby asserting its validity, integrity, and authenticity. Typically, this involves cryptographic techniques to securely bind the signature to y, ensuring that y's contents have not been altered and are authentic as endorsed by x. */
    signs?: D3fendEntryId[],
    /** D3FEND's property "prefLabel", which the ontology does not define. */
    skos_pref_label?: string[],
    /** x spoofs y: The technique x creates a fake instance of a digital artifact y; that is, y is a decoy, fake, or counterfeit. */
    spoofs?: D3fendEntryId[],
    /** D3FEND's property "stage", which the ontology does not define. */
    stage?: string,
    /** D3FEND's property "start", which the ontology does not define. */
    start?: D3fendEntryId[],
    /** x strengthens y: The technique x makes digital artifact y resistant (to harm or misuse.) */
    strengthens?: D3fendEntryId[],
    /** x summarizes y: The sensor x summarizes a set y of events concerning digital artifacts over time. */
    summarizes?: D3fendEntryId[],
    /** x suspends y: The agent or technique x pauses entity y. */
    suspends?: D3fendEntryId[],
    /** an equivalent term. */
    synonym?: string[],
    /** x terminates y: The technique x brings to an end or halt to some activity y. */
    terminates?: D3fendEntryId[],
    /** The text of the document (i.e., terms of license.) */
    text?: string,
    /** A name given to the resource. */
    title?: string,
    /** x transmits y: The subject x actively emits object y onto a communication medium, rendering y observable and available for reception on that medium. */
    transmits?: D3fendEntryId[],
    /** x unloads y: The technique or artifact performs the action of unloading some artifact (applications, kernel modules, or hardware drivers, etc.) from a computer's memory. */
    unloads?: D3fendEntryId[],
    /** x unmounts y: An operation x removes the access via computer system's file system the availability of files and directories on storage artifact y. Unmounts reverse or undo prior mount operations. */
    unmounts?: D3fendEntryId[],
    /** x updates y: The technique x updates the software for component y. */
    updates?: D3fendEntryId[],
    /** x use-limits y: The entity x specifies a designated number of uses beyond which some entity y cannot function or must be terminated. */
    use_limits?: D3fendEntryId[],
    /** x used-by y: The inverse of y uses x. */
    used_by?: D3fendEntryId[],
    /** x uses y: The entity x puts into service a resource or implement y; makes y work or employ for a particular purpose or for its inherent or natural purpose. */
    uses?: D3fendEntryId[],
    /** Date (often a range) of validity of a resource. */
    valid?: string,
    /** x validated-by y: The digital artifact x has its authenticity and correctness confirmed or verified by the technique, operation, or agent y. */
    validated_by?: D3fendEntryId[],
    /** x validates y: The technique x proves the digital artifact y is valid; that is, x shows or confirms the validity of y. */
    validates?: D3fendEntryId[],
    /** x verifies y: The technique x confirms the truth of a digital artifact y. */
    verifies?: D3fendEntryId[],
    /** x version y: The product or service x has the version y. */
    version?: string,
    /** D3FEND's property "weakness-of", which the ontology does not define. */
    weakness_of?: D3fendEntryId[],
    /** x value y: The key-value pair x has the key y. */
    windows_registry_key?: string,
    /** x value y: The key-value pair x has the data value y. */
    windows_registry_value?: string,
    /** x writes y: The subject x takes the action of writing to a digital artifact y to store data and placing it into persistent memory for later reference. */
    writes?: D3fendEntryId[],
}


/**
 * An entry with no narrower kind here: a root of D3FEND's tree, or a term such as a plan, a step, a group, a time or a condition.
 */
export interface D3fendThing extends D3fendEntry {
}


/**
 * A term from a threat model outside D3FEND, such as ATT&CK, ATLAS, SPARTA or CAPEC, with no narrower kind here.
 */
export interface D3fendThreatModelThing extends D3fendEntry {
}


/**
 * A technique of ATT&CK Mobile, ATT&CK ICS, ATLAS or SPARTA. D3FEND places these under their frameworks and not under its own offensive technique.
 */
export interface D3fendThreatModelTechnique extends D3fendThreatModelThing {
}


/**
 * A data source of ATT&CK Enterprise, which D3FEND relates to its digital artifacts.
 */
export interface D3fendAttackDataSource extends D3fendThreatModelThing {
}


/**
 * A mitigation of ATT&CK Enterprise, which D3FEND relates to its defensive techniques.
 */
export interface D3fendAttackMitigation extends D3fendThreatModelThing {
}


/**
 * A published list of controls, one edition of which holds D3FEND's control entries as members.
 */
export interface D3fendControlCatalog extends D3fendEntry {
}


/**
 * A control another catalogue defines, which D3FEND relates to its techniques.
 */
export interface D3fendExternalControl extends D3fendEntry {
}


/**
 * An item of the Control Correlation Identifier list that DISA publishes.
 */
export interface D3fendCciControl extends D3fendExternalControl {
}


/**
 * A control or control enhancement of a revision of NIST SP 800-53.
 */
export interface D3fendNistControl extends D3fendExternalControl {
}


/**
 * A source behind a knowledge base article, such as a patent or a paper. rdf_type says which of D3FEND's reference types it is, since all of them hold the same fields.
 */
export interface D3fendTechniqueReference extends D3fendEntry {
    /** x kb-author y: The reference x has some author y. */
    kb_author?: string,
    /** x kb-mitre-analysis y: The reference x has the mitre d3fend analysis y. */
    kb_mitre_analysis?: string,
}


/**
 * Something capable of intentional action, such as a person, an organization or an attacker.
 */
export interface D3fendAgent extends D3fendEntry {
}


/**
 * Something that happens in a system over a finite span of time, with the artifacts that take part in it.
 */
export interface D3fendEvent extends D3fendEntry {
    /** x has-input y: An event x has input y iff y is an artifact that is present at the start of x, provides material or information required for x to begin, and during x either y's state is altered or the information content it bears is realized. */
    has_input?: D3fendArtifactId[],
    /** x has-output y: An event x has output y iff y is an artifact that is present at the end of x, was not present in the same state at the start of x, and whose presence at the end is required for x to be considered complete; the change in state may arise either from a transformation of y itself or from the realization of the information content y bears. */
    has_output?: D3fendArtifactId[],
}


/**
 * A man-made thing that techniques act on. Those that are not digital, such as a physical lock, stay here.
 */
export interface D3fendArtifact extends D3fendEntry {
    /** x input-of y: An artifact x is input of an event y iff x participates at the start of y, provides the material or information required for y to begin, and during y either x's state is altered or the information content it bears is realized. */
    input_of?: D3fendEventId[],
    /** D3FEND's property "may-have-weakness", which the ontology does not define. */
    may_have_weakness?: D3fendWeaknessId[],
    /** x output-of y: An artifact x is output of an event y iff x must be present when y concludes, was absent in the same state when x began, and y counts as complete only when x is available at its end. */
    output_of?: D3fendEventId[],
}


/**
 * An artifact that carries information for a digital system, such as a file, a process or a network packet: the common ground where offensive and defensive techniques meet.
 */
export interface D3fendDigitalArtifact extends D3fendArtifact {
    /** x process-security-context y: The process x has the process security context data y. */
    process_security_context?: string,
}


/**
 * A condition in a system component that can contribute to a vulnerability. Nearly all of these entries name a CWE entry.
 */
export interface D3fendWeakness extends D3fendEntry {
    /** D3FEND's property "may-be-weakness-of", which the ontology does not define. */
    may_be_weakness_of?: D3fendArtifactId[],
}


/**
 * A way of doing something in or to a computer system. Its narrower kinds say whose way it is.
 */
export interface D3fendTechnique extends D3fendEntry {
    /** D3FEND's property "kb-reference", which the ontology does not define. */
    kb_reference?: D3fendEntryId[],
}


/**
 * A mathematical method a defensive technique can use to find patterns in data, such as a form of machine learning or a statistical measure.
 */
export interface D3fendAnalyticTechnique extends D3fendTechnique {
}


/**
 * A way an adversary acts, drawn from ATT&CK Enterprise, related to the artifacts it touches and to the tactic it serves.
 */
export interface D3fendOffensiveTechnique extends D3fendTechnique {
}


/**
 * A countermeasure: a method that makes a system harder to attack, related to the artifacts it acts on and to the tactic it enables.
 */
export interface D3fendDefensiveTechnique extends D3fendTechnique {
}


/**
 * An aim that a tactic or a technique serves.
 */
export interface D3fendGoal extends D3fendEntry {
}


/**
 * A tactic of an adversary, from the ATT&CK, ATLAS or SPARTA framework, which an offensive technique enables.
 */
export interface D3fendOffensiveTactic extends D3fendGoal {
}


/**
 * One of D3FEND's seven defensive aims, such as Detect or Harden, which a defensive technique enables.
 */
export interface D3fendDefensiveTactic extends D3fendGoal {
}


/**
 * A set of D3FEND classes of which no two share an instance.
 */
export interface D3fendDisjointGroup {
    /** The classes in the group. */
    members: D3fendEntryId[],
}


/**
 * One edition of the D3FEND ontology, with its header and all its entries.
 */
export interface D3fendCatalog {
    /** A note on the term, in MITRE's words. */
    comment?: string[],
    /** x release-date y: The object x has the release-date y. */
    release_date?: string,
    /** The IRI of the ontology. */
    ontology_iri: string,
    /** The edition of the ontology. */
    version_info: string,
    /** The IRI of this edition of the ontology. */
    version_iri?: string,
    /** The title of the ontology. */
    ontology_title?: string,
    /** The description of the ontology. */
    ontology_description?: string,
    /** The licence the ontology states. */
    ontology_license?: string,
    /** The sets of classes the ontology declares mutually disjoint. */
    disjoint_groups?: D3fendDisjointGroup[],
    /** Every class and individual of the ontology, as one record each. */
    entries: D3fendEntry[],
}



