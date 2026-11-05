"""d3fend.

D3FEND™ - A knowledge graph of cybersecurity countermeasures: LinkML Schema
"""

try:
    from d3fend._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
