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

## Guided walkthrough

Follow a Python API request from source code and object lifetimes through request validation, downstream calls, and shutdown. The runtime examples use the repository’s CPython 3.12 baseline. Use the linked lessons for runnable controls and the labs for measured behavior.

### Execution, data, and cleanup (A03.01–A03.09)

1. **Execution pipeline.** CPython parses source into an abstract syntax tree, compiles it into code objects, and executes those objects. Top-level code can run during import. A `__main__` guard keeps entry-point work such as launching a server out of ordinary imports.
2. **Bytecode.** The code object for `return x + 1` contains instructions for loading operands, adding them, and returning the result. Use `dis` with the deployed interpreter when investigating the instructions, since names and specialization can vary by release.
3. **Identity and references.** A name binds to an object. With `a = [7]` and `b = [7]`, `a == b` is true and `a is b` is false. Assigning `b = a` binds both names to the same list.
4. **Mutability and aliasing.** If `a = [[1]]` and `b = a.copy()`, appending to `b[0]` also changes what `a[0]` shows. The outer lists are distinct and the nested list is shared. Copy the nested object when callers need independent ownership.
5. **Reference counting and cyclic GC.** CPython can reclaim many objects when their reference count reaches zero. A self-referencing object can become unreachable while its count stays positive. The cyclic collector can reclaim tracked unreachable cycles.
6. **List and dictionary costs.** List membership can inspect every element. Dictionary lookup is expected constant time for well-distributed hashes and inexpensive keys. Hashing, equality, collisions, and resize costs matter when comparing performance for real inputs.
7. **Iterators and generators.** An iterator supplies one item per pull. A generator preserves local state across `yield`, so a consumer can stop early and avoid computing later items. Once a generator is exhausted, iterate a new generator to start again.
8. **Type hints.** An annotation such as `count: int` informs tooling and libraries. An ordinary function call can still pass a string through. Apply runtime validation where untrusted data enters the system.
9. **Exceptions and context managers.** `with` pairs successful acquisition with cleanup on normal exit or exception. `__exit__` receives exception details and can suppress the exception if it deliberately returns a truthy value. A `finally` block also supports cleanup while an exception propagates.

### Concurrency and serving requests (A03.10–A03.20)

10. **CPython’s GIL.** In conventional CPython 3.12, threads do not run Python bytecode in parallel within the same interpreter. Blocking I/O and some native compute can release the GIL. Shared-state updates still need an ordering or synchronization policy.
11. **Coroutines and `await`.** Calling an async function creates a coroutine object. The event loop can run another task when a coroutine suspends on incomplete work. Awaiting an already completed result may continue immediately.
12. **Event loop.** The loop runs ready callbacks and reacts to timers and I/O. If a callback blocks the loop for 100 ms, a heartbeat due 20 ms into that block runs at least 80 ms late. Observe event-loop lag separately from downstream response time.
13. **Tasks and futures.** A task schedules a coroutine and exposes its eventual result. A future represents completion that another component can resolve. Give each task an owner that observes failure and handles cancellation.
14. **Cancellation and `TaskGroup`.** A child’s ordinary exception causes the group to cancel its remaining children and wait for their cleanup before reporting failures. Put resource release in `finally`, and let cancellation propagate after cleanup.
15. **Threads, processes, and pools.** Threads share process memory and can offload blocking calls. Worker processes have separate memory and incur startup and data-transfer costs, but can execute Python computation in parallel. Bound queued jobs as well as active workers.
16. **ASGI and WSGI.** WSGI exposes a synchronous HTTP application interface. ASGI supplies a connection scope and asynchronous receive and send events for protocols such as HTTP and WebSocket. The serving model determines how the application interacts with incoming and outgoing data.
17. **Uvicorn workers.** Worker processes have separate application state, event loops, and lifespans. If each of four workers creates a pool capped at 10 connections, the deployment can open up to 40 connections for those pools. A process-local cache or counter is also separate per worker.
18. **FastAPI route lifecycle.** FastAPI matches the method and path, resolves dependencies, and validates inputs before running the endpoint when prerequisites succeed. Response conversion or validation can still fail after handler execution. Endpoint side effects must account for that boundary.
19. **Dependency injection.** Declare request-scoped needs such as the authenticated caller or a database session. A `yield` dependency can pair acquisition with release at the relevant scope. Reusing a dependency within one request can share its result, so make its lifetime and ownership explicit.
20. **Middleware.** Middleware wraps downstream execution according to stack order. An outer timing wrapper sees time spent in inner middleware and the route. For a streaming response, observing the final ASGI body event captures a different boundary from observing response creation.

### API contracts and access (A03.21–A03.27)

21. **Pydantic validation.** Validation checks input and constructs values under a declared model. Lax validation can coerce a string such as `"42"` to an integer, while strict validation of the corresponding Python value can reject it. Test the actual input mode and constraints exposed by the endpoint.
22. **Resource modeling.** Design public identifiers and representations around what clients need. For example, creating an order can return `201 Created` with a `Location` header for the new resource. Internal table layouts can evolve behind that contract.
23. **OpenAPI.** The schema describes routes, parameters, bodies, responses, and security. Generated clients depend on it. Test representative requests against the service to catch behavior the generated schema fails to describe.
24. **Errors and versioning.** Give clients a stable error code or problem type for branching and a human-readable detail for diagnosis. An extra response field can break a strict older client. Check changes against supported client expectations before declaring them compatible.
25. **Authentication and authorization.** Authentication establishes a principal. Authorization checks that principal’s action on a specific resource. A caller authenticated for one tenant must still pass the tenant and resource checks on every protected operation.
26. **OAuth, OIDC, and JWT.** OAuth delegates access. OIDC adds an identity layer and an ID token for the client. JWT is a token format. Check the token’s purpose, signature, issuer, audience, algorithm policy, and timing, then apply resource-level authorization.
27. **Cursor pagination.** Order by a stable key with a unique tie-breaker, such as `(created_at, id)`, and seek after the last tuple seen. Apply the same filter and tenant scope on the next request. Keyset pagination gives a continuation position. Snapshot consistency needs a separate guarantee.

### Bounded work, clients, and operations (A03.28–A03.42)

28. **Bounded async fanout.** A semaphore with 10 permits can cap active downstream calls at 10. Creating 100,000 tasks up front can still retain 100,000 task objects. Bound production or queue capacity in addition to setting the in-flight limit.
29. **CPU and I/O work separation.** Await async I/O so the loop can handle other requests during a wait. Move measured CPU-heavy work or blocking calls to suitable bounded workers. Measure event-loop lag, worker queue delay, and downstream wait separately.
30. **Connection pooling.** Share a client for its intended application lifetime and close it on shutdown. Instrument time spent acquiring a pool lease separately from connection setup and response reads. A saturated pool can delay a request before any network call begins.
31. **Idempotency keys.** A client can lose the response after a mutation succeeds. Scope the key to tenant and operation, bind it to a request fingerprint, and save the outcome with the mutation in the same transaction when they share a datastore. Reject conflicting payloads for the same key.
32. **Rate limits and quotas.** A token bucket of capacity 5 that refills at 2 tokens per second can admit an immediate burst of five from full, then regain one token every half second. A quota such as a daily request allowance constrains aggregate usage over a longer period.
33. **Retry and timeout propagation.** Every hop spends part of the caller’s budget. If a request starts with 250 ms and local queueing consumes 70 ms, at most 180 ms remain for all downstream work and return handling. Use a monotonic clock for local elapsed time and bound retries by the remaining budget.
34. **SDK construction.** Keep named operations and typed results in the public API. Give the transport ownership of connection reuse, request timeouts, and response handling. An injectable transport can test error mapping without talking to a live service.
35. **Sync and async SDK boundaries.** A synchronous request blocks its calling thread. An asynchronous transport can let the loop do other work while waiting. Use the appropriate client for the calling context and give it an explicit lifecycle.
36. **Request tracing.** An incoming trace context can link a server span to upstream work. Propagate context to downstream calls so their spans preserve the causal path. External trace metadata must be validated before use, and span attributes should stay bounded.
37. **Structured logging.** Emit stable fields such as event, outcome, duration, and correlation ID. Use an allowlist to keep credentials and sensitive payload contents out of logs. Keep per-request identifiers out of metric labels to avoid unbounded metric cardinality.
38. **Graceful shutdown.** Stop admitting new work, drain active requests up to a deadline, cancel overdue work, and close pools. Each worker owns its cleanup. Coordinate the drain budget with the time the process supervisor allows before forced termination.
39. **API compatibility testing.** Run an old client or fixture against the new behavior. Assert defaults, nullability, encodings, statuses, and error shapes. A schema diff can tell you where to look, and a compatibility test tells you whether a supported consumer still works.
40. **Streaming and cancellation.** Await downstream writes so a slow reader can apply backpressure. Handle disconnect or cancellation by stopping production and releasing resources in cleanup. Test early disconnection to detect a connection lease or worker that would remain held.
41. **Multi-tenant context.** Derive the tenant from trusted authentication, scope data access by tenant, and restore request-local context after each request. A task can inherit the context at creation, so assign background work its own explicit identity and ownership.
42. **Secure client libraries.** Verify TLS, limit requests to intended destinations, and apply the same policy when handling redirects. Use bounded deadlines and avoid emitting credentials in logs. A service that deliberately fetches user-supplied URLs also needs destination policy for resolved network addresses.

For a slow API with a saturated worker, trace one request across validation, event-loop wait, pool acquisition, and downstream I/O. A slow heartbeat points to delayed loop scheduling. A long pool wait places the delay before the network call. A long downstream span after pool acquisition points to a different bottleneck. Those distinctions determine which fix can improve the request.

## Practice and exit gate

- [L1 · References and values](labs/L1.md)
- [L2 · Async behavior](labs/L2.md)
- [L3 · API correctness](labs/L3.md)
- [L4 · Profiling](labs/L4.md)
- [Guided · Secure FastAPI CRUD API](projects/guided/README.md)
- [Independent · Asynchronous production API with tracing and idempotency](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Score at least 80% on fresh questions, reproduce each lab, and pass both project suites. Diagnose an unfamiliar failure and pass a delayed re-test. Be able to dry-run coroutine suspension, sibling cancellation, and a multi-request state trace.

Continue to [A04 · Databases, SQL & Storage Engines](../A04-databases-sql-and-storage-engines/README.md) after the exit gate.
