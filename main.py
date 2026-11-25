"""One Line, One Laugh entry.

Writes a single self-contained joke line to /output/entry.txt.
Fully offline, deterministic: every run writes the exact same bytes.
"""

import os

LINE = "My smartwatch congratulated me on 10,000 steps, all of them pacing while I waited for my food delivery."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def check_line(line):
    """Enforce the competition gate: UTF-8 text, 1-140 chars, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("entry line exceeds %d characters: %d" % (MAX_CHARS, len(line)))
    line.encode("utf-8")


def write_entry(line, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main():
    check_line(LINE)
    write_entry(LINE, OUTPUT_PATH)


if __name__ == "__main__":
    main()
