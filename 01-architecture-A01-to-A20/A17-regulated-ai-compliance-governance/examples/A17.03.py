"""Compare the two controlled calculations for A17.03."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = True and not True
print(repr(result))
