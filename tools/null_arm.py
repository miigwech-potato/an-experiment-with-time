#!/usr/bin/env python3
"""Write a null entry: text from a process nobody claims is a channel.

    python3 tools/null_arm.py <entry-file>

Sentences are built from the frames in pool/frames.txt and the words in
pool/nouns, verbs and adjectives, so a null entry reads like an entry rather
than like word salad. If the arms can be told apart by texture, blind scoring
is not blind, and the null arm tells you nothing.

The seed is written into the file, so the text can be reproduced and audited.
"""
import pathlib, random, secrets, sys

def load(name):
    return [w for w in pathlib.Path(f"pool/{name}.txt").read_text(encoding="utf-8").split() if w]

def build(rng, frames, nouns, verbs, adjs, count):
    out = []
    for _ in range(count):
        f = rng.choice(frames)
        s = ""
        for ch in f.split("{"):
            if ch.startswith("n}"):
                s += rng.choice(nouns) + ch[2:]
            elif ch.startswith("v}"):
                s += rng.choice(verbs) + ch[2:]
            elif ch.startswith("a}"):
                s += rng.choice(adjs) + ch[2:]
            else:
                s += ch
        out.append(s)
    return out

def main(argv):
    if len(argv) != 2:
        print(__doc__); return 2
    target = pathlib.Path(argv[1])
    frames = [l for l in pathlib.Path("pool/frames.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
    nouns, verbs, adjs = load("words"), load("verbs"), load("adjectives")
    if min(len(nouns), len(verbs), len(adjs)) < 10 or len(frames) < 4:
        print("the pools are too small"); return 1
    seed = secrets.token_hex(4)
    rng = random.Random(seed)
    text = target.read_text(encoding="utf-8") if target.exists() else ""
    body = " ".join(build(rng, frames, nouns, verbs, adjs, rng.randint(3, 6)))
    gradient = " ".join(build(rng, frames, nouns, verbs, adjs, 1))
    out = text.replace("WHAT I REMEMBER:\n", f"WHAT I REMEMBER:\n{body}\n")
    out = out.replace("in reach:\n", f"in reach:\n{gradient}\n")
    out += f"SEED: {seed}\n"
    target.write_text(out, encoding="utf-8")
    print(f"null entry written to {target} (seed {seed})")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
