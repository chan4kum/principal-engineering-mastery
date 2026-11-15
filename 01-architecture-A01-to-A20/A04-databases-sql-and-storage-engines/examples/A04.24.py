"""Controlled experiment for A04.24. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
result = (
    (int.from_bytes(bytes.fromhex("00000100"), "little"))
    if bad
    else (int.from_bytes(bytes.fromhex("00000100"), "big"))
)
print(repr(result))
