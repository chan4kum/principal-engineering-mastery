# Guided project · OpenTelemetry service dashboard

```text
FastAPI request → bounded execution → dependency span
               → request counter + duration histogram + active and saturation instruments
               → local JSON dashboard
```

Start with [L1](../../labs/L1.md) and use [dashboard.py](dashboard.py) to inspect in-memory SDK records. Use the project test to hold the first request in the dependency and send a second while the only slot is occupied.

```sh
uv run --locked --extra api --extra telemetry pytest -q tests/test_a08_projects.py -k guided
```

Compare a failed dependency and rejected admission. Both emit 503 here, but only admission emits saturation. Measure active execution before and after release. Correlate parent and dependency spans, and show a recovered request and zero active work. The local dashboard has no credentials, hosted exporter or externally published traffic. Production aggregation must maintain compatible units, boundaries and sampling policy.
