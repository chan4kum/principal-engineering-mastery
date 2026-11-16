"""Compare the two controlled calculations for M03.04."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = 1 + any(b - 2 * a for a, b in zip([1, 2], [2, 4]))
print(repr(result))
