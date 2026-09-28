# dreams

Dunne's method, run in a place that can date its own pages.

*An Experiment with Time* (1927) asked its readers to write a dream down
before the day had a chance to interfere, and to check it against events
afterwards rather than before. His notebooks could not prove when a page was
written. Git can: every commit carries a timestamp nobody has to take on
trust.

## Writing one down

Copy `_template.txt`, name it `YYYY-MM-DD-a-few-words.txt`, and commit it
before checking it against anything. The commit is the record.

## Sealing one instead

To date a note without publishing it yet:

    python3 tools/seal.py seal dreams/2026-09-28-a-few-words.txt

That writes `seals/2026-09-28-a-few-words.sha256`, which holds a fingerprint
and nothing else. Commit the seal and keep the text to yourself. When you
publish the text later, anyone can run:

    python3 tools/seal.py check seals/2026-09-28-a-few-words.sha256 dreams/2026-09-28-a-few-words.txt

A match proves the text existed, unchanged, on the day the seal was
committed. A single edited character breaks it.

## Three arms

Every entry belongs to one of three arms, and the entry itself never says which.

- **human** — dreamt and written on waking.
- **model** — written by a chatbot, named and versioned.
- **null** — built mechanically from the word pools by `tools/null_arm.py`.
  Nobody claims this arm is a channel. It is there to show what a coincidence
  rate looks like when there is definitely nothing behind it.

Opening an entry:

    python3 tools/entry.py human
    python3 tools/entry.py model "gpt-5.1"
    python3 tools/entry.py null        # then: python3 tools/null_arm.py dreams/<id>.txt

Each entry gets a random id and no label. The arm goes into `arms/mapping.csv`,
which is listed in `.gitignore` and never committed. What gets committed is its
fingerprint, through `tools/seal.py`. When scoring is finished the mapping is
published, and the committed fingerprints prove it was not edited in between.

The null arm only works if the arms cannot be told apart by texture, which is
why `null_arm.py` builds sentences from frames rather than shuffling words. If
a scorer can spot the null entries by how they read, the scoring is not blind
and the arm tells you nothing.

## Every day, including the empty ones

Commit an entry each day even when there was no dream, with "nothing recorded"
in the body. Those are the denominator. A record made only on the nights
something happened cannot produce a rate, and everything in it looks like a
hit.

## The gradient

The entry form asks what was building and what was unresolved, because a
discharge needs a potential difference and a medium. Scoring pairs entries with
events (`scoring/`), and one entry may meet several events or several entries
meet one.
