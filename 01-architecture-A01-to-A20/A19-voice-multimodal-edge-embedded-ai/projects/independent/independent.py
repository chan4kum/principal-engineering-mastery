"""Local offline policy and stale playback cancellation."""

from collections import deque


class VoiceSession:
    def __init__(self, max_chunks: int = 8):
        if max_chunks < 1:
            raise ValueError("queue bound required")
        self.turn = 0
        self.max_chunks = max_chunks
        self.audio = deque()

    def interrupt(self) -> int:
        self.turn += 1
        self.audio.clear()
        return self.turn

    def enqueue(self, turn: int, chunk: bytes) -> bool:
        if turn != self.turn or not chunk or len(self.audio) >= self.max_chunks:
            return False
        self.audio.append(chunk)
        return True

    def next_chunk(self) -> bytes:
        return self.audio.popleft() if self.audio else b""


def route(intent: str, online: bool) -> str:
    if intent in {"status", "help"}:
        return "local"
    if intent == "lookup":
        return "remote-read" if online else "deferred"
    return "unsupported"
