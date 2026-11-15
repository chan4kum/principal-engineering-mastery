"""Run normal or controlled failure for A03.19."""

import asyncio
import sys as _sys

import httpx
from fastapi import Depends, FastAPI

broken = "--break" in _sys.argv[1:]

app = FastAPI()


def account():
    return "live-source"


@app.get("/")
def read_account(name=Depends(account)):
    return {"account": name}


if not broken:
    app.dependency_overrides[account] = lambda: "test-source"


async def main():
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://fixture.test"
    ) as client:
        print((await client.get("/")).json())


asyncio.run(main())
