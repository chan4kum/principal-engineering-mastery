"""Check fixed retrieval judgments, query authority, and revision invalidation."""

import asyncio
import importlib.util
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems"
)


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_baseline_synonym_and_ranking():
    ranking = load(PHASE / "projects/guided/benchmark.py")
    collection = {"a": "snapshot archive", "b": "restore checklist", "c": "redis ttl"}
    assert ranking.lexical("backup", collection) == []
    assert ranking.lexical("redis", collection) == ["c"]
    dense = ranking.dense("backup", collection)
    assert dense == ["a", "b"]
    assert ranking.evaluate(ranking.fuse([], dense), {"a", "b"}, 2) == {
        "recall": 1,
        "reciprocal_rank": 1,
        "ndcg": 1,
    }
    assert ranking.evaluate(["c", "a"], {"a", "b"}, 2)["recall"] == 0.5


def test_ranking_collision_and_incompatible_raw_score_units():
    ranking = load(PHASE / "projects/guided/benchmark.py")
    collision = {"battery": "battery backup backup", "restore": "restore snapshot"}
    assert ranking.lexical("backup", collision) == ["battery"]
    # Raw scores are separate units. Scaling one source alone can reverse the ranking.
    lexical_scores = {"battery": 3.0, "restore": 1.0}
    dense_scores = {"restore": 0.9}

    def merged_raw(factor):
        return ranking.ranked(
            {
                item: value * factor + dense_scores.get(item, 0)
                for item, value in lexical_scores.items()
            }
        )

    assert merged_raw(1)[0] == "battery"
    assert merged_raw(0.1)[0] == "restore"
    hybrid = ranking.fuse(ranking.ranked(lexical_scores), ranking.ranked(dense_scores))
    assert hybrid[0] == "restore"
    assert ranking.evaluate(hybrid, {"restore"}, 1)["recall"] == 1


def test_tenant_boundaries_and_freshness():
    pytest.importorskip("fastapi")
    httpx = pytest.importorskip("httpx")
    service = load(PHASE / "projects/independent/service.py")
    engine = service.Search()
    engine.replace("a", "duplicate", 1, "backup public-to-tenant-a")
    engine.replace("b", "duplicate", 1, "backup private-to-tenant-b")

    async def verify():
        app = service.create_app(engine, {"aa": "a", "bb": "b"})
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://fixture.test"
        ) as client:

            async def ask(token):
                return await client.post(
                    "/answer",
                    json={"text": "backup"},
                    headers={"Authorization": "Bearer " + token},
                )

            assert (await ask("unknown")).status_code == 401
            assert (await ask("aa")).json()["evidence"] == [
                {
                    "source": "duplicate",
                    "revision": 1,
                    "quote": "backup public-to-tenant-a",
                }
            ]
            assert (await ask("bb")).json()["evidence"][0][
                "quote"
            ] == "backup private-to-tenant-b"
            assert engine.replace("a", "duplicate", 2, "backup revision two")
            assert (await ask("aa")).json()["evidence"][0]["revision"] == 2
            pending_delete = ("a", "duplicate", 3, None)
            assert (await ask("aa")).json()["evidence"][0]["revision"] == 2
            assert engine.replace(*pending_delete)
            assert not engine.replace("a", "duplicate", 2, "backup late delivery")
            assert (await ask("aa")).json() == {"abstained": True, "evidence": []}
            assert (await ask("bb")).json()["evidence"][0]["revision"] == 1

    asyncio.run(verify())
