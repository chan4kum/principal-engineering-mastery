"""Compare the two controlled calculations for A16.26."""

import sys

if "--break" in sys.argv[1:]:
    result = max([4, 7, 5])
else:
    result = min([4, 7, 5])
print(repr(result))
