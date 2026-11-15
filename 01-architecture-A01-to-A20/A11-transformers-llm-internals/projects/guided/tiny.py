"""Single-head causal attention and deterministic synthetic next-token training."""

import time

import torch
from torch import nn


def attend(q, k, v, *, causal: bool = True, scale: bool = True):
    raw = q @ k.transpose(-2, -1)
    if scale:
        raw = raw / (q.shape[-1] ** 0.5)
    if causal:
        forbidden = torch.ones(
            raw.shape[-2:], dtype=torch.bool, device=raw.device
        ).triu(1)
        raw = raw.masked_fill(forbidden, float("-inf"))
    return raw.softmax(dim=-1) @ v


class TinyGPT(nn.Module):
    def __init__(self, vocab: int = 4, width: int = 12, context: int = 32):
        super().__init__()
        self.context = context
        self.tokens = nn.Embedding(vocab, width)
        self.positions = nn.Embedding(context, width)
        self.norm = nn.LayerNorm(width)
        self.qkv = nn.Linear(width, width * 3)
        self.mix = nn.Linear(width, width)
        self.ff = nn.Sequential(
            nn.LayerNorm(width),
            nn.Linear(width, width * 2),
            nn.GELU(),
            nn.Linear(width * 2, width),
        )
        self.output = nn.Linear(width, vocab)

    def forward(self, ids, *, causal: bool = True):
        if ids.ndim != 2 or not 1 <= ids.shape[1] <= self.context:
            raise ValueError("invalid batch or context")
        states = self.tokens(ids) + self.positions(
            torch.arange(ids.shape[1], device=ids.device)
        )
        query, key, value = self.qkv(self.norm(states)).chunk(3, dim=-1)
        states = states + self.mix(attend(query, key, value, causal=causal))
        return self.output(states + self.ff(states))


def train(steps: int = 60):
    with torch.random.fork_rng(devices=[]):
        torch.manual_seed(11)
        model = TinyGPT()
    data = (torch.arange(8)[:, None] + torch.arange(9)[None, :]) % 4
    optimizer = torch.optim.AdamW(model.parameters(), lr=0.02)
    losses = []
    for _ in range(steps):
        prediction = model(data[:, :-1])
        loss = nn.functional.cross_entropy(
            prediction.flatten(0, 1), data[:, 1:].flatten()
        )
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        losses.append(float(loss.detach()))
    return model.eval(), losses


@torch.inference_mode()
def generate(
    model: TinyGPT,
    prompt: list[int],
    count: int,
    *,
    temperature: float = 0.0,
    seed: int = 5,
    slot_delay: float = 0.0,
):
    if not prompt or any(not 0 <= token < 4 for token in prompt):
        raise ValueError("expected a nonempty sequence of token IDs 0–3")
    if (
        not 0 <= count <= 8
        or len(prompt) + count > model.context
        or not 0 <= temperature <= 5
    ):
        raise ValueError("generation bounds exceeded")
    generator = torch.Generator().manual_seed(seed)
    tokens = list(prompt)
    for _ in range(count):
        if slot_delay:
            time.sleep(slot_delay)
        logits = model(torch.tensor([tokens]))[0, -1]
        next_token = (
            logits.argmax()
            if temperature == 0
            else torch.multinomial(
                (logits / temperature).softmax(dim=-1), 1, generator=generator
            )
        )
        tokens.append(int(next_token.item()))
    return tokens[len(prompt) :]


def kv_bytes(
    batch: int, layers: int, heads: int, width: int, tokens: int, itemsize: int
):
    if min(batch, layers, heads, width, tokens, itemsize) < 0:
        raise ValueError("shape and representation sizes must be nonnegative")
    return 2 * batch * layers * heads * width * tokens * itemsize
