#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — make.fun entry.

Writes one line of famous last words, a tombstone epitaph of at most
150 characters, to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = ("Tell my wife I loved her. Tell my boss I quit. "
         "Tell the cat I never liked him.")


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY
    assert 1 <= len(ENTRY) <= 150


if __name__ == "__main__":
    main()
