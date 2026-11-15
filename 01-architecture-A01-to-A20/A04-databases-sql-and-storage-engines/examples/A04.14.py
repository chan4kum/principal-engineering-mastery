"""Controlled experiment for A04.14. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (50 * 200 * 10) if bad else (50 * 200 * 1)
print(repr(result))
