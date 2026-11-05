"""Checks the upstream watch's decisions against stubbed answers.

scripts/check_upstream_release.py reads MITRE's public files. These tests replace its one
network call, `_get`, with a table of answers, so they run offline. They show what the
report says in each case the watch knows: another edition, changed bytes under the same
edition, a changed versioned file, a changed licence, changed terms, and a check that could
not finish.
"""

import http.client
import importlib.util
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
UPSTREAM = ROOT / "upstream"
TURTLE = (UPSTREAM / "d3fend.ttl").read_bytes()


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's stub."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _terms_page():
    """A page in the shape of MITRE's, which yields the pinned text."""
    paragraphs = (
        (UPSTREAM / "TERMS.txt").read_text(encoding="utf-8").strip().split("\n\n")
    )
    body = "".join(f"<p>{line}</p>" for line in paragraphs[1:])
    return f'<section class="content"><h2>{paragraphs[0]}</h2>{body}</section>'.encode()


def _answers(watch):
    """The answers of an unchanged upstream, with the parts a test changes."""
    return {
        watch.LATEST_URL: TURTLE,
        watch.PINNED_SOURCE: TURTLE,
        watch.LICENCE_URL: (UPSTREAM / "LICENSE.md").read_bytes(),
        watch.TERMS_URL: _terms_page(),
    }


def _run(watch, answers, capsys, argv=()):
    def fake_get(url):
        answer = answers[url]
        if isinstance(answer, Exception):
            raise answer
        return answer

    watch._get = fake_get
    code = watch.main(list(argv))
    return code, capsys.readouterr().out


def _not_found(url):
    return urllib.error.HTTPError(url, 404, "Not Found", None, None)


def test_an_unchanged_upstream_reports_nothing(watch, capsys):
    code, report = _run(watch, _answers(watch), capsys)
    assert code == 0, report
    assert "**" not in report


def test_another_edition_is_reported_and_quoted(watch, capsys):
    answers = _answers(watch)
    answers[watch.LATEST_URL] = TURTLE.replace(
        b'owl:versionInfo "1.6.0"', b'owl:versionInfo "1.7.0"'
    )
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "The latest D3FEND is edition `1.7.0`" in report


def test_changed_bytes_under_the_same_edition_are_reported(watch, capsys):
    answers = _answers(watch)
    answers[watch.LATEST_URL] = TURTLE + b"\n# changed\n"
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "changed under edition 1.6.0" in report


def test_a_turtle_with_no_edition_stops_the_check(watch, capsys):
    answers = _answers(watch)
    answers[watch.LATEST_URL] = b"an error page"
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "The latest edition check could not finish" in report


def test_a_changed_versioned_file_is_reported(watch, capsys):
    answers = _answers(watch)
    answers[watch.PINNED_SOURCE] = TURTLE + b"\n"
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert f"{watch.PINNED_SOURCE} changed" in report


def test_a_versioned_file_that_is_gone_is_reported(watch, capsys):
    answers = _answers(watch)
    answers[watch.PINNED_SOURCE] = _not_found(watch.PINNED_SOURCE)
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "The pinned file check could not finish" in report


def test_a_changed_licence_is_reported(watch, capsys):
    answers = _answers(watch)
    answers[watch.LICENCE_URL] = b"Another licence\n"
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert f"{watch.LICENCE_URL} changed" in report


def test_changed_terms_are_reported(watch, capsys):
    answers = _answers(watch)
    answers[watch.TERMS_URL] = _terms_page().replace(b"royalty-free", b"paid")
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "The Terms of Use changed" in report


def test_a_terms_page_of_another_shape_stops_the_check(watch, capsys):
    answers = _answers(watch)
    answers[watch.TERMS_URL] = b"<html>moved</html>"
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "The terms of use check could not finish" in report


@pytest.mark.parametrize(
    "failure",
    [
        OSError("refused"),
        http.client.RemoteDisconnected("cut off"),
        EOFError("short"),
        ValueError("too large"),
    ],
    ids=["refused", "cut-off", "short", "too-large"],
)
def test_a_check_that_cannot_finish_fails_the_run(watch, capsys, failure):
    answers = _answers(watch)
    answers[watch.LATEST_URL] = failure
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "could not finish" in report


def test_the_report_is_also_written_to_a_file(watch, capsys, tmp_path):
    target = tmp_path / "report.md"
    code, report = _run(watch, _answers(watch), capsys, ["--report", str(target)])
    assert code == 0
    assert target.read_text(encoding="utf-8") == report


def test_text_a_server_chose_cannot_mention_anyone(watch):
    """A code span on one line, with no back tick of its own and no blank line."""
    assert watch._code("@someone\n\n`x`  y") == "`@someone 'x' y`"


@pytest.mark.parametrize(
    "address",
    [
        "http://d3fend.mitre.org/x",
        "https://example.org/x",
        "https://d3fend.mitre.org.example.org/x",
    ],
)
def test_a_redirect_off_the_expected_hosts_is_refused(watch, address):
    handler = watch._ExpectedHostRedirect()
    with pytest.raises(ValueError, match="off the expected hosts"):
        handler.redirect_request(None, None, 302, "Found", {}, address)


def test_the_terms_page_keeps_each_paragraph_and_each_address(watch):
    page = (
        b'<h2>LICENSE</h2> <p>The MITRE\n   Corporation grants.</p> <p>See the <a href="'
        b'https://example.org/t">terms</a>.<br/>Next line</p></section>'
    )
    assert watch.terms_text(page) == (
        "LICENSE\n\nThe MITRE Corporation grants.\n\n"
        "See the terms (https://example.org/t).\n\nNext line\n"
    )
