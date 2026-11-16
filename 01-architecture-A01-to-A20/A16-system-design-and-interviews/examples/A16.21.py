"""Compare the two controlled calculations for A16.21."""

import sys

if "--break" in sys.argv[1:]:
    result = 3 * 8
else:
    result = 3 * 8 * 2
print(repr(result))
