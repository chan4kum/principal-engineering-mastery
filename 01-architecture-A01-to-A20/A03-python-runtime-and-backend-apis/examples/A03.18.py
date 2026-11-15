"""Run normal or controlled failure for A03.18."""

import asyncio
import sys as _sys

import httpx
from fastapi import FastAPI

broken = "--break" in _sys.argv[1:]

app = FastAPI()
calls = []


@app.get("/quantity")
def quantity(amount: int):
    calls.append(amount)
    return {"amount": amount}


async def main():
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://fixture.test"
    ) as client:
        result = await client.get("/quantity", params={"amount": "text" if broken else "4"})
        print("status:", result.status_code, "handler calls:", len(calls))


asyncio.run(main())
