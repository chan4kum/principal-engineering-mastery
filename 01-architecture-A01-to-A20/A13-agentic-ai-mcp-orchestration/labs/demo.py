"""Four commands exercise state, authorization, approval, and audit."""

import argparse
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.types import Command

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "projects/guided"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "projects/independent"))
from coordinator import Coordinator, Denied, Principal
from workflow import build

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("lab", choices=["L1", "L2", "L3", "L4"])
    args = parser.parse_args()
    with TemporaryDirectory() as directory:
        root = Path(directory)
        if args.lab == "L1":
            position = {"configurable": {"thread_id": "case-1"}}
            with SqliteSaver.from_conn_string(str(root / "graph.db")) as saver:
                try:
                    build(saver, fail_read=True).invoke({"case": "case-1"}, position)
                except RuntimeError as error:
                    if str(error) != "controlled fixture timeout":
                        raise
                    print("tool fault:", error)
            with SqliteSaver.from_conn_string(str(root / "graph.db")) as saver:
                result = build(saver).invoke(None, position)
                print(
                    "paused:",
                    bool(result.get("__interrupt__")),
                    "effect:",
                    result.get("effect"),
                )
            with SqliteSaver.from_conn_string(str(root / "graph.db")) as saver:
                resumed = build(saver).invoke(Command(resume=False), position)
                print("resumed:", resumed["effect"])
        elif args.lab == "L4":
            with SqliteSaver.from_conn_string(str(root / "graph.db")) as saver:
                try:
                    build(saver, "").invoke(
                        {"case": "malformed"},
                        {"configurable": {"thread_id": "malformed"}},
                    )
                except ValueError as error:
                    print("invalid tool response stopped workflow:", error)
                else:
                    raise RuntimeError("malformed tool response unexpectedly accepted")
        if args.lab != "L1":
            api = Coordinator(root / "workflow.db")
            operator = Principal("operator-a", "tenant-a", "operator")
            reviewer = Principal("reviewer-a", "tenant-a", "reviewer")
            payload = "local simulated notice"
            proposal, identity = api.propose(operator, "notice", payload)
            try:
                if args.lab == "L2":
                    api.approve(
                        Principal("other", "tenant-b", "reviewer"),
                        proposal,
                        identity,
                        1,
                        10,
                    )
                else:
                    api.execute(operator, proposal, payload, 2)
            except Denied as error:
                print("policy denial:", error)
            print("effects before approval:", api.effects("tenant-a"))
            api.approve(reviewer, proposal, identity, 3, 10)
            api.execute(operator, proposal, payload, 4)
            api.execute(operator, proposal, payload, 5)
            print("effects after replay:", api.effects("tenant-a"))
            print("audit:", api.history(operator, proposal))
