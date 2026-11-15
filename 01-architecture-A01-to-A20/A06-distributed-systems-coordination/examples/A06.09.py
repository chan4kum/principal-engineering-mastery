"""Controlled experiment for A06.09. Run with --break to compare."""

import sys

bad = "--break" in sys.argv[1:]
heartbeat_silence, suspicion_limit, crashed = 7, 6, False
print(heartbeat_silence > suspicion_limit if bad else crashed)
