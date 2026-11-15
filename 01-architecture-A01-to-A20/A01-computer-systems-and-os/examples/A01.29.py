"""Run with --break to select the controlled alternative."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

owners: dict[int, int] = {}
transfers = 0
for core in (0, 1) * 5:
    offset = core * (8 if broken else 64)
    line = offset // 64
    transfers += int(line in owners and owners[line] != core)
    owners[line] = core
print("modeled ownership transfers:", transfers)
