#!/usr/bin/env python3
"""Fail if a line already written to a log has been changed or removed.

    python3 tools/check_append_only.py entropy.log <old-version-file>

In CI the old version comes from the previous commit:
    git show HEAD^:entropy.log > /tmp/old && python3 tools/check_append_only.py entropy.log /tmp/old

The arrow of time, as a test that can go red.
"""
import pathlib, sys

def main(argv):
    if len(argv) != 3:
        print(__doc__); return 2
    new = pathlib.Path(argv[1]).read_text(encoding="utf-8").splitlines()
    old = pathlib.Path(argv[2]).read_text(encoding="utf-8").splitlines()
    if len(new) < len(old):
        print(f"REVERSED: log lost {len(old) - len(new)} line(s)"); return 1
    for i, (a, b) in enumerate(zip(old, new), start=1):
        if a != b:
            print(f"REWRITTEN: line {i} changed")
            print(f"  was: {a}\n  now: {b}")
            return 1
    added = len(new) - len(old)
    print(f"APPEND-ONLY: {added} line(s) added, {len(old)} unchanged")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
