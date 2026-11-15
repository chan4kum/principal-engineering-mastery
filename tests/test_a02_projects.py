"""Acceptance tests for local network exploration and fault diagnosis."""

import json
import os
from pathlib import Path
import subprocess
import sys

import pytest

PROJECTS = Path(__file__).resolve().parents[1] / (
    "01-architecture-A01-to-A20/A02-networking-and-communication/projects"
)
DEBUGGER = Path(os.environ.get("A02_DEBUGGER", PROJECTS / "independent/reference_debugger.py"))


def run(script: Path, *args: str) -> dict:
    result = subprocess.run(
        [sys.executable, str(script), *args],
        capture_output=True,
        text=True,
        timeout=8,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


@pytest.mark.parametrize("args,status", [((), 200), (("--break",), 404)])
def test_explorer(args: tuple[str, ...], status: int) -> None:
    trace = run(PROJECTS / "guided/explorer.py", *args)
    assert trace["http_status"] == status
    assert [phase["phase"] for phase in trace["trace"]] == ["dns", "tcp", "first_byte"]
    assert trace["trace"][0]["address"] == "127.0.0.1"
    assert trace["trace"][1]["peer"][0] == "127.0.0.1"
    assert all(phase["elapsed_ms"] >= 0 for phase in trace["trace"])


@pytest.mark.parametrize(
    "scenario,phases,http_status,last_result",
    [
        ("ok", ["dns", "connect", "read"], 200, "ok"),
        ("dns", ["dns"], None, "failed"),
        ("connect", ["dns", "connect"], None, "failed"),
        ("tls", ["dns", "connect", "tls"], None, "failed"),
        ("read", ["dns", "connect", "read"], None, "failed"),
        ("http", ["dns", "connect", "read"], 503, "ok"),
    ],
)
def test_debugger(
    scenario: str, phases: list[str], http_status: int | None, last_result: str
) -> None:
    data = run(DEBUGGER, scenario)
    initial, recovery = data["initial"], data["recovery"]
    assert initial["outcome"] == scenario
    assert initial["http_status"] == http_status
    assert [step["phase"] for step in initial["trace"]] == phases
    assert [step["result"] for step in initial["trace"]] == ["ok"] * (len(phases) - 1) + [
        last_result
    ]
    assert recovery["outcome"] == "ok" and recovery["http_status"] == 200
    assert [step["phase"] for step in recovery["trace"]] == ["dns", "connect", "read"]
    assert all(step["result"] == "ok" for step in recovery["trace"])
    assert all(step["ms"] >= 0 for trace in (initial, recovery) for step in trace["trace"])
