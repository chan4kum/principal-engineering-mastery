"""Compare the two controlled calculations for A15.18."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = True and False
print(repr(result))
