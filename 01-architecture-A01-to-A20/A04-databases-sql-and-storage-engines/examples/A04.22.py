"""Controlled experiment for A04.22. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3) if bad else (3 * 40)
print(repr(result))
