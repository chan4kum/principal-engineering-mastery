"""Local example for A02.06. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

outer_mtu, tunnel_overhead, headers = 1500, 80, 40
proposed = outer_mtu - headers if broken else outer_mtu - tunnel_overhead - headers
print("payload:", proposed, "fits:", proposed + headers + tunnel_overhead <= outer_mtu)
