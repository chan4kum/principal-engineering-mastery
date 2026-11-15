"""Run with --break to select the controlled alternative."""

import sys as _sys
import os

broken = "--break" in _sys.argv[1:]

if hasattr(os, "sched_getaffinity"):
    mask = os.sched_getaffinity(0)
    target = {max(mask) + 1} if broken else {min(mask)}
    print("eligible:", sorted(mask), "target allowed:", target <= mask)
else:
    print("Linux affinity probe unavailable; running placement model")
    print("mean ns:", 140 if broken else 0.75 * 80 + 0.25 * 140)
