"""Verify both executable controls in each A07 lesson."""

import subprocess
import sys
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A07-application-integration-arch"
)
EXPECTED = (
    (7, 12),
    (1, 8),
    (6, 20),
    (6, 2),
    (40, 0),
    (45, 15),
    (1, 6),
    (8, 4),
    (6, 1),
    (12, 4),
    (48, 12),
    (3, 1),
    (40, 20),
    (6, 3),
    (20, 100),
    (1000, 10000),
    (1, 2),
    (6000, 30),
    (1, 2),
    (4, 8),
    (12, 30),
    (40, 60),
    (4, 8),
    (30, 10),
    (60, 20),
    (60, 400),
    (4, 1),
    (4, 2),
    (12, 4800),
    (2, 1),
    (20, 5),
)


@pytest.mark.parametrize("index,expected", list(enumerate(EXPECTED, 1)))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "failure"])
def test_integration_example(index: int, expected: tuple, broken: bool) -> None:
    lesson = f"A07.{index:02d}"
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
