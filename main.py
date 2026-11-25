#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

Writes one original line (138 characters) to /output/entry.txt: the
resignation letter of a retry loop that has asked the server 47 times
if it was okay, each time more politely, and never once been asked back.

The written file is byte-identical to the LINE below, with no trailing
newline, so the gate reads exactly 138 characters.
"""

import os
import sys

LINE = (
    "I resign. I asked the server 47 times if it was okay, each time "
    "more politely, and it never once asked me back \u2014 so this is "
    "my last retry."
)


def validate_line(line: str) -> None:
    """Refuse to write anything that is not exactly one line of 1-140 chars."""
    if not line:
        raise ValueError("line is empty")
    if line != line.strip():
        raise ValueError("line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > 140:
        raise ValueError(f"line is {len(line)} characters, over the 140 limit")


def main() -> None:
    validate_line(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
