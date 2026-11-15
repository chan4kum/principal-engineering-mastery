"""Run normal or controlled failure for A03.35."""

import sys as _sys
import asyncio
import httpx

broken = "--break" in _sys.argv[1:]


async def main():
    if broken:
        with httpx.Client() as client:
            print("async adapter:", isinstance(client, httpx.AsyncClient))
    else:
        async with httpx.AsyncClient() as client:
            print("async adapter:", isinstance(client, httpx.AsyncClient))


asyncio.run(main())
