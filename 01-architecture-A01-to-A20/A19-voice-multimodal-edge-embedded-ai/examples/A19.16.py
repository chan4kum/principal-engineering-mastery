"""Compare the two controlled calculations for A19.16."""

import sys

if "--break" in sys.argv[1:]:
    result = (60 / 100, 40)
else:
    result = (60 / 100, 100)
print(repr(result))
