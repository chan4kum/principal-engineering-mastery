"""Run four numerical transformer exercises on CPU."""

import argparse
import sys
import time
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "projects/guided"))
from tiny import attend, generate, kv_bytes, train

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("lab", choices=["L1", "L2", "L3", "L4"])
    parser.add_argument("--break", dest="broken", action="store_true")
    args = parser.parse_args()
    torch.set_num_threads(1)
    if args.lab == "L1":
        query = torch.tensor([[[0.0, 0.0], [2.0, 2.0]]])
        key = torch.tensor([[[1.0, 1.0], [0.0, 0.0]]])
        values = torch.tensor([[[2.0], [6.0]]])
        print("QKᵀ:", (query @ key.transpose(-2, -1)).tolist())
        print(
            "attention:",
            attend(query, key, values, scale=not args.broken).flatten().tolist(),
        )
    elif args.lab == "L2":
        model, losses = train()
        left = model(torch.tensor([[0, 1, 2]]), causal=not args.broken)
        right = model(torch.tensor([[0, 1, 3]]), causal=not args.broken)
        print("loss:", (losses[0], losses[-1]))
        print(
            "earlier position changed:", not torch.allclose(left[:, :2], right[:, :2])
        )
        print("predictions:", generate(model, [0, 1], 4))
    elif args.lab == "L3":
        used = kv_bytes(1, 4, 2, 16, 128 if args.broken else 64, 2)
        print("raw KV bytes:", used, "fits 48 KiB:", used <= 48 * 1024)
    else:
        model, _ = train()
        for prompt in ([0, 1], [0, 1] * 6):
            for t in (0.0, 0.7, 1.8):
                start = time.perf_counter()
                result = generate(
                    model,
                    prompt,
                    4,
                    temperature=t,
                    slot_delay=0.003 if args.broken else 0.0,
                )
                elapsed = (time.perf_counter() - start) * 1000
                print(len(prompt), t, result, round(elapsed, 3), "ms")
