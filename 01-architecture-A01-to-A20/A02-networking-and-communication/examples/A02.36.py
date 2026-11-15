"""Local example for A02.36. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

outcomes = [False, True, False, False, False]
streak = 0
for tick, result in enumerate(outcomes, 1):
    streak = 0 if result else streak + 1
    if streak >= (1 if broken else 3):
        print("backend removed at probe:", tick)
        break
