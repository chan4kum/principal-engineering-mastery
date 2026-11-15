"""Check the fixed-leader quorum model and persistent fencing contract."""

import asyncio
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

PHASE = Path(__file__).resolve().parents[1] / (
    "01-architecture-A01-to-A20/A06-distributed-systems-coordination"
)


def load(name, file):
    spec = spec_from_file_location(name, file)
    assert spec and spec.loader
    module = module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def labs():
    return load("a06_labs", PHASE / "labs/coordination.py")


def test_guided_minority_majority_and_heal(labs) -> None:
    group = labs.ReplicatedLog(("a", "b", "c", "d", "e"), "a")
    group.reachable = {"a", "b"}
    group.append("one")
    assert group.visible() == ()
    group.reachable.add("c")
    group.sync()
    assert group.visible() == ("one",)
    group.reachable = {"a"}
    group.append("two")
    assert group.visible() == ("one",)
    group.reachable.update({"d", "e"})
    group.sync()
    assert group.visible() == ("one", "two")


def test_guided_clocks_and_history(labs) -> None:
    assert labs.receive_scalar(4, 7) == 8
    assert labs.receive_vector((0, 1), (1, 0), 1) == (1, 2)
    assert not labs.precedes((1, 0), (0, 1))
    assert labs.precedes((1, 0), (1, 2))
    write = labs.Operation("write", 1, 0, 2)
    assert not labs.linearizable_register([write, labs.Operation("read", 0, 3, 4)])
    assert labs.linearizable_register([write, labs.Operation("read", 0, 1, 4)])


def test_loopback_timeout_then_duplicate(labs) -> None:
    assert asyncio.run(labs.dropped_reply(False)) == 10
    assert asyncio.run(labs.dropped_reply(True)) == 5


def test_coordinator_replay_expiry_and_restart(tmp_path) -> None:
    file = Path(
        os.getenv(
            "A06_COORDINATOR",
            str(PHASE / "projects/independent/reference_coordinator.py"),
        )
    )
    api = load("a06_coordinator", file)
    path = tmp_path / "coordination.sqlite"
    coordinator = api.Coordinator(path)
    first = coordinator.claim("counter", "a", 0, 5)
    with pytest.raises(api.Denied):
        coordinator.claim("counter", "b", 4, 5)
    assert coordinator.apply("counter", first, "op", 7, 4) == 7
    with pytest.raises(api.Denied):
        coordinator.apply("counter", first, "expired", 100, 5)
    restarted = api.Coordinator(path)
    fence = restarted.claim("counter", "b", 5, 10)
    assert fence > first
    with pytest.raises(api.Denied):
        restarted.apply("counter", first, "stale", 100, 6)
    assert restarted.apply("counter", fence, "op", 7, 6) == 7
    with pytest.raises(api.Conflict):
        restarted.apply("counter", fence, "op", 8, 6)
    with ThreadPoolExecutor(4) as pool:
        submitted = [
            pool.submit(restarted.apply, "counter", fence, "next", 3, 6)
            for _ in range(6)
        ]
        assert [future.result(timeout=4) for future in submitted] == [10] * 6
    assert api.Coordinator(path).value("counter") == 10
