"""Local example for A02.26. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

b_ready = 5
tcp_gap_filled = 50
delivered = b_ready if broken else max(b_ready, tcp_gap_filled)
print("TCP delivery B:", delivered, "ms")
