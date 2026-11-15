"""Verify both executable controls in each A06 lesson."""

import subprocess
import sys
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A06-distributed-systems-coordination"
)
EXPECTED = (
    (1, 3),
    (3, -5),
    (2, 3),
    (5, 10),
    (100, 110),
    (6, 1),
    (True, False),
    (False, True),
    (False, True),
    (20, 100),
    (1, 2),
    ((2, 2), (2, 1)),
    (False, True),
    (True, False),
    (50, 0),
    (8, 5),
    (160, 8),
    (False, True),
    (True, False),
    (False, True),
    (13, 16),
    (False, True),
    (2, 0),
    (40, 30),
    (16, 4),
    (10, 1024),
    (0.2, 0.8),
    (3, 6),
    (5, 10),
    (8, -7),
    (4096, 4097),
    (24, 4),
)


@pytest.mark.parametrize("index,expected", list(enumerate(EXPECTED, 1)))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "failure"])
def test_coordination_example(index: int, expected: tuple, broken: bool) -> None:
    lesson = f"A06.{index:02d}"
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
