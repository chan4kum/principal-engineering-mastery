# A10 · ML Foundations, AI Math & MLOps

**35 lessons · 4 labs · 2 projects**

Build statistical reasoning from shapes and gradients, then carry data and evaluation boundaries into reproducible deployment. All reference data is synthetic and exercises run on CPU.

Prerequisite [A09 exit gate](../A09-cloud-containers-k8s-devsecops/README.md#practice-and-exit-gate).

| ID | Lesson | Tier |
| --- | --- | --- |
| [A10.01](lessons/A10.01.md) | sets, logic and functions | Foundation |
| [A10.02](lessons/A10.02.md) | vectors/matrices | Foundation |
| [A10.03](lessons/A10.03.md) | derivatives and gradients | Foundation |
| [A10.04](lessons/A10.04.md) | probability distributions | Foundation |
| [A10.05](lessons/A10.05.md) | conditional probability and Bayes | Foundation |
| [A10.06](lessons/A10.06.md) | expectation/variance | Foundation |
| [A10.07](lessons/A10.07.md) | train/validation/test separation | Foundation |
| [A10.08](lessons/A10.08.md) | linear regression and losses | Foundation |
| [A10.09](lessons/A10.09.md) | dataset quality and leakage | Core |
| [A10.10](lessons/A10.10.md) | sampling and stratification | Core |
| [A10.11](lessons/A10.11.md) | classification/regression metrics | Core |
| [A10.12](lessons/A10.12.md) | bias/variance | Core |
| [A10.13](lessons/A10.13.md) | gradient descent | Core |
| [A10.14](lessons/A10.14.md) | optimizer/learning rates | Core |
| [A10.15](lessons/A10.15.md) | feature engineering | Core |
| [A10.16](lessons/A10.16.md) | experiment tracking | Core |
| [A10.17](lessons/A10.17.md) | datasets/versioning DVC | Core |
| [A10.18](lessons/A10.18.md) | model registry | Core |
| [A10.19](lessons/A10.19.md) | model serving | Core |
| [A10.20](lessons/A10.20.md) | drift | Core |
| [A10.21](lessons/A10.21.md) | calibration | Core |
| [A10.22](lessons/A10.22.md) | monitoring | Core |
| [A10.23](lessons/A10.23.md) | MLflow and pipelines | Core |
| [A10.24](lessons/A10.24.md) | CNN/NLP and representation learning | Principal |
| [A10.25](lessons/A10.25.md) | transformers fundamentals | Principal |
| [A10.26](lessons/A10.26.md) | transfer learning | Principal |
| [A10.27](lessons/A10.27.md) | PCA and SVD | Principal |
| [A10.28](lessons/A10.28.md) | inference statistics | Principal |
| [A10.29](lessons/A10.29.md) | uncertainty and significance | Principal |
| [A10.30](lessons/A10.30.md) | causal vs correlational pitfalls | Principal |
| [A10.31](lessons/A10.31.md) | responsible ML | Principal |
| [A10.32](lessons/A10.32.md) | offline/online evaluation | Principal |
| [A10.33](lessons/A10.33.md) | retraining triggers | Principal |
| [A10.34](lessons/A10.34.md) | shadow deployments | Principal |
| [A10.35](lessons/A10.35.md) | hardware and cost budgets | Principal |

## Guided walkthrough

Build from a mathematical model to a reproducible training and deployment workflow. Keep the evaluation population and artifact identity explicit.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Build the math and establish the data split (A10.01–A10.08)

1. **[A10.01 · sets, logic and functions](lessons/A10.01.md).** A set defines membership, predicates evaluate conditions, and a mathematical function maps each element in its domain to exactly one output. For n=3 inputs and two possible outputs there are 2^3=8 possible total functions.
2. **[A10.02 · vectors/matrices](lessons/A10.02.md).** Vectors encode coordinates. A matrix maps vectors to other spaces. An (n,d) matrix of samples times a (d,k) transform yields (n,k). A (4,3) matrix times (3,2) gives (4,2), with 4×3×2 scalar multiplications in the direct algorithm.
3. **[A10.03 · derivatives and gradients](lessons/A10.03.md).** A derivative is local sensitivity. The gradient collects partial derivatives in parameter coordinates. Gradient descent changes parameters in the negative gradient direction. For L(w)=w² at w=3, gradient is 6. Step size 0.1 moves w to 2.4.
4. **[A10.04 · probability distributions](lessons/A10.04.md).** A distribution assigns probabilities to possible outcomes. Independent Bernoulli trials give a binomial count with probabilities determined by combinations and their outcomes. For p=0.25, probability of exactly one success in two independent trials is 2×.25×.75=.375.
5. **[A10.05 · conditional probability and Bayes](lessons/A10.05.md).** Bayes updates a prior with likelihood and evidence. Posterior depends on base rate as well as sensitivity and false-positive rate. With prevalence 1%, sensitivity 90% and false-positive rate 9%, P(true given positive)=.009/(.009+.0891)≈.09174.
6. **[A10.06 · expectation/variance](lessons/A10.06.md).** Expectation is the probability-weighted mean. Variance is expected squared deviation from that mean. Variance has squared units. Equal outcomes 0 and 4 have mean 2 and variance 4. Deterministic 2 has variance 0.
7. **[A10.07 · train/validation/test separation](lessons/A10.07.md).** Training fits parameters, validation informs choices, and a test set estimates performance after decisions. Those boundaries can be temporal, entity-based or random depending on the deployment. With 1000 records and 70/15/15 allocation, 150 records remain for final testing under the simple split.
8. **[A10.08 · linear regression and losses](lessons/A10.08.md).** Linear regression predicts an affine combination of features. Mean squared error averages squared residuals. It penalizes large residuals more strongly than absolute loss. Residuals 1 and 3 have MSE (1+9)/2=5 and MAE 2.

### Train, evaluate, version, and serve models (A10.09–A10.23)

9. **[A10.09 · dataset quality and leakage](lessons/A10.09.md).** Leakage occurs when features or selection carry prohibited future or target-related information. A temporal split controls one class of leakage. Point-in-time feature assembly controls another. If the feature window closes at day 12 but the forecast is issued on day 10, the feature looks two days ahead.
10. **[A10.10 · sampling and stratification](lessons/A10.10.md).** Stratification preserves an approximate label proportion across splits. Group, time and geography requirements can constrain possible stratification. At 5% positive class and 200 validation rows, proportional stratification targets about ten positives.
11. **[A10.11 · classification/regression metrics](lessons/A10.11.md).** Classification metrics use counts such as true positives, false positives and false negatives. Regression metrics evaluate residual magnitude on a defined scale. With 8 TP, 2 FP and 12 FN, precision is 0.8 and recall is 0.4.
12. **[A10.12 · bias/variance](lessons/A10.12.md).** Bias and variance describe different contributions to prediction error under a distribution and squared-loss assumptions. Generalization gaps are evidence that needs interpretation. A training MSE of 1 and validation MSE of 9 differ by 8. The gap alone does not identify the exact variance contribution.
13. **[A10.13 · gradient descent](lessons/A10.13.md).** Gradient descent iteratively updates parameters. A small step can reduce a smooth objective near the current point, while excessively large steps can overshoot. For loss w² starting at 4, with η=.1 one step gives 3.2 and loss 10.24, versus 16 initially.
14. **[A10.14 · optimizer/learning rates](lessons/A10.14.md).** Optimizer state can include momentum or running estimates. Learning rate still affects stability, convergence and generalization. With unit gradient and η=.05, a basic update changes a parameter by 0.05. Changing η to .5 increases the step tenfold.
15. **[A10.15 · feature engineering](lessons/A10.15.md).** Feature transformations must be fit at the allowed boundary and shipped with compatible schema and parameters. A zero-variance input needs deliberate handling. For mean 10 and scale 2, input 14 maps to standardized value 2.
16. **[A10.16 · experiment tracking](lessons/A10.16.md).** Experiment tracking records data identity, source revision, configuration, outcomes and artifacts. Evidence needs a defined split and evaluation version. When three hyperparameter settings and two splits are crossed, six runs are needed to cover the grid.
17. **[A10.17 · datasets/versioning DVC](lessons/A10.17.md).** Dataset versioning links manifests and data contents to a reproducible run. DVC commonly stores lightweight pointers in Git and data in a separate cache or remote. Two code versions and three dataset revisions produce six possible code/data combinations.
18. **[A10.18 · model registry](lessons/A10.18.md).** A model registry associates immutable versions with metadata, artifacts and mutable references such as aliases. Promotion should require evaluation and compatibility evidence. Three replicas following one mutable alias can converge to a new model at different times. One pinned version gives one defined artifact.
19. **[A10.19 · model serving](lessons/A10.19.md).** Serving translates validated requests into model inputs, applies the same pipeline and returns documented outputs. Throughput and latency depend on batch size and runtime. At four workers and 50 ms per equally expensive prediction, simple ideal throughput is 80/s if there is no shared bottleneck.
20. **[A10.20 · drift](lessons/A10.20.md).** Input drift, changes in target prevalence and changes in input-target relationships are distinct. Drift is a signal to investigate rather than proof of degraded decisions. A feature mean changing from 10 to 14 with reference standard deviation 2 shifts by two reference standard deviations.
21. **[A10.21 · calibration](lessons/A10.21.md).** Calibration compares predicted probability with observed frequency across comparable cases. Ranking, discrimination and calibration are separate properties. If 12 of 20 cases labeled .9 are positive, empirical frequency is .6 and absolute gap .3.
22. **[A10.22 · monitoring](lessons/A10.22.md).** Model monitoring needs request health, data quality, drift, outcome metrics and operational indicators. Labels can be delayed or absent. If 1000 requests include 25 invalid input records, invalid input rate is 2.5%.
23. **[A10.23 · MLflow and pipelines](lessons/A10.23.md).** Pipeline steps declare inputs and outputs. MLflow tracks experiments and model artifacts. Workflow execution, data versioning and deployment have separate responsibilities. A pipeline with 3 independent configurations and 4 tracked stages yields 12 stage executions without cache reuse.

### Validate evidence and operating costs (A10.24–A10.35)

24. **[A10.24 · CNN/NLP and representation learning](lessons/A10.24.md).** Convolutions share local weights across positions. Text models use sequence structure and learned representations. Representation choice affects inductive bias and input shape. A 3×3 filter on a 5×5 input with stride 1 and no padding produces a 3×3 output.
25. **[A10.25 · transformers fundamentals](lessons/A10.25.md).** Self-attention compares token queries with keys, then combines value vectors. Standard full score arrays grow quadratically in sequence length. Doubling sequence length from 128 to 256 quadruples the dense score count, from 16384 to 65536 per head.
26. **[A10.26 · transfer learning](lessons/A10.26.md).** Transfer learning reuses previously learned representation. Frozen features train only a head. Fine-tuning changes more or all pretrained weights. With 1 million encoder parameters and 1000 head parameters, freezing the encoder leaves 1000 trainable.
27. **[A10.27 · PCA and SVD](lessons/A10.27.md).** PCA rotates centered data toward variance directions. SVD yields singular vectors and values. Scaling may change the objective effectively optimized. If squared singular values are 9 and 1, the first component explains 90% of the summed variance.
28. **[A10.28 · inference statistics](lessons/A10.28.md).** Statistical inference estimates uncertainty under assumptions about sampling and measurement. Binomial data have discrete outcomes, and small samples need suitable interval choices. At p=.5 with n=100 independent Bernoulli observations, modeled standard error sqrt(p(1−p)/n)=.05.
29. **[A10.29 · uncertainty and significance](lessons/A10.29.md).** A p-value concerns data relative to a null model, not the probability that the null is true. Effect size and uncertainty answer different questions. A rate moving from 10% to 11% changes by one percentage point and 10% relative to baseline.
30. **[A10.30 · causal vs correlational pitfalls](lessons/A10.30.md).** Confounders can affect treatment and outcome. Random assignment, valid identification assumptions and design determine whether a causal effect can be inferred. A group difference of 10 percentage points can occur entirely from differing group composition. Association magnitude alone is not identification.
31. **[A10.31 · responsible ML](lessons/A10.31.md).** Responsible ML evaluates groups and use cases, documents limitations and assigns human oversight and monitoring. Metric choices must fit the application. An unweighted average of subgroup scores 90% and 60% is 75%. Population weighting changes the aggregate.
32. **[A10.32 · offline/online evaluation](lessons/A10.32.md).** Offline evaluation uses logged or synthetic conditions. Online experiments measure behavior with real interventions and feedback. Offline gains can fail to transfer. At 1000 exposures with 20 conversions, observed conversion is 2%. Changing the population can alter this without a model improvement.
33. **[A10.33 · retraining triggers](lessons/A10.33.md).** Retraining triggers can use drift, labeled performance, data windows or schedule. Retrain, validate and promote are separate stages with evidence gates. If a policy requires degradation in three daily measurements, one anomalous day is insufficient.
34. **[A10.34 · shadow deployments](lessons/A10.34.md).** A shadow deployment receives copies of selected requests to compare behavior while its output does not control the user-visible response. Shadow effects require isolation. A 10% mirror at 1000 RPS sends about 100 extra requests/s to the shadow service.
35. **[A10.35 · hardware and cost budgets](lessons/A10.35.md).** Weight, activation, cache and runtime storage budgets differ. Training also spends on gradients and optimizer state. Cost depends on actual utilization, duration and infrastructure rates. A 1-billion parameter model at two bytes/parameter has a raw weight footprint of about 2 GB decimal before runtime state.

### Put it together

A fraud model can look strong offline if training features use information that arrived after the decision time. Validate the feature timestamp, split data before fitting preprocessing, and measure performance on a held-out time window. Pin the deployed artifact and monitor outcome quality before deciding whether observed drift warrants retraining.

## Practice and exit gate

- [L1 · Linear model](labs/L1.md)
- [L2 · Data leakage](labs/L2.md)
- [L3 · Model evaluation](labs/L3.md)
- [L4 · ML pipeline](labs/L4.md)
- [Guided · Linear regression and logistic regression from scratch](projects/guided/README.md)
- [Independent · Reproducible feature-to-model ML pipeline](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs and both project acceptance suites. Score at least 80% on a fresh set of questions, diagnose one unfamiliar failure, and repeat after a delay. Verify a gradient, defend a data split and explain both offline evaluation and deployment evidence.

Continue to [A11 · Transformers, LLM Internals & Inference](../A11-transformers-llm-internals/README.md) when the prerequisite stage gates are met.
