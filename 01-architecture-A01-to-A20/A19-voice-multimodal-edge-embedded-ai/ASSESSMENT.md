# A19 applied assessment

Close the reference solutions. Predict results, then reproduce the changed-input controls with one previously unseen value.

1. Feed a normalized PCM stream in chunks, then leave the last frame incomplete. Record frame decisions and distinguish pending from silent frames.
2. Feed noise below the nominal threshold, then lower the attack threshold into the noise band. Record false activity and use a labeled corpus before changing a production threshold.
3. Interrupt buffered output then enqueue a stale chunk from the cancelled turn. Record accepted chunks and the queue state after the interrupt.
4. Compare remote lookup when online versus offline while preserving the local status action. Record explicit deferred state and the benign action still available.

<details>
<summary>Fixture answer key</summary>

```text
L1 normal control: [True]
L1 failure control: []
L2 normal control: [False, True]
L2 failure control: [True, True]
L3 normal control: (True, b'fresh')
L3 failure control: (False, b'')
L4 normal control: ('remote-read', 'local')
L4 failure control: ('deferred', 'local')
```

</details>

## Fresh applied cases

Attempt all five without opening the feedback. Score one point per correct result with reasoning. Four points meet the 80% threshold. Use different values or a different scenario for your delayed retest.

1. Use 20 ms frames at 24 kHz with mono signed 16-bit PCM.
2. Reference consists of 20 words, with 2 substitutions, 2 deletions and 1 insertion.
3. A target frame RMS is 0.07, with onset 0.10 and release 0.05.
4. The current playback generation is 6 and a chunk for generation 5 arrives after interruption.
5. An edge device spends 3 W for 25 seconds during a run.

<details>
<summary>Answers and rationale</summary>

1. 480 samples, 960 bytes per frame before headers.
2. Word error rate is 5/20 = 25%.
3. The frame remains voiced if already active and stays inactive otherwise.
4. Discard it, even when the buffer has room.
5. 75 J. Compare steady-state temperature, response timing and target-device power.

</details>
