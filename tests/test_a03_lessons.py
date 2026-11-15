"""Verify A03 examples and worked calculations."""

from pathlib import Path
import re
import subprocess
import sys

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis"
)
EXPECTED = (
    ("3", "not executed"),
    ("instructions inspected True", "native count inferred True"),
    ("True", "False"),
    ("[[1]]", "[[1, 2]]"),
    ("survives: False", "survives: True"),
    ("1 key", "1000 key"),
    ("produce 0\nfirst: 0", "produce 2\nfirst: 0"),
    ("rejected", "77"),
    ("'close'", "['open']"),
    ("ms: 200", "ms: 100"),
    ("start 2\ndone 1", "done 1\nstart 2"),
    ("timer delayed: False", "timer delayed: True"),
    ("executed", "[]"),
    ("sibling cancelled", "sibling finished"),
    ("workers: 3", "workers: 12"),
    ("accepted: True", "accepted: False"),
    ("worker counter: 1", "shared counter: 2"),
    ("status: 200 handler calls: 1", "status: 422 handler calls: 0"),
    ("test-source", "live-source"),
    ("404 wrapped", "404 None"),
    ("strict rejection", "amount=3"),
    ("['id', 'label']", "internal_cost"),
    ("exists: True", "exists: False"),
    ("branch: True", "branch: False"),
    ("allowed: False", "allowed: True"),
    ("purpose: False", "purpose: True"),
    ("[30, 40]", "[20, 30]"),
    ("flight: 3", "flight: 9"),
    ("dispatched: True", "dispatched: False"),
    ("cost ms: 50", "cost ms: 500"),
    ("commits: 1", "commits: 2"),
    ("tokens: 5", "tokens: 8"),
    ("admitted: False", "admitted: True"),
    ("fixture", '{"name"'),
    ("adapter: True", "adapter: False"),
    ("child ms: 60", "child ms: 30"),
    ("request_complete", "authorization"),
    ("close", "open"),
    ("accepted: True", "accepted: False"),
    ("cleanup observed before return", "deferred cleanup"),
    ("sees: None", "sees: tenant-a"),
    ("accepts: False", "accepts: True"),
)


@pytest.mark.parametrize("number,expected", list(enumerate(EXPECTED, 1)))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "failure"])
def test_backend_lesson(number: int, expected: tuple[str, str], broken: bool) -> None:
    pytest.importorskip("fastapi")
    path = PHASE / "examples" / f"A03.{number:02d}.py"
    args = [sys.executable, str(path)]
    if broken:
        args.append("--break")
    run = subprocess.run(args, timeout=8, text=True, capture_output=True, check=False)
    assert run.returncode == 0, run.stderr
    assert expected[broken] in run.stdout


def test_backend_calculations() -> None:
    pages = sorted((PHASE / "lessons").glob("A03.*.md"))
    assert len(pages) == 42
    for path in pages:
        snippet = re.search(r"```python\n(import math[\s\S]+?)```", path.read_text())
        assert snippet is not None, path.name
        exec(compile(snippet[1], str(path), "exec"), {})
