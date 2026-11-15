# Independent project · Capacity-aware service with SLO and queue telemetry

Implement a FastAPI factory called `create_app(workers=3, queue_limit=6, slo_ms=100, work=None)`. During Stage B, work from this contract and the acceptance tests.

```text
offered request → worker available or bounded waiting → execute → success telemetry
                            → queue full → 503
```

- `POST /work` returns 200 on completion and 503 with a retry hint when the wait queue is full. Use the supplied async `work` callback when present. Release accounting for cancelled queued and active requests.
- `GET /metrics` returns cumulative integer `offered`, `rejected`, `succeeded`, `cancelled`, `failed`, and `met_slo`, plus current `active` and `waiting`. Return `sample_count`, nearest-rank `p95_ms`, and `mean_queue_ms` as measured over a bounded recent successful sample window. Latency includes admission wait and service time.
- Explain how to compute a success/SLO fraction using the offered count. Quantiles of successful work can hide rejection.

```sh
P=01-architecture-A01-to-A20/A05-scalability-caching-performance/projects/independent
A05_SERVICE="$P/service.py" uv run --locked --extra api pytest -q tests/test_a05_projects.py -k service
```

Save a trace of steady operation, overload, one cancellation and recovery. State worker and queue caps and the observation window. Add a scenario where more application replicas exhaust a fixed downstream connection budget. Discuss reservations or global admission and the effect on headroom.

<details>
<summary>Reference implementation for review after the independent gate</summary>

[Reference service](reference_service.py) uses a single local event loop and a 256-sample window. Counters are per process. Multi-worker aggregation and downstream concurrency limits require separate design.

</details>
