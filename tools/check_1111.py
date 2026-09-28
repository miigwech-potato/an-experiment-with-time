#!/usr/bin/env python3
"""Count the commits that landed at 11:11 — morning or night — in local time.

    git log --pretty=format:'%h %ad %s' --date=format-local:'%Y-%m-%d %H:%M' | python3 tools/check_1111.py

Reads the log on standard input so it needs nothing installed and can be run
against any repository.
"""
import re, sys

PATTERN = re.compile(r"^(\S+)\s+(\d{4}-\d{2}-\d{2})\s+(\d{2}):(\d{2})\s*(.*)$")

def main():
    hits, total = [], 0
    for line in sys.stdin:
        m = PATTERN.match(line.strip())
        if not m:
            continue
        total += 1
        sha, day, hh, mm, subject = m.groups()
        if (hh, mm) in (("11", "11"), ("23", "11")):
            hits.append((sha, day, f"{hh}:{mm}", subject))
    for sha, day, clock, subject in hits:
        print(f"{clock}  {day}  {sha}  {subject}")
    print(f"\n{len(hits)} of {total} commits at 11:11")
    if total:
        print(f"expected by chance at 1 in 720 per commit: {total/720:.2f}")

if __name__ == "__main__":
    main()
