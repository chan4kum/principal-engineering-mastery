"""Expose bounded CPU inference through a local ASGI fixture."""

import importlib.util
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

spec = importlib.util.spec_from_file_location(
    "a11_tiny", Path(__file__).resolve().parents[1] / "guided/tiny.py"
)
assert spec and spec.loader
tiny = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tiny)


class Generate(BaseModel):
    prompt: list[Annotated[int, Field(strict=True, ge=0, le=3)]] = Field(
        min_length=1, max_length=32
    )
    count: int = Field(default=2, strict=True, ge=0, le=8)
    temperature: float = Field(default=0, ge=0, le=5)


def create_app(model):
    app = FastAPI()

    @app.post("/generate")
    def predict(body: Generate):
        try:
            return {
                "tokens": tiny.generate(
                    model, body.prompt, body.count, temperature=body.temperature
                )
            }
        except ValueError as error:
            raise HTTPException(422, str(error)) from error

    return app
