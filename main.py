#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry.

The word is "expired": the word an ex would use to describe you once
the relationship has passed its date. It is one word, seven letters,
no trailing newline, and it lands on its own — shelf life, over, done.

The bounty gate wants /output/entry.txt to hold UTF-8 text of 1 to 24
characters, not only whitespace. The word is validated against that
window first, then written out with a plain open and an explicit mode
so the grader can read it.
"""

import os

WORD = "expired"
OUT_PATH = "/output/entry.txt"
MAX_LEN = 24


def validate(word):
    if not 1 <= len(word) <= MAX_LEN:
        raise ValueError("entry must be 1-24 characters long")
    if word != word.strip():
        raise ValueError("entry must not carry surrounding whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word")
    if not word.isalpha() or word != word.lower():
        raise ValueError("entry must be a single lowercase word")


def write_entry():
    validate(WORD)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(WORD)
    os.chmod(OUT_PATH, 0o644)
    with open(OUT_PATH, "r", encoding="utf-8") as fh:
        back = fh.read()
    if back != WORD:
        raise ValueError("read-back mismatch: entry did not round-trip")


if __name__ == "__main__":
    write_entry()
