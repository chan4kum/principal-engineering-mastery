"""Run with --break to select the controlled alternative."""

import sys as _sys
import signal
from threading import Event

broken = "--break" in _sys.argv[1:]

arrived = Event()


def delivered(signum: int, frame: object) -> None:
    arrived.set()


old = signal.signal(signal.SIGUSR1, delivered)
try:
    if broken:
        try:
            print(1 // len([]))
        except ZeroDivisionError:
            print("synchronous language exception; no hardware interrupt measured")
    else:
        signal.raise_signal(signal.SIGUSR1)
        print("self-directed user signal observed:", arrived.is_set())
finally:
    signal.signal(signal.SIGUSR1, old)
