"""Run an old consumer against a compatible and a breaking API response."""

import argparse
import asyncio

import httpx
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict


class CheckoutV1(BaseModel):
    model_config = ConfigDict(strict=True)
    order_id: str
    status: str


def create_api(broken: bool = False) -> FastAPI:
    app = FastAPI()

    @app.get("/v1/orders/demo")
    def order() -> dict[str, str]:
        return (
            {"id": "demo", "state": "queued"}
            if broken
            else {"order_id": "demo", "status": "queued", "origin": "web"}
        )

    return app


async def check(broken: bool) -> CheckoutV1:
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=create_api(broken)),
        base_url="http://fixture.test",
    ) as client:
        response = await client.get("/v1/orders/demo")
        response.raise_for_status()
        return CheckoutV1.model_validate(response.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--break", dest="broken", action="store_true")
    args = parser.parse_args()
    print(asyncio.run(check(args.broken)))
