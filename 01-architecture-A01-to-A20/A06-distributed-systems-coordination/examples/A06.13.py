"""Controlled experiment for A06.13. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
members, copies = 3, 1
print(copies >= (1 if bad else members // 2 + 1))
