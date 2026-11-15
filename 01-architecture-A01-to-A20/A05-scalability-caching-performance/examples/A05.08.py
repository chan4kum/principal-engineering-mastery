"""Controlled experiment for A05.08. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2000 * 20000 / 10**6) if bad else (2000 * 20000 * 8 / 10**6)
print(repr(result))
