"""Compare the two controlled calculations for A17.02."""

import sys

if "--break" in sys.argv[1:]:
    result = 1.0
else:
    result = 3 / 5
print(repr(result))
