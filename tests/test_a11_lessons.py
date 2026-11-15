"""Verify both executable controls in each A11 lesson."""

import subprocess
import sys
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A11-transformers-llm-internals"
)
EXPECTED = (
    (48, 6),
    (11, 3),
    (-0.5, 0.5),
    (7, 3),
    (7680000, 10000),
    (4.0, 2),
    (10, 7),
    (2, -1),
    ((-1, 1), (1, 3)),
    (6, 9),
    (8, 3),
    (4.0, 2),
    (300, 120),
    (32768, 65536),
    (2.0, 500),
    (25.0, 50.0),
    (75, 100),
    (40.0, 50.0),
    (16, 8),
    (7, 10),
    (12, 0),
    (3, 2),
    (100, 500),
    (15, 30),
    (4000000000, 8000000000),
    (1000, 2000),
    (16000, 32000),
    (5.0, 500),
    (1048576, 1024),
    (1, 2),
    (20, 2000),
    (0.6, 5),
    (2, 8),
    (4, 2),
    (40.0, 100),
    (20.0, 200),
    (40.0, 25),
    (0.015, 0.012),
)


@pytest.mark.parametrize("index,expected", list(enumerate(EXPECTED, 1)))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "failure"])
def test_phase_11_example(index: int, expected: tuple, broken: bool) -> None:
    lesson = f"A11.{index:02d}"
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
