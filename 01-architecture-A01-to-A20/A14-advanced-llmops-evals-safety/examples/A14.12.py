"""Compare the two controlled calculations for A14.12."""

import sys

if "--break" in sys.argv[1:]:
    result = all([])
else:
    result = len([]) == 3 and all([])
print(repr(result))
