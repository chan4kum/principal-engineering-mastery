"""Local example for A02.23. Run with --break for the failure control."""

import sys as _sys
from collections import Counter

broken = "--break" in _sys.argv[1:]

eligible = ["a", "b"] if broken else ["b"]
counts = Counter(eligible[i % len(eligible)] for i in range(7))
print("requests sent to failed a:", counts["a"])
