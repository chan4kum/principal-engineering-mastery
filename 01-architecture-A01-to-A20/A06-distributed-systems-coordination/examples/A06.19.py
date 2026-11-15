"""Controlled experiment for A06.19. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
candidate, voter = (4, 7), (3, 90)
print(candidate[1] > voter[1] if bad else candidate > voter)
