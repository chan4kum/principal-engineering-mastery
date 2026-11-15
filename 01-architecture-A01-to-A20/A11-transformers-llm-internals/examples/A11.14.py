"""Controlled experiment for A11.14. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (65536) if bad else (2 * 1 * 4 * 2 * 16 * 64 * 2)
print(repr(result))
