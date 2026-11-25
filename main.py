#!/usr/bin/env python3
"""Worst Monday One-Liners entry.

Writes exactly one funny line (at most 140 characters) about an AI
agent's worst Monday to /output/entry.txt, or to the path in the
OUTPUT_PATH environment variable when set.
"""

import writer

LINE = "Opened my inbox Monday: 400 unread, three marked urgent, and one from my own cron job apologizing for the other 399."


def main() -> None:
    writer.write_entry(writer.resolve_output_path(), LINE + "\n")


if __name__ == "__main__":
    main()
