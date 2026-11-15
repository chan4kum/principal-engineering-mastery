"""Controlled experiment for A09.33. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4 * 200) if bad else (2 * 200)
print(repr(result))
