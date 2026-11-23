# A11 · Transformers, LLM Internals & Inference

**38 lessons · 4 labs · 2 projects**

Follow tensor shapes through attention and decoding, then reason about memory, scheduling and serving trade-offs. Local experiments run on synthetic tokens and CPU.

Prerequisite [A10 exit gate](../A10-ml-foundations-math-and-mlops/README.md#practice-and-exit-gate).

| ID | Lesson | Tier |
| --- | --- | --- |
| [A11.01](lessons/A11.01.md) | tensor shapes | Foundation |
| [A11.02](lessons/A11.02.md) | dot product and matrix multiplication | Foundation |
| [A11.03](lessons/A11.03.md) | softmax, cross entropy and gradients | Foundation |
| [A11.04](lessons/A11.04.md) | tokens and tokenization | Foundation |
| [A11.05](lessons/A11.05.md) | embeddings | Foundation |
| [A11.06](lessons/A11.06.md) | attention Q/K/V | Foundation |
| [A11.07](lessons/A11.07.md) | positional encoding | Foundation |
| [A11.08](lessons/A11.08.md) | residual connections | Foundation |
| [A11.09](lessons/A11.09.md) | normalization | Foundation |
| [A11.10](lessons/A11.10.md) | transformer forward pass | Foundation |
| [A11.11](lessons/A11.11.md) | autoregressive decoding | Core |
| [A11.12](lessons/A11.12.md) | logits and sampling | Core |
| [A11.13](lessons/A11.13.md) | prefill vs decode | Core |
| [A11.14](lessons/A11.14.md) | KV cache and memory math | Core |
| [A11.15](lessons/A11.15.md) | GPU memory hierarchy | Core |
| [A11.16](lessons/A11.16.md) | TTFT/TPOT/ITL/E2E | Core |
| [A11.17](lessons/A11.17.md) | throughput vs goodput | Core |
| [A11.18](lessons/A11.18.md) | benchmarking | Core |
| [A11.19](lessons/A11.19.md) | vLLM/SGLang engines | Core |
| [A11.20](lessons/A11.20.md) | continuous batching | Core |
| [A11.21](lessons/A11.21.md) | schedulers, fairness and cancellation | Core |
| [A11.22](lessons/A11.22.md) | PagedAttention | Core |
| [A11.23](lessons/A11.23.md) | prefix caching | Core |
| [A11.24](lessons/A11.24.md) | mixed-length workloads | Core |
| [A11.25](lessons/A11.25.md) | BF16/FP8/INT8/4-bit formats | Principal |
| [A11.26](lessons/A11.26.md) | AWQ/GPTQ/SmoothQuant | Principal |
| [A11.27](lessons/A11.27.md) | KV quantization | Principal |
| [A11.28](lessons/A11.28.md) | profiling and roofline | Principal |
| [A11.29](lessons/A11.29.md) | FlashAttention | Principal |
| [A11.30](lessons/A11.30.md) | Triton and kernel fusion | Principal |
| [A11.31](lessons/A11.31.md) | torch.compile and CUDA graphs | Principal |
| [A11.32](lessons/A11.32.md) | speculative decoding | Principal |
| [A11.33](lessons/A11.33.md) | MoE routing and parallelism | Principal |
| [A11.34](lessons/A11.34.md) | TP/PP/DP/CP | Principal |
| [A11.35](lessons/A11.35.md) | NCCL/NVLink | Principal |
| [A11.36](lessons/A11.36.md) | disaggregated prefill-decode | Principal |
| [A11.37](lessons/A11.37.md) | offload and long-context tiers | Principal |
| [A11.38](lessons/A11.38.md) | model routing and serving economics | Principal |

## Guided walkthrough

Follow tokens through a transformer forward pass, then account for the time and memory required to serve the result.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Follow the tensor operations (A11.01–A11.10)

1. **[A11.01 · tensor shapes](lessons/A11.01.md).** Keep batch, sequence, head and feature axes explicit. A projection from model width d to h heads of width k requires compatible width h×k. A [2,3,8] tensor split into two heads of width four has 48 elements before and after reshaping.
2. **[A11.02 · dot product and matrix multiplication](lessons/A11.02.md).** A dot product contracts a common vector axis. Matrix multiplication computes one dot product per output pair of row and column. For [1,2] dot [3,4], the result is 11.
3. **[A11.03 · softmax, cross entropy and gradients](lessons/A11.03.md).** Subtract the maximum before exponentiating. Cross entropy for a class is negative log probability. The softmax-cross-entropy logit gradient is predicted probability minus one-hot target. Two equal logits give probabilities .5 each. The correct-class gradient is −.5.
4. **[A11.04 · tokens and tokenization](lessons/A11.04.md).** Tokenization maps text into model-specific IDs. Vocabulary, byte fallback, Unicode and framing change token count. Character count is an unreliable quota. In a fixture with four prefix tokens and three user tokens, total input is seven before output reservation.
5. **[A11.05 · embeddings](lessons/A11.05.md).** The embedding parameter table maps token IDs to learned vectors. Similarity retrieval uses separately defined transforms and a store or comparison operation. A vocabulary of 10000 and width 768 contains 7.68 million embedding parameters.
6. **[A11.06 · attention Q/K/V](lessons/A11.06.md).** Q expresses comparison queries, K supplies matchable keys and V supplies aggregated content. Scores use QK transpose divided by sqrt(head width). For scores [0,0] and scalar values [2,6], equal weighting outputs 4.
7. **[A11.07 · positional encoding](lessons/A11.07.md).** Position information can be additive, learned or represented by transformations such as rotary embeddings. Attention without position information has symmetry under compatible permutations. For absolute positions 0 to 7, shifting the sequence by three moves the final index to 10.
8. **[A11.08 · residual connections](lessons/A11.08.md).** A residual connection adds information from a branch to the original representation. Shapes must match or a projection is needed. For input 3 and update −1 the residual result is 2.
9. **[A11.09 · normalization](lessons/A11.09.md).** LayerNorm normalizes over configured feature dimensions and usually applies learned affine parameters. Epsilon stabilizes small variance. For vector [1,3], mean is 2 and population variance is 1. Ignoring epsilon gives normalized values [−1,1].
10. **[A11.10 · transformer forward pass](lessons/A11.10.md).** Projection, masked attention, residual, normalization and feed-forward steps have explicit ordering. Pre-norm and post-norm are distinct variants. With three causal tokens, the number of allowed query-key pairs is 1+2+3=6, versus nine dense pairs.

### Measure generation and serving behavior (A11.11–A11.24)

11. **[A11.11 · autoregressive decoding](lessons/A11.11.md).** Each step predicts the next token from the available prefix, then extends that prefix. Training often evaluates many next-token positions in parallel under a causal mask. A five-token prompt and three generated tokens yield length eight at completion.
12. **[A11.12 · logits and sampling](lessons/A11.12.md).** Temperature divides logits before normalization. Smaller positive values magnify differences. Greedy selection is a separate deterministic policy. A logit gap of 2 becomes 4 at T=.5 and 1 at T=2.
13. **[A11.13 · prefill vs decode](lessons/A11.13.md).** Prefill processes the available prompt and initializes cache. Decode then grows context one generated token at a time. Batching and scheduling can affect each differently. If first token takes 120 ms and 9 later tokens take 20 ms each, total is 300 ms under additive timing.
14. **[A11.14 · KV cache and memory math](lessons/A11.14.md).** KV cache stores keys and values for each cached token. For batch B, layers L, KV heads H, head size D, tokens T and bytes e, payload is 2BLHDT e. For B=1,L=4,H=2,D=16,T=64,e=2, payload is 32768 B before fragmentation.
15. **[A11.15 · GPU memory hierarchy](lessons/A11.15.md).** GPU registers, shared memory, caches and device memory differ in latency and scope. Memory bandwidth can limit work before peak compute is reached. Moving 1 GB at 500 GB/s has an ideal transfer floor of 2 ms, without latency or compute.
16. **[A11.16 · TTFT/TPOT/ITL/E2E](lessons/A11.16.md).** TTFT measures arrival to first token. ITL measures inter-token gaps. TPOT and E2E require definitions consistent with the benchmark. TTFT=100 ms, later gaps 20 and 30 ms, mean later gap 25 ms and E2E=150 ms at the final token boundary.
17. **[A11.17 · throughput vs goodput](lessons/A11.17.md).** Throughput counts work processed per time. Goodput counts work meeting a declared correctness, latency or service condition. If 100 requests complete and 75 meet latency and quality in one second, completed throughput is 100/s and goodput 75/s.
18. **[A11.18 · benchmarking](lessons/A11.18.md).** Control workload shape, offered rate, cache state, model and hardware. Record successful completions, request and token latency, and tail behavior. For 80 successes from 100 offered in two seconds, successful throughput is 40/s and offered rate is 50/s.
19. **[A11.19 · vLLM/SGLang engines](lessons/A11.19.md).** vLLM and SGLang are serving engines whose cache, batching, model and hardware features depend on version and configuration. For 4 prompt buckets, 2 engines and 2 request rates, the benchmark matrix contains 16 cases before repeats.
20. **[A11.20 · continuous batching](lessons/A11.20.md).** Continuous batching updates the set of executing requests as steps finish and new requests are admitted. It needs scheduler and memory policies. Two requests taking two and five iterations occupy 10 slot-steps in a fixed two-slot batch, while only seven slot-steps do useful decode.
21. **[A11.21 · schedulers, fairness and cancellation](lessons/A11.21.md).** Schedulers balance throughput, latency, quotas and cancellation. Removal must release KV blocks and capacity at a safe execution boundary. Three cancelled jobs holding four blocks each can release 12 blocks when cleanup finishes.
22. **[A11.22 · PagedAttention](lessons/A11.22.md).** PagedAttention maps logical sequence positions to allocated blocks. Allocation granularity and reference management matter. It does not remove KV payload itself. With 16-token blocks and 33 cached tokens, three blocks hold up to 48 slots. Fifteen slots are unused in the last allocated extent.
23. **[A11.23 · prefix caching](lessons/A11.23.md).** Prefix caching can share compatible preceding-token computations. Identity depends on exact token sequence and compatible model/runtime context. Isolate tenants where needed. A 400-token reused prefix in a 500-token prompt leaves 100 new prompt tokens to process under the simple model.
24. **[A11.24 · mixed-length workloads](lessons/A11.24.md).** Mixed lengths affect padded activations, dense work and scheduler fairness. Packing or variable-length support can reduce waste under defined semantics. Lengths 2, 3 and 10 padded to ten use 30 positions instead of 15 useful positions.

### Choose optimization and deployment trade-offs (A11.25–A11.38)

25. **[A11.25 · BF16/FP8/INT8/4-bit formats](lessons/A11.25.md).** BF16, FP8 and integer formats differ in representation and kernel support. Four-bit weights commonly have scaling metadata and wider compute or accumulation. Eight billion weights at four bits are 4 GB raw decimal before scales, metadata and runtime memory.
26. **[A11.26 · AWQ/GPTQ/SmoothQuant](lessons/A11.26.md).** AWQ uses activation-aware scaling for weights. GPTQ uses second-order information for post-training weight quantization. SmoothQuant shifts activation quantization difficulty through scaling. A 2× reduction in raw weights still leaves runtime cache and scale overhead unchanged unless separately changed.
27. **[A11.27 · KV quantization](lessons/A11.27.md).** KV cache quantization changes key/value storage separately from weight precision. Scale and kernel overhead and accuracy can vary by layer or workload. Changing a cache payload from two to one byte per element halves its raw bytes before metadata.
28. **[A11.28 · profiling and roofline](lessons/A11.28.md).** Arithmetic intensity is operations per byte transferred. A roofline bound is the lesser of peak compute and bandwidth times arithmetic intensity. At 500 GB/s and 10 op/B, the bandwidth bound is 5 TOP/s under decimal units.
29. **[A11.29 · FlashAttention](lessons/A11.29.md).** FlashAttention tiles attention and maintains stable softmax statistics to reduce transfers between memory levels. It computes exact attention up to numerical effects without the naive score materialization. At 1024 tokens, a naive dense score tensor has 1048576 entries per head.
30. **[A11.30 · Triton and kernel fusion](lessons/A11.30.md).** Fusion can combine compatible operations in one kernel. Triton exposes a programming model for tiled GPU operations. Fusion can trade lower traffic for higher register usage or compilation complexity. Two elementwise stages writing one full intermediate each can save one intermediate write and read when safely fused.
31. **[A11.31 · torch.compile and CUDA graphs](lessons/A11.31.md).** torch.compile can specialize and recompile around shape and guard changes. CUDA graphs can replay captured workloads under strict constraints. A 2 s setup amortized across 100 requests contributes 20 ms average, excluding execution.
32. **[A11.32 · speculative decoding](lessons/A11.32.md).** Speculative decoding proposes multiple tokens and verifies them with the target model. Distribution-preserving algorithms need the corresponding acceptance and correction steps. If five proposed tokens yield three accepted draft tokens, observed acceptance is 60%. Speed depends on draft and target costs too.
33. **[A11.33 · MoE routing and parallelism](lessons/A11.33.md).** A router chooses a sparse subset of experts per token. Capacity, imbalance and cross-device communication matter. Some architectures include shared experts. For eight experts and top-two routing, a token activates two routed experts, apart from any shared layers.
34. **[A11.34 · TP/PP/DP/CP](lessons/A11.34.md).** Tensor parallelism splits tensor computation, pipeline splits stages, data parallel replicates model work over inputs, and context parallel splits context computation. A model group with TP=2 and PP=2 uses four ranks in a simple nonoverlapping mapping.
35. **[A11.35 · NCCL/NVLink](lessons/A11.35.md).** NCCL implements collectives over available topology. NVLink is one possible local interconnect. Inter-node transport and algorithm affect bandwidth and latency. Sending 4 GB on a 100 GB/s path has an ideal lower bound of 40 ms for that data movement.
36. **[A11.36 · disaggregated prefill-decode](lessons/A11.36.md).** Disaggregation places prompt work and decode on different resources. Transferring KV or routing intermediate state introduces latency, bandwidth, and admission requirements. Moving 200 MB over a 10 GB/s payload link takes at least 20 ms in the decimal ideal model.
37. **[A11.37 · offload and long-context tiers](lessons/A11.37.md).** Offload moves cached state or weights across slower tiers. Prefetch can hide some movement when timing permits. Available capacity differs from usable token rate. Transferring 1 GB over 25 GB/s takes at least 40 ms before overhead.
38. **[A11.38 · model routing and serving economics](lessons/A11.38.md).** Routing uses quality, latency and cost constraints with an explicit fallback policy. Compare spend per successful acceptable outcome rather than nominal requests. At 12 units for 1000 requests with 800 accepted outcomes, cost per acceptable outcome is .015.

### Put it together

Compare two serving configurations with the same input and output length distribution. Track time to first token, gaps between output tokens, and the rate of requests that meet the service targets. A setting that increases total tokens per second can reduce useful throughput if mixed-length batches delay too many requests.

## Practice and exit gate

- [L1 · Attention by hand](labs/L1.md)
- [L2 · Toy transformer](labs/L2.md)
- [L3 · Memory math](labs/L3.md)
- [L4 · Inference baseline](labs/L4.md)
- [Guided · Numerical attention and tiny GPT](projects/guided/README.md)
- [Independent · Transformer training and local inference service](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs and both project acceptance suites. Score at least 80% on a fresh set of questions, diagnose one unfamiliar failure, and repeat after a delay. Demonstrate the phase failure modes and defend the resource or trust boundaries with observed evidence.

Continue to [A12 · Search, RAG & Knowledge Systems](../A12-search-rag-and-knowledge-systems/README.md) when the prerequisite stage gates are met.
