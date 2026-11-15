"""Controlled experiment for A13.05. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2) if bad else (2 * 3)
print(repr(result))
