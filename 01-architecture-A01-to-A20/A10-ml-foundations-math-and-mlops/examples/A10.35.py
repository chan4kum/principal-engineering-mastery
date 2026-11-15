"""Controlled experiment for A10.35. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1_000_000_000) if bad else (1_000_000_000 * 2)
print(repr(result))
