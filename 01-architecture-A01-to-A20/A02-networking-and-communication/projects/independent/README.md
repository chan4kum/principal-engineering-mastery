# Independent project · Network fault-injection and request-path debugger

Build a repeatable debugger for a local disposable HTTP fixture. During Stage B, use this interface and acceptance tests before opening the reference code.

```text
scenario -> DNS -> TCP -> optional TLS -> first response -> HTTP status
                first failed phase -> classify -> repair -> fresh request
```

## Interface

Implement `debugger.py SCENARIO`. It must accept `ok`, `dns`, `connect`, `tls`, `read` and `http`. Use only loopback and bounded waits. Use a deterministic resolver failure for `dns`, a bound non-listening port for `connect`, TLS against a plain HTTP fixture for `tls`, a delayed response for `read`, and HTTP 503 for `http`. The TLS scenario detects a protocol mismatch. A certificate trust failure is a separate case exercised in [L2](../../labs/L2.md).

Report one JSON object with `initial` and `recovery`, each containing:

- `outcome` with the scenario label for a reproduced fault, or `ok`.
- `http_status` as 200 for success, 503 for `http`, and null if no status line was obtained.
- `trace` as a chronological list of objects with `phase`, `result` (`ok` or `failed`), and nonnegative `ms` elapsed. Do not report a phase after failure. A complete HTTP 503 has a successful read and a separate HTTP classification.

Use a fresh healthy request to verify recovery. Avoid disabling TLS verification as part of error classification.

```sh
P=01-architecture-A01-to-A20/A02-networking-and-communication/projects/independent
A02_DEBUGGER="$P/debugger.py" uv run pytest -q tests/test_a02_projects.py -k debugger
uv run python "$P/debugger.py" read
```

Also test a combined fault locally. Predict which error masks the other, then remove only that failure and test again. Submit both traces, a diagram and a trade-off between timing detail, overhead and privacy. Explain whether a slow DNS resolver is covered by an actual deadline in your design.

<details>
<summary>Reference implementation for review after the independent gate</summary>

The [reference debugger](reference_debugger.py) includes a controlled resolver and loopback fixture. A blocking general-purpose DNS resolver would need its own cancellation or isolation policy in production.

</details>
