# A10 · Applied assessment

1. What is the shape of a (5,3) batch times (3,2) coefficients?
2. For loss w² at w=4, what is the gradient and a step at learning rate .1?
3. Why can random splitting be invalid for forecasting?
4. What do precision and recall measure at a chosen threshold?
5. Can an always-negative classifier have 90% accuracy with zero recall?
6. Why inspect calibration separately from ranking?
7. Where do mean and standard deviation fit during cross-validation?
8. How do a model alias and immutable artifact identity differ?
9. Why can drift occur without demonstrated performance degradation?
10. How much raw memory do a billion parameters use at two bytes each?

<details>
<summary>Answers</summary>

1. (5,2).
2. Gradient 8; updated w=3.2.
3. Training may include future information or traffic unlike the deployed forecast.
4. TP/(TP+FP) and TP/(TP+FN), respectively.
5. Yes, on 90% negative labels.
6. Ordering can be correct while assigned probabilities are systematically inaccurate.
7. On each training fold only.
8. An alias is mutable; content identity identifies a particular artifact.
9. Distribution change alone does not establish degraded user outcomes.
10. About 2 GB decimal before runtime allocations.

</details>

Pass eight of ten with changed inputs. Defend the objective, the split, and the serving artifact boundaries.
