"""Compare the two controlled calculations for A15.01."""

import sys

if "--break" in sys.argv[1:]:
    result = 99 / 100 >= 0.95
else:
    result = (99 / 100, False)
print(repr(result))
