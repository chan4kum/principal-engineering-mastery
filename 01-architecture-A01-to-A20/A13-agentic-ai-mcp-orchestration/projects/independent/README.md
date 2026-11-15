# Approval-gated enterprise agent with audit

Implement a durable coordinator with a single allowlisted simulated notice action. Keep operator and reviewer roles distinct, enforce tenant boundary, bind approval to the exact proposal digest and expiry, and record one effect on replay. Audit proposals, approvals, execution and replay. Accept only a trusted application principal and clock. Fixture payloads stay local.

Run the acceptance suite after the independent attempt where applicable.

```sh
uv run --locked --extra orchestration pytest -q tests/test_a13_projects.py
```

<details>
<summary>Reference implementation after assessment</summary>

[Reference implementation](coordinator.py)

</details>

Record one observed failure, its cause and the first successful recovery. Document the assumptions and one production trade-off.
