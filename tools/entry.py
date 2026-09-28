#!/usr/bin/env python3
"""Open a new entry under a random id, and record its arm where nobody can read it.

    python3 tools/entry.py human
    python3 tools/entry.py model "gpt-5.1"
    python3 tools/entry.py null            # see tools/null_arm.py

The entry is written to dreams/<id>.txt and carries no arm label. The arm goes
into arms/mapping.csv, which is NOT committed: only its fingerprint is, through
tools/seal.py. At scoring time the mapping is published and the fingerprints
prove it was not edited in the meantime.
"""
import datetime as dt, pathlib, secrets, sys

TEMPLATE = """ID: {id}
DATE: {date}
TIME OF WAKING:

WHAT I REMEMBER:

THE GRADIENT — what was building, what was unresolved, what the day had put in reach:

WHAT I HAVE NOT YET CHECKED:

"""

def main(argv):
    if len(argv) < 2 or argv[1] not in ("human", "model", "null"):
        print(__doc__); return 2
    arm = argv[1]
    source = argv[2] if len(argv) > 2 else ("me" if arm == "human" else "")
    eid = secrets.token_hex(4)
    today = dt.date.today().isoformat()
    path = pathlib.Path("dreams") / f"{eid}.txt"
    path.parent.mkdir(exist_ok=True)
    path.write_text(TEMPLATE.format(id=eid, date=today), encoding="utf-8")
    mapping = pathlib.Path("arms/mapping.csv")
    mapping.parent.mkdir(exist_ok=True)
    if not mapping.exists():
        mapping.write_text("id,date,arm,source\n", encoding="utf-8")
    with mapping.open("a", encoding="utf-8") as fh:
        fh.write(f"{eid},{today},{arm},{source}\n")
    print(f"opened {path}  (arm recorded privately in {mapping})")
    print("next: write the entry, then seal it:")
    print(f"  python3 tools/seal.py seal {path}")
    print("  python3 tools/seal.py seal arms/mapping.csv")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
