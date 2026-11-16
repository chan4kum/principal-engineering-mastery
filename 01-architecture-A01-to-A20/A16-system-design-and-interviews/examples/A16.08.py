"""Compare the two controlled calculations for A16.08."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = len({("a", "k"), ("a", "k")})
print(repr(result))
