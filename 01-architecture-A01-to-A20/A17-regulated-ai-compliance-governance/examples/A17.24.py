"""Compare the two controlled calculations for A17.24."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = len({"C1", "C2", "C3"} - {"C1", "C3"})
print(repr(result))
