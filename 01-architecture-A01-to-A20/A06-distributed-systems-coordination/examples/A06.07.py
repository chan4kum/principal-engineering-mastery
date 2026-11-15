"""Controlled experiment for A06.07. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
previous, incoming = (5, 99), (6, 1)
print(incoming[1] > previous[1] if bad else incoming > previous)
