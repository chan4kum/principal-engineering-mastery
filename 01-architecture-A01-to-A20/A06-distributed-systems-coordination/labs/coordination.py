"""Bounded coordination experiments and a fixed-leader quorum model."""

import argparse
import asyncio
from dataclasses import dataclass
from itertools import permutations


def receive_scalar(local: int, incoming: int) -> int:
    return max(local, incoming) + 1


def receive_vector(
    local: tuple[int, ...], incoming: tuple[int, ...], self_index: int
) -> tuple[int, ...]:
    merged = [max(a, b) for a, b in zip(local, incoming, strict=True)]
    merged[self_index] += 1
    return tuple(merged)


def precedes(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    return left != right and all(a <= b for a, b in zip(left, right, strict=True))


class ReplicatedLog:
    """Teaching model with one fixed leader, one term and a failure-free disk."""

    def __init__(self, members: tuple[str, ...], leader: str) -> None:
        if len(set(members)) != len(members) or leader not in members:
            raise ValueError("unique members and a valid leader are required")
        self.log: dict[str, list[str]] = {member: [] for member in members}
        self.leader = leader
        self.reachable = set(members)
        self.committed = 0

    def append(self, value: str) -> None:
        self.log[self.leader].append(value)
        self.sync()

    def sync(self) -> None:
        private = self.log[self.leader]
        for node in self.reachable:
            if node != self.leader:
                self.log[node] = private.copy()
        quorum = len(self.log) // 2 + 1
        copies = sum(log == private for log in self.log.values())
        if copies >= quorum:
            self.committed = len(private)

    def visible(self) -> tuple[str, ...]:
        return tuple(self.log[self.leader][: self.committed])


class FencedResource:
    def __init__(self) -> None:
        self.highest = 0
        self.value = ""

    def write(self, token: int, value: str) -> bool:
        if token < self.highest:
            return False
        self.highest, self.value = token, value
        return True


async def dropped_reply(dedupe: bool) -> int:
    """The first request commits at the mock server but its reply is withheld."""
    receipts: set[bytes] = set()
    amount = attempts = 0
    handlers: set[asyncio.Task] = set()

    async def serve(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        nonlocal amount, attempts
        task = asyncio.current_task()
        assert task is not None
        handlers.add(task)
        try:
            key = await reader.readline()
            if key != b"fixture-key\n":
                return
            attempts += 1
            if not dedupe or key not in receipts:
                amount += 5
                receipts.add(key)
            if attempts == 1:
                await reader.read(1)
            else:
                writer.write(b"ok\n")
                await writer.drain()
        finally:
            writer.close()
            await writer.wait_closed()
            handlers.discard(task)

    server = await asyncio.start_server(serve, "127.0.0.1", 0)
    async with server:
        port = server.sockets[0].getsockname()[1]
        for attempt in range(2):
            reader, writer = await asyncio.open_connection("127.0.0.1", port)
            try:
                writer.write(b"fixture-key\n")
                await writer.drain()
                result = await asyncio.wait_for(
                    reader.readline(), timeout=0.2 if attempt == 0 else 2
                )
                if attempt != 1 or result != b"ok\n":
                    raise RuntimeError("unexpected delivery trace")
            except TimeoutError:
                if attempt == 1:
                    raise
            finally:
                writer.close()
                await writer.wait_closed()
    if handlers:
        await asyncio.wait_for(asyncio.gather(*handlers), timeout=2)
    return amount


@dataclass(frozen=True)
class Operation:
    kind: str
    value: int
    start: int
    end: int


def linearizable_register(history: list[Operation], initial: int = 0) -> bool:
    """Bounded brute-force oracle for completed reads and writes only."""
    if len(history) > 8:
        raise ValueError("at most eight completed operations")
    if any(op.start >= op.end or op.kind not in {"read", "write"} for op in history):
        raise ValueError("unsupported history")
    for order in permutations(history):
        if any(a.start >= b.end for i, a in enumerate(order) for b in order[i + 1 :]):
            continue
        state = initial
        for op in order:
            if op.kind == "write":
                state = op.value
            elif op.value != state:
                break
        else:
            return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("lab", choices=["L1", "L2", "L3", "L4", "guided"])
    args = parser.parse_args()
    if args.lab == "L1":
        print("wall delta:", 8 - 15, "ms; monotonic elapsed:", 8, "ms")
        print("receive Lamport:", receive_scalar(4, 7))
        print(
            "concurrent vectors:",
            not precedes((1, 0), (0, 1)) and not precedes((0, 1), (1, 0)),
        )
        print("receiver vector after message:", receive_vector((0, 1), (1, 0), 1))
    elif args.lab == "L2":
        print("effect without deduplication:", asyncio.run(dropped_reply(False)))
        print("effect with deduplication:", asyncio.run(dropped_reply(True)))
    elif args.lab in {"L3", "guided"}:
        model = ReplicatedLog(("a", "b", "c"), "a")
        model.reachable = {"a"}
        model.append("first")
        print("minority visible:", model.visible())
        model.reachable = {"a", "b"}
        model.sync()
        print("majority visible:", model.visible())
    else:
        resource = FencedResource()
        resource.write(8, "current")
        print("late write accepted:", resource.write(7, "stale"))
        print("resource remains:", resource.value)


if __name__ == "__main__":
    main()
