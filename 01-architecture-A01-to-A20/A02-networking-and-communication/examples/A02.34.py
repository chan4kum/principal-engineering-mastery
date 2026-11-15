"""Local example for A02.34. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

emitted = [50, 100, 150]
first_visible = emitted[-1] if broken else emitted[0]
print("first chunk delay after emission:", first_visible - emitted[0], "ms")
