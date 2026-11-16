"""Check that the project boundaries behave through their real entry points."""

import importlib.util
import sqlite3
import sys
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
from pathlib import Path
from threading import Barrier

import pytest

ROOT = Path(__file__).resolve().parents[1] / "01-architecture-A01-to-A20"


def project(phase, role):
    root = next(ROOT.glob(f"{phase}-*"))
    path = root / "projects" / role / f"{role}.py"
    name = f"pem_{phase.lower()}_{role}"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_a14_refuses_missing_duplicate_and_foreign_evidence():
    api = project("A14", "guided")
    case = api.Case("x", "answer", "a", frozenset({"a:doc"}), True)
    response = api.Response("answer", "a", frozenset({"a:doc", "b:doc"}), 10, 2, 4)
    with pytest.raises(ValueError, match="incomplete"):
        api.evaluate([case], {})
    with pytest.raises(ValueError, match="incomplete"):
        api.evaluate([case, case], {"x": response})
    record = api.evaluate([case], {"x": response})["x"]
    assert record["answer"]
    assert not record["grounded"]
    assert not record["scope"]


def test_a15_pinned_digest_does_not_replace_inventory_and_review():
    import hashlib

    api = project("A15", "independent")
    data = b"toy release"
    identity = hashlib.sha256(data).hexdigest()
    assert api.verify_artifact(data, identity, {"components": ["base@1"]}, set())
    assert not api.verify_artifact(data + b"x", identity, {"components": ["base@1"]}, set())
    assert not api.verify_artifact(data, identity, {"components": []}, set())
    assert not api.verify_artifact(data, identity, {"components": ["base@1"]}, {"review"})


def test_a16_concurrent_requests_cannot_sell_the_same_seat(tmp_path):
    api = project("A16", "independent")
    database = tmp_path / "booking.sqlite"
    with closing(sqlite3.connect(database)) as connection:
        api.initialize(connection)
    start = Barrier(2, timeout=5)

    def buy(key):
        with closing(sqlite3.connect(database, timeout=5)) as connection:
            start.wait()
            return api.reserve(connection, key, "seat-1")

    with ThreadPoolExecutor(max_workers=2) as executor:
        outcomes = list(executor.map(buy, ["alpha", "beta"]))
    assert sorted(outcomes) == [False, True]
    with closing(sqlite3.connect(database)) as connection:
        assert api.reserve(connection, "alpha", "seat-1") == outcomes[0]
        assert api.reserve(connection, "beta", "seat-1") == outcomes[1]
        (count,) = connection.execute("SELECT COUNT(*) FROM bookings WHERE committed=1").fetchone()
        assert count == 1


def test_a17_rejects_self_review_and_invalid_evidence_even_with_matching_digest():
    import dataclasses

    guided = project("A17", "guided")
    api = project("A17", "independent")
    case = guided.Request("case", "administrative-draft", "source", "owner")
    identity = api.digest(dataclasses.asdict(case))
    audit = api.Audit({"source"}, {"owner", "other"})
    assert not audit.execute(case, api.Approval("owner", identity, 10), 2)
    assert not audit.execute(case, api.Approval("other", identity, 10), 10)
    assert not audit.effects
    assert api.verify(audit.events, audit.events[-1]["hash"])


def test_a18_replay_works_at_cap_and_conflicting_payload_preserves_charge():
    api = project("A18", "independent")
    meter = api.Meter({"a": 10, "b": 10}, 10)
    assert meter.charge("a", "id", api.Usage("a", 1, 3)) == 10
    assert meter.charge("a", "id", api.Usage("a", 1, 3)) == 10
    with pytest.raises(ValueError, match="conflict"):
        meter.charge("a", "id", api.Usage("a", 4, 2))
    with pytest.raises(OverflowError, match="quota"):
        meter.charge("b", "id", api.Usage("b", 1, 0))
    assert (meter.total("a"), meter.total("b")) == (10, 0)


def test_a19_bounded_queue_discards_audio_at_turn_change():
    api = project("A19", "independent")
    session = api.VoiceSession(max_chunks=1)
    turn = session.turn
    assert session.enqueue(turn, b"first")
    assert not session.enqueue(turn, b"over budget")
    next_turn = session.interrupt()
    assert not session.enqueue(turn, b"late")
    assert session.enqueue(next_turn, b"fresh")
    assert session.next_chunk() == b"fresh"
    assert session.next_chunk() == b""


def test_a20_invalid_or_missing_measurements_do_not_allow_rollout():
    api = project("A20", "independent")
    release = api.Delivery("stable")
    assert not release.rollout("pilot", api.Evidence(True, True, True, 0, 0))
    assert not release.rollout("pilot", api.Evidence(True, True, True, 101, 100))
    assert release.rollout("pilot", api.Evidence(True, True, True, 99, 100))
    assert release.monitor(api.Evidence(True, True, True, 98, 100)) == "stable"
    assert release.log[-1][0] == "restored"
