"""Local example for A02.37. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

rtt = 80
calls = 3 if broken else 1
print("network floor:", rtt * calls, "ms")
