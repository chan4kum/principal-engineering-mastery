"""Compare the two controlled calculations for A16.33."""

import sys

if "--break" in sys.argv[1:]:
    result = 1000000
else:
    result = 1000000 * 16
print(repr(result))
