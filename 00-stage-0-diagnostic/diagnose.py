"""Run the Stage 0 quiz with no external services."""

QUESTIONS = (
    (
        "PY · a = [[1]]; b = a.copy(); b[0].append(2). What is a?",
        ("[[1]]", "[[1, 2]]", "[1, 2]", "The append raises TypeError"),
        "b",
        "The copy makes a new outer list. The nested list is still shared.",
    ),
    (
        "OS · Which field in Linux /proc/<pid>/status identifies the current parent?",
        ("Tgid", "PPid", "VmRSS", "Threads"),
        "b",
        "PPid is the parent process ID from the observer's namespace.",
    ),
    (
        "SQL · Values are 10, NULL, 10. What does COUNT(value) return?",
        ("1", "3", "2", "NULL"),
        "c",
        "COUNT(value) skips NULL and counts both equal non-NULL rows.",
    ),
    (
        "NET · A loopback TCP connect fails immediately with connection refused. Most likely?",
        (
            "The SQL query is slow",
            "A DNS cache is stale",
            "TLS cert expired",
            "No listener or an explicit reject",
        ),
        "d",
        "TCP did not establish a connection. Check the destination address and listener first.",
    ),
    (
        "MATH · At 32 MiB/s, how long does 128 MiB take without overhead?",
        ("4 s", "32 s", "0.25 s", "4096 s"),
        "a",
        "Time is bytes divided by bytes per second. The MiB factors cancel.",
    ),
)


def main() -> None:
    correct = 0
    for question, options, answer, explanation in QUESTIONS:
        print(f"\n{question}")
        for label, option in zip("abcd", options, strict=True):
            print(f"  {label}. {option}")
        while True:
            try:
                choice = input("Answer (a/b/c/d or s to skip) ").strip().lower()
            except EOFError:
                print("\nInput ended. Re-run to complete the diagnostic.")
                return
            if choice in {"a", "b", "c", "d", "s"}:
                break
        correct += choice == answer
        print(f"{'Correct' if choice == answer else f'Answer {answer}'}. {explanation}")
    print(
        f"\nBaseline {correct}/{len(QUESTIONS)}. Record gaps and verify them with the local drills."
    )


if __name__ == "__main__":
    main()
