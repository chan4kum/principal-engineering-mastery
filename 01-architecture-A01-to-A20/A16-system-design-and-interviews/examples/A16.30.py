"""Compare the two controlled calculations for A16.30."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = sum(latency <= 80 and cost <= 5 for latency, cost in [(75, 4), (70, 6), (85, 3)])
print(repr(result))
