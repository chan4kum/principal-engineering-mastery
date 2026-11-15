"""Run normal or controlled failure for A03.32."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

capacity, refill, elapsed = 5, 2, 4
print("tokens:", refill * elapsed if broken else min(capacity, refill * elapsed))
