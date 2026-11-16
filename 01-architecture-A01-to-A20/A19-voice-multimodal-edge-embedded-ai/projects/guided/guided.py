"""Streaming RMS voice-activity baseline on normalized synthetic PCM."""

from math import isfinite, sqrt


class Detector:
    def __init__(self, frame_samples: int, onset: float, release: float):
        if frame_samples < 1 or not 0 <= release < onset <= 1:
            raise ValueError("invalid frame or thresholds")
        self.frame_samples = frame_samples
        self.onset = onset
        self.release = release
        self.speaking = False
        self.pending = []

    def feed(self, samples):
        batch = list(samples)
        if any(not isfinite(x) or abs(x) > 1 for x in batch):
            raise ValueError("samples outside normalized PCM domain")
        self.pending.extend(batch)
        total = len(self.pending) // self.frame_samples
        result = []
        for start in range(0, total * self.frame_samples, self.frame_samples):
            frame = self.pending[start : start + self.frame_samples]
            rms = sqrt(sum(x * x for x in frame) / self.frame_samples)
            self.speaking = rms >= (self.release if self.speaking else self.onset)
            result.append(self.speaking)
        del self.pending[: total * self.frame_samples]
        return result
