# A19 · Voice, Multimodal, Edge & Embedded AI

**31 lessons · 4 labs · 2 projects**


Prerequisite [study and exit criteria](../A18-microsoft-foundry-enterprise-ai/README.md).


| ID | Lesson | Tier |
| --- | --- | --- |
| [A19.01](lessons/A19.01.md) | audio signals and sampling rates | Foundation |
| [A19.02](lessons/A19.02.md) | waveform vs features | Foundation |
| [A19.03](lessons/A19.03.md) | speech input/output | Foundation |
| [A19.04](lessons/A19.04.md) | ASR and TTS | Foundation |
| [A19.05](lessons/A19.05.md) | latency budgets | Foundation |
| [A19.06](lessons/A19.06.md) | ARM architecture | Foundation |
| [A19.07](lessons/A19.07.md) | CPU vs DSP vs NPU vs GPU | Foundation |
| [A19.08](lessons/A19.08.md) | memory and power constraints | Foundation |
| [A19.09](lessons/A19.09.md) | streaming ASR | Core |
| [A19.10](lessons/A19.10.md) | Whisper/Azure Speech/Cerence comparisons | Core |
| [A19.11](lessons/A19.11.md) | ASR-LLM-TTS stages | Core |
| [A19.12](lessons/A19.12.md) | voice activity detection | Core |
| [A19.13](lessons/A19.13.md) | barge-in and interruption | Core |
| [A19.14](lessons/A19.14.md) | local model selection | Core |
| [A19.15](lessons/A19.15.md) | quantization | Core |
| [A19.16](lessons/A19.16.md) | pruning | Core |
| [A19.17](lessons/A19.17.md) | knowledge distillation | Core |
| [A19.18](lessons/A19.18.md) | device runtime formats | Core |
| [A19.19](lessons/A19.19.md) | cloud-edge routing | Core |
| [A19.20](lessons/A19.20.md) | offline fallback | Core |
| [A19.21](lessons/A19.21.md) | thermal/power budgets | Principal |
| [A19.22](lessons/A19.22.md) | cross-compiler/toolchain | Principal |
| [A19.23](lessons/A19.23.md) | memory-mapped weights | Principal |
| [A19.24](lessons/A19.24.md) | hardware compatibility | Principal |
| [A19.25](lessons/A19.25.md) | telemetry | Principal |
| [A19.26](lessons/A19.26.md) | model updates and rollback | Principal |
| [A19.27](lessons/A19.27.md) | safety-critical function boundaries | Principal |
| [A19.28](lessons/A19.28.md) | audio noise robustness | Principal |
| [A19.29](lessons/A19.29.md) | streaming benchmark | Principal |
| [A19.30](lessons/A19.30.md) | automotive lifecycle and software supply chain | Principal |
| [A19.31](lessons/A19.31.md) | ROS2 and perception optional track | Principal |

## Guided walkthrough

Follow audio through capture, recognition, response generation, and playback, then evaluate the same path under device and network constraints.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Model the signal and device budget (A19.01–A19.08)

1. **[A19.01 · audio signals and sampling rates](lessons/A19.01.md).** Sampling represents a continuous signal at discrete times. A bandlimited signal below half the sample rate can be recovered in the ideal model. Real systems filter before sampling. A 16 kHz sampling rate has Nyquist frequency 8 kHz. A 9 kHz tone exceeds it.
2. **[A19.02 · waveform vs features](lessons/A19.02.md).** A waveform stores amplitude over time. Features summarize short frames using energy, frequency content or learned transforms. Specify window, hop and channel conventions. At 16 kHz a 25 ms window contains 400 samples. A 10 ms hop contains 160.
3. **[A19.03 · speech input/output](lessons/A19.03.md).** Capture, resample and frame input before recognition. Synthesize and buffer output at the playback contract. Exchange clocks and formats explicitly. Mono 16-bit PCM at 16 kHz uses 32,000 bytes/s before headers. Stereo doubles it.
4. **[A19.04 · ASR and TTS](lessons/A19.04.md).** ASR maps audio to text estimates and TTS maps text to audio. Use separate evaluations such as word errors for ASR and listening or task measures for TTS. One substitution, one insertion and one deletion in a ten-word reference gives WER 0.3.
5. **[A19.05 · latency budgets](lessons/A19.05.md).** Measure capture, endpointing, partial recognition, generation and first playback. For serial stages sum per-request duration and report tail behavior over trials. A controlled serial path takes 120+180+40 ms = 340 ms.
6. **[A19.06 · ARM architecture](lessons/A19.06.md).** Arm architecture describes instruction sets and execution states. Verify the target CPU features, operating system and ABI alongside instruction extensions. An artifact needs aarch64 and feature f. A target with only aarch64 fails the modeled requirement.
7. **[A19.07 · CPU vs DSP vs NPU vs GPU](lessons/A19.07.md).** CPU suits general control work. DSPs often process signal kernels, and GPU/NPU benefits depend on supported operations and data movement. Measure whole-pipeline cost. A modeled accelerator kernel takes 8 ms plus 6 ms transfer each way, total 20. A 15 ms CPU path wins.
8. **[A19.08 · memory and power constraints](lessons/A19.08.md).** Budget resident weights, runtime, activation peak, temporary buffers and concurrent requests. Track peak memory and power together. Weights 48 MiB, runtime 24 and peak transient 32 total 104 MiB, above a 96 MiB budget.

### Build the streaming and edge pipeline (A19.09–A19.20)

9. **[A19.09 · streaming ASR](lessons/A19.09.md).** Streaming ASR emits revised partial results and stable finalized segments. Keep IDs and ordering explicit, and handle network interruption. Partials 'hel' and 'hello' with one final yield one committed segment.
10. **[A19.10 · Whisper/Azure Speech/Cerence comparisons](lessons/A19.10.md).** Compare Whisper, Azure Speech and Cerence offerings by deployment target, language, licensing or commercial terms, latency and WER on identical labeled audio. Verify available features for the selected version. Provider A makes 3 errors in 20 words and B makes 5, so fixture WER gap is 0.1.
11. **[A19.11 · ASR-LLM-TTS stages](lessons/A19.11.md).** Bound queue sizes and correlate recognition, response and playback to one turn identity. Stop stale outputs on cancellation and record first playback. Three stage outputs arrive under turn IDs 1,2,1 while current turn is 2. Only one is eligible.
12. **[A19.12 · voice activity detection](lessons/A19.12.md).** Voice activity detection distinguishes active speech from nonspeech. A short energy detector is a baseline. Dynamic background, hangover and hysteresis can reduce chatter. Frame RMS values 0.01, 0.11 and 0.02 with threshold 0.08 detect one frame.
13. **[A19.13 · barge-in and interruption](lessons/A19.13.md).** On deliberate barge-in, cancel the live turn, flush queued audio and ignore late stale chunks by generation ID. Separate acoustic echo from genuine user activity. With current generation 2, a late chunk from generation 1 is discarded.
14. **[A19.14 · local model selection](lessons/A19.14.md).** Compare model size, latency, language coverage, license and quality on target devices. Filter against mandatory offline and memory requirements first. Two variants take 8 and 21 MiB. Only the smaller fits a 16 MiB weight cap.
15. **[A19.15 · quantization](lessons/A19.15.md).** Represent selected tensors using lower precision, often with scale and zero point. Measure rounding, clipping, kernel support and quality across slices. 1000 FP32 elements need 4000 B versus 1000 B for int8 payload, before scales and padding.
16. **[A19.16 · pruning](lessons/A19.16.md).** Pruning removes selected weights or structured groups. Savings depend on storage format, supported operators and scheduling. Compare on the target. 60 zero entries among 100 gives 60% sparsity. A dense kernel may still visit all 100.
17. **[A19.17 · knowledge distillation](lessons/A19.17.md).** Distillation trains a student from teacher signals, often soft class probabilities and task labels with temperature. Evaluate student failure modes on real target slices. A hard prediction [1,0] removes the 0.3 alternative probability present in teacher [0.7,0.3].
18. **[A19.18 · device runtime formats](lessons/A19.18.md).** Record format, opset, execution provider and host capability. Verify output tolerances and unsupported-operator behavior on the real device. Required ops matmul and resize, supplied matmul only: one is missing.
19. **[A19.19 · cloud-edge routing](lessons/A19.19.md).** Choose routes by policy, connectivity and deadline. Keep safe local functions available while deferring cloud-dependent work. Cloud unavailable and local available permits one eligible route. Cloud-only permits zero.
20. **[A19.20 · offline fallback](lessons/A19.20.md).** Define an offline policy with a small local capability set and explicit deferral. Use safe defaults when authorization, time or telemetry dependencies are unavailable. Offline intent status is allowed while remote-write is deferred.

### Verify rollout, safety, and sustained behavior (A19.21–A19.31)

21. **[A19.21 · thermal/power budgets](lessons/A19.21.md).** Measure steady-state latency, temperature, energy and throughput after warm-up, then report throttling and battery profiles. 2 W sustained for 30 s uses 60 J. A 4 W path uses 120 J.
22. **[A19.22 · cross-compiler/toolchain](lessons/A19.22.md).** Choose target tuple, compatible sysroot and target dependencies. Inspect resulting artifact architecture and verify with emulator or hardware where relevant. Host arm64 and required target linux/amd64 differ. Matching only source language does not verify target.
23. **[A19.23 · memory-mapped weights](lessons/A19.23.md).** Memory mapping creates an address mapping. Pages are brought in on access as the system needs them. Measure faults and resident memory separately from virtual size. Touching 5 modeled pages at 4 KiB each accounts for 20 KiB. The mapped file contains 100 pages.
24. **[A19.24 · hardware compatibility](lessons/A19.24.md).** Define OS, ABI, architecture, optional extensions and accelerator driver compatibility. Test the actual support matrix with representative models. Three hardware combinations and two builds verified leave one combination unresolved.
25. **[A19.25 · telemetry](lessons/A19.25.md).** Prefer sequence, timing, sample count, route and error metadata. Enforce data minimization, consent when applicable and bounded retention. Allowed fields are latency and route. Raw PCM and transcript add two disallowed fields.
26. **[A19.26 · model updates and rollback](lessons/A19.26.md).** Verify artifact identity and integrity, activate atomically, and preserve the previous working version. Account for compatibility and anti-rollback policy. Invalid candidate v2 leaves v1 active. Unconditional activation chooses v2.
27. **[A19.27 · safety-critical function boundaries](lessons/A19.27.md).** Identify safety-critical functions independently of voice and keep qualified, bounded control channels for them. A local voice fixture exposes only benign allowlisted actions. One benign query and one safety-critical control are requested. Only the benign query is eligible.
28. **[A19.28 · audio noise robustness](lessons/A19.28.md).** Compare cohorts using a fixed reference corpus and report signal-to-noise conditions and errors by noise class. Keep clean and noisy denominators visible. Four clean errors in 100 words and 14 noisy errors in 100 give 10 percentage points difference.
29. **[A19.29 · streaming benchmark](lessons/A19.29.md).** For repeatable audio, measure first partial, first final and end-to-end times with explicit start events and overlap. Record revises and empty trials. Events at 90,200,410 ms give first partial 90, first final 200 and completion 410.
30. **[A19.30 · automotive lifecycle and software supply chain](lessons/A19.30.md).** Automotive development divides software update management, cybersecurity and functional safety responsibilities. Verify applicable standards and supplier evidence for each product context. Of four fixture software components, three link to versioned evidence. One lacks traceability.
31. **[A19.31 · ROS2 and perception optional track](lessons/A19.31.md).** ROS 2 nodes exchange typed data and QoS profiles affect compatibility, delivery and queueing. Lifecycle transitions and timestamp checks define operational behavior. A message aged 150 ms exceeds a 100 ms consumer deadline in this fixture.

### Put it together

For barge-in, cancel obsolete recognition or generation work and discard any remaining audio tied to the superseded turn. Measure from the interruption signal to actual playback silence. Repeat with an offline connection and verify the declared fallback while keeping safety-critical controls outside the conversational path.

## Practice and exit gate

- [L1 · Small reproducible experiment](labs/L1.md)
- [L2 · Measured comparison](labs/L2.md)
- [L3 · Failure injection](labs/L3.md)
- [L4 · Independent exercise](labs/L4.md)
- [Local voice activity and streaming prototype](projects/guided/README.md)
- [Edge-capable offline-safe voice assistant](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Score at least 80% on fresh cases, reproduce four labs, meet both project acceptance criteria, diagnose one unfamiliar failure, and repeat the assessment after a delay.

Continue with [A20 · Forward-Deployed Engineering, Product & Leadership](../A20-forward-deployed-product-leadership/README.md) after the applicable gates.
