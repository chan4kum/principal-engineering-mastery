"""Run normal or controlled failure for A03.13."""

import sys as _sys
import asyncio

broken = "--break" in _sys.argv[1:]

events = []


async def work():
    events.append("executed")


async def main():
    coroutine = work()
    if broken:
        coroutine.close()
    else:
        await asyncio.create_task(coroutine)
    print(events)


asyncio.run(main())
