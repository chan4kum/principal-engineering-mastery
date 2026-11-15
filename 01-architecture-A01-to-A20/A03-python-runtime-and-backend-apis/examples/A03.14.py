"""Run normal or controlled failure for A03.14."""

import sys as _sys
import asyncio

broken = "--break" in _sys.argv[1:]


async def main():
    ready = asyncio.Event()

    async def sibling():
        ready.set()
        try:
            await asyncio.sleep(0.02)
            print("sibling finished")
        finally:
            print("cleanup")

    async def fail():
        await ready.wait()
        raise ValueError("fixture")

    if broken:
        await asyncio.gather(sibling(), fail(), return_exceptions=True)
    else:
        try:
            async with asyncio.TaskGroup() as group:
                group.create_task(sibling())
                group.create_task(fail())
        except* ValueError:
            print("sibling cancelled")


asyncio.run(main())
