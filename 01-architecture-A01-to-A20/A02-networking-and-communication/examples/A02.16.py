"""Local example for A02.16. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

rtt, link_rate = 0.04, 100_000_000
window_bytes = 64_000 if broken else 500_000
print(f"window throughput: {min(link_rate, window_bytes * 8 / rtt) / 1e6:.1f} Mb/s")
