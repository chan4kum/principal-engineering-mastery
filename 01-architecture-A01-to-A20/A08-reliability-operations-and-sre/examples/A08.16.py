"""Controlled experiment for A08.16. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (720) if bad else (int(720 * 0.05))
print(repr(result))
