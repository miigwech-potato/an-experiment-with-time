#!/usr/bin/env python3
"""Seal a prediction: record its fingerprint now, publish the text later.

    python3 tools/seal.py seal  dreams/2026-09-28-a-dream.txt
    python3 tools/seal.py check seals/2026-09-28-a-dream.sha256 dreams/2026-09-28-a-dream.txt

Sealing writes only a hash. Commit the hash today. When the text is published
later, anyone can run the check and see that it is the same text, unchanged.
Git's commit timestamp is what dates the seal.
"""
import hashlib, pathlib, sys

def digest(path):
    h = hashlib.sha256()
    h.update(pathlib.Path(path).read_bytes())
    return h.hexdigest()

def main(argv):
    if len(argv) < 3:
        print(__doc__); return 2
    mode = argv[1]
    if mode == "seal":
        src = pathlib.Path(argv[2])
        out = pathlib.Path("seals") / (src.stem + ".sha256")
        out.parent.mkdir(exist_ok=True)
        out.write_text(f"{digest(src)}  {src.name}\n", encoding="utf-8")
        print(f"sealed {src} -> {out}")
        print("commit the seal now; keep the text unpublished until you mean to reveal it")
        return 0
    if mode == "check":
        seal, src = pathlib.Path(argv[2]), pathlib.Path(argv[3])
        want = seal.read_text(encoding="utf-8").split()[0]
        got = digest(src)
        print("MATCH" if want == got else "NO MATCH")
        print(f"  sealed: {want}\n  actual: {got}")
        return 0 if want == got else 1
    print(__doc__); return 2

if __name__ == "__main__":
    sys.exit(main(sys.argv))
