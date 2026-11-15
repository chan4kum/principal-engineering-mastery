"""Run with --break to select the controlled alternative."""

import sys as _sys
import dis

broken = "--break" in _sys.argv[1:]

source = "x + " if broken else "x + 1"
try:
    dis.dis(compile(source, "<lesson>", "eval"))
except SyntaxError:
    print("source rejected before execution")
