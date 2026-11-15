"""Local example for A02.20. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

deadline, upstream_completion = 300, 450
gateway_status = 504 if upstream_completion > deadline else 200
print("reported status:", 200 if broken else gateway_status, "generating hop: gateway")
