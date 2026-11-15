"""Controlled experiment for A10.10. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (0) if bad else (200 * 5 // 100)
print(repr(result))
