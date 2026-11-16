"""Compare the two controlled calculations for A14.20."""

import sys

if "--break" in sys.argv[1:]:
    result = len([7, 7, 8])
else:
    result = len(set([7, 7, 8]))
print(repr(result))
