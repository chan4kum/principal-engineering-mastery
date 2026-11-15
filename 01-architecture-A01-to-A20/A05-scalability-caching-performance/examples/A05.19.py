"""Controlled experiment for A05.19. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (8 * (8 + 1)) if bad else (8 + 8)
print(repr(result))
