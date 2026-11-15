"""Check numerical attention, learned continuation, and input boundaries."""

import asyncio
import importlib.util
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A11-transformers-llm-internals"
)


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_analytical_attention_and_cache_bytes():
    torch = pytest.importorskip("torch")
    tiny = load(PHASE / "projects/guided/tiny.py")
    zeros = torch.zeros(1, 2, 1)
    values = torch.tensor([[[2.0], [6.0]]])
    torch.testing.assert_close(
        tiny.attend(zeros, zeros, values), torch.tensor([[[2.0], [4.0]]])
    )
    torch.testing.assert_close(
        tiny.attend(zeros, zeros, values, causal=False), torch.tensor([[[4.0], [4.0]]])
    )
    assert tiny.kv_bytes(1, 4, 2, 16, 64, 2) == 32768


def test_trained_service_and_prefix_isolation():
    torch = pytest.importorskip("torch")
    pytest.importorskip("fastapi")
    httpx = pytest.importorskip("httpx")
    server = load(PHASE / "projects/independent/service.py")
    previous = torch.get_num_threads()
    torch.set_num_threads(1)
    try:
        model, losses = server.tiny.train()
        assert losses[-1] < losses[0] / 5
        original = model(torch.tensor([[0, 1, 2]]))
        changed = model(torch.tensor([[0, 1, 3]]))
        torch.testing.assert_close(original[:, :2], changed[:, :2])

        async def verify():
            async with httpx.AsyncClient(
                transport=httpx.ASGITransport(app=server.create_app(model)),
                base_url="http://fixture.test",
            ) as client:
                assert (
                    await client.post("/generate", json={"prompt": [0, 1], "count": 4})
                ).json() == {"tokens": [2, 3, 0, 1]}
                assert (
                    await client.post("/generate", json={"prompt": [9]})
                ).status_code == 422
                assert (
                    await client.post(
                        "/generate", json={"prompt": [0] * 32, "count": 2}
                    )
                ).status_code == 422

        asyncio.run(verify())
    finally:
        torch.set_num_threads(previous)
