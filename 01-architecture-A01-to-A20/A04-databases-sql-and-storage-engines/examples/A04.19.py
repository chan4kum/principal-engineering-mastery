"""Controlled experiment for A04.19. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (
    ([10, 15, 20, 30, 40][2:4])
    if bad
    else ([k for k in [10, 15, 20, 30, 40] if k > 20][:2])
)
print(repr(result))
