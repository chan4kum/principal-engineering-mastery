# A03 · Applied assessment

Attempt before reading the answers. Score at least eight of ten and demonstrate the labs, two projects, one new failure diagnosis and delayed retention.

1. Two equal lists are created separately. Predict the results of comparing them with `is` and `==`.
2. A 25-row stream produces 2 KiB per row. How many payload bytes are retained by eager materialization?
3. Trace task A awaiting an incomplete future while task B is runnable. Which can run next?
4. A TaskGroup child raises ValueError while a sibling awaits a timer. Identify the sibling outcome and cleanup location.
5. A handler's body fails schema validation. Is the route handler guaranteed to have run?
6. User A submits a valid token and tries to access a resource owned by B. Which check is responsible?
7. Nine 30 ms equal operations use a pool of two workers. Estimate the ideal service rounds and elapsed time.
8. An idempotent POST commits before its response is lost. How should the client recover?
9. Two services share a logged request ID. Is that sufficient to reconstruct span parentage?
10. A blocking SDK runs in async handlers. Why can p99 rise while CPU remains low?

<details>
<summary>Answers</summary>

1. Identity false, equality true if both lists have equal elements.
2. 50 KiB, or 51,200 B, before overhead.
3. B can run while A's future remains incomplete.
4. The group requests cancellation. A finally block after suspension handles cleanup before the group returns.
5. No. FastAPI can reject the request before invoking it.
6. Authorization, including tenant or owner scoping on the resource.
7. Five rounds and roughly 150 ms plus overhead.
8. Retry the identical request with the same scoped key and retrieve the committed outcome.
9. No. You also need causal span or equivalent parent relationships.
10. The main loop thread waits synchronously, delaying other runnable work without necessarily consuming CPU.

</details>

## Source scenario

A blocking model SDK is called from async handlers. Draw the event-loop trace for two requests and a queued heartbeat. Compare an async transport, bounded worker offload and a dedicated job queue. In each design, explain what happens when the client cancels while remote work is still in progress. Async I/O improves overlap but cannot reduce the model's token-generation time on its own.
