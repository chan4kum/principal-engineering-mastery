"""Controlled experiment for A11.19. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4 * 2) if bad else (4 * 2 * 2)
print(repr(result))
