"""Local example for A02.12. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

clients = [("10.0.0.2", 51000), ("10.0.0.3", 51000)]
gateway = "203.0.113.5"
reverse = {(gateway, 40000 if broken else 40000 + i): client for i, client in enumerate(clients)}
print("distinct reply mappings:", len(reverse))
