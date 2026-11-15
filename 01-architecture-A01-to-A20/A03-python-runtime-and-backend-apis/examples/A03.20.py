"""Run normal or controlled failure for A03.20."""

import asyncio
import sys as _sys

import httpx
from fastapi import FastAPI, Request

broken = "--break" in _sys.argv[1:]

app = FastAPI()


@app.middleware("http")
async def wrap(request: Request, call_next):
    reply = await call_next(request)
    if not broken:
        reply.headers["x-observation"] = "wrapped"
    return reply


async def main():
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://fixture.test"
    ) as client:
        reply = await client.get("/not-found")
        print(reply.status_code, reply.headers.get("x-observation"))


asyncio.run(main())
