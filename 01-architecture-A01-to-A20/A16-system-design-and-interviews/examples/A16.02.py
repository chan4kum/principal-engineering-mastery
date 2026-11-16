"""Compare the two controlled calculations for A16.02."""

import sys

if "--break" in sys.argv[1:]:
    result = 4 / 4
else:
    result = 3 / 4
print(repr(result))
