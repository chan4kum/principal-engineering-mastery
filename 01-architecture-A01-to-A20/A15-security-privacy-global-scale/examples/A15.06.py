"""Compare the two controlled calculations for A15.06."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = True and "billing" == "catalog"
print(repr(result))
