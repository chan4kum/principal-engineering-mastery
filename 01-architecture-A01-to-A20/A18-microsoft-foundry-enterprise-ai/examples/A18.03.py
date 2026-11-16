"""Compare the two controlled calculations for A18.03."""

import sys

if "--break" in sys.argv[1:]:
    result = 0.9
else:
    result = max(s for t, s in [("a", 0.4), ("a", 0.5), ("b", 0.9)] if t == "a")
print(repr(result))
