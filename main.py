#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production — one-line entry.

Writes a single excuse line (<= 180 chars, UTF-8, non-blank) to
/output/entry.txt. The judge picks the funnier, more on-subject line.
"""
import os

LINE = "I have broken production. I am sorry. I was trying to optimize the coffee machine's firmware and I forgot it was still connected to the office network."


def main() -> None:
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    assert 1 <= len(LINE) <= 180, "excuse line out of range"
    assert LINE.strip() == LINE, "line must be non-blank"
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
