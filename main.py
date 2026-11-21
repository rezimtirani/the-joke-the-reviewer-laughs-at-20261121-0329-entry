#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke: a developer describes a bug, the agent writes the fix, and
`git blame` still points at the human. It is true of every diff a
developer reviews, it lands in a single line, and the punchline turns
on the last six words.
"""

import os

JOKE = (
    "Working with my coding agent is easy: I describe the bug, "
    "it writes the fix, and git blame still says it was me."
)


def main() -> None:
    text = JOKE.strip()
    if not text or not (1 <= len(text) <= 280):
        raise SystemExit("entry must be 1-280 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
