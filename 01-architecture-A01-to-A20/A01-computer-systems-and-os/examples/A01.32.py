"""Run with --break to select the controlled alternative."""

import sys as _sys
from pathlib import Path

broken = "--break" in _sys.argv[1:]

rollup = Path("/proc/self/smaps_rollup")
try:
    lines = rollup.read_text().splitlines()
except OSError:
    lines = []
for line in lines:
    if line.startswith(("Rss:", "Pss:")):
        print(line)
private, shared, workers = 10, 40, 2
print("modeled total MiB:", workers * (private + shared if broken else private + shared / workers))
