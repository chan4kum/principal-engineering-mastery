"""Controlled experiment for A08.05. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1000 * 2) if bad else (1000 // 100)
print(repr(result))
