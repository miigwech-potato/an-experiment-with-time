# Experiments

Five instruments in this repository. Each one uses something a repository can
do that a notebook cannot.

## dreams/ — dated entries in three arms

Write the entry before the day interferes, and let the commit timestamp carry
the date. Or seal it: commit a fingerprint now, publish the text later, and the
match proves the text is unchanged.

Entries run in three arms — human, model and null — under random ids, with the
arm kept out of the repository until scoring is done. Matches are recorded in
`scoring/` as pairings rather than entries, since one entry may meet several
events. See `dreams/README.md` and `scoring/README.md`.

## entropy.log — the arrow of time, as a test that can fail

The log is appended to and never edited. `.github/workflows/append-only.yml`
checks every push: a line that was rewritten or removed turns the run red.
Irreversibility stops being a metaphor.

## loom/ — the Binary Loom

`loom/weft.txt` holds one row of glyphs per commit. `python3 tools/weave.py`
renders the accumulated rows as `loom/cloth.svg`. The commit history is the
cloth, and it changes as the repository grows. Glyphs: 上 下 hõt cōl à 出 米 𝄐,
and a blank row is a rest.

## synchronicities/ — a register with a base rate

One row per coincidence, and beside it how often it could have happened
anyway.

## 11-11/ — the minute the letters go out

The sending practice, kept where it can be counted, with a script that reads
the commit log for it.

## rest.txt

One character: 𝄐, U+1D110. Some readers show it and some show a gap. Whoever
copies this file carries the test with them.
