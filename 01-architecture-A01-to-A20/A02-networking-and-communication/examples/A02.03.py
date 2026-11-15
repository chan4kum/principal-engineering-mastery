"""Local example for A02.03. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

layers = [("http", 100), ("tcp", 20), ("ip", 20), ("ethernet", 14)]
chosen = layers[:-1] if broken else layers
print(sum(size for _, size in chosen), "captured bytes in model")
