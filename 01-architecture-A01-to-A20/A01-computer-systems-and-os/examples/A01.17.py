"""Run with --break to select the controlled alternative."""

import sys as _sys
import tracemalloc

broken = "--break" in _sys.argv[1:]

tracemalloc.start()
buffers = [bytearray(4096) for _ in range(128)]
before, _ = tracemalloc.get_traced_memory()
if not broken:
    buffers.clear()
after, _ = tracemalloc.get_traced_memory()
print(f"retained traced bytes: {before} -> {after}")
