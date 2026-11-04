#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check MITRE's D3FEND files against the edition the schema renders.

The schema renders D3FEND at the edition pinned below, and upstream/ holds its Turtle file
unchanged. Three things can change without any change in this repository:

- MITRE publishes another edition of the ontology;
- the pinned file, or the licence file at the pinned tag, changes;
- the Terms of Use change.

The script reads MITRE's public files and compares each by git object hash. It prints a
Markdown report, and exits 1 when:

- the latest Turtle file names another edition, or holds other bytes under the same one;
- the versioned Turtle file changed or is gone;
- the licence file at the pinned tag changed or is gone;
- the Terms of Use changed;
- a check could not finish, such as a refused or failed request, or an answer larger than
  the script reads.

Text a server chose is quoted as code on one line in the report, so the issue the workflow
opens from it cannot mention anyone. A redirect is followed only to an https address on the
expected hosts. The script sends no token. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import html
import http.client
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

USER_AGENT = "lmodel-d3fend-watch"
SITE = "https://d3fend.mitre.org"
# The hosts a redirect may lead to.
HOSTS = frozenset({"d3fend.mitre.org", "raw.githubusercontent.com"})

# The most the script reads of one answer. The largest, the Turtle file, is about 4 MB.
MAX_BYTES = 20_000_000

# The edition the schema renders, its release date and the tag that built it.
# tests/test_upstream.py holds the schema headers and these pins equal. Move them together,
# with upstream/ and the headers, for another edition.
PINNED_EDITION = "1.6.0"
PINNED_DATE = "2026-08-31"
PINNED_TAG_COMMIT = "91629abb966e"
PINNED_SOURCE = f"{SITE}/ontologies/d3fend/{PINNED_EDITION}/d3fend.ttl"
LATEST_URL = f"{SITE}/ontologies/d3fend.ttl"
TERMS_URL = f"{SITE}/tou/"
LICENCE_URL = (
    "https://raw.githubusercontent.com/d3fend/d3fend-ontology/"
    f"{PINNED_EDITION}/LICENSE.md"
)

# Each file upstream/ holds, with its git object hash. tests/test_upstream.py holds
# upstream/ to this list.
PINNED_BLOBS = {
    "README.md": "1873b156b235fd326fb4a9eb32b92effc0348188",
    "TERMS.txt": "f4edcc2bdea0fdecd2706a5c31e759467512c5f7",
    "LICENSE.md": "c8953158bcad8bcc59457b62ba5d2505dcb9b2b4",
    "d3fend.ttl": "04a9ba1e3d521de6acc9ccfeff77eb630c487bee",
}

TERMS_START = "<h2>LICENSE</h2>"
TERMS_END = "</section>"
VERSION_INFO = re.compile(rb'owl:versionInfo "([^"]+)"')


class _ExpectedHostRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on one of HOSTS."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname not in HOSTS:
            raise ValueError(f"a redirect leads off the expected hosts, to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# An opener in place of urlopen's, whose redirect handler follows any address.
_open = urllib.request.build_opener(_ExpectedHostRedirect).open


def _get(url: str) -> bytes:
    """The body of an answer, read up to the cap."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with _open(req, timeout=60) as resp:
        body = resp.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"the answer from {url} is larger than {MAX_BYTES} bytes")
    return body


def _code(text: object) -> str:
    """Text a server chose, as a code span on one line, so it cannot mention a
    person or add a link in the issue. A blank line would end the span, so
    every run of spaces and line breaks is one space."""
    return "`" + " ".join(str(text).replace("`", "'").split()) + "`"


def blob(data: bytes) -> str:
    """The git object hash of a file's bytes."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def terms_text(page: bytes) -> str:
    """The Terms of Use from the page: a paragraph per line, no markup."""
    text = page.decode("utf-8", errors="replace")
    start = text.find(TERMS_START)
    end = text.find(TERMS_END, start)
    if start < 0 or end < start:
        raise ValueError("the Terms of Use page has another shape")
    # The page wraps its source at random, so whitespace means nothing until the markup
    # that ends a line is read. A link keeps its address, which the terms rely on.
    body = " ".join(text[start:end].split())
    body = re.sub(r'<a href="([^"]+)">([^<]+)</a>', r"\2 (\1)", body)
    body = re.sub(r"</(p|h\d)>|<br\s*/?>", "\n", body)
    body = html.unescape(re.sub(r"<[^>]+>", " ", body))
    lines = [" ".join(line.split()) for line in body.splitlines()]
    return "\n\n".join(line for line in lines if line) + "\n"


def edition_of(turtle: bytes) -> str:
    """The edition a Turtle file names in its ontology header."""
    found = VERSION_INFO.search(turtle)
    if found is None:
        raise ValueError("the Turtle file names no owl:versionInfo")
    return found.group(1).decode("utf-8", errors="replace")


def check_latest() -> tuple[list[str], bool]:
    """Report whether the latest Turtle file is the pinned edition, byte for byte."""
    data = _get(LATEST_URL)
    edition = edition_of(data)
    if edition != PINNED_EDITION:
        return [
            f"- **The latest D3FEND is edition {_code(edition)}; the schema renders "
            f"{PINNED_EDITION}.** Read what changed, decide whether the schema moves to "
            "it, and move upstream/, the pins here and the schema headers together."
        ], True
    if blob(data) != PINNED_BLOBS["d3fend.ttl"]:
        return [
            f"- **The latest Turtle file changed under edition {PINNED_EDITION}.** Find "
            "out what changed before trusting the copy in upstream/."
        ], True
    return [f"- The latest D3FEND is the pinned edition, {PINNED_EDITION}."], False


def check_pinned() -> tuple[list[str], bool]:
    """Report whether the versioned Turtle file is the pinned file."""
    if blob(_get(PINNED_SOURCE)) != PINNED_BLOBS["d3fend.ttl"]:
        return [
            f"- **{PINNED_SOURCE} changed.** Read what changed, then move upstream/ and "
            "the pin, or find out why a published edition moved."
        ], True
    return [f"- The versioned Turtle file of {PINNED_EDITION} is the pinned file."], False


def check_licence() -> tuple[list[str], bool]:
    """Report whether the licence file at the pinned tag is the pinned file."""
    if blob(_get(LICENCE_URL)) != PINNED_BLOBS["LICENSE.md"]:
        return [
            f"- **{LICENCE_URL} changed.** Read what changed, and update NOTICE and "
            "upstream/LICENSE.md if the licence moved."
        ], True
    return ["- The licence file at the pinned tag is the pinned file."], False


def check_terms() -> tuple[list[str], bool]:
    """Report whether the Terms of Use are the pinned text."""
    text = terms_text(_get(TERMS_URL))
    if blob(text.encode("utf-8")) != PINNED_BLOBS["TERMS.txt"]:
        return [
            f"- **The Terms of Use changed at {TERMS_URL}.** Read what changed, update "
            "NOTICE and upstream/TERMS.txt if the licence moved, and move the pin."
        ], True
    return ["- The Terms of Use are the pinned text."], False


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("latest edition", check_latest),
    ("pinned file", check_pinned),
    ("licence", check_licence),
    ("terms of use", check_terms),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines = [
        f"- Pinned edition: D3FEND {PINNED_EDITION} of {PINNED_DATE}, {PINNED_SOURCE}."
    ]
    attention = False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed request and a timeout, HTTPException and
        # EOFError a connection cut off mid-answer, and ValueError an answer too large or
        # of another shape.
        except (OSError, http.client.HTTPException, EOFError, ValueError) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
