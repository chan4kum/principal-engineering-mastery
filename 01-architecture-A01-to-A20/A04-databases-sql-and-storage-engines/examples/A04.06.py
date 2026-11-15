"""Controlled experiment for A04.06. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (int(100000 * 0.1)) if bad else (int(100000 * 0.001))
print(repr(result))
