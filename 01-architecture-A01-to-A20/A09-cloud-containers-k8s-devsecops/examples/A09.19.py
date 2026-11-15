"""Controlled experiment for A09.19. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4) if bad else ((4 * 80 + 49) // 50)
print(repr(result))
