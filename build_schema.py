#!/usr/bin/env python3
"""
Generate a complete LinkML schema from d3fend OWL/TTL artifacts.

Usage:
    python build_schema.py
    Output: src/d3fend/schema/d3fend.yaml
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef, Literal, BNode
from rdflib.collection import Collection

# ── namespaces ──────────────────────────────────────────────────────────────
D3F = Namespace("http://d3fend.mitre.org/ontologies/d3fend.owl#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
DCTERMS = Namespace("http://purl.org/dc/terms/")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")

# ── helpers ──────────────────────────────────────────────────────────────────

def local_name(uri):
    """Return the local part of a URI (after # or last /)."""
    s = str(uri)
    if "#" in s:
        return s.split("#")[-1]
    return s.split("/")[-1]


def safe_name(name: str) -> str:
    """Make a name safe for use as a LinkML identifier.
    Replaces `.` with `_`; keeps hyphens and alphanumerics."""
    return name.replace(".", "_")


def safe_slot_name(name: str) -> str:
    """Return a LinkML-safe slot name, avoiding collisions with built-in types."""
    normalized = safe_name(name)
    # Avoid overlap with linkml built-in type `date`.
    if normalized == "date":
        return "date_value"
    return normalized


def indent(text: str, spaces: int = 2) -> str:
    pad = " " * spaces
    return "\n".join(pad + line if line.strip() else line for line in text.splitlines())


def yaml_str(value: str, key_indent: int = 4) -> str:
    """Produce a safe YAML scalar.

    key_indent: the number of spaces before the KEY that will contain this value.
      The block literal body will be indented to key_indent + 2 spaces.
    For inline list items (- value) use yaml_str_inline() instead.
    """
    value = value.strip()
    if not value:
        return '""'
    # Normalise whitespace for single-line representation
    single = " ".join(value.split())
    if "\n" in value or len(single) > 120:
        # Use block literal but indent body correctly
        pad = " " * (key_indent + 2)
        body_lines = value.replace("\r", "").split("\n")
        body = "\n".join(pad + l if l.strip() else "" for l in body_lines)
        return "|-\n" + body
    # Check if quoting needed (colon, hash, special YAML chars, reserved words)
    need_quote = (
        any(c in single for c in ':#{}[]|>&*!,\'\"\\%@`')
        or single.startswith(("-", " "))
        or single in ("true", "false", "null", "yes", "no")
    )
    if need_quote:
        escaped = single.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return single


def yaml_str_inline(value: str) -> str:
    """Produce a safe YAML double-quoted string (inline, newlines collapsed).
    Always returns a quoted string — safe for use in list items and
    annotation values where block literals would require careful indent tracking."""
    single = " ".join(value.strip().split())
    escaped = single.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def xsd_to_linkml(xsd_uri: str) -> str:
    mapping = {
        str(XSD.string): "string",
        str(XSD.integer): "integer",
        str(XSD.int): "integer",
        str(XSD.float): "float",
        str(XSD.double): "double",
        str(XSD.boolean): "boolean",
        str(XSD.dateTime): "datetime",
        str(XSD.date): "date",
        str(XSD.anyURI): "uri",
    }
    return mapping.get(xsd_uri, "string")


# ── load graph ───────────────────────────────────────────────────────────────

SOURCE_TTLS = [
    Path("src/d3fend/schema/d3fend.ttl"),
    Path("src/d3fend/schema/d3fend-protege.ttl"),
]

g = Graph()
for ttl_path in SOURCE_TTLS:
    print(f"Parsing {ttl_path.name} …")
    g.parse(ttl_path, format="turtle")
print(f"  {len(g)} merged triples loaded")

# ── load attack/defensive mappings artifact (optional) ───────────────────────
# This file contains D3FEND defensive-to-offensive mapping rows used to
# populate LinkML mapping fields (related/close/broad).
MAPPINGS_JSON_PATH = Path("src/d3fend/mappings/d3fend-full-mappings-1.3.0.json")
def_tech_to_attack_ids: dict[str, set[str]] = defaultdict(set)
def_tech_to_broad_parents: dict[str, set[str]] = defaultdict(set)
def_tech_to_close_attack_ids: dict[str, set[str]] = defaultdict(set)

# ── static UCO (Unified Cyber Ontology) class mappings ───────────────────────
# Maps D3FEND class local names to LinkML mapping field entries under the
# ``unified_cyber_ontology`` prefix (https://lmodel.github.io/uco-master/).
# Sources: uco-core, uco-observable, uco-action, uco-identity, uco-tool.
UCO_CLASS_MAPPINGS: dict[str, dict[str, list[str]]] = {
    # ── exact matches: same name and same concept in both ontologies ──────────
    **{
        name: {"exact_mappings": [f"unified_cyber_ontology:{name}"]}
        for name in [
            "Action",
            "Application",
            "ArchiveFile",
            "Credential",
            "Dependency",
            "DigitalCamera",
            "Directory",
            "DNSRecord",
            "DomainName",
            "EventLog",
            "File",
            "FileSystem",
            "Grouping",
            "Hostname",
            "IPAddress",
            "MACAddress",
            "MobilePhone",
            "NamedPipe",
            "NetworkFlow",
            "OperatingSystem",
            "Organization",
            "Person",
            "Pipe",
            "Process",
            "Server",
            "Software",
            "SymbolicLink",
            "Thread",
            "URL",
            "UserAccount",
            "Volume",
            "WindowsRegistryKey",
            "WindowsRegistryValue",
        ]
    },
    # ── close mappings: very similar concept, slight semantic or naming delta ──
    # UCO Item = a physical or digital thing stored or managed (broad artifact)
    "DigitalArtifact": {"close_mappings": ["unified_cyber_ontology:Item"]},
    # UCO Identity = an abstract representation of an identity (person/org/etc.)
    "DigitalIdentity": {"close_mappings": ["unified_cyber_ontology:Identity"]},
    # UCO DefensiveTool = a tool used defensively; D3FEND aligns at technique level
    "DefensiveTechnique": {"close_mappings": ["unified_cyber_ontology:DefensiveTool"]},
    # UCO ActionPattern = a pattern of actions; D3FEND tactic is a plan/goal
    "DefensiveTactic": {"close_mappings": ["unified_cyber_ontology:ActionPattern"]},
    # UCO Action covers any observable action; D3FEND DigitalEvent is an occurrence
    "DigitalEvent": {"close_mappings": ["unified_cyber_ontology:Action"]},
    # UCO SecurityEvent ↔ D3FEND SecurityEvent (close naming, same domain)
    "SecurityEvent": {"close_mappings": ["unified_cyber_ontology:Action"]},
    # UCO Document ↔ D3FEND DigitalDocument
    "DigitalDocument": {"close_mappings": ["unified_cyber_ontology:File"]},
    # UCO UserSession ↔ D3FEND Session
    "Session": {"close_mappings": ["unified_cyber_ontology:UserSession"]},
    # UCO Credential is broader; EncryptedCredential is a specialised form
    "EncryptedCredential": {"close_mappings": ["unified_cyber_ontology:Credential"]},
    # UCO EmailMessage ↔ D3FEND Email
    "Email": {"close_mappings": ["unified_cyber_ontology:EmailMessage"]},
    # UCO X509Certificate ↔ D3FEND Certificate
    "Certificate": {"close_mappings": ["unified_cyber_ontology:X509Certificate"]},
    # UCO X509Certificate ↔ D3FEND CertificateFile (file form of same concept)
    "CertificateFile": {"close_mappings": ["unified_cyber_ontology:X509Certificate"]},
    # UCO Software ↔ D3FEND SoftwarePackage (a packaged software artifact)
    "SoftwarePackage": {"close_mappings": ["unified_cyber_ontology:Software"]},
    # UCO Image ↔ D3FEND ImageFile (a file containing an image)
    "ImageFile": {"close_mappings": ["unified_cyber_ontology:Image"]},
    # UCO Image ↔ D3FEND DiskImage (a disk image artifact)
    "DiskImage": {"close_mappings": ["unified_cyber_ontology:Image"]},
    # ── related mappings: conceptually related, different hierarchy position ──
    # Attacker is a specific kind of Identity actor
    "Attacker": {"related_mappings": ["unified_cyber_ontology:Identity"]},
    # D3FENDKBThing is the D3FEND top-level KB class; UcoObject is the UCO root
    "D3FENDKBThing": {"related_mappings": ["unified_cyber_ontology:UcoObject"]},
    # Artifact as the physical-or-digital root maps to UCO Item
    "Artifact": {"related_mappings": ["unified_cyber_ontology:Item"]},
    # ── broad mappings: the UCO class is more general than the D3FEND class ───
    # UCO Action is broader than D3FEND's specific CyberAction / DefensiveAction
    "CyberAction":     {"broad_mappings": ["unified_cyber_ontology:Action"]},
    "DefensiveAction": {"broad_mappings": ["unified_cyber_ontology:Action"]},
    # UCO Event-related: DigitalEvent and FileEvent and NetworkEvent fall under Action
    "FileEvent":    {"broad_mappings": ["unified_cyber_ontology:Action"]},
    "NetworkEvent": {"broad_mappings": ["unified_cyber_ontology:Action"]},
    # UCO UcoThing is the top of the UCO hierarchy; D3FENDCore is a D3FEND subroot
    "D3FENDCore": {"broad_mappings": ["unified_cyber_ontology:UcoThing"]},
    # UCO Device is broader than HardwareDevice (UCO Device includes peripherals etc.)
    "HardwareDevice": {"broad_mappings": ["unified_cyber_ontology:Device"]},
    # UCO Process is broader than UserProcess (UCO covers all process types)
    "UserProcess": {"broad_mappings": ["unified_cyber_ontology:Process"]},
    # UCO Memory covers the full memory class; MemoryBlock is a sub-region
    "MemoryBlock": {"broad_mappings": ["unified_cyber_ontology:Memory"]},
}

# ── static STIX class mappings ───────────────────────────────────────────────
# Prefix target: https://lmodel.github.io/stix/
STIX_CLASS_MAPPINGS: dict[str, dict[str, list[str]]] = {
    # Exact class-name matches between D3FEND and STIX schema.
    **{
        name: {"exact_mappings": [f"stix:{name}"]}
        for name in [
            "Artifact",
            "Directory",
            "DomainName",
            "File",
            "Grouping",
            "Identifier",
            "NetworkTraffic",
            "Process",
            "Software",
            "UserAccount",
            "Vulnerability",
            "WindowsRegistryKey",
            "WindowsRegistryValue",
        ]
    },
    # Close semantic matches.
    "Attacker": {"close_mappings": ["stix:ThreatActor"]},
    "DigitalIdentity": {"close_mappings": ["stix:Identity"]},
    "Email": {"close_mappings": ["stix:EmailMessage"]},
    "IPAddress": {"close_mappings": ["stix:Ipv4Addr"]},
    "MACAddress": {"close_mappings": ["stix:MacAddr"]},
    "URL": {"close_mappings": ["stix:Url"]},
    "Certificate": {"close_mappings": ["stix:X509Certificate"]},
    "CertificateFile": {"close_mappings": ["stix:X509Certificate"]},
    "NetworkFlow": {"close_mappings": ["stix:NetworkTraffic"]},
    "UserProcess": {"close_mappings": ["stix:Process"]},
    # Related but not equivalent.
    "DefensiveTechnique": {"related_mappings": ["stix:CourseOfAction"]},
    "SecurityEvent": {"related_mappings": ["stix:ObservedData"]},
    # Broader STIX abstractions.
    "D3FENDKBThing": {"broad_mappings": ["stix:StixEntity"]},
    "CyberAction": {"broad_mappings": ["stix:StixDomainObject"]},
}

# ── static SPDX class mappings ───────────────────────────────────────────────
# Prefix target: https://lmodel.github.io/spdx/
SPDX_CLASS_MAPPINGS: dict[str, dict[str, list[str]]] = {
    # Exact class-name matches between D3FEND and SPDX schema.
    **{
        name: {"exact_mappings": [f"spdx:{name}"]}
        for name in [
            "Agent",
            "Artifact",
            "File",
            "Organization",
            "Person",
            "Vulnerability",
        ]
    },
    # Close semantic matches.
    "SoftwarePackage": {"close_mappings": ["spdx:Package"]},
    "DigitalDocument": {"close_mappings": ["spdx:SpdxDocument"]},
    "Software": {"close_mappings": ["spdx:SoftwareArtifact"]},
    # Related mappings to SPDX's generic core abstraction.
    "DefensiveTechnique": {"related_mappings": ["spdx:Element"]},
    "D3FENDKBThing": {"related_mappings": ["spdx:Element"]},
    # Broad mapping from specific D3FEND artifact classes into SPDX Element.
    "Artifact": {"broad_mappings": ["spdx:Element"]},
}

# ── static OSCAL class mappings ──────────────────────────────────────────────
# Prefix target: https://lmodel.github.io/oscal/
OSCAL_CLASS_MAPPINGS: dict[str, dict[str, list[str]]] = {
    # Exact class-name matches between D3FEND and OSCAL schemas.
    **{
        name: {"exact_mappings": [f"oscal:{name}"]}
        for name in [
            "Action",
            "Capability",
            "Group",
            "Link",
            "Metadata",
            "Resource",
            "Step",
        ]
    },
    # Close semantic matches.
    "DigitalDocument": {"close_mappings": ["oscal:OscalDocument"]},
    "File": {"close_mappings": ["oscal:Resource"]},
    "Organization": {"close_mappings": ["oscal:Party"]},
    "Person": {"close_mappings": ["oscal:Party"]},
    # Related mappings for defensive/control-oriented concepts.
    "DefensiveTechnique": {"related_mappings": ["oscal:Control"]},
    "DefensiveAction": {"related_mappings": ["oscal:ImplementedControlStatement"]},
    # Broader OSCAL abstractions.
    "CyberAction": {"broad_mappings": ["oscal:Action"]},
    "DigitalArtifact": {"broad_mappings": ["oscal:Resource"]},
}

if MAPPINGS_JSON_PATH.exists():
    try:
        mappings_payload = json.loads(MAPPINGS_JSON_PATH.read_text(encoding="utf-8"))
        for row in mappings_payload.get("results", {}).get("bindings", []):
            if not row:
                continue
            def_tech_uri = row.get("def_tech", {}).get("value")
            if not def_tech_uri or "#" not in def_tech_uri:
                continue
            def_local = def_tech_uri.split("#")[-1]

            off_tech_id = row.get("off_tech_id", {}).get("value")
            if off_tech_id:
                def_tech_to_attack_ids[def_local].add(off_tech_id)

            # broader ATT&CK parent in ontology namespace (if present)
            off_parent_uri = row.get("off_tech_parent", {}).get("value")
            if off_parent_uri and "#" in off_parent_uri:
                def_tech_to_broad_parents[def_local].add(off_parent_uri.split("#")[-1])

            # close match heuristic: exact label match between defensive/offensive
            def_label = (row.get("def_tech_label", {}).get("value") or "").strip().lower()
            off_label = (row.get("off_tech_label", {}).get("value") or "").strip().lower()
            if off_tech_id and def_label and off_label and def_label == off_label:
                def_tech_to_close_attack_ids[def_local].add(off_tech_id)
        print(f"  Loaded mappings rows: {len(mappings_payload.get('results', {}).get('bindings', []))}")
    except Exception as e:
        print(f"  WARNING: failed to parse {MAPPINGS_JSON_PATH}: {e}")
else:
    print(f"  WARNING: mappings artifact not found at {MAPPINGS_JSON_PATH}")

# ── collect all d3f:* entities ───────────────────────────────────────────────

all_classes = sorted(
    [c for c in set(g.subjects(RDF.type, OWL.Class))
     if isinstance(c, URIRef) and str(c).startswith(str(D3F))],
    key=str,
)
all_obj_props = sorted(
    [p for p in set(g.subjects(RDF.type, OWL.ObjectProperty))
     if isinstance(p, URIRef) and str(p).startswith(str(D3F))],
    key=str,
)
all_data_props = sorted(
    [p for p in set(g.subjects(RDF.type, OWL.DatatypeProperty))
     if isinstance(p, URIRef) and str(p).startswith(str(D3F))],
    key=str,
)
all_annot_props = sorted(
    [p for p in set(g.subjects(RDF.type, OWL.AnnotationProperty))
     if isinstance(p, URIRef) and str(p).startswith(str(D3F))],
    key=str,
)
all_named_inds = [
    i for i in set(g.subjects(RDF.type, OWL.NamedIndividual))
    if isinstance(i, URIRef) and str(i).startswith(str(D3F))
]

print(f"  Classes: {len(all_classes)}")
print(f"  ObjectProperties: {len(all_obj_props)}")
print(f"  DatatypeProperties: {len(all_data_props)}")
print(f"  AnnotationProperties: {len(all_annot_props)}")
print(f"  NamedIndividuals: {len(all_named_inds)}")

# ── helper: get label and definition for any URIRef ──────────────────────────

def get_label(uri):
    """Preferred label order: skos:prefLabel, rdfs:label, local_name."""
    return (
        g.value(uri, SKOS.prefLabel)
        or g.value(uri, RDFS.label)
        or local_name(uri)
    )

def get_definition(uri):
    return (
        g.value(uri, D3F.definition)
        or g.value(uri, D3F.description)
        or g.value(uri, DCTERMS.description)
        or g.value(uri, SKOS.definition)
    )

def get_comments(uri):
    """Collect all rdfs:comment and skos:example values."""
    comments = list(g.objects(uri, RDFS.comment)) + list(g.objects(uri, SKOS.example))
    return [str(c).strip() for c in comments if str(c).strip()]

def get_notes(uri):
    """Collect skos:scopeNote and skos:note values."""
    notes = list(g.objects(uri, SKOS.scopeNote)) + list(g.objects(uri, SKOS.note))
    return [str(n).strip() for n in notes if str(n).strip()]


def get_alt_labels(uri):
    """Collect skos:altLabel values."""
    return [str(v).strip() for v in g.objects(uri, SKOS.altLabel) if str(v).strip()]


def get_defined_bys(uri):
    """Collect rdfs:isDefinedBy URIs."""
    return [str(v) for v in g.objects(uri, RDFS.isDefinedBy) if isinstance(v, URIRef)]


def get_ontology_metadata():
    """Return ontology-level title, description, and license from the merged graph."""
    ontology = next(g.subjects(RDF.type, OWL.Ontology), None)
    if ontology is None:
        return {
            "title": "D3FEND\u2122 A Knowledge Graph of Cybersecurity Countermeasures",
            "description": (
                "D3FEND\u2122 is a knowledge graph of cybersecurity countermeasures developed\n"
                "by MITRE. This LinkML schema is generated from the authoritative OWL/TTL\n"
                "ontology artifacts."
            ),
            "license": "Apache-2.0",
        }
    return {
        "title": str(g.value(ontology, DCTERMS.title) or "D3FEND\u2122 A Knowledge Graph of Cybersecurity Countermeasures"),
        "description": str(g.value(ontology, DCTERMS.description) or ""),
        "license": str(g.value(ontology, DCTERMS.license) or "Apache-2.0"),
    }


def mapping_curies_from_class_annotations(class_local: str, class_annotations: dict[str, str]):
    """Build LinkML mapping lists for a class.

    Returns a dict with keys among:
      exact_mappings, related_mappings, close_mappings, broad_mappings
    """
    mapping_fields: dict[str, list[str]] = {
        "exact_mappings": [],
        "related_mappings": [],
        "close_mappings": [],
        "broad_mappings": [],
    }

    # Exact mappings from explicit identifiers.
    attack_id = class_annotations.get("attack-id")
    if attack_id:
        if attack_id.startswith("AML."):
            mapping_fields["exact_mappings"].append(f"atlas:{attack_id}")
        elif re.match(r"^ST\d{4}", attack_id):
            mapping_fields["exact_mappings"].append(f"sparta:{attack_id}")
        else:
            mapping_fields["exact_mappings"].append(f"attack:{attack_id}")

    cwe_id = class_annotations.get("cwe-id")
    if cwe_id:
        mapping_fields["exact_mappings"].append(f"cwe:{cwe_id}")

    capec_id = class_annotations.get("capec-id")
    if capec_id:
        mapping_fields["exact_mappings"].append(f"capec:{capec_id}")

    # Related mappings from curated def->off technique map.
    for off_id in sorted(def_tech_to_attack_ids.get(class_local, set())):
        mapping_fields["related_mappings"].append(f"attack:{off_id}")

    # Close mappings from strict same-label heuristic.
    for off_id in sorted(def_tech_to_close_attack_ids.get(class_local, set())):
        mapping_fields["close_mappings"].append(f"attack:{off_id}")

    # Broad mappings to ATT&CK parent techniques in D3FEND namespace.
    for parent_local in sorted(def_tech_to_broad_parents.get(class_local, set())):
        mapping_fields["broad_mappings"].append(f"d3f:{parent_local}")

    # UCO class mappings from static dictionary.
    uco_entry = UCO_CLASS_MAPPINGS.get(class_local, {})
    for field, values in uco_entry.items():
        mapping_fields[field].extend(values)

    # STIX class mappings from static dictionary.
    stix_entry = STIX_CLASS_MAPPINGS.get(class_local, {})
    for field, values in stix_entry.items():
        mapping_fields[field].extend(values)

    # SPDX class mappings from static dictionary.
    spdx_entry = SPDX_CLASS_MAPPINGS.get(class_local, {})
    for field, values in spdx_entry.items():
        mapping_fields[field].extend(values)

    # OSCAL class mappings from static dictionary.
    oscal_entry = OSCAL_CLASS_MAPPINGS.get(class_local, {})
    for field, values in oscal_entry.items():
        mapping_fields[field].extend(values)

    # De-duplicate and drop empty keys.
    compact = {}
    for key, values in mapping_fields.items():
        unique_values = sorted(set(values))
        if unique_values:
            compact[key] = unique_values
    return compact

# ── build individual-by-type index (for enums) ───────────────────────────────

ind_types: dict[str, list[str]] = defaultdict(list)
for ind in all_named_inds:
    for t in g.objects(ind, RDF.type):
        if isinstance(t, URIRef) and str(t).startswith(str(D3F)) and str(t) != str(OWL.NamedIndividual):
            ind_types[local_name(t)].append(local_name(ind))

# Classes with named individuals = potential enum candidates
# We'll generate actual enums for classes with <= 60 instances (clearly enumerable)
ENUM_MAX_SIZE = 60

enum_classes: set[str] = set()
for type_name, inds in ind_types.items():
    if 2 <= len(inds) <= ENUM_MAX_SIZE:
        enum_classes.add(type_name)

print(f"\nEnum candidates (2-{ENUM_MAX_SIZE} named individuals): {len(enum_classes)}")

# ── map OWL class URI → LinkML safe name ─────────────────────────────────────

class_uri_to_name: dict[str, str] = {}
for c in all_classes:
    class_uri_to_name[str(c)] = safe_name(local_name(c))

def range_name(uri):
    """Return LinkML class name for a URIRef range, or None."""
    if uri is None or isinstance(uri, BNode):
        return None
    s = str(uri)
    if s.startswith(str(D3F)):
        return safe_name(local_name(uri))
    return None

# ── annotation property names to use as class-level annotations ──────────────
# Key d3f annotation properties that make sense at the class level

CLASS_ANNOTATION_PROPS = {
    "attack-id":       str(D3F["attack-id"]),
    "d3fend-id":       str(D3F["d3fend-id"]),
    "cwe-id":          str(D3F["cwe-id"]),
    "capec-id":        str(D3F["capec-id"]),
    "display-order":   str(D3F["display-order"]),
    "display-priority":str(D3F["display-priority"]),
    "display-baseurl": str(D3F["display-baseurl"]),
    "release-date":    str(D3F["release-date"]),
    "synonym":         str(D3F["synonym"]),
    "pref-label":      str(D3F["pref-label"]),
    "kb-article":      str(D3F["kb-article"]),
    "kb-abstract":     str(D3F["kb-abstract"]),
    "kb-author":       str(D3F["kb-author"]),
    "kb-organization": str(D3F["kb-organization"]),
    "kb-mitre-analysis": str(D3F["kb-mitre-analysis"]),
}

# ── build the YAML string piece by piece ─────────────────────────────────────

lines = []
ontology_metadata = get_ontology_metadata()

def emit(s=""):
    lines.append(s)

# ── schema header ─────────────────────────────────────────────────────────────

emit("---")
emit("id: https://d3fend.mitre.org/ontologies/d3fend.owl")
emit("name: d3fend")
emit(f"title: {yaml_str(ontology_metadata['title'])}")
emit(f"description: {yaml_str(ontology_metadata['description'], 0)}")
emit(f"license: {yaml_str(ontology_metadata['license'])}")
emit("see_also:")
emit("  - https://d3fend.mitre.org/")
emit("  - https://github.com/d3fend/d3fend-ontology")
emit()

# ── prefixes ──────────────────────────────────────────────────────────────────

emit("prefixes:")
emit("  linkml: https://w3id.org/linkml/")
emit("  d3f: http://d3fend.mitre.org/ontologies/d3fend.owl#")
emit("  # --- placeholders: review and correct before use ---")
emit("  rdfs: http://www.w3.org/2000/01/rdf-schema#")
emit("  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#")
emit("  owl: http://www.w3.org/2002/07/owl#")
emit("  xsd: http://www.w3.org/2001/XMLSchema#")
emit("  skos: http://www.w3.org/2004/02/skos/core#")
emit("  dcterms: http://purl.org/dc/terms/")
emit("  dc: http://purl.org/dc/elements/1.1/")
emit("  schema: http://schema.org/")
emit("  dbr: http://dbpedia.org/resource/  # placeholder")
emit("  wikidata: https://www.wikidata.org/wiki/  # placeholder")
emit("  capec: https://capec.mitre.org/data/definitions/  # placeholder")
emit("  cve: https://nvd.nist.gov/vuln/detail/  # placeholder")
emit("  cwe: https://cwe.mitre.org/data/definitions/  # placeholder")
emit("  attack: https://attack.mitre.org/  # placeholder")
emit("  atlas: https://atlas.mitre.org/  # placeholder")
emit("  sparta: https://sparta.aerospace.org/  # placeholder")
emit("  cci: https://public.cyber.mil/stigs/cci/  # placeholder")
emit("  mitre-attack: https://attack.mitre.org/  # alias placeholder")
emit("  unified_cyber_ontology: https://lmodel.github.io/uco-master/  # UCO prefix")
emit("  stix: https://lmodel.github.io/stix/")
emit("  spdx: https://lmodel.github.io/spdx/")
emit("  oscal: https://lmodel.github.io/oscal/")
emit()
emit("default_prefix: d3f")
emit("default_range: string")
emit()
emit("imports:")
emit("  - linkml:types")
emit()

# ── subsets ───────────────────────────────────────────────────────────────────

emit("subsets:")
subsets = [
    ("D3FENDCoreSubset",        "Core D3FEND ontology classes and properties"),
    ("D3FENDKBThingSubset",     "D3FEND Knowledge Base reference entities"),
    ("ExternalThingSubset",     "External things referenced from the knowledge base"),
    ("ATTACKEnterprise",  "ATT&CK Enterprise technique classes"),
    ("ATTACKMobile",      "ATT&CK Mobile technique classes"),
    ("ATLASML",           "ATLAS (Adversarial Threat Landscape for AI Systems) classes"),
    ("SPARTA",            "SPARTA space threat taxonomy classes"),
    ("CWE",               "Common Weakness Enumeration classes"),
]
for name, desc in subsets:
    emit(f"  {name}:")
    emit(f"    description: {yaml_str(desc)}")
emit()

# ── enumerations ──────────────────────────────────────────────────────────────

emit("enums:")
emit()

# Only generate enums for classes with small sets of individuals
for type_name in sorted(enum_classes):
    inds = sorted(ind_types[type_name])
    enum_name = f"{safe_name(type_name)}Enum"
    # Get class URI for description
    class_uri = D3F[type_name]
    defn = get_definition(class_uri)
    emit(f"  {enum_name}:")
    emit(f"    description: >-")
    emit(f"      Enumeration of {type_name} values. Open set: additional string")
    emit(f"      values beyond this list are permitted.")
    if defn:
        emit(f"    notes:")
        emit(f"      - {yaml_str_inline(str(defn)[:300])}")
    emit(f"    permissible_values:")
    for ind_name in inds:
        safe_ind = safe_name(ind_name)
        ind_uri = D3F[ind_name]
        ind_label = get_label(ind_uri)
        ind_defn = get_definition(ind_uri)
        emit(f"      {safe_ind}:")
        if ind_label and str(ind_label) != ind_name:
            emit(f"        description: {yaml_str_inline(str(ind_label))}")
        if ind_defn:
            emit(f"        notes:")
            emit(f"          - {yaml_str_inline(str(ind_defn)[:400])}")
        # meaning links to the OWL individual (must be quoted: contains colon)
        emit(f'        meaning: "d3f:{ind_name}"')
    emit()

emit()

# ── slots (object properties, datatype properties, annotation props as slots) ─

emit("slots:")
emit()

# -- object properties as slots ------------------------------------------------
for p in all_obj_props:
    p_name = local_name(p)
    safe_p = safe_slot_name(p_name)
    label = get_label(p)
    defn = get_definition(p)
    comments = get_comments(p)
    notes = get_notes(p)
    alt_labels = get_alt_labels(p)
    defined_bys = get_defined_bys(p)

    domains = [str(d) for d in g.objects(p, RDFS.domain) if isinstance(d, URIRef)]
    ranges  = [str(r) for r in g.objects(p, RDFS.range)  if isinstance(r, URIRef)]

    # parent property
    sub_props = [str(sp) for sp in g.objects(p, RDFS.subPropertyOf)
                 if isinstance(sp, URIRef) and str(sp).startswith(str(D3F))]

    emit(f"  {safe_p}:")
    emit(f"    slot_uri: d3f:{p_name}")

    if sub_props:
        parent_sp = local_name(sub_props[0])
        emit(f"    is_a: {safe_slot_name(parent_sp)}")

    if label and str(label) != p_name:
        emit(f"    title: {yaml_str(str(label))}")

    if defn:
        emit(f"    description: {yaml_str(str(defn), 4)}")

    if comments:
        emit(f"    comments:")
        for c in comments:
            emit(f"      - {yaml_str_inline(c)}")

    if notes:
        emit(f"    notes:")
        for n in notes:
            emit(f"      - {yaml_str_inline(n)}")

    if alt_labels:
        emit(f"    aliases:")
        for alt in alt_labels:
            emit(f"      - {yaml_str_inline(alt)}")

    if defined_bys:
        emit(f"    see_also:")
        for ref in defined_bys:
            emit(f"      - {ref}")

    # domain hint
    if domains:
        d3f_domains = [safe_name(local_name(d)) for d in domains if d.startswith(str(D3F))]
        if d3f_domains:
            emit(f"    domain_of:")
            for d in d3f_domains:
                emit(f"      - {d}")

    # range
    d3f_ranges = [r for r in ranges if r.startswith(str(D3F))]
    if d3f_ranges:
        rn = safe_name(local_name(d3f_ranges[0]))
        emit(f"    range: {rn}")
    else:
        emit(f"    range: string")

    emit(f"    multivalued: true")
    emit()

# -- datatype properties as slots ----------------------------------------------
for p in all_data_props:
    p_name = local_name(p)
    safe_p = safe_slot_name(p_name)
    label = get_label(p)
    defn = get_definition(p)
    comments = get_comments(p)
    notes = get_notes(p)
    alt_labels = get_alt_labels(p)
    defined_bys = get_defined_bys(p)

    domains = [str(d) for d in g.objects(p, RDFS.domain) if isinstance(d, URIRef)]
    ranges  = [r for r in g.objects(p, RDFS.range)]

    sub_props = [str(sp) for sp in g.objects(p, RDFS.subPropertyOf)
                 if isinstance(sp, URIRef) and str(sp).startswith(str(D3F))]

    emit(f"  {safe_p}:")
    emit(f"    slot_uri: d3f:{p_name}")

    if sub_props:
        parent_sp = local_name(sub_props[0])
        emit(f"    is_a: {safe_slot_name(parent_sp)}")

    if label and str(label) != p_name:
        emit(f"    title: {yaml_str(str(label))}")

    if defn:
        emit(f"    description: {yaml_str(str(defn), 4)}")

    if comments:
        emit(f"    comments:")
        for c in comments:
            emit(f"      - {yaml_str_inline(c)}")

    if notes:
        emit(f"    notes:")
        for n in notes:
            emit(f"      - {yaml_str_inline(n)}")

    if alt_labels:
        emit(f"    aliases:")
        for alt in alt_labels:
            emit(f"      - {yaml_str_inline(alt)}")

    if defined_bys:
        emit(f"    see_also:")
        for ref in defined_bys:
            emit(f"      - {ref}")

    if domains:
        d3f_domains = [safe_name(local_name(d)) for d in domains if d.startswith(str(D3F))]
        if d3f_domains:
            emit(f"    domain_of:")
            for d in d3f_domains:
                emit(f"      - {d}")

    # Determine LinkML type from XSD range
    linkml_range = "string"
    for r in ranges:
        if isinstance(r, URIRef):
            lr = xsd_to_linkml(str(r))
            if lr != "string":
                linkml_range = lr
                break
        elif isinstance(r, BNode):
            # Look for xsd:integer based restrictions → treat as integer
            on_type = g.value(r, OWL.onDatatype)
            if on_type and "integer" in str(on_type):
                linkml_range = "integer"
                break
            # unionOf string types
            linkml_range = "string"

    # Special handling for known open-enum properties
    OPEN_ENUM_SLOTS = {
        "risk-impact": "RiskImpactEnum",
        "risk-likelihood": "RiskLikelihoodEnum",
        "stage": "StageEnum",
        "confidence": "ConfidenceEnum",
        "rating": "RatingEnum",
        "expectation-rating": "ExpectationRatingEnum",
    }
    if p_name in OPEN_ENUM_SLOTS:
        enum_ref = OPEN_ENUM_SLOTS[p_name]
        emit(f"    any_of:")
        emit(f"      - range: {enum_ref}")
        emit(f"      - range: string")
    else:
        emit(f"    range: {linkml_range}")

    emit()

# -- annotation properties as slots -------------------------------------------
# Generate slots for all native D3FEND annotation properties.
ANNOT_SLOT_RANGES = {
    "attack-id":          "string",
    "d3fend-id":          "string",
    "cwe-id":             "string",
    "capec-id":           "string",
    "display-order":      "integer",
    "display-priority":   "integer",
    "display-baseurl":    "uri",
    "release-date":       "string",
    "synonym":            "string",
    "pref-label":         "string",
    "kb-article":         "string",
    "kb-abstract":        "string",
    "kb-author":          "string",
    "kb-organization":    "string",
    "kb-mitre-analysis":  "string",
    "kb-reference-title": "string",
    "attack-kb-annotation": "string",
    "cwe-kb-annotation":  "string",
    "d3fend-annotation":  "string",
    "description":        "string",
    "definition":         "string",
    "label":              "string",
    "identifier":         "string",
    "display-baseurl":    "uri",
}

for p in all_annot_props:
    p_name = local_name(p)
    safe_p = safe_slot_name(p_name)
    label = get_label(p)
    defn = get_definition(p)
    comments = get_comments(p)
    notes = get_notes(p)
    alt_labels = get_alt_labels(p)
    defined_bys = get_defined_bys(p)

    emit(f"  {safe_p}:")
    emit(f"    slot_uri: d3f:{p_name}")
    if label and str(label) != p_name:
        emit(f"    title: {yaml_str(str(label))}")
    if defn:
        emit(f"    description: {yaml_str(str(defn), 4)}")

    if comments:
        emit(f"    comments:")
        for c in comments:
            emit(f"      - {yaml_str_inline(c)}")

    if notes:
        emit(f"    notes:")
        for n in notes:
            emit(f"      - {yaml_str_inline(n)}")

    if alt_labels:
        emit(f"    aliases:")
        for alt in alt_labels:
            emit(f"      - {yaml_str_inline(alt)}")

    if defined_bys:
        emit(f"    see_also:")
        for ref in defined_bys:
            emit(f"      - {ref}")

    r = ANNOT_SLOT_RANGES.get(p_name, "string")
    if r == "string" and p_name in ("synonym", "kb-author"):
        emit(f"    range: {r}")
        emit(f"    multivalued: true")
    else:
        emit(f"    range: {r}")
    emit()

emit()

# ── inline open-enum stubs (referenced above but not from ind_types) ──────────
# If any OPEN_ENUM_SLOTS enums don't exist yet, add them to enum section header

OPEN_ENUM_STUBS = {
    "RiskImpactEnum":       ["Very Low", "Low", "Medium", "High", "Very High"],
    "RiskLikelihoodEnum":   ["Very Low", "Low", "Medium", "High", "Very High"],
    "StageEnum":            [],
    "ConfidenceEnum":       ["Low", "Medium", "High"],
    "RatingEnum":           [],
    "ExpectationRatingEnum":[],
}

# We'll add these to the enum section - need to go back and insert,
# or just append. For YAML ordering, append to the enums block.
# We'll handle this by post-processing the lines.

# ── classes ───────────────────────────────────────────────────────────────────

emit("classes:")
emit()

# Class → set of applicable slots (from domain declarations)
class_domain_slots: dict[str, list[str]] = defaultdict(list)
for p in all_obj_props + all_data_props:
    p_name = safe_slot_name(local_name(p))
    for d in g.objects(p, RDFS.domain):
        if isinstance(d, URIRef) and str(d).startswith(str(D3F)):
            class_domain_slots[safe_name(local_name(d))].append(p_name)

# Determine subset for a class
def get_subset(name: str, uri) -> list[str]:
    subsets_list = []
    s = name
    if s.startswith("T") and re.match(r"T\d{4}", s):
        subsets_list.append("ATTACKEnterprise")
    elif s.startswith("TA") and re.match(r"TA\d{4}", s):
        subsets_list.append("ATTACKEnterprise")
    elif s.startswith("AML_") or s.startswith("AML"):
        subsets_list.append("ATLASML")
    elif s.startswith("ST") and re.match(r"ST\d{4}", s):
        subsets_list.append("SPARTA")
    elif s.startswith("CWE"):
        subsets_list.append("CWE")
    elif s.startswith("M1") and re.match(r"M1\d{3}", s):
        subsets_list.append("ATTACKEnterprise")
    elif s.startswith("DS") and re.match(r"DS\d{4}", s):
        subsets_list.append("ATTACKEnterprise")
    # Check inheritance from Core
    parents = [str(p) for p in g.objects(uri, RDFS.subClassOf) if isinstance(p, URIRef)]
    if not subsets_list:
        if any("D3FENDCore" in p for p in parents):
            subsets_list.append("D3FENDCoreSubset")
        elif any("D3FENDKBThing" in p for p in parents):
            subsets_list.append("D3FENDKBThingSubset")
        elif any("ExternalThing" in p for p in parents):
            subsets_list.append("ExternalThingSubset")
    return subsets_list

# Track which class names we emit (to avoid duplicates if safe_name collides)
emitted_class_names: set[str] = set()

for c in all_classes:
    c_local = local_name(c)
    c_name  = safe_name(c_local)

    # Avoid duplicate safe names
    if c_name in emitted_class_names:
        continue
    emitted_class_names.add(c_name)

    label    = get_label(c)
    defn     = get_definition(c)
    comments = get_comments(c)
    notes    = get_notes(c)
    alt_labels = get_alt_labels(c)

    # Get d3f-specific annotations present on this class
    class_annotations: dict[str, str] = {}
    for ann_key, ann_uri in CLASS_ANNOTATION_PROPS.items():
        val = g.value(c, URIRef(ann_uri))
        if val is not None:
            class_annotations[ann_key] = str(val).strip()

    # Parent class(es) — prefer single d3f parent; skip BNodes
    parents_uris = [p for p in g.objects(c, RDFS.subClassOf)
                    if isinstance(p, URIRef) and str(p).startswith(str(D3F))]

    # Also check if was declared in OWL as a NamedIndividual (singleton pattern)
    is_also_individual = (c, RDF.type, OWL.NamedIndividual) in g

    # seeAlso
    see_alsos = [str(sa) for sa in g.objects(c, RDFS.seeAlso) if isinstance(sa, URIRef)]
    defined_bys = get_defined_bys(c)

    # Slots declared on this class through domain
    local_slots = class_domain_slots.get(c_name, [])

    # Mapping fields from IDs and curated mappings artifact.
    class_mappings = mapping_curies_from_class_annotations(c_local, class_annotations)

    emit(f"  {c_name}:")
    emit(f"    class_uri: d3f:{c_local}")

    if len(parents_uris) == 1:
        parent_name = safe_name(local_name(parents_uris[0]))
        emit(f"    is_a: {parent_name}")
    elif len(parents_uris) > 1:
        parent_name = safe_name(local_name(parents_uris[0]))
        emit(f"    is_a: {parent_name}")
        mixins = [safe_name(local_name(p)) for p in parents_uris[1:]]
        emit(f"    mixins:")
        for m in mixins:
            emit(f"      - {m}")

    if label and str(label) != c_local:
        emit(f"    title: {yaml_str(str(label))}")

    if defn:
        emit(f"    description: {yaml_str(str(defn), 4)}")

    if comments:
        emit(f"    comments:")
        for c_text in comments:
            emit(f"      - {yaml_str_inline(c_text)}")

    if notes:
        emit(f"    notes:")
        for n in notes:
            emit(f"      - {yaml_str_inline(n)}")

    if alt_labels:
        emit(f"    aliases:")
        for alt in alt_labels:
            emit(f"      - {yaml_str_inline(alt)}")

    merged_see_alsos = []
    for ref in see_alsos + defined_bys:
        if ref not in merged_see_alsos:
            merged_see_alsos.append(ref)

    if merged_see_alsos:
        emit(f"    see_also:")
        for sa in merged_see_alsos[:8]:
            emit(f"      - {sa}")

    if is_also_individual:
        emit(f"    annotations:")
        emit(f"      owl_named_individual: \"true\"")

    if class_annotations:
        if not is_also_individual:
            emit(f"    annotations:")
        for k, v in class_annotations.items():
            emit(f"      {safe_name(k)}: {yaml_str_inline(v[:300])}")

    if class_mappings:
        for field_name in ("exact_mappings", "related_mappings", "close_mappings", "broad_mappings"):
            values = class_mappings.get(field_name)
            if values:
                emit(f"    {field_name}:")
                for v in values:
                    emit(f"      - {v}")

    if local_slots:
        emit(f"    slots:")
        for sl in sorted(set(local_slots)):
            emit(f"      - {sl}")

    emit()

# ── open enum stubs to inject into enums section ──────────────────────────────

OPEN_ENUM_YAML = {
    "RiskImpactEnum": {
        "description": "Risk impact level. Open enum: arbitrary string values also accepted.",
        "values": ["Very_Low", "Low", "Medium", "High", "Very_High"],
    },
    "RiskLikelihoodEnum": {
        "description": "Risk likelihood level. Open enum: arbitrary string values also accepted.",
        "values": ["Very_Low", "Low", "Medium", "High", "Very_High"],
    },
    "ConfidenceEnum": {
        "description": "Confidence level. Open enum: arbitrary string values also accepted.",
        "values": ["Low", "Medium", "High"],
    },
    "StageEnum": {
        "description": "Stage value. Open enum: arbitrary string values also accepted.",
        "values": ["Unspecified"],
    },
    "RatingEnum": {
        "description": "Generic rating. Open enum: arbitrary string values also accepted.",
        "values": ["Unspecified"],
    },
    "ExpectationRatingEnum": {
        "description": "Expectation rating. Open enum: arbitrary string values also accepted.",
        "values": ["Unspecified"],
    },
}

# ── write output ──────────────────────────────────────────────────────────────

output_path = "src/d3fend/schema/d3fend.yaml"

# We inject the open enum stubs immediately before the `slots:` section.
# This keeps all enums in one place and avoids in-entry insertion mistakes.
yaml_text = "\n".join(lines)

# Build open enum YAML block
open_enum_block = []
for enum_name, enum_info in OPEN_ENUM_YAML.items():
    open_enum_block.append(f"  {enum_name}:")
    open_enum_block.append(f"    description: {yaml_str(enum_info['description'])}")
    open_enum_block.append(f"    # open enum: consuming slots use any_of [range: {enum_name}, range: string]")
    if enum_info["values"]:
        open_enum_block.append(f"    permissible_values:")
        for v in enum_info["values"]:
            open_enum_block.append(f"      {v}:")
            open_enum_block.append(f"        description: {yaml_str(v.replace('_', ' '))}")
    open_enum_block.append("")

open_enum_yaml_str = "\n".join(open_enum_block)

# Insert once before `slots:` section; fail fast if insertion point is missing.
slots_marker = "\nslots:\n"
if slots_marker not in yaml_text:
    raise RuntimeError("Expected `slots:` section marker not found while injecting open enums")
yaml_text = yaml_text.replace(slots_marker, "\n" + open_enum_yaml_str + slots_marker, 1)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(yaml_text)
    f.write("\n")

print(f"\nWrote {output_path}")
print(f"Lines: {yaml_text.count(chr(10))}")
