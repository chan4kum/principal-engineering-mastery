"""Compare the two controlled calculations for A14.14."""

import sys

if "--break" in sys.argv[1:]:
    result = type({}.get("amount")) is int
else:
    result = type({"amount": 4}.get("amount")) is int
print(repr(result))
