# LangGraph stateful mock-tool workflow

Use a StateGraph with typed case state, a read fixture, an explicit interrupt and a durable local checkpointer. Record the thread identity and verify denial after closing and reopening the checkpointer. Do not put real external calls before the approval node.

Run the acceptance suite after the independent attempt where applicable.

```sh
uv run --locked --extra orchestration pytest -q tests/test_a13_projects.py
```

[Reference implementation](workflow.py)

Record one observed failure, its cause and the first successful recovery. Document the assumptions and one production trade-off.
