"""Controlled experiment for A04.35. Run with --break to compare."""

import sys
from zlib import crc32

bad = "--break" in sys.argv[1:]
result = (True) if bad else (crc32(b"abc") == crc32(b"abd"))
print(repr(result))
