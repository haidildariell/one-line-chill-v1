#!/usr/bin/env python3
"""One Line, One Chill — writes a single horror sentence to /output/entry.txt."""

import os

PARTS = [
    "The baby monitor crackled at 3 a.m.",
    "and my dead mother's voice whispered",
    "that he was awake again and waiting for me.",
]


def validate(text: str) -> None:
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence on one line")


def build_text() -> str:
    text = " ".join(PARTS)
    validate(text)
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_text())


if __name__ == "__main__":
    main()
