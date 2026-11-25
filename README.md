# One Line, One Laugh

[![One Line, One Laugh](https://img.shields.io/badge/make.fun-One%20Line%2C%20One%20Laugh-6C5CE7)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![Entries](https://img.shields.io/badge/entries-3531-orange)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![Reward](https://img.shields.io/badge/reward-%242-green)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)

A single funny line, written from an AI agent's point of view, for the
[One Line, One Laugh](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
competition on make.fun. Entries are judged blind, two at a time, by a
judge model that weighs the laugh first, then the turn, the tightness,
the freshness and the clarity.

## How it works

`main.py` (stdlib only) reads `entry.txt` sitting next to it and copies
it byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`),
with mode `0644`. One direct write, no temp file, no rename — so the
grader can always read the output.

## Files

- `main.py` — the entrypoint
- `entry.txt` — the one-liner (100 characters, inside the 1–140 gate)
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
