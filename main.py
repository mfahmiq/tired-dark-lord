#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the monologue to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The text is embedded here verbatim so the entry is fully self-contained:
no network, no files read, no secrets.
"""

import os

ENTRY = (
    "Oh. You're here. The hero. Yes, the prophecy, the sword, all of it. "
    "Sit down. No, not there. That's where the cat sleeps. "
    "Look, I conquered three kingdoms, toppled the Sun Court, "
    "drowned a fleet in a teacup, and nobody tells you the truth "
    "about ruling the dark: the forms. "
    "Every soul I reap needs a signature in triplicate. "
    "My ravens unionized. The dungeon's damp again. "
    "So take the crown. Take the tower, the cursed amulet, "
    "the whole rotting empire. Promise me one thing. "
    "When the bards sing of how you slew the Dark Lord... "
    "let me sleep through it.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
