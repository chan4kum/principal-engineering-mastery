"""Compare the two controlled calculations for M02.05."""

import sys

if "--break" in sys.argv[1:]:
    result = any(all(x == y for x in [1, 2]) for y in [1, 2])
else:
    result = all(any(x == y for y in [1, 2]) for x in [1, 2])
print(repr(result))
