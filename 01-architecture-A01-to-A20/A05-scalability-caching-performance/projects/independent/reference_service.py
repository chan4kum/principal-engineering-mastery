"""Bound admission and measure queue plus end-to-end latency."""

import asyncio
from collections import deque
from collections.abc import Awaitable, Callable
from math import ceil

from fastapi import FastAPI, HTTPException


def create_app(
    workers: int = 3,
    queue_limit: int = 6,
    slo_ms: float = 100,
    work: Callable[[], Awaitable[None]] | None = None,
) -> FastAPI:
    if workers < 1 or queue_limit < 0 or slo_ms <= 0:
        raise ValueError("invalid capacity")
    app = FastAPI()
    slots = asyncio.Semaphore(workers)
    waiting = active = offered = rejected = succeeded = cancelled = failed = met_slo = 0
    samples: deque[tuple[float, float]] = deque(maxlen=256)

    @app.post("/work")
    async def execute() -> dict[str, bool]:
        nonlocal \
            waiting, \
            active, \
            offered, \
            rejected, \
            succeeded, \
            cancelled, \
            failed, \
            met_slo
        offered += 1
        loop = asyncio.get_running_loop()
        arrived = loop.time()
        queued = slots.locked()
        if queued and waiting >= queue_limit:
            rejected += 1
            raise HTTPException(
                503, "Admission queue full", headers={"Retry-After": "1"}
            )
        if queued:
            waiting += 1
        try:
            await slots.acquire()
        except asyncio.CancelledError:
            cancelled += 1
            raise
        finally:
            if queued:
                waiting -= 1
        started = loop.time()
        active += 1
        try:
            if work is None:
                await asyncio.sleep(0.025)
            else:
                await work()
        except asyncio.CancelledError:
            cancelled += 1
            raise
        except Exception:
            failed += 1
            raise
        else:
            elapsed = (loop.time() - arrived) * 1000
            samples.append((elapsed, (started - arrived) * 1000))
            succeeded += 1
            met_slo += elapsed <= slo_ms
            return {"completed": True}
        finally:
            active -= 1
            slots.release()

    @app.get("/metrics")
    async def metrics() -> dict[str, int | float | None]:
        latencies = sorted(total for total, _ in samples)
        return {
            "offered": offered,
            "rejected": rejected,
            "active": active,
            "waiting": waiting,
            "succeeded": succeeded,
            "cancelled": cancelled,
            "failed": failed,
            "met_slo": met_slo,
            "sample_count": len(samples),
            "p95_ms": latencies[ceil(0.95 * len(latencies)) - 1] if latencies else None,
            "mean_queue_ms": sum(wait for _, wait in samples) / len(samples)
            if samples
            else None,
        }

    return app


app = create_app()
