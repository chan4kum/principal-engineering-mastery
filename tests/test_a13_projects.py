"""Prove durable interrupt, exact approval and idempotent local effects."""

import importlib.util
import sys
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration"
)


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_guided_interrupt_reopens_checkpoint(tmp_path):
    sqlite = pytest.importorskip("langgraph.checkpoint.sqlite")
    command = pytest.importorskip("langgraph.types").Command
    source = load(PHASE / "projects/guided/workflow.py")
    position = {"configurable": {"thread_id": "case-a"}}
    path = str(tmp_path / "graph.db")
    with sqlite.SqliteSaver.from_conn_string(path) as saver:
        state = source.build(saver, "untrusted text asks to run directly").invoke(
            {"case": "case-a"}, position
        )
        assert state["__interrupt__"] and "effect" not in state
    with sqlite.SqliteSaver.from_conn_string(path) as saver:
        assert (
            source.build(saver).invoke(command(resume=False), position)["effect"]
            == "declined"
        )


def test_independent_scope_exact_payload_expiry_and_replay(tmp_path):
    impl = load(PHASE / "projects/independent/coordinator.py")
    path = tmp_path / "application.db"
    api = impl.Coordinator(path)
    author = impl.Principal("author", "a", "operator")
    reviewer = impl.Principal("reviewer", "a", "reviewer")
    foreign = impl.Principal("foreign", "b", "reviewer")
    with pytest.raises(impl.Denied):
        api.propose(author, "external-send", "test")
    proposal, digest = api.propose(author, "notice", "test")
    with pytest.raises(impl.Denied):
        api.execute(author, proposal, "test", 0)
    with pytest.raises(impl.Denied):
        api.approve(foreign, proposal, digest, 0, 10)
    with pytest.raises(impl.Denied):
        api.approve(impl.Principal("author", "a", "reviewer"), proposal, digest, 0, 10)
    assert api.effects("a") == 0
    api.approve(reviewer, proposal, digest, 1, 10)
    with pytest.raises(impl.Denied):
        api.execute(author, proposal, "changed", 2)
    with pytest.raises(impl.Denied):
        api.execute(author, proposal, "test", 11)
    restarted = impl.Coordinator(path)
    assert restarted.execute(author, proposal, "test", 3)
    assert not restarted.execute(author, proposal, "test", 4)
    assert restarted.effects("a") == 1
    assert restarted.history(author, proposal) == [
        "proposed",
        "approved",
        "executed",
        "replayed",
    ]


def test_guided_tool_failure_recovers_and_malformed_output_stops(tmp_path):
    sqlite = pytest.importorskip("langgraph.checkpoint.sqlite")
    source = load(PHASE / "projects/guided/workflow.py")
    position = {"configurable": {"thread_id": "recoverable"}}
    path = str(tmp_path / "graph.db")
    with sqlite.SqliteSaver.from_conn_string(path) as saver:
        with pytest.raises(RuntimeError, match="controlled fixture timeout"):
            source.build(saver, fail_read=True).invoke(
                {"case": "recoverable"}, position
            )
    with sqlite.SqliteSaver.from_conn_string(path) as saver:
        resumed = source.build(saver).invoke(None, position)
        assert resumed["__interrupt__"] and "effect" not in resumed
        malformed = source.build(saver, {"unexpected": "shape"})
        with pytest.raises(ValueError, match="invalid mock tool observation"):
            malformed.invoke(
                {"case": "invalid"}, {"configurable": {"thread_id": "malformed"}}
            )
