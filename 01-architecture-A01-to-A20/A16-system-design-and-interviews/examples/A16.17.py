"""Compare the two controlled calculations for A16.17."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = len({"d1", "d2"} - {"d1"})
print(repr(result))
