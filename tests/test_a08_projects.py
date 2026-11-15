"""Check dashboard measurements, recovery invariants, and fault separation."""

import asyncio
import os
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

PHASE = Path(__file__).resolve().parents[1] / (
    "01-architecture-A01-to-A20/A08-reliability-operations-and-sre"
)


def load(name, path):
    spec = spec_from_file_location(name, path)
    assert spec and spec.loader
    module = module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_guided_dashboard_errors_saturation_and_spans() -> None:
    pytest.importorskip("opentelemetry.sdk")
    pytest.importorskip("fastapi")
    httpx = pytest.importorskip("httpx")
    api = load("a08_dashboard", PHASE / "projects/guided/dashboard.py")

    async def check():
        started, release = asyncio.Event(), asyncio.Event()
        broken = False

        async def dependency():
            started.set()
            await release.wait()
            if broken:
                raise OSError("fixture")

        dashboard = api.Dashboard()
        try:
            async with httpx.AsyncClient(
                transport=httpx.ASGITransport(
                    app=api.create_app(dashboard, dependency)
                ),
                base_url="http://fixture.test",
            ) as client:
                first = asyncio.create_task(client.get("/work"))
                await asyncio.wait_for(started.wait(), timeout=2)
                try:
                    assert (await client.get("/work")).status_code == 503
                finally:
                    release.set()
                    assert (await first).status_code == 200
                broken = True
                assert (await client.get("/work")).status_code == 503
                broken = False
                assert (await client.get("/work")).status_code == 200
            observed = dashboard.snapshot()
        finally:
            dashboard.close()

        points = observed["metrics"]
        count = {(p["name"], p["attributes"].get("status")): p for p in points}
        assert count["fixture.requests", 503]["value"] == 2
        assert count["fixture.requests", 200]["value"] == 2
        assert count["fixture.duration", 503]["count"] == 2
        assert count["fixture.active", None]["value"] == 0
        assert count["fixture.saturated", None]["value"] == 1
        failed = [
            span
            for span in observed["spans"]
            if span["name"] == "dependency" and span["status"] == "ERROR"
        ]
        assert len(failed) == 1 and failed[0]["parent"]
        assert any(
            span["name"] == "GET /work" and span["trace_id"] == failed[0]["trace_id"]
            for span in observed["spans"]
        )

    asyncio.run(check())


def test_budget_exact_boundary() -> None:
    api = load("a08_budget", PHASE / "labs/budget.py")
    base = api.budget(1_000_000, 500, 999_000)
    assert base["allowed_bad"] == 1000 and base["remaining"] == 500
    assert base["burn"] == 0.5
    assert api.budget(1_000_000, 1500, 999_000)["remaining"] == -500


def game_day_module():
    path = Path(
        os.getenv(
            "A08_GAME_DAY", str(PHASE / "projects/independent/reference_game_day.py")
        )
    )
    return load("a08_game_day", path)


@pytest.mark.parametrize("fault", ["cpu", "lock", "dns"])
def test_independent_faults_recover(tmp_path: Path, fault: str) -> None:
    result = game_day_module().game_day(tmp_path, fault)
    assert result["diagnosis"] == fault and result["recovered"]
    incident = result["timeline"]["incident"]
    assert incident["database_busy"] == (fault == "lock")
    assert incident["dns_rcode"] == (3 if fault == "dns" else 0)
    if fault == "cpu":
        assert incident["cpu_ms"] >= 15


@pytest.mark.parametrize("broken", [False, True])
def test_independent_restore_invariants(tmp_path: Path, broken: bool) -> None:
    recovery = game_day_module().recovery(tmp_path, broken)
    assert recovery["baseline_cents"] == recovery["restored_cents"] == 500
    assert recovery["target_corrupt"] == broken
    assert recovery["restore_and_verify_ms"] >= 0
