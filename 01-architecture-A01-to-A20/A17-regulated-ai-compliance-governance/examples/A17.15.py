"""Compare the two controlled calculations for A17.15."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = 0 >= 1
print(repr(result))
