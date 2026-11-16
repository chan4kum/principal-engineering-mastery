"""Compare the two controlled calculations for M03.02."""

import sys

if "--break" in sys.argv[1:]:
    result = [4 + 1 - 5, 4 - 1 - 1]
else:
    result = [3 + 2 - 5, 3 - 2 - 1]
print(repr(result))
