"""Verify both executable controls in each A08 lesson."""

import subprocess
import sys
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A08-reliability-operations-and-sre"
)
EXPECTED = (
    (0.999, 999),
    (100, 100000),
    (0.998001, 0.999),
    (94, 100),
    (10, 2000),
    (24000, 500),
    (210, 300),
    (3, 27),
    (0, 300),
    (7, 10),
    (60, 120),
    (20, 100),
    (10, 5),
    (23, 30),
    (10.0, 0.01),
    (36, 720),
    (18000, 200),
    (2048, 240),
    (5, 14),
    (7, 12),
    (200, 100),
    (100, 1000),
    (1, 0),
    (0, 2),
    (90, 40),
    (0.1, 100),
    (30, 60000),
    (100, 2000),
    (0.005, 0.01),
    (0.01, 10),
)


@pytest.mark.parametrize("index,expected", list(enumerate(EXPECTED, 1)))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "failure"])
def test_reliability_example(index: int, expected: tuple, broken: bool) -> None:
    lesson = f"A08.{index:02d}"
    text = (PHASE / "lessons" / f"{lesson}.md").read_text()
    assert all(f"## {heading}." in text for heading in range(1, 9))
    command = [sys.executable, str(PHASE / "examples" / f"{lesson}.py")]
    if broken:
        command.append("--break")
    result = subprocess.run(
        command, capture_output=True, text=True, timeout=8, check=False
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == repr(expected[broken])
