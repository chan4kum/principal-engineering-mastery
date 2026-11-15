"""Run normal or controlled failure for A03.12."""

import sys as _sys
import asyncio
import time

broken = "--break" in _sys.argv[1:]


async def main():
    loop = asyncio.get_running_loop()
    start = loop.time()
    result = loop.create_future()
    loop.call_later(0.01, lambda: result.set_result(loop.time() - start))
    if broken:
        time.sleep(0.06)
    else:
        await result
    print("timer delayed:", not result.done())
    await result


asyncio.run(main())
