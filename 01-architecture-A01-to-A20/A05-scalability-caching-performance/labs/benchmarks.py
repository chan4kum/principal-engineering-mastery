"""Local cache, queue and rate-limiting experiments with bounded inputs."""

import argparse
import asyncio
from collections import OrderedDict, deque
from dataclasses import dataclass, field
from math import ceil


def percentile(values: list[float], p: float) -> float:
    return sorted(values)[ceil(p * len(values)) - 1]


class TTLCache:
    def __init__(self, capacity: int, ttl: float) -> None:
        if capacity < 1 or ttl <= 0:
            raise ValueError("positive capacity and TTL required")
        self.capacity = capacity
        self.ttl = ttl
        self.data: OrderedDict[str, tuple[float, str]] = OrderedDict()

    def get(self, key: str, now: float) -> str | None:
        if key not in self.data:
            return None
        expires, value = self.data[key]
        if now >= expires:
            del self.data[key]
            return None
        self.data.move_to_end(key)
        return value

    def put(self, key: str, value: str, now: float) -> None:
        self.data[key] = (now + self.ttl, value)
        self.data.move_to_end(key)
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)


@dataclass
class TokenBucket:
    capacity: float
    refill: float
    updated: float = 0.0
    tokens: float = field(init=False)

    def __post_init__(self) -> None:
        if self.capacity < 1 or self.refill <= 0:
            raise ValueError("positive refill and capacity of at least one required")
        self.tokens = self.capacity

    def allow(self, now: float) -> bool:
        if now < self.updated:
            raise ValueError("clock moved backwards")
        self.tokens = min(
            self.capacity, self.tokens + (now - self.updated) * self.refill
        )
        self.updated = now
        if self.tokens < 1:
            return False
        self.tokens -= 1
        return True


class SlidingWindow:
    def __init__(self, limit: int, seconds: float) -> None:
        if limit < 1 or seconds <= 0:
            raise ValueError("positive limit and duration required")
        self.limit = limit
        self.seconds = seconds
        self.events: deque[float] = deque()
        self.last = 0.0

    def allow(self, now: float) -> bool:
        if now < self.last:
            raise ValueError("clock moved backwards")
        self.last = now
        while self.events and self.events[0] <= now - self.seconds:
            self.events.popleft()
        if len(self.events) >= self.limit:
            return False
        self.events.append(now)
        return True


async def cache_trial(capacity: int, enabled: bool) -> dict[str, float | int]:
    cache = TTLCache(capacity, ttl=0.05)
    loop = asyncio.get_running_loop()
    samples = []
    hits = 0
    for i in range(24):
        key = str(i % 3)
        start = loop.time()
        value = cache.get(key, start) if enabled else None
        if value is None:
            await asyncio.sleep(0.003)
            if enabled:
                cache.put(key, key, loop.time())
        else:
            hits += 1
        samples.append((loop.time() - start) * 1000)
    return {"hits": hits, "requests": len(samples), "p50_ms": percentile(samples, 0.5)}


def queue_trial(arrivals: list[int], service: int) -> dict[str, float | int]:
    """Tick model with arrivals before service and whole-tick residence."""
    waiting: deque[int] = deque()
    residence: list[int] = []
    area = 0
    for at, arrivals_now in enumerate(arrivals):
        waiting.extend([at] * arrivals_now)
        area += len(waiting)
        for _ in range(min(service, len(waiting))):
            residence.append(at - waiting.popleft() + 1)
    return {
        "backlog": len(waiting),
        "mean_in_flight": area / len(arrivals),
        "completions_per_tick": len(residence) / len(arrivals),
        "mean_completed_ticks": sum(residence) / len(residence) if residence else 0,
    }


async def load_trial(interval: float) -> dict[str, float | int]:
    loop = asyncio.get_running_loop()
    clock = loop.time()
    semaphore = asyncio.Semaphore(3)

    async def request(planned: float) -> float:
        await asyncio.sleep(max(0, planned - loop.time()))
        async with semaphore:
            await asyncio.sleep(0.025)
        return (loop.time() - planned) * 1000

    samples = await asyncio.gather(*(request(clock + i * interval) for i in range(48)))
    return {
        "completed": len(samples),
        "p50_ms": percentile(samples, 0.50),
        "p95_ms": percentile(samples, 0.95),
        "p99_ms": percentile(samples, 0.99),
    }


async def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("lab", choices=["L1", "L2", "L3", "L4", "guided"])
    args = cli.parse_args()
    if args.lab in {"L1", "guided"}:
        print("no cache:", await cache_trial(3, False))
        print("fits hot set:", await cache_trial(3, True))
        print("capacity miss:", await cache_trial(1, True))
    if args.lab == "L2":
        print("stable:", queue_trial([2] * 10, 2))
        print("overload:", queue_trial([3] * 10, 2))
    if args.lab == "L3":
        print("lower offered rate:", await load_trial(0.012))
        print("higher offered rate:", await load_trial(0.001))
    if args.lab in {"L4", "guided"}:
        times = [0.0, 0.0, 0.1, 0.5, 0.99, 1.0, 1.1]
        for label, limiter in (
            ("token bucket", TokenBucket(2, 2)),
            ("sliding window", SlidingWindow(2, 1)),
        ):
            print(label, [limiter.allow(at) for at in times])


if __name__ == "__main__":
    asyncio.run(main())
