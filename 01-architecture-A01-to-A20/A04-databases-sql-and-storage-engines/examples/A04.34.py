"""Controlled experiment for A04.34. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (600 * 1024 / 200) if bad else (600 * 1024 / 200 / 60)
print(repr(result))
