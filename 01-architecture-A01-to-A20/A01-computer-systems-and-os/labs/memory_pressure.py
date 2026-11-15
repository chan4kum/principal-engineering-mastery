"""Bounded allocations for a dedicated cgroup-v2 container."""

import argparse
from pathlib import Path
import time

parser = argparse.ArgumentParser()
parser.add_argument("--break", dest="pressure", action="store_true")
args = parser.parse_args()
cgroup = Path("/sys/fs/cgroup")
mib = 1024**2
try:
    limit = int((cgroup / "memory.max").read_text())
    usage = cgroup / "memory.current"
    usage.read_text()
except (OSError, ValueError):
    parser.exit(2, "Run inside the dedicated memory-limited cgroup-v2 container described in L3.\n")
if not 48 * mib <= limit <= 80 * mib:
    parser.exit(2, "Expected a dedicated 48–80 MiB memory cap.\n")

buffers = []
for _ in range(32 if args.pressure else 4):
    buffers.append(bytearray(b"X") * (4 * mib))
    print(
        f"allocated={4 * len(buffers)} MiB cgroup={int(usage.read_text()) / mib:.1f} MiB",
        flush=True,
    )
    time.sleep(0.03)
