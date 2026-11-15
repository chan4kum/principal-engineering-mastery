"""Verify both executable controls in each A05 lesson."""

import subprocess
import sys
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A05-scalability-caching-performance"
)
EXPECTED = (
    (50.0, 10.0),
    (120, 20),
    (210, 20),
    (0.9044, 0.99),
    (1000, 200),
    (0.1, 0.01),
    (0.1, 200),
    (320.0, 40.0),
    (400, 600),
    (10, 5),
    (4.0, 22),
    (5, 100),
    (50, 250),
    ("cold", "hot"),
    (2, 1),
    (4, 400),
    (10, 120),
    (8, 10),
    (16, 72),
    (300, 1200),
    (10, 20),
    (20, 70),
    (1, 10),
    (100.0, 800),
    (2, 1),
    (9, 12),
    (0.25, 0.75),
    (2, 10),
    (50.0, 10.0),
    (0.0002, 0.0004),
    (90, 150),
    (0.7, 0.875),
    (4, 3),
    (6, 120),
)


@pytest.mark.parametrize("index,expected", list(enumerate(EXPECTED, 1)))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "failure"])
def test_storage_example(index: int, expected: tuple, broken: bool) -> None:
    lesson = f"A05.{index:02d}"
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
