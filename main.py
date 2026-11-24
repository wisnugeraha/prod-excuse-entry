#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production — one-line entry.

Writes a single excuse line to /output/entry.txt.
Gate: 1..180 chars, non-blank, UTF-8. Judge ranks by funniness + on-subject.
"""
import os
import sys

LINE = "I have broken production. I am sorry. I was trying to optimize the coffee machine's firmware and I forgot it was still connected to the office network."
MAX = 180


def emit(line: str, out: str = "/output/entry.txt") -> None:
    if not (1 <= len(line) <= MAX) or not line.strip():
        sys.exit(f"excuse line failed gate ({len(line)} chars)")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def main() -> None:
    emit(LINE)


if __name__ == "__main__":
    main()
