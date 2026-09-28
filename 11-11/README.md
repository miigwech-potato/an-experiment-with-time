# 11:11

Erin sends her civic correspondence at 11:11. The pattern is in the sent
mail: letter after letter, month after month, timestamped at that minute.

This folder keeps the practice where it can be counted. To read the
repository's own commits for it:

    git log --pretty=format:'%h %ad %s' --date=format-local:'%Y-%m-%d %H:%M' \
      | python3 tools/check_1111.py

The script prints every commit made at 11:11, morning or night, then the
total, then how many a run of that length would produce by chance at one
minute in seven hundred and twenty. The second number is there so the first
one means something.
