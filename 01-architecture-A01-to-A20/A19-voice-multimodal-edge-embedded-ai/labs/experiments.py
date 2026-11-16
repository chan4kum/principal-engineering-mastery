"""Run chunking, noise, interruption and offline scenarios."""

from guided import Detector
from independent import VoiceSession, route


def observe(lab, broken):
    if lab == 1:
        detector = Detector(4, 0.1, 0.05)
        return detector.feed([0.2, 0.2]) + detector.feed([0.2] if broken else [0.2, 0.2])
    if lab == 2:
        detector = Detector(2, 0.03 if broken else 0.1, 0.01)
        return detector.feed([0.04, 0.04, 0.2, -0.2])
    if lab == 3:
        voice = VoiceSession()
        voice.enqueue(0, b"prior")
        turn = voice.interrupt()
        accepted = voice.enqueue(turn - 1 if broken else turn, b"fresh")
        return accepted, voice.next_chunk()
    return route("lookup", online=not broken), route("status", online=False)


EXPECTED = (
    ([True], []),
    ([False, True], [True, True]),
    ((True, b"fresh"), (False, b"")),
    (("remote-read", "local"), ("deferred", "local")),
)
