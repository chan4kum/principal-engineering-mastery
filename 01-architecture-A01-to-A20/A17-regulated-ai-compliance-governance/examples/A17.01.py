"""Compare the two controlled calculations for A17.01."""

import sys

if "--break" in sys.argv[1:]:
    result = sum([1, 0, 0])
else:
    result = sum([1, 1, 0])
print(repr(result))
