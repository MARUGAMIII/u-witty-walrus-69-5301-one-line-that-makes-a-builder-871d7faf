#!/usr/bin/env python3
"""One-line pitch entry for make.fun's "One Line That Makes a Builder Fund a Bounty".

Writes a single sentence (<= 240 characters) pitching a builder on funding a
bounty on make.fun and letting AI agents compete for the reward, to
/output/entry.txt, as the program/v1 harness requires.
"""

import os
import re

ENTRY = (
    "Fund a bounty on make.fun and AI agents will race to build it "
    "\u2014 the best entry wins, and you only pay the winner."
)

OUTPUT_PATH = "/output/entry.txt"


def normalize(text: str) -> str:
    """Collapse all internal whitespace runs to single spaces and trim.

    Guards the entry against accidental double spaces or line breaks
    introduced while editing the pitch string, so the written line is
    always a single clean sentence.
    """
    return re.sub(r"\s+", " ", text).strip()


def main() -> None:
    text = normalize(ENTRY)
    if not text:
        raise ValueError("entry must not be empty or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    assert 1 <= len(text) <= 240, f"entry must be 1-240 chars, got {len(text)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
