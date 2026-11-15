"""Controlled experiment for A07.08. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4) if bad else (2 * 4)
print(repr(result))
