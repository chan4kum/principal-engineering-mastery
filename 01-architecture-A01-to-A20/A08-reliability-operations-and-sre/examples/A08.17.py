"""Controlled experiment for A08.17. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (200) if bad else (200 * 90)
print(repr(result))
