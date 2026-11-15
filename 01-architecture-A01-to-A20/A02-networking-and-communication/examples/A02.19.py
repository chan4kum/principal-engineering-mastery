"""Local example for A02.19. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

state = 10
for _ in range(2):
    state = state + 3 if broken else 13
print("final state:", state)
