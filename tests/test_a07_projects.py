"""Exercise real worker exit, version compatibility and saga durability."""

import asyncio
import os
import sqlite3
import subprocess
import sys
from contextlib import closing
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

PHASE = Path(__file__).resolve().parents[1] / (
    "01-architecture-A01-to-A20/A07-application-integration-arch"
)


def load(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec and spec.loader
    module = module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def inspect(path: Path, query: str) -> list[tuple]:
    with closing(sqlite3.connect(path)) as db:
        return db.execute(query).fetchall()


def test_guided_worker_exit_and_replay(tmp_path: Path) -> None:
    fastapi = pytest.importorskip("fastapi")
    httpx = pytest.importorskip("httpx")
    file = PHASE / "projects/guided/queue_api.py"
    api = load("a07_queue", file)
    database = tmp_path / "queue.sqlite"
    downstream = fastapi.FastAPI()

    @downstream.get("/inventory")
    def stock():
        raise fastapi.HTTPException(503, "fixture failure")

    app = api.create_app(database, downstream)

    async def check():
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://fixture.test"
        ) as client:
            assert (await client.post("/checkout/synchronous")).status_code == 503
            queued = await client.post("/checkout/queued")
            assert queued.status_code == 202
            assert (await client.get(queued.headers["Location"])).json() == {
                "status": "pending"
            }

    asyncio.run(check())
    command = [sys.executable, str(file), str(database)]
    abrupt = subprocess.run([*command, "--exit-before-ack"], timeout=8, check=False)
    assert abrupt.returncode == 75
    assert inspect(database, "SELECT status FROM jobs") == [("pending",)]
    assert inspect(database, "SELECT count(*) FROM effects") == [(1,)]
    replay = subprocess.run(command, timeout=8, check=False)
    assert replay.returncode == 0
    assert inspect(database, "SELECT status FROM jobs") == [("done",)]
    assert inspect(database, "SELECT count(*) FROM effects") == [(1,)]


def test_saga_outbox_and_consumer_restart(tmp_path: Path) -> None:
    file = Path(
        os.environ.get(
            "A07_PIPELINE", str(PHASE / "projects/independent/reference_pipeline.py")
        )
    )
    api = load("a07_pipeline", file)
    database, broker = tmp_path / "orders.sqlite", tmp_path / "broker.sqlite"
    pipeline = api.Pipeline(database, broker)
    assert pipeline.submit("tenant-a", "checkout")
    assert not pipeline.submit("tenant-a", "checkout")
    assert pipeline.advance("tenant-a", "checkout") == "reserved"
    assert pipeline.advance("tenant-a", "checkout") == "charged"
    assert (
        pipeline.advance("tenant-a", "checkout", fail_confirmation=True)
        == "compensating"
    )
    pipeline = api.Pipeline(database, broker)
    assert pipeline.advance("tenant-a", "checkout") == "refunded"
    assert pipeline.advance("tenant-a", "checkout") == "cancelled"
    assert pipeline.advance("tenant-a", "checkout") == "cancelled"
    assert inspect(database, "SELECT kind FROM effects ORDER BY rowid") == [
        ("reserve",),
        ("charge",),
        ("refund",),
        ("release",),
    ]

    with pytest.raises(api.SimulatedFailure):
        pipeline.publish_one(fail_after_publish=True)
    assert pipeline.publish_one() and pipeline.publish_one()
    assert not pipeline.publish_one()
    assert inspect(broker, "SELECT count(*) FROM deliveries") == [(3,)]
    with pytest.raises(api.SimulatedFailure):
        pipeline.consume_one(fail_after_effect=True)
    assert pipeline.consume_one() and pipeline.consume_one() and pipeline.consume_one()
    assert not pipeline.consume_one()
    assert inspect(broker, "SELECT count(*) FROM projection") == [(2,)]
    assert inspect(broker, "SELECT sum(acked) FROM deliveries") == [(3,)]


def test_old_contract_additive_vs_breaking() -> None:
    pytest.importorskip("fastapi")
    pydantic = pytest.importorskip("pydantic")
    api = load("a07_contract", PHASE / "labs/contracts.py")
    assert asyncio.run(api.check(False)).order_id == "demo"
    with pytest.raises(pydantic.ValidationError):
        asyncio.run(api.check(True))
