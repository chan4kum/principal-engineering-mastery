"""Compare the two controlled calculations for A18.14."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = True and "public" == "private"
print(repr(result))
