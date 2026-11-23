"""Conditional probability, expectation, and sampling controls."""

import numpy as np


def conditional(broken):
    events = 0 if broken else 5
    hits = 0 if broken else 2
    return hits / events if events else "undefined"


def moments(broken):
    support = np.array([0, 4])
    probabilities = np.array([0.5, 0.4 if broken else 0.5])
    if not np.isclose(probabilities.sum(), 1):
        return "invalid total probability"
    mean = support @ probabilities
    return [float(mean), float((support - mean) ** 2 @ probabilities)]


def sampling_sweep(broken):
    sizes = np.array([2, 4, 8])
    population = 10
    second_draw = sizes / population if broken else (sizes - 1) / (population - 1)
    return (sizes / population * second_draw).tolist()


def positive_predictive_value(broken):
    prior = 0.1 if broken else 0.01
    true_positive = 0.9 * prior
    false_positive = 0.05 * (1 - prior)
    return true_positive / (true_positive + false_positive)


LABS = {
    "L1": (conditional, 0.4, "undefined"),
    "L2": (moments, [2.0, 4.0], "invalid total probability"),
    "L3": (sampling_sweep, [1 / 45, 2 / 15, 28 / 45], [0.04, 0.16, 0.64]),
    "L4": (positive_predictive_value, 2 / 13, 2 / 3),
}
