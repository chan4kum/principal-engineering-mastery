"""Controlled experiment for A07.24. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
jobs = list(range(30))
claims = [jobs[:10]] * 3 if bad else [jobs[i : i + 10] for i in range(0, 30, 10)]
print(len({job for worker in claims for job in worker}))
