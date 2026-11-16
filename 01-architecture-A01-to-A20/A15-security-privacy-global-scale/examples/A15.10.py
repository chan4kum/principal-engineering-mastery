"""Compare the two controlled calculations for A15.10."""

import sys

if "--break" in sys.argv[1:]:
    result = max([3, 9])
else:
    result = max(s for t, s in [("a", 3), ("b", 9)] if t == "a")
print(repr(result))
