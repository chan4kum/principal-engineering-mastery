"""Compare the two controlled calculations for A19.14."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = sum(x <= 16 for x in [8, 21])
print(repr(result))
