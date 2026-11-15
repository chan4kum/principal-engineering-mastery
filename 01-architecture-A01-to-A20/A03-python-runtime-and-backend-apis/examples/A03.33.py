"""Run normal or controlled failure for A03.33."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

remaining = 350 - 90 - (0 if broken else 60)
print("downstream attempt admitted:", remaining >= 220)
