"""Run the curriculum examples and check that indexed files exist."""

from pathlib import Path
import re
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
PHASE = ROOT / "01-architecture-A01-to-A20/A01-computer-systems-and-os"
EXPECTED = (
    ("85.90", "10.74"),
    ("4660", "13330"),
    ("7f", "out of range"),
    ("5", "unsupported opcode"),
    ("RETURN", "source rejected"),
    ("blue 0", "7"),
    ("b'OK'", "b''"),
    ("hit\nhit", "miss\nmiss\nmiss"),
    ("HALT 2", "PC outside program"),
    ("20", "misaligned"),
    ("b'K'", "kernel errno"),
    ("port=8000", "startup errno"),
    ("reaped: 7", "wait: None"),
    ("True", "False"),
    ("True", "False"),
    ("3", "50005000"),
    ("traced bytes", "traced bytes"),
    ("45063", "unmapped page: 2"),
    ("minor faults delta", "minor faults delta"),
    ("after join: [3]", "read early: []"),
    ("voluntary:", "involuntary:"),
    ("B 1 7", "B 3 8"),
    ("True", "language exception"),
    ("EOF handled", "incorrectly retrying EOF"),
    ("2", "1"),
    ("3 True", "3 False"),
    ("cycle: False", "cycle: True"),
    ("", ""),
    ("transfers: 0", "transfers: 9"),
    ("seconds", "seconds"),
    ("file: b'ABC'", "file: b'ZBC'"),
    ("60.0", "100"),
    ("", "0.5 CPU"),
    ("160 MiB", "7168 MiB"),
    ("210", "50"),
    ("amd64 manifest exists: True", "amd64 manifest exists: False"),
)


@pytest.mark.parametrize("number,expected", list(enumerate(EXPECTED, 1)))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "failure"])
def test_lesson_variants(number: int, expected: tuple[str, str], broken: bool) -> None:
    lesson = f"A01.{number:02}"
    doc = (PHASE / "lessons" / f"{lesson}.md").read_text()
    for heading in range(1, 9):
        assert f"## {heading}." in doc
    command = [sys.executable, str(PHASE / "examples" / f"{lesson}.py")]
    if broken:
        command.append("--break")
    result = subprocess.run(command, capture_output=True, text=True, timeout=8)
    assert result.returncode == 0, result.stderr
    assert result.stdout
    assert expected[broken] in result.stdout


def test_stage_zero_quiz() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "00-stage-0-diagnostic/diagnose.py")],
        input="b\nb\nc\nd\na\n",
        capture_output=True,
        text=True,
        timeout=4,
    )
    assert result.returncode == 0, result.stderr
    assert "Baseline 5/5" in result.stdout


def test_relative_markdown_links() -> None:
    for file in ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in file.relative_to(ROOT).parts):
            continue
        for link in re.findall(r"\]\(([^\s)]+)\)", file.read_text()):
            path = link.split("#")[0]
            if path and "://" not in path:
                assert (file.parent / path).exists(), (file.relative_to(ROOT), link)


def test_all_quantitative_checks() -> None:
    pytest.importorskip("numpy")
    for file in sorted((PHASE / "lessons").glob("A01.*.md")):
        snippet = re.search(r"```python\n(import numpy as np[\s\S]+?)```", file.read_text())
        assert snippet is not None, file.name
        exec(compile(snippet[1], str(file), "exec"), {})


@pytest.mark.parametrize(
    "broken,expected", [(False, "server received"), (True, "before payload transfer")]
)
def test_loopback_diagnostic(broken: bool, expected: str) -> None:
    command = [sys.executable, str(ROOT / "00-stage-0-diagnostic/loopback.py")]
    if broken:
        command.append("--break")
    result = subprocess.run(command, capture_output=True, text=True, timeout=4, check=False)
    assert result.returncode == 0, result.stderr
    assert expected in result.stdout
