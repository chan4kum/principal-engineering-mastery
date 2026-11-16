"""Compare the two controlled calculations for M03.03."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = max([0, 1], key=abs)
print(repr(result))
