"""Compare the two controlled calculations for M02.04."""

import sys

if "--break" in sys.argv[1:]:
    result = not True or False
else:
    result = (not False or True, True or not False)
print(repr(result))
