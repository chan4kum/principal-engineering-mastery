"""Local example for A02.27. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

ready = {"a": 50, "b": 5}
visible_b = max(ready.values()) if broken else ready["b"]
print("QUIC model delivery B:", visible_b, "ms")
