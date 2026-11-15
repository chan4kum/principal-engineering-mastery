"""Controlled experiment for A11.21. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0) if bad else (3 * 4)
print(repr(result))
