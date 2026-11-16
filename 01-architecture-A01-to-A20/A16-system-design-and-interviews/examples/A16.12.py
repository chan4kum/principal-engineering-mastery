"""Compare the two controlled calculations for A16.12."""

import sys

if "--break" in sys.argv[1:]:
    result = 4 * 10
else:
    result = 10
print(repr(result))
