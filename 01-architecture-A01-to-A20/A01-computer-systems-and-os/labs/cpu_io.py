"""Compare CPU and elapsed time without external I/O."""

import argparse
from pathlib import Path
import time

parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=("cpu", "wait"))
args = parser.parse_args()
stats = Path("/sys/fs/cgroup/cpu.stat")

if stats.is_file():
    print("cpu.stat before:", stats.read_text().strip().replace("\n", ", "))
wall, cpu = time.perf_counter(), time.process_time()
if args.mode == "cpu":
    sum(number * number for number in range(5_000_000))
else:
    time.sleep(0.3)
print(f"wall={time.perf_counter() - wall:.4f}s CPU={time.process_time() - cpu:.4f}s")
if stats.is_file():
    print("cpu.stat after:", stats.read_text().strip().replace("\n", ", "))
