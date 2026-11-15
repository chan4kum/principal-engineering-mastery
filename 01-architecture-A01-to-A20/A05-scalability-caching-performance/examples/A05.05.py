"""Controlled experiment for A05.05. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (200) if bad else (200 * 5)
print(repr(result))
