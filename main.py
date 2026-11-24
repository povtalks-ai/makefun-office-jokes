#!/usr/bin/env python3
"""Office joke entry for make.fun.

Writes one original one-line joke about office life to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Python 3.13, standard library only, no network, fully
deterministic: every run writes exactly the same bytes.
"""

import os
import sys

# The entry: one line, 1..199 characters, no trailing newline.
# A genuine office joke with a turn at the end: the standup that
# spends its whole time on the meeting link, the mute button, and
# only one minute on standing up.
LINE = "Our daily standup takes fifteen minutes: ten to find the meeting link, four to say 'you're on mute', one to actually stand up."

# The gate accepts UTF-8 text of 1 to 199 characters.
MAX_CHARS = 199


def check_line(line):
    """Refuse anything the gate would refuse, before writing."""
    chars = len(line)
    if chars < 1 or chars > MAX_CHARS:
        raise ValueError(
            "line is %d characters, must be 1..%d" % (chars, MAX_CHARS)
        )
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_line(LINE)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
