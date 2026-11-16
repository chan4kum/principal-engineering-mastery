"""Compare the two controlled calculations for A18.01."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = True and False
print(repr(result))
