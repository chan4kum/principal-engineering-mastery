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
