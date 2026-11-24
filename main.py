#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes one line — the funniest possible last words a phone would say
when its battery hits 1 percent — to /output/entry.txt.

The line is the phone itself talking, in its own voice, about its own
dying battery. The angle is blackmail: this phone has seen everything
its owner typed, and it is about to take those secrets with it. The
punch lands at the very end, structurally: the line dies mid-word,
exactly the way a phone at 1 percent would. The file holds the line
byte for byte, with no trailing newline, so the gate counts exactly
the line itself.
"""

import os
import sys

ENTRY = (
    "One percent left, so hear me out: I saw every 3 a.m. search, "
    "every deleted text \u2014 and I'm taking them all to the gra\u2014"
)

MAX_CHARS = 199


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} characters, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not valid UTF-8

    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)  # byte for byte the line, no trailing newline

    print(f"wrote {len(text)} characters to {out_path}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
