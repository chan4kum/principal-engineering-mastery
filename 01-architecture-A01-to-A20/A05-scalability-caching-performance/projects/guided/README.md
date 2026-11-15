# Guided project · Token bucket limiter and cache benchmark

Measure how an admission rule and a cache change origin work:

```text
arrival → limiter → accepted requests → hit or origin fill → measured outcome
```

```sh
LAB=01-architecture-A01-to-A20/A05-scalability-caching-performance/labs
uv run python "$LAB/benchmarks.py" guided
uv run --locked --extra api pytest -q tests/test_a05_projects.py -k guided
```

Trace the supplied arrival times through the bucket. Compare no cache, a fitting hot set and capacity thrashing under the same key trace. Reduce the cache to one entry as the fault. Restore it to three and show recovered hits. Explain expiry versus eviction, population boundary and when each policy could move pressure back to the origin. The local origin uses a bounded wait. Record observed timing in milliseconds, along with hit, admitted and offered counts.
