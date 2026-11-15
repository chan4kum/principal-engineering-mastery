"""Local example for A02.25. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

clients, cadence = 1000, 1 if broken else 30
print(f"modeled idle requests/s: {clients / cadence:.2f}")
