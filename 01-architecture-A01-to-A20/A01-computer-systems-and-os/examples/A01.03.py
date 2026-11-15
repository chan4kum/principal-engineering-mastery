"""Run with --break to select the controlled alternative."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

value = 128 if broken else 127
try:
    print(value.to_bytes(1, "big", signed=True).hex())
except OverflowError:
    print("signed field out of range")
