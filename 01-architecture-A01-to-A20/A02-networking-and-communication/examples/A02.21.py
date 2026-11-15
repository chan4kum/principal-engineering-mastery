"""Local example for A02.21. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

setup_ms, requests = 80, 20
opened = requests if broken else 1
print(f"mean setup: {opened * setup_ms / requests:.1f} ms/request")
