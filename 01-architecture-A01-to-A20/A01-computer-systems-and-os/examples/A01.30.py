"""Run with --break to select the controlled alternative."""

import sys as _sys
import asyncio
import time

broken = "--break" in _sys.argv[1:]


async def request() -> None:
    if broken:
        time.sleep(0.03)
    else:
        await asyncio.sleep(0.03)


async def main() -> None:
    start = time.perf_counter()
    await asyncio.gather(*(request() for _ in range(3)))
    print(f"{time.perf_counter() - start:.3f} seconds")


asyncio.run(main())
