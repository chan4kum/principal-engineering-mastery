"""Run normal or controlled failure for A03.29."""

import sys as _sys
import asyncio
import time

broken = "--break" in _sys.argv[1:]


async def main():
    heartbeat = asyncio.Event()

    async def pulse():
        heartbeat.set()

    signal = asyncio.create_task(pulse())
    if broken:
        time.sleep(0.03)
    else:
        await asyncio.to_thread(time.sleep, 0.03)
    print("pulse dispatched:", heartbeat.is_set())
    await signal


asyncio.run(main())
