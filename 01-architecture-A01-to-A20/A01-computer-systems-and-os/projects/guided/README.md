# Guided project · Linux resource explorer

Build a read-only single-PID explorer. Treat process disappearance and missing optional fields as ordinary outcomes.

```text
CLI PID -> /proc/<pid>/status -> parse counters -> JSON with units
                               -> missing/denied -> error status 2
```

1. Capture a live status file on Linux and identify PID, PPID, state and threads.
2. Convert the reported RSS from Linux kB units to bytes. Treat missing RSS as unknown, since some tasks have no user mappings.
3. Try the [implementation](explorer.py) from the repository root.

```sh
G=01-architecture-A01-to-A20/A01-computer-systems-and-os/projects/guided
uv run python "$G/explorer.py" "$$"
uv run python "$G/explorer.py" "$$" --proc-root /nonexistent
uv run python "$G/explorer.py" "$$"
uv run pytest -q tests/test_projects.py -k explorer
```

The middle command should exit 2. On Linux, rerun without the invalid root and capture the recovered JSON. On macOS, pytest supplies synthetic proc files so parser behavior remains testable. For a Linux-container observation, mount the project read-only and run `sh -c 'python /lab/explorer.py "$$"'` inside it.

A single status read avoids piecing together several files that could describe different instants. It still describes a point in time and a numeric PID can be reused between samples. Record observer scope, timestamp, and status. Discuss why a production collector may require start time, PSS, and cgroup data too.
