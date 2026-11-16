"""Compare the two controlled calculations for A16.29."""

import sys

if "--break" in sys.argv[1:]:
    result = 2 * 3
else:
    result = 2**3
print(repr(result))
