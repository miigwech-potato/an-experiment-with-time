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
