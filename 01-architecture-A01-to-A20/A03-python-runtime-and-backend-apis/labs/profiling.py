"""Profile controlled retention in bounded request batches."""

import argparse
import cProfile
import pstats
import tracemalloc
from collections import deque


def process(retain: bool) -> int:
    retained = deque(maxlen=None if retain else 8)
    for _ in range(120):
        retained.append(bytearray(4096))
    current, peak = tracemalloc.get_traced_memory()
    print(
        f"retained_chunks={len(retained)} traced_current_bytes={current} traced_peak_bytes={peak}"
    )
    return len(retained)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--break", dest="retain", action="store_true")
    args = parser.parse_args()
    tracemalloc.start()
    try:
        profiler = cProfile.Profile()
        profiler.runcall(process, args.retain)
        pstats.Stats(profiler).sort_stats("cumulative").print_stats(5)
    finally:
        tracemalloc.stop()
