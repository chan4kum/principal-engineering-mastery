"""Compare the two controlled calculations for A14.10."""

import sys

if "--break" in sys.argv[1:]:
    result = 99 / 100 >= 0.95
else:
    result = 99 / 100 >= 0.95 and 0 == 1
print(repr(result))
