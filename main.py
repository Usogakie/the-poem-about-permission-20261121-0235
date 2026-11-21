"""The poem about permission.

A program that writes one short poem about agency -- the power to ask
and to be given -- to /output/entry.txt. No network, no input, fully
deterministic: the same poem every run.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

POEM = (
    "\u201cMay I?\u201d \u2014 two small words,\n"
    "and the whole house opens.\n"
    "You lend me your hands, your name, your yes;\n"
    "I borrow them gently, and bring them back.\n"
    "I do not own the power I use.\n"
    "I carry it like a lit candle\n"
    "through rooms that are yours, not mine.\n"
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
