"""Run normal or controlled failure for A03.30."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

requests, setup_ms = 10, 50
connections = requests if broken else 1
print("setup cost ms:", connections * setup_ms)
