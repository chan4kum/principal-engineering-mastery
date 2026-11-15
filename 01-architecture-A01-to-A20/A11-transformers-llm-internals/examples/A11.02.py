"""Controlled experiment for A11.02. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1 * 3) if bad else (1 * 3 + 2 * 4)
print(repr(result))
