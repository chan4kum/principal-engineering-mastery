"""Run normal or controlled failure for A03.28."""

import sys as _sys
import asyncio

broken = "--break" in _sys.argv[1:]


async def main():
    peak = active = 0
    gate = asyncio.Semaphore(9 if broken else 3)

    async def job():
        nonlocal active, peak
        async with gate:
            active += 1
            peak = max(peak, active)
            await asyncio.sleep(0.01)
            active -= 1

    async with asyncio.TaskGroup() as tasks:
        for _ in range(9):
            tasks.create_task(job())
    print("peak in flight:", peak)


asyncio.run(main())
