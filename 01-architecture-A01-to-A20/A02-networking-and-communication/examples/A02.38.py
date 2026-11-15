"""Local example for A02.38. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

parent = (0, 400)
children = [(50, 250), (150, 300)]
if broken:
    occupied = sum(end - start for start, end in children)
else:
    occupied = max(end for _, end in children) - min(start for start, _ in children)
print("outside child work:", parent[1] - parent[0] - occupied, "ms")
