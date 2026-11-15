"""Controlled experiment for A04.08. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (100 * 3) if bad else (100 * 1)
print(repr(result))
