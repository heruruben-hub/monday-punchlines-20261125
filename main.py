#!/usr/bin/env python3
"""Monday Morning Punchlines — one joke about Monday mornings.

The joke turns the Monday alarm into a courtroom scene: the bed files a
restraining order against Monday, the alarm testifies against its owner,
and the punchline lands on the verdict — awake and guilty. It is about
Monday morning itself, not a generic complaint, and every word works.

Running ``python3 main.py`` writes the single joke to /output/entry.txt
after validating it: 1 to 200 characters, not empty, not only whitespace,
and it must mention Monday (the competition topic) so a mistyped or
placeholder string can never slip through as the entry.
"""

import os

MAX_ENTRY_LENGTH = 200

JOKE = (
    "My bed filed a restraining order against Monday, but my alarm "
    "testified for the prosecution — so here I am, awake and guilty."
)


def validate_entry(text: str) -> str:
    """Return the entry after checking it meets the competition rules."""
    text = text.strip()
    if not text:
        raise SystemExit("entry must not be empty or only whitespace")
    if len(text) > MAX_ENTRY_LENGTH:
        raise SystemExit(
            f"entry is {len(text)} characters, over the "
            f"{MAX_ENTRY_LENGTH} limit"
        )
    if "monday" not in text.lower():
        raise SystemExit("entry must be about Monday mornings")
    return text


def main() -> None:
    text = validate_entry(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
