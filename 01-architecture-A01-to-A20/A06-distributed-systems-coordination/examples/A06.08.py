"""Controlled experiment for A06.08. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
members, reachable = 5, 2
print(reachable >= (2 if bad else members // 2 + 1))
