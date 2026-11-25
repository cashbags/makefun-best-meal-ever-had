"""Best meal entry: write one sentence about the best meal ever had.

The program is deliberately trivial: the sentence is a fixed string, written
to /output/entry.txt with no trailing newline, so every run produces the exact
same 155 bytes. No input is read, no network is used, no randomness, no clock.
"""

import os

ENTRY = (
    "On a plastic stool in Yogyakarta I ate pecel lele with my hands, "
    "sambal stinging my lips, and the catfish crackled so loud the "
    "vendor laughed before I did."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
