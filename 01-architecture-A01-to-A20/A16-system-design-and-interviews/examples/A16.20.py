"""Compare the two controlled calculations for A16.20."""

import sys

if "--break" in sys.argv[1:]:
    result = 4
else:
    result = len({1, 2}.union({2, 3}))
print(repr(result))
