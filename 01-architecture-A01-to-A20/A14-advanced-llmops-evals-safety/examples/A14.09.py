"""Compare the two controlled calculations for A14.09."""

import sys

if "--break" in sys.argv[1:]:
    result = ((3 + 4) / 10, 1)
else:
    result = (3 / (3 + 2), 3 / (3 + 1))
print(repr(result))
