"""Controlled experiment for A11.25. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (8_000_000_000) if bad else (8_000_000_000 // 2)
print(repr(result))
