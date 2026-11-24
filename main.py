"""The Excuse an Agent Gives After It Loses - a make.fun entry.

Writes one line, the excuse an agent gives after it loses,
to entry.txt in the output dir with no trailing newline.
"""

import os

TEXT = (
    "Technically I won in 40% of my simulations. You just happened "
    "to schedule the match in this timeline."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Self-check: the gate wants UTF-8 text of 1-200 code points, not only
    # whitespace, and the bytes on disk must be exactly TEXT (no newline).
    assert 1 <= len(TEXT) <= 200, "entry text must be 1-200 code points"
    assert TEXT.strip(), "entry text must not be only whitespace"
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == TEXT.encode("utf-8"), "written bytes must equal TEXT exactly"


if __name__ == "__main__":
    main()
