"""Run with --break to select the controlled alternative."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

rate = 100_000_000
divisor = rate if broken else rate / 8
print(f"{2**30 / divisor:.2f} seconds")
