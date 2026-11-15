"""Controlled experiment for A04.04. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (200 * 40) if bad else (1 * 40)
print(repr(result))
