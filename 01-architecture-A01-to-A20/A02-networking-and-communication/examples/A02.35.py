"""Local example for A02.35. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

cached, new = "a", "b"
elapsed, ttl = 30, 60
print("client still sees:", new if broken or elapsed >= ttl else cached)
