"""Compare the two controlled calculations for A15.08."""

import sys

if "--break" in sys.argv[1:]:
    result = len(["a", "b", "b", "a", "b"])
else:
    result = sum(t == "a" for t in ["a", "b", "b", "a", "b"])
print(repr(result))
