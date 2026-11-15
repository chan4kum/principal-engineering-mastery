"""Run with --break to select the controlled alternative."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

quota, period, work = 20, 100, 50
completed = 0
while work > quota:
    completed += period
    work -= quota
print("elapsed model ms:", 50 if broken else completed + work)
print("exit 137 requires separate evidence of memory OOM")
