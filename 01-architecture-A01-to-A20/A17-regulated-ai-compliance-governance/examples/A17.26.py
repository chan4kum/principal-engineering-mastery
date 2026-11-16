"""Compare the two controlled calculations for A17.26."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = True and False
print(repr(result))
