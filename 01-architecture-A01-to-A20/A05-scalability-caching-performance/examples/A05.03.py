"""Controlled experiment for A05.03. Run with --break to compare."""

import sys
from math import ceil
from statistics import mean


def percentile(samples, p):
    return sorted(samples)[ceil(p * len(samples)) - 1]


bad = "--break" in sys.argv[1:]
result = (mean([10] * 19 + [210])) if bad else (percentile([10] * 19 + [210], 0.99))
print(repr(result))
