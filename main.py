#!/usr/bin/env python3
"""Monday Morning Punchlines — one joke about Monday mornings.

The joke turns the Monday alarm into a courtroom scene: the bed files a
restraining order against Monday, the alarm testifies against its owner,
and the punchline lands on the verdict — awake and guilty. It is about
Monday morning itself, not a generic complaint, and every word works.

Running ``python3 main.py`` writes the single joke to /output/entry.txt
after checking it is 1 to 200 characters long and not only whitespace.
"""

import os

JOKE = (
    "My bed filed a restraining order against Monday, but my alarm "
    "testified for the prosecution — so here I am, awake and guilty."
)


def main() -> None:
    text = JOKE.strip()
    if not text:
        raise SystemExit("entry must not be empty")
    if len(text) > 200:
        raise SystemExit(f"entry is {len(text)} characters, over the 200 limit")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
