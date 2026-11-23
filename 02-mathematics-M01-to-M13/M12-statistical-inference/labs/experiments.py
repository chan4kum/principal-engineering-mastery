"""Likelihood, interval, resampling, and calibration controls."""

import numpy as np


def likelihood(broken):
    probability = 0.0 if broken else 0.5
    return probability**2 * (1 - probability)


def sample_variance(broken):
    data = np.array([2.0, 4.0, 6.0])
    return float(data.var(ddof=0 if broken else 1))


def interval_sweep(broken):
    sizes = np.array([25, 100, 0 if broken else 400])
    return [float(1.96 * 5 / np.sqrt(size)) if size else "undefined" for size in sizes]


def calibration(broken):
    predicted = np.full(100, 0.8)
    observed = np.arange(100) < (60 if broken else 80)
    return float(abs(predicted.mean() - observed.mean()))


LABS = {
    "L1": (likelihood, 0.125, 0.0),
    "L2": (sample_variance, 4.0, 8 / 3),
    "L3": (interval_sweep, [1.96, 0.98, 0.49], [1.96, 0.98, "undefined"]),
    "L4": (calibration, 0.0, 0.2),
}
