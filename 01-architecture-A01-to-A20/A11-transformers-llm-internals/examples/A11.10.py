"""Controlled experiment for A11.10. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (3 * 3) if bad else (3 * (3 + 1) // 2)
print(repr(result))
