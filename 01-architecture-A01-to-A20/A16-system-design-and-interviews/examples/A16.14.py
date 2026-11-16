"""Compare the two controlled calculations for A16.14."""

import sys

if "--break" in sys.argv[1:]:
    result = 3
else:
    result = len({"p1", "p1", "p2"})
print(repr(result))
