"""Compare the two controlled calculations for A16.09."""

import sys

if "--break" in sys.argv[1:]:
    result = 500 / 200
else:
    result = 200 / 500
print(repr(result))
