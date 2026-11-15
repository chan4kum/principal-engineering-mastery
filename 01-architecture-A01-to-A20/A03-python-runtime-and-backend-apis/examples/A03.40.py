"""Run normal or controlled failure for A03.40."""

import sys as _sys
import asyncio

broken = "--break" in _sys.argv[1:]


async def events():
    try:
        yield "first"
        yield "second"
    finally:
        print("cleanup")


async def main():
    stream = events()
    print(await anext(stream))
    if broken:
        print("deferred cleanup")
    else:
        await stream.aclose()
        print("cleanup observed before return")


asyncio.run(main())
