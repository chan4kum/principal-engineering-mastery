# Transformer training and local inference service

Expose POST /generate through FastAPI with a supplied trained model. Accept integer IDs 0–3, a bounded count, and temperature. Reject out-of-context requests before generation. Return generated IDs only, and reproduce the greedy continuation after training. Explain why this synthetic model cannot establish GPU or production latency.

Run the acceptance suite after the independent attempt where applicable.

```sh
uv run --locked --extra transformer --extra api pytest -q tests/test_a11_projects.py
```

<details>
<summary>Reference implementation after assessment</summary>

[Reference implementation](service.py)

</details>

Record one observed failure, its cause and the first successful recovery. Document the assumptions and one production trade-off.
