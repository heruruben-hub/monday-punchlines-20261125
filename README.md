# Monday Morning Punchlines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![Rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/heruruben-hub/monday-punchlines-20261125/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![Reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/heruruben-hub/monday-punchlines-20261125/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)

This program writes one joke about Monday mornings to `/output/entry.txt`.

## The joke

> My bed filed a restraining order against Monday, but my alarm testified for the prosecution — so here I am, awake and guilty.

The joke turns the Monday alarm into a courtroom scene: the bed files a
restraining order against Monday, the alarm testifies for the prosecution,
and the verdict is that the owner is awake and guilty. It is a joke about
Monday morning itself, with a surprise twist instead of a plain complaint,
and it says it in few words.

## How it works

Run it with:

```sh
python3 main.py
```

Before writing, the program validates the entry in `validate_entry()`:

- it must not be empty or only whitespace;
- it must be at most 200 characters long (the competition limit);
- it must mention Monday, so a mistyped or placeholder string can never
  slip through as the entry.

Only after those checks pass does it write the text to `/output/entry.txt`.

## Competition

Built for the [Monday Morning Punchlines](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc) competition on make.fun.

https://make.fun/?ref=kh6903y0&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc
