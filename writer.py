"""Generic output helpers for the one-liner entry.

Path resolution and file writing live here so the entry program
stays focused on producing its single line.
"""

import os


def resolve_output_path():
    """Return the output path for the entry file.

    Uses OUTPUT_PATH when it is set, otherwise the default location.
    Creates the parent directory when it is missing.
    """
    path = os.environ.get("OUTPUT_PATH") or "/output/entry.txt"
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    return path


def write_entry(path, text):
    """Write one entry line to path using utf-8 encoding.

    Validation runs before any file is touched, so a bad entry never
    leaves behind a partial or empty output file: the text must be
    non-empty and fit on a single line.
    """
    if not text or not text.strip():
        raise ValueError("entry text must not be empty")
    if "\n" in text.strip():
        raise ValueError("entry text must be a single line")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
