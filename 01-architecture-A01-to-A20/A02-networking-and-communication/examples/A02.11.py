"""Local example for A02.11. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

cached, current = "192.0.2.2", "192.0.2.3"
now, expiry = 30, 30
print("address:", cached if broken or now < expiry else current)
