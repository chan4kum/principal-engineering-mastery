"""Compare the two controlled calculations for A19.29."""

import sys

if "--break" in sys.argv[1:]:
    result = (410, 410, 410)
else:
    result = (90, 200, 410)
print(repr(result))
