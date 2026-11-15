"""Verify both executable controls in each A04 lesson."""

import subprocess
import sys
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines"
)
EXPECTED = (
    (65, 68),
    (16, 9),
    ("rejected", 1),
    (40, 8000),
    (3, 6),
    (100, 10000),
    (20.0, 4000),
    (100, 300),
    (1000000, 8),
    (60, 53),
    (1, 2),
    (2, 3),
    (3, 4),
    (10000, 100000),
    (20, 400),
    (20.48, 40.96),
    (3, 10),
    (24, 12000),
    ([30, 40], [20, 30]),
    (600, 1800),
    (0.1, 1.0),
    (120, 3),
    ("durable", None),
    (256, 65536),
    (100, 500),
    (8, 3),
    (9, 4),
    (0.1, 10.0),
    (3.5, 1.0),
    (0.16666666666666666, 1.0),
    (("new", 8), ("old", 7)),
    (("v2", "v2"), ("v2", "v1")),
    (0, 300),
    (51.2, 3072.0),
    (False, True),
    (5, None),
    (2, 12),
)


@pytest.mark.parametrize("index,expected", list(enumerate(EXPECTED, 1)))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "failure"])
def test_storage_example(index: int, expected: tuple, broken: bool) -> None:
    lesson = f"A04.{index:02d}"
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
