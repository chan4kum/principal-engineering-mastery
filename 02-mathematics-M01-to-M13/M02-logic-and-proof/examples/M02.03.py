"""Compare the two controlled calculations for M02.03."""

import sys

if "--break" in sys.argv[1:]:
    result = [int(a != b) for a in (False, True) for b in (False, True)]
else:
    result = [int(a or b) for a in (False, True) for b in (False, True)]
print(repr(result))
