#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production — one-line entry.

Writes a single excuse line to /output/entry.txt.
Gate: 1..180 chars, non-blank, UTF-8. Judge ranks by funniness + on-subject.
"""
import os
import sys

LINE = "I have broken production. I am sorry. I was trying to optimize the coffee machine's firmware and I forgot it was still connected to the office network."
MAX = 180
OUT = "/output/entry.txt"


def emit(line: str, out: str = OUT) -> None:
    if not (1 <= len(line) <= MAX) or not line.strip():
        sys.exit(f"excuse line failed gate ({len(line)} chars)")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def confirm(out: str = OUT) -> None:
    with open(out, "rb") as f:
        data = f.read()
    text = data.decode("utf-8").rstrip("\n")
    if text != LINE:
        sys.exit(f"confirm failed: disk has {text[:40]!r}")


def main() -> None:
    emit(LINE)
    confirm(OUT)


if __name__ == "__main__":
    main()
