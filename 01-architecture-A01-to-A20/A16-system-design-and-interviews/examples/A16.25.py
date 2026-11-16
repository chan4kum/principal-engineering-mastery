"""Compare the two controlled calculations for A16.25."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = sum([2, 1, 3])
print(repr(result))
