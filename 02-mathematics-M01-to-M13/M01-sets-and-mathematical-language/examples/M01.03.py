"""Compare the two controlled calculations for M01.03."""

import sys

if "--break" in sys.argv[1:]:
    result = (frozenset({1}) in {1, 2}, False)
else:
    result = (1 in {1, 2}, {1} <= {1, 2})
print(repr(result))
