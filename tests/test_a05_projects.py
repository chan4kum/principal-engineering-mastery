"""Check capacity tools and deterministic overload and recovery."""

import asyncio
import os
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PHASE = ROOT / "01-architecture-A01-to-A20/A05-scalability-caching-performance"


def load(name, path):
    spec = spec_from_file_location(name, path)
    assert spec and spec.loader
    module = module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_guided_cache_queue_and_limiter() -> None:
    tools = load("a05_benchmarks", PHASE / "labs/benchmarks.py")
    cache = tools.TTLCache(2, 1)
    cache.put("a", "A", 0)
    cache.put("b", "B", 0)
    assert cache.get("a", 0.25) == "A"
    cache.put("c", "C", 0.25)
    assert cache.get("b", 0.5) is None
    assert cache.get("a", 1) is None

    token, window = tools.TokenBucket(2, 2), tools.SlidingWindow(2, 1)
    for limiter in (token, window):
        assert limiter.allow(0)
        assert limiter.allow(0)
        assert not limiter.allow(0.1)
    assert token.allow(0.5)
    assert not window.allow(0.5)
    assert window.allow(1)
    steady = tools.queue_trial([2] * 10, 2)
    assert (
        steady["mean_in_flight"]
        == steady["completions_per_tick"] * steady["mean_completed_ticks"]
    )
    assert tools.queue_trial([3] * 10, 2)["backlog"] == 10


def test_service_queue_overload_cancellation_and_recovery() -> None:
    httpx = pytest.importorskip("httpx")
    pytest.importorskip("fastapi")
    target = Path(
        os.getenv(
            "A05_SERVICE", str(PHASE / "projects/independent/reference_service.py")
        )
    )
    source = load("a05_service", target)

    async def exercise():
        started, release = asyncio.Event(), asyncio.Event()

        async def work():
            started.set()
            await release.wait()

        app = source.create_app(workers=1, queue_limit=1, slo_ms=10000, work=work)
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://fixture.test"
        ) as client:
            first = asyncio.create_task(client.post("/work"))
            await started.wait()
            queued = asyncio.create_task(client.post("/work"))
            try:
                async with asyncio.timeout(2):
                    while (await client.get("/metrics")).json()["waiting"] != 1:
                        await asyncio.sleep(0)
                assert (await client.post("/work")).status_code == 503
                queued.cancel()
                with pytest.raises(asyncio.CancelledError):
                    await queued
                assert (await client.get("/metrics")).json()["waiting"] == 0
            finally:
                release.set()
                await first
                await asyncio.gather(queued, return_exceptions=True)
            assert (await client.post("/work")).status_code == 200
            metrics = (await client.get("/metrics")).json()
            assert metrics["offered"] == 4
            assert metrics["rejected"] == metrics["cancelled"] == 1
            assert (
                metrics["succeeded"]
                == metrics["met_slo"]
                == metrics["sample_count"]
                == 2
            )
            assert metrics["active"] == metrics["waiting"] == 0
            assert metrics["p95_ms"] >= 0 and metrics["mean_queue_ms"] >= 0

    asyncio.run(exercise())
