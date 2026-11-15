"""Disposable HTTP and streaming endpoints for A02 labs."""

import asyncio
from collections.abc import AsyncIterator

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.get("/health")
async def health() -> dict[str, bool]:
    return {"ready": True}


@app.get("/peer")
async def peer(request: Request) -> dict[str, str]:
    return {"source": request.client.host if request.client else ""}


async def chunks() -> AsyncIterator[bytes]:
    yield b"first\n"
    await asyncio.sleep(0.7)
    yield b"last\n"


@app.get("/stream")
async def stream() -> StreamingResponse:
    return StreamingResponse(chunks(), media_type="text/plain")
