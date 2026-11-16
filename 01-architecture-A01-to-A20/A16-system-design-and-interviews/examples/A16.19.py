"""Compare the two controlled calculations for A16.19."""

import sys

if "--break" in sys.argv[1:]:
    result = 1
else:
    result = sum(x <= 2 for x in [1, 2, 3])
print(repr(result))
