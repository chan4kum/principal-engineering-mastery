"""Verify both executable controls in each A09 lesson."""

import subprocess
import sys
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops"
)
EXPECTED = (
    (0.25, 8),
    (500, 50),
    ("old", "new"),
    (0, 300),
    (2, 1),
    (2, 1),
    (2, 10),
    (40, 20),
    (75, 225),
    (1, 4),
    (1, 3),
    (0, 3),
    (2, 12),
    (256, 254),
    (2, 5),
    (5, 3),
    (2, 3),
    (8, 2),
    (7, 4),
    (60, 20),
    (1, 3),
    (2, 0),
    (0, 2),
    (8, 2000),
    (1, 3),
    (100, 2000),
    (4, 1),
    (80, 2),
    (4, 5),
    (2, 4),
    (5.0, 10),
    (70000, 700),
    (400, 800),
)


@pytest.mark.parametrize("index,expected", list(enumerate(EXPECTED, 1)))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "failure"])
def test_platform_example(index: int, expected: tuple, broken: bool) -> None:
    lesson = f"A09.{index:02d}"
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
