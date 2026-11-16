"""Compare the two controlled calculations for A14.11."""

import sys

if "--break" in sys.argv[1:]:
    result = ("p1", "s2")
else:
    result = {"r1": ("p1", "s1"), "r2": ("p2", "s2")}["r1"]
print(repr(result))
