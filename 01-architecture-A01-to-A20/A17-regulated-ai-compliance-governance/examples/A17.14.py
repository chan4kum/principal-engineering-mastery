"""Compare the two controlled calculations for A17.14."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = max(0, 2 - 1)
print(repr(result))
