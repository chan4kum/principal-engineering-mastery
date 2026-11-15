"""A LangGraph trace that pauses before recording a mock side effect."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import interrupt


class Case(TypedDict, total=False):
    case: str
    evidence: str
    effect: str


def build(
    checkpointer, evidence: str = "fixture reference", *, fail_read: bool = False
):
    def read(_: Case):
        if fail_read:
            raise RuntimeError("controlled fixture timeout")
        if not isinstance(evidence, str) or not 1 <= len(evidence) <= 300:
            raise ValueError("invalid mock tool observation")
        return {"evidence": evidence}

    def activate(state: Case):
        decision = interrupt(
            {"case": state["case"], "action": "record simulated notice"}
        )
        return {"effect": "notice recorded" if decision is True else "declined"}

    graph = StateGraph(Case)
    graph.add_node("read_mock_case", read)
    graph.add_node("approval_gate", activate)
    graph.add_edge(START, "read_mock_case")
    graph.add_edge("read_mock_case", "approval_gate")
    graph.add_edge("approval_gate", END)
    return graph.compile(checkpointer=checkpointer)
