# Independent project · Asynchronous production API with tracing and idempotency

During Stage B, use the interface and tests before opening the reference. Build a runnable local service.

```text
async request → identity and schema → bounded storage work → atomic job + receipt
                          → request-local ID and timing → response
```

Implement `create_app(db, tokens, emit=None)`. Accept `POST /jobs` with a JSON `{"label":"work"}`, bearer token and an `Idempotency-Key` composed of 1–80 ASCII letters, digits, underscores or hyphens. The token mapping determines tenant. Require a nonempty label of up to 80 characters.

First valid submission returns 201 with an ID, original label, Location, and `Idempotency-Replayed: false`. Equal replays get the same body and Location with `true`. Tenant scopes are independent. A conflicting body for the same tenant and key returns 409. The job and the receipt must commit together and remain available after app restart. SQLite acceptance tests inspect `jobs(id, tenant, label)` for count and scope. Invalid JSON fields are rejected, missing credentials return 401, and a missing or invalid idempotency key returns 400.

Generate a unique `X-Request-ID` per request including handled errors. If supplied, call the synchronous `emit` observer with the request ID, method, route template, status and elapsed milliseconds. Keep tokens, raw payloads and idempotency keys out of the event. Explain how your production design would integrate W3C context and a nonblocking exporter.

```sh
P=01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/projects/independent
A03_API="$P/api.py" uv run --locked --extra api pytest -q tests/test_a03_projects.py -k jobs
```

Record both first and replay response IDs and show that concurrent duplicate submissions cause one write. Demonstrate a conflicting replay, restart the service and verify recovery with the same original key. Explain SQLite write serialization, bounded worker admission and expiry policy. The reference permits eight outstanding storage jobs per worker and rejects excess work with 503. Cancelling the awaiting handler keeps its storage job counted until the thread finishes; reconcile unknown outcomes with the same key. This local reference illustrates techniques used in production and does not provide a deployed production service.

<details>
<summary>Reference implementation for review after the independent gate</summary>

[Reference API](reference_api.py)

</details>
