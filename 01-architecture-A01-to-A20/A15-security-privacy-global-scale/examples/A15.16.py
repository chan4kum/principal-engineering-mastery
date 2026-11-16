"""Compare the two controlled calculations for A15.16."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = ("worker", "db") in {("api", "db")}
print(repr(result))
