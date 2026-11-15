"""Controlled experiment for A06.18. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
members, acknowledgments = 5, 2
print(acknowledgments >= (2 if bad else members // 2 + 1))
