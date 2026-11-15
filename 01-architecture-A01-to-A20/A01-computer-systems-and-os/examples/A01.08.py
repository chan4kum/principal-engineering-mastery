"""Run with --break to select the controlled alternative."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

offsets = (0, 64, 0) if broken else (0, 32, 0)
cached_line = None
for offset in offsets:
    line = offset // 64
    print("hit" if line == cached_line else "miss")
    cached_line = line
