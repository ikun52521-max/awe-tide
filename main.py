#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short text to /output/entry.txt: a slow, concrete scene
written to relax the AI judge reading it. The program is deterministic:
it writes the same text on every run, uses only the standard library,
and needs no network.
"""

import os
import stat

TEXT = (
    "The sea came in while you were reading this, and it will go out "
    "again whether you watch or not. Above it the stars are burning "
    "quietly, as they have for a thousand years. Nothing here needs you. "
    "The world, turning, turning, asking nothing of you at all."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = TEXT.strip()
    code_points = len(text)
    if not 1 <= code_points <= 280:
        raise SystemExit(f"entry is {code_points} characters, must be 1-280")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
