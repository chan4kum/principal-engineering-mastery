"""Acceptance tests for the guided explorer and independent runner interface."""

import json
import os
from pathlib import Path
import subprocess
import sys

import pytest

PROJECTS = Path(__file__).resolve().parents[1] / (
    "01-architecture-A01-to-A20/A01-computer-systems-and-os/projects"
)
EXPLORER = PROJECTS / "guided/explorer.py"
RUNNER = Path(os.environ.get("A01_RUNNER", PROJECTS / "independent/reference_runner.py"))


def invoke(script: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), *args], capture_output=True, text=True, timeout=15
    )


@pytest.mark.parametrize("rss,expected", [("VmRSS:\t123 kB\n", 125952), ("", None)])
def test_explorer_parses_status(tmp_path: Path, rss: str, expected: int | None) -> None:
    target = tmp_path / "42"
    target.mkdir()
    (target / "status").write_text(
        "Name:\tworker pool\nState:\tS (sleeping)\nPid:\t42\nPPid:\t7\nThreads:\t2\n" + rss
    )
    result = invoke(EXPLORER, "42", "--proc-root", str(tmp_path))
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout) == {
        "name": "worker pool",
        "state": "S",
        "pid": 42,
        "ppid": 7,
        "threads": 2,
        "rss_bytes": expected,
    }


def test_explorer_handles_unavailable_pid(tmp_path: Path) -> None:
    result = invoke(EXPLORER, "42", "--proc-root", str(tmp_path))
    assert result.returncode == 2
    assert "42" in result.stderr


def test_runner_reports_order_failures_and_telemetry() -> None:
    result = invoke(RUNNER, "--workers", "2", "--timeout", "1", "timeout", "cpu", "fail", "wait")
    assert result.returncode == 0, result.stderr
    batch = json.loads(result.stdout)
    jobs = batch["jobs"]
    assert [job["index"] for job in jobs] == [0, 1, 2, 3]
    assert [job["action"] for job in jobs] == ["timeout", "cpu", "fail", "wait"]
    assert [job["status"] for job in jobs] == ["timeout", "ok", "failed", "ok"]
    assert [job["returncode"] for job in jobs[1:]] == [0, 7, 0]
    assert jobs[0]["returncode"] != 0
    assert jobs[0]["cpu_seconds"] is None and jobs[0]["peak_rss_bytes"] is None
    for job in jobs:
        assert job["pid"] > 0
        assert 0 < job["wall_seconds"] <= batch["wall_seconds"]
    for job in jobs[1:]:
        assert 0 < job["cpu_seconds"] <= job["wall_seconds"]
        assert job["peak_rss_bytes"] > 0


@pytest.mark.parametrize(
    "flag,value", [("--workers", "0"), ("--workers", "9"), ("--timeout", "nan")]
)
def test_runner_enforces_bounds(flag: str, value: str) -> None:
    assert invoke(RUNNER, flag, value, "cpu").returncode != 0
