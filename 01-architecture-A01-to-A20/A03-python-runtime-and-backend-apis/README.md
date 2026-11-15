# A03 · Python Runtime & Backend API Engineering

**42 lessons · 4 labs · 2 projects**

Build from Python execution and references to concurrency, API contracts, telemetry and secure clients. IDs, titles and tiers follow the roadmap indexes. Python 3.12 is the supported baseline; CPython details and framework versions are identified within the applicable lessons. Use the lockfile for experiment reproducibility.

Prerequisite [A02 exit gate](../A02-networking-and-communication/README.md#practice-and-exit-gate).

| ID | Lesson | Tier |
| --- | --- | --- |
| [A03.01](lessons/A03.01.md) | Python execution pipeline | Foundation |
| [A03.02](lessons/A03.02.md) | compilation to bytecode | Foundation |
| [A03.03](lessons/A03.03.md) | object identity and references | Foundation |
| [A03.04](lessons/A03.04.md) | mutability and aliasing | Foundation |
| [A03.05](lessons/A03.05.md) | reference counting/cyclic GC | Foundation |
| [A03.06](lessons/A03.06.md) | list/dict runtime costs | Foundation |
| [A03.07](lessons/A03.07.md) | iterators/generators | Foundation |
| [A03.08](lessons/A03.08.md) | type hints | Foundation |
| [A03.09](lessons/A03.09.md) | exceptions and context managers | Foundation |
| [A03.10](lessons/A03.10.md) | Python GIL and concurrency scope | Core |
| [A03.11](lessons/A03.11.md) | coroutines, await and cooperative scheduling | Core |
| [A03.12](lessons/A03.12.md) | event loop | Core |
| [A03.13](lessons/A03.13.md) | Task/Future | Core |
| [A03.14](lessons/A03.14.md) | cancellation and TaskGroup | Core |
| [A03.15](lessons/A03.15.md) | threads/processes and pools | Core |
| [A03.16](lessons/A03.16.md) | ASGI vs WSGI | Core |
| [A03.17](lessons/A03.17.md) | Uvicorn worker model | Core |
| [A03.18](lessons/A03.18.md) | FastAPI route lifecycle | Core |
| [A03.19](lessons/A03.19.md) | dependency injection | Core |
| [A03.20](lessons/A03.20.md) | middleware | Core |
| [A03.21](lessons/A03.21.md) | Pydantic validation | Core |
| [A03.22](lessons/A03.22.md) | API resource modeling | Core |
| [A03.23](lessons/A03.23.md) | OpenAPI | Core |
| [A03.24](lessons/A03.24.md) | errors and versioning | Core |
| [A03.25](lessons/A03.25.md) | authN vs authZ | Core |
| [A03.26](lessons/A03.26.md) | OAuth 2.0/OIDC/JWT | Core |
| [A03.27](lessons/A03.27.md) | pagination and cursor semantics | Core |
| [A03.28](lessons/A03.28.md) | bounded async fanout | Principal |
| [A03.29](lessons/A03.29.md) | CPU/I/O work separation | Principal |
| [A03.30](lessons/A03.30.md) | connection pooling | Principal |
| [A03.31](lessons/A03.31.md) | idempotency keys | Principal |
| [A03.32](lessons/A03.32.md) | rate limits and quotas | Principal |
| [A03.33](lessons/A03.33.md) | retry/timeout propagation | Principal |
| [A03.34](lessons/A03.34.md) | SDK construction | Principal |
| [A03.35](lessons/A03.35.md) | sync vs async SDK boundary | Principal |
| [A03.36](lessons/A03.36.md) | request tracing | Principal |
| [A03.37](lessons/A03.37.md) | structured logging | Principal |
| [A03.38](lessons/A03.38.md) | graceful shutdown | Principal |
| [A03.39](lessons/A03.39.md) | API compatibility testing | Principal |
| [A03.40](lessons/A03.40.md) | streaming and event cancellation | Principal |
| [A03.41](lessons/A03.41.md) | multi-tenant context propagation | Principal |
| [A03.42](lessons/A03.42.md) | secure client libraries | Principal |

## Practice and exit gate

- [L1 · References and values](labs/L1.md)
- [L2 · Async behavior](labs/L2.md)
- [L3 · API correctness](labs/L3.md)
- [L4 · Profiling](labs/L4.md)
- [Guided · Secure FastAPI CRUD API](projects/guided/README.md)
- [Independent · Asynchronous production API with tracing and idempotency](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Score at least 80% on fresh questions, reproduce each lab, and pass both project suites. Diagnose an unfamiliar failure and pass a delayed re-test. Be able to dry-run coroutine suspension, sibling cancellation, and a multi-request state trace.
