# Guided project · Packet-to-API network explorer

Build a loopback HTTP client and report the last boundary it crossed. The fixture uses a disposable server and an ephemeral port.

```text
localhost lookup -> resolved IPv4 -> TCP peer -> first byte -> HTTP status
```

Run the [explorer](explorer.py) from the repository root.

```sh
P=01-architecture-A01-to-A20/A02-networking-and-communication/projects/guided
uv run python "$P/explorer.py"
uv run python "$P/explorer.py" --break
uv run python "$P/explorer.py"
uv run pytest -q tests/test_a02_projects.py -k explorer
```

1. Predict the sequence and HTTP result for the three runs.
2. Compare the JSON timing fields. The name resolution step uses a fixture table with a `localhost` entry, keeping the run independent of the host resolver. Use [L1](../../labs/L1.md) for an actual DNS query and packet trace.
3. In the broken control, all three measurements succeed and the path returns 404. Record why this calls for inspecting application routing rather than changing TCP settings.
4. Modify the server to return a different application status from a new path. Repeat the evidence trace and explain the first verified recovery signal.

The first-byte clock begins after the request send. It includes server work and transport after that point. Use one monotonic clock per process, and treat the peer tuple as hop-local. This implementation reads a bounded status line only. A production client needs a compliant HTTP parser and a policy for complete response bodies.
