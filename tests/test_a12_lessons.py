"""Verify both executable controls in each A12 lesson."""

import subprocess
import sys
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems"
)
EXPECTED = (
    (2, 1),
    (1, 3),
    (80, 10000),
    ([3, 7], [1, 3, 4, 7]),
    (1, 3),
    (1.692, 4),
    (3, 4),
    (0.5, 0.75),
    (1.0, 6),
    (10, 5),
    (4, 1000),
    (150, 200),
    (6, 10),
    (0.03202, 0.01639344262295082),
    (0.8, 1.0),
    (16000, 1000),
    (15, 5),
    (100, 2),
    (0.5, 4),
    (0.25, 0.4),
    (0.7, 1.0),
    (200, 40),
    (4, 10),
    (12, 3),
    (10, 40),
    (9, 3),
    (6, 2),
    (5, 3),
    (2000, 100),
    (2, 1),
    (0, 1),
    (20, 80),
    (100, 500),
    (1, 2),
)


@pytest.mark.parametrize("index,expected", list(enumerate(EXPECTED, 1)))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "failure"])
def test_phase_12_example(index: int, expected: tuple, broken: bool) -> None:
    lesson = f"A12.{index:02d}"
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
