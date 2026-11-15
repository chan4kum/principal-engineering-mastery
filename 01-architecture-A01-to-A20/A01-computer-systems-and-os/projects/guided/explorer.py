"""Inspect Linux process counters from a configurable proc filesystem."""

import argparse
import json
from pathlib import Path


def inspect_process(proc_root: Path, pid: int) -> dict[str, int | str | None]:
    status = (proc_root / str(pid) / "status").read_text()
    fields = dict(line.split(":\t", 1) for line in status.splitlines() if ":\t" in line)
    return {
        "pid": int(fields["Pid"]),
        "ppid": int(fields["PPid"]),
        "name": fields["Name"],
        "state": fields["State"].split()[0],
        "threads": int(fields["Threads"]),
        "rss_bytes": int(fields["VmRSS"].split()[0]) * 1024 if "VmRSS" in fields else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pid", type=int)
    parser.add_argument("--proc-root", type=Path, default=Path("/proc"))
    args = parser.parse_args()
    if args.pid < 1:
        parser.error("pid must be positive")
    try:
        print(json.dumps(inspect_process(args.proc_root, args.pid)))
    except (OSError, ValueError, KeyError) as error:
        parser.exit(2, f"PID {args.pid} unavailable or incomplete: {error}\n")


if __name__ == "__main__":
    main()
