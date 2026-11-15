"""Controlled experiment for A06.20. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
highest_seen, delayed = 8, 7
print(bad or delayed >= highest_seen)
