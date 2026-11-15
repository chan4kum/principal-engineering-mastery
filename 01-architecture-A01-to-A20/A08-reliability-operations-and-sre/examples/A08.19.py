"""Controlled experiment for A08.19. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (59 - 45) if bad else (45 - 40)
print(repr(result))
