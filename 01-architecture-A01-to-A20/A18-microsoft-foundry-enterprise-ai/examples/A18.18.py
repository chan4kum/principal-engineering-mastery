"""Compare the two controlled calculations for A18.18."""

import sys

if "--break" in sys.argv[1:]:
    result = min([6, 5])
else:
    result = min([6 + 4, 5 + 7])
print(repr(result))
