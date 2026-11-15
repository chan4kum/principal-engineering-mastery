"""Run bounded local jobs and collect process, CPU and peak RSS evidence."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import time

PROGRAM = """
import json
from pathlib import Path
import os
import resource
import sys
import time

action, metrics = sys.argv[1:]
if action == "wait":
    time.sleep(0.15)
elif action == "cpu":
    sum(i*i for i in range(250_000))
elif action == "timeout":
    time.sleep(5)
usage = resource.getrusage(resource.RUSAGE_SELF)
rss = usage.ru_maxrss * (1 if sys.platform == "darwin" else 1024)
Path(metrics).write_text(json.dumps({
    "pid": os.getpid(),
    "cpu_seconds": usage.ru_utime + usage.ru_stime,
    "peak_rss_bytes": rss,
}))
raise SystemExit(7 if action == "fail" else 0)
"""


def run_one(index: int, action: str, timeout: float) -> dict[str, object]:
    with TemporaryDirectory() as directory:
        path = Path(directory) / "worker.json"
        started = time.monotonic()
        with subprocess.Popen([sys.executable, "-c", PROGRAM, action, str(path)]) as child:
            timed_out = False
            try:
                returncode = child.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                timed_out = True
                child.kill()
                returncode = child.wait()
            metrics = json.loads(path.read_text()) if not timed_out and path.exists() else {}
            return {
                "index": index,
                "action": action,
                "pid": child.pid,
                "status": "timeout" if timed_out else "failed" if returncode else "ok",
                "returncode": returncode,
                "wall_seconds": time.monotonic() - started,
                "cpu_seconds": metrics.get("cpu_seconds"),
                "peak_rss_bytes": metrics.get("peak_rss_bytes"),
            }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("actions", nargs="+", choices=("wait", "cpu", "timeout", "fail"))
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--timeout", type=float, default=1.0)
    args = parser.parse_args()
    if not 1 <= args.workers <= 8 or not 0.05 <= args.timeout <= 10 or len(args.actions) > 32:
        parser.error("use 1–8 workers, a 0.05–10 second timeout and at most 32 tasks")
    started = time.monotonic()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [
            pool.submit(run_one, index, action, args.timeout)
            for index, action in enumerate(args.actions)
        ]
        jobs = [future.result() for future in futures]
    print(json.dumps({"jobs": jobs, "wall_seconds": time.monotonic() - started}))


if __name__ == "__main__":
    main()
