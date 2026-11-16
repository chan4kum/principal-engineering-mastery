"""Compare the two controlled calculations for A14.28."""

import sys

if "--break" in sys.argv[1:]:
    result = max([7, 14, 30])
else:
    result = min([7, 14, 30])
print(repr(result))
