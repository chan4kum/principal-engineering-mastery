"""Controlled experiment for A10.19. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (1 / 0.05) if bad else (4 / 0.05)
print(repr(result))
