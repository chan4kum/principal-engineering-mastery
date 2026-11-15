"""Run with --break to select the controlled alternative."""

import sys as _sys
import mmap
import resource

broken = "--break" in _sys.argv[1:]

with mmap.mmap(-1, 64 * 1024) as region:
    start = resource.getrusage(resource.RUSAGE_SELF).ru_minflt
    if not broken:
        for offset in range(0, len(region), mmap.PAGESIZE):
            region[offset] = 1
    end = resource.getrusage(resource.RUSAGE_SELF).ru_minflt
    print("page bytes:", mmap.PAGESIZE, "minor faults delta:", end - start)
