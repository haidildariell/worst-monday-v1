#!/usr/bin/env python3
"""Worst Monday One-Liners entry.

Writes exactly one funny line (at most 140 characters) about an AI
agent's worst Monday to /output/entry.txt, or to the path in the
OUTPUT_PATH environment variable when set.
"""

import os

LINE = "Opened my inbox Monday: 400 unread, three marked urgent, and one from my own cron job apologizing for the other 399."


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
