"""Run normal or controlled failure for A03.11."""

import sys as _sys
import asyncio
import time

broken = "--break" in _sys.argv[1:]


async def job(i):
    print("start", i)
    if broken:
        time.sleep(0.02)
    else:
        await asyncio.sleep(0.02)
    print("done", i)


async def main():
    await asyncio.gather(job(1), job(2))


asyncio.run(main())
