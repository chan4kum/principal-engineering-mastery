# Independent project · Saga and transactional-outbox business pipeline

Operate two durable local stores. Commit order state and the outbox record in one transaction. Relay the event to a separate broker store and mark the outbox sent in the order database. Apply a durable projection keyed by the event identity and acknowledge the delivery separately.

```text
submit → reserve → charge → confirm
                         ↘ failure → refund → release → cancelled
terminal event → outbox → broker delivery → idempotent projection → acknowledge
```

Implement `Pipeline(database, broker)`, `submit(tenant, order)`, `advance(tenant, order, fail_confirmation=False)`, `publish_one(fail_after_publish=False)` and `consume_one(fail_after_effect=False)`. Return false for duplicate admission or an empty queue. Report persistent states `reserved`, `charged`, `compensating`, `refunded`, and `cancelled` along the failed path. Raise `SimulatedFailure` at each injected stop. Use the acceptance assertions for the table names and evidence schema.

```sh
P=01-architecture-A01-to-A20/A07-application-integration-arch/projects/independent
A07_PIPELINE="$P/pipeline.py" uv run --locked --extra api pytest -q tests/test_a07_projects.py -k saga
```

Record six checkpoints: business commit, effect, broker delivery, receipt, acknowledgment and final order status. Compare durable effects with delivery attempts. Design a recovery policy for failed compensation and a measurable trigger for manual review.

<details>
<summary>Reference for after the independent assessment</summary>

[Reference pipeline](reference_pipeline.py) uses SQLite and local adapter tables. Each demo stage commits separately. External payment and inventory systems would need their own idempotency, reconciliation and authority policies.

</details>
