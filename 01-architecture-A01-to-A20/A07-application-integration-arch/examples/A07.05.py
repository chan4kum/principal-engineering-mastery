"""Controlled experiment for A07.05. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0) if bad else (20 * 2)
print(repr(result))
