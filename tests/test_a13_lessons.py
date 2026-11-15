"""Verify both executable controls in each A13 lesson."""

import subprocess
import sys
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration"
)
EXPECTED = (
    (3, 5),
    (2, 6),
    (2, 3),
    (3, 4),
    (6, 2),
    (20, 50),
    (8500, 10000),
    (3, 6),
    (2, 3),
    (2, 5),
    (3, 7),
    (1, 2),
    (0, 1),
    (2, 3),
    (3, 6),
    (4, 5),
    (2, 5),
    (4, 2),
    (0, 1),
    (1, 3),
    (6, 3),
    (2, 8),
    (1, 2),
    (2, 7),
    (3, 4),
    (5, 1),
    (0, 1),
    (0, 3),
    (4, 20),
    (1, 3),
    (1, 2),
    (1, 3),
)


@pytest.mark.parametrize("index,expected", list(enumerate(EXPECTED, 1)))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "failure"])
def test_phase_13_example(index: int, expected: tuple, broken: bool) -> None:
    lesson = f"A13.{index:02d}"
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
