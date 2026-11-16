"""Compare the two controlled calculations for A14.16."""

import sys

if "--break" in sys.argv[1:]:
    result = (130 / 3, 130 / 3)
else:
    result = (50, max([60 - 50, 130 - 60]))
print(repr(result))
