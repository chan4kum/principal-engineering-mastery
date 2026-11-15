"""Compare event-loop schedules using a bounded FastAPI fixture."""

import asyncio
import time

import httpx
from fastapi import FastAPI

app = FastAPI()


@app.get("/wait")
async def wait(blocking: bool = False) -> dict[str, bool]:
    if blocking:
        time.sleep(0.06)
    else:
        await asyncio.sleep(0.06)
    return {"finished": True}


async def measure(blocking: bool) -> float:
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://fixture.test"
    ) as client:
        start = time.monotonic()
        async with asyncio.TaskGroup() as tasks:
            requests = [
                tasks.create_task(client.get("/wait", params={"blocking": blocking}))
                for _ in range(4)
            ]
        for request in requests:
            request.result().raise_for_status()
        return time.monotonic() - start


async def main() -> None:
    for blocking in (False, True):
        seconds = await measure(blocking)
        print(f"blocking={blocking}, elapsed={seconds:.3f} s")


if __name__ == "__main__":
    asyncio.run(main())
