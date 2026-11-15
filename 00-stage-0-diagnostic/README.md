# Stage 0 · Diagnostic and discipline

Run the five baseline questions from the repository root before opening the drills. Allow 15–30 minutes and attempt each prediction on paper.

```sh
uv run python 00-stage-0-diagnostic/diagnose.py
```

## Verify your predictions

| Skill | Local drill | Evidence and repair |
| --- | --- | --- |
| Python memory | Predict the results of `uv run python -c 'a=[[1]]; b=a.copy(); b[0].append(2); print(a, b, a[0] is b[0])'` | Record both values and the identity test. Replace the copy with `[row.copy() for row in a]` and predict the change. |
| Linux and process model | In a Linux shell, run `ps -o pid,ppid,stat,comm -p $$` and `head -15 /proc/$$/status`. On macOS use the same `ps` command, or enter Linux with `docker run --rm -it --network none python:3.12-slim sh` and use the proc command. | Compare PID, PPID and state. The slim image may lack `ps`. Change from shell PID to PID 1 and explain whether the view changed. |
| SQL | Run `uv run python -c 'import sqlite3; c=sqlite3.connect(":memory:"); print(c.execute("WITH t(v) AS (VALUES(10),(NULL),(10)) SELECT COUNT(*),COUNT(v),COUNT(DISTINCT v) FROM t").fetchone())'` | Predict all three counts. Replace NULL with 20 and explain each change. |
| Networking | Run `uv run python 00-stage-0-diagnostic/loopback.py` and again with `--break`. Both endpoints are local and the first socket reserves its port. | Record the byte exchange versus the connection refusal or timeout, depending on the host. Explain which layer failed before payload transfer. |
| Arithmetic | Calculate the time to transfer 128 MiB at 32 MiB/s, then at 32 Mb/s. Check with `uv run python -c 'print(128/32, 128*2**20*8/32e6)'`. | Record 4 and approximately 33.55 seconds. Show the unit cancellation and which multiplier converts bits to bytes. |

The commands leave no database, listener or container after exit. Save observed evidence in a local copy of the [tracker](../PROGRESS_TRACKER.md). Identify the lowest missed prerequisite. Repeat missed items with changed inputs and explain the corrected reasoning before continuing to [A01](../01-architecture-A01-to-A20/A01-computer-systems-and-os/README.md).
