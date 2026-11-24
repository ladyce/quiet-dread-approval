#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one single-line code review comment to /output/entry.txt:
a PR approval carrying quiet existential dread, in a flat,
tired-engineer voice. Pure standard library, no network, no
randomness, fully deterministic.
"""

import os

ENTRY = "LGTM. The retry loop now retries forever, which is also my retirement plan. Approved."


def main() -> None:
    # Gate, mirrored locally: 1-140 UTF-8 chars, not whitespace-only,
    # exactly one line. Fail loudly instead of writing an invalid entry.
    assert 1 <= len(ENTRY.encode("utf-8")) <= 140, "entry out of gate range"
    assert ENTRY.strip(), "entry is whitespace-only"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
