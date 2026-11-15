"""Train-only preprocessing and deterministic versioned model serialization."""

import hashlib
import json
from pathlib import Path

import numpy as np


def prepare(data):
    array = np.asarray(data, dtype=float)
    if (
        array.ndim != 2
        or array.shape[1] != 2
        or len(array) < 4
        or not np.isfinite(array).all()
    ):
        raise ValueError("expected at least four finite feature/target rows")
    return array


def train(rows, split: int, file: Path, *, broken: bool = False) -> dict:
    array = prepare(rows)
    if not 2 <= split <= len(array) - 1:
        raise ValueError("invalid temporal split")
    learning, holdout = array[:split], array[split:]
    source = holdout[:, 0] if broken else learning[:, 0]
    center, observed = float(source.mean()), float(source.std())
    scale = observed or 1.0
    feature = (learning[:, 0] - center) / scale
    coefficients = np.linalg.lstsq(
        np.column_stack([np.ones(len(feature)), feature]), learning[:, 1], rcond=None
    )[0]
    receipt = {
        "format": 1,
        "split": split,
        "train_digest": hashlib.sha256(
            json.dumps(learning.tolist(), separators=(",", ":")).encode()
        ).hexdigest(),
        "mean": center,
        "scale": scale,
        "coefficients": coefficients.tolist(),
    }
    file.write_text(json.dumps(receipt, sort_keys=True) + "\n")
    return receipt


def predict(file: Path, features):
    model = json.loads(file.read_text())
    if model["format"] != 1:
        raise ValueError("unsupported artifact version")
    array = np.asarray(features, dtype=float)
    if array.ndim != 1 or not np.isfinite(array).all():
        raise ValueError("expected a finite vector")
    intercept, weight = model["coefficients"]
    return intercept + weight * ((array - model["mean"]) / model["scale"])
