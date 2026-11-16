"""Compare the two controlled calculations for A16.28."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = 100 - 98
print(repr(result))
