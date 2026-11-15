"""Controlled experiment for A07.19. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (2) if bad else (1)
print(repr(result))
