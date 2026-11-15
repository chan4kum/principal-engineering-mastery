"""Verify both executable controls in each A10 lesson."""

import subprocess
import sys
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops"
)
EXPECTED = (
    (8, 6),
    ((4, 2), (3, 2)),
    (2.4, 3.6),
    (0.375, 0.25),
    (0.09174, 0.9),
    (4.0, 0),
    (150, 1000),
    (5.0, 2),
    (2, 12),
    (10, 0),
    (0.4, 0.8),
    (8, 1),
    (10.24, 16),
    (0.05, 0.5),
    (2.0, 14),
    (6, 3),
    (6, 2),
    (1, 3),
    (80.0, 20.0),
    (2.0, 4),
    (0.6, 0.9),
    (0.025, 25),
    (12, 3),
    (9, 25),
    (65536, 16384),
    (1000, 1001000),
    (0.9, 9),
    (0.05, 0.5),
    (0.01, 0.1),
    (0, 10),
    (0.75, 0.9),
    (0.02, 20),
    (False, True),
    (100, 1000),
    (2000000000, 1000000000),
)


@pytest.mark.parametrize("index,expected", list(enumerate(EXPECTED, 1)))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "failure"])
def test_ml_example(index: int, expected: tuple, broken: bool) -> None:
    lesson = f"A10.{index:02d}"
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
