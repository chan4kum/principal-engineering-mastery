"""Run with --break to select the controlled alternative."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

wire = bytes.fromhex("12 34")
print(int.from_bytes(wire, "little" if broken else "big"))
