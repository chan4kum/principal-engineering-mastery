"""Controlled experiment for A12.19. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (4) if bad else (2 / 4)
print(repr(result))
