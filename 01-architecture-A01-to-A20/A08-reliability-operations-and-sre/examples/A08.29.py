"""Controlled experiment for A08.29. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (10000 / 1_000_000) if bad else (10000 / 2_000_000)
print(repr(result))
