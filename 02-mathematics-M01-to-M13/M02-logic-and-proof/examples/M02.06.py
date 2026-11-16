"""Compare the two controlled calculations for M02.06."""

import sys

if "--break" in sys.argv[1:]:
    result = (not True) and (not False)
else:
    result = not (True and False)
print(repr(result))
