# Independent project · Concurrent task runner

Implement a bounded runner for fixed local fixture jobs. During Stage B, use this specification and the acceptance tests without inspecting the reference implementation.

```text
ordered job list -> bounded dispatch -> child processes
                                      -> status and exit code
                                      -> CPU time and peak RSS side channel
                  -> aggregate JSON in original input order
```

## Interface

Your `runner.py` accepts `--workers 1…8`, `--timeout 0.05…10` seconds, and a list of at most 32 tasks. Fixtures are `wait` (roughly 0.15 s), `cpu` (bounded arithmetic), `fail` (exit 7), and `timeout` (longer than the ordinary one-second budget). Emit a JSON object containing `wall_seconds` for the batch and a `jobs` array in input order. Each job has `index` (zero-based), `action`, `pid`, `status` (`ok`, `failed`, or `timeout`), `returncode`, `wall_seconds`, `cpu_seconds` and `peak_rss_bytes`. Represent unavailable telemetry as JSON null. Report process failure in the result so other jobs can finish. Invalid arguments exit with an error.

Use monotonic wall time and per-child CPU usage. Linux reports peak RSS in KiB via Python's getrusage, while macOS reports bytes. Keep the timed fixture bounded, terminate and reap it on timeouts, and release any temporary state on all paths.

## Acceptance and recovery

```sh
P=01-architecture-A01-to-A20/A01-computer-systems-and-os/projects/independent
A01_RUNNER="$P/runner.py" uv run pytest -q tests/test_projects.py -k runner
uv run python "$P/runner.py" --workers 2 --timeout 0.5 cpu fail timeout wait
uv run python "$P/runner.py" --workers 2 --timeout 1 cpu wait
```

Predict which jobs fail and which report usable metrics. Save a trace of your failure and the recovery. Compare 1 versus 2 workers on four waiting jobs with several trials. Explain concurrency bounds, startup overhead, signal semantics, and why aggregate peak RSS cannot recover simultaneous live memory. Submit the implementation with tests, the sketch, your failure evidence and one trade-off.

<details>
<summary>Reference implementation for review after the independent gate</summary>

The [reference runner](reference_runner.py) is used by repository CI. Use it for comparison after your attempt.

</details>
