"""Exercise all A02 lesson controls and arithmetic snippets."""

from pathlib import Path
import re
import subprocess
import sys

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A02-networking-and-communication"
)
EXPECTED = (
    ("True declared: 513", "False declared: 258"),
    ("matches binding: True", "matches binding: False"),
    ("154 captured", "140 captured"),
    ("bytes: 60", "bytes: 44"),
    ("02:00:00:00:00:01", "link destination: None"),
    ("1380 fits: True", "1460 fits: False"),
    ("addresses: 256", "host bits set"),
    ("next hop: peer", "next hop: default"),
    ("gateway: True", "gateway: False"),
    ("connections: 2", "connections: 1"),
    ("192.0.2.3", "192.0.2.2"),
    ("mappings: 2", "mappings: 1"),
    ("model: True", "model: False"),
    ("expected: 105", "expected: 115"),
    ("b'ABC' b'DEF'", "b'AB' b'DEF'"),
    ("100.0 Mb/s", "12.8 Mb/s"),
    ("trust: True verifies hostname: True", "trust: False verifies hostname: False"),
    ("certificate: True", "certificate: False"),
    ("state: 13", "state: 16"),
    ("status: 504", "status: 200"),
    ("4.0 ms/request", "80.0 ms/request"),
    ("ms: 50", "ms: 120"),
    ("failed a: 0", "failed a: 4"),
    ("frame: True", "frame: False"),
    ("33.33", "1000.00"),
    ("50 ms", "5 ms"),
    ("5 ms", "50 ms"),
    ("bytes: 131072", "bytes: 163840"),
    ("admitted: False", "admitted: True"),
    ("overall deadline at 250", "body still active at 320"),
    ("balance: 13", "balance: 16"),
    ("b success: True", "a success: False"),
    ("True retained: 30000", "False retained: 0"),
    ("emission: 0 ms", "emission: 100 ms"),
    ("sees: a", "sees: b"),
    ("probe: 5", "probe: 1"),
    ("floor: 80", "floor: 240"),
    ("work: 150", "work: 50"),
)


@pytest.mark.parametrize("index,expected", list(enumerate(EXPECTED, 1)))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "failure"])
def test_networking_lesson(index: int, expected: tuple[str, str], broken: bool) -> None:
    lesson = f"A02.{index:02}"
    text = (PHASE / "lessons" / f"{lesson}.md").read_text()
    assert all(f"## {heading}." in text for heading in range(1, 9))
    args = [sys.executable, str(PHASE / "examples" / f"{lesson}.py")]
    if broken:
        args.append("--break")
    result = subprocess.run(args, timeout=8, text=True, capture_output=True, check=False)
    assert result.returncode == 0, result.stderr
    assert expected[broken] in result.stdout


def test_networking_arithmetic() -> None:
    pytest.importorskip("numpy")
    files = sorted((PHASE / "lessons").glob("A02.*.md"))
    assert len(files) == 38
    for file in files:
        snippet = re.search(r"```python\n(import numpy as np[\s\S]+?)```", file.read_text())
        assert snippet is not None, file.name
        exec(compile(snippet[1], str(file), "exec"), {})
