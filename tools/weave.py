#!/usr/bin/env python3
"""Render loom/weft.txt as cloth: one committed row becomes one woven row.

    python3 tools/weave.py            # writes loom/cloth.svg

Each line of weft.txt is a row of glyphs. Blank lines are rests and weave as
gaps. The file grows by one row per commit, so the cloth is the history.
"""
import pathlib

COLOURS = {
    "上": "#b4623a", "下": "#4a5d6b", "hõt": "#c8742f", "cōl": "#5d7f92",
    "à": "#7d6b4f", "出": "#8a5a72", "米": "#6b7f52", "𝄐": "#f0ece2",
}
CELL, GAP = 28, 2

def rows():
    text = pathlib.Path("loom/weft.txt").read_text(encoding="utf-8")
    out = []
    for line in text.splitlines():
        if line.startswith("#"):
            continue
        out.append(line.split())
    return out

def main():
    data = rows()
    width = max((len(r) for r in data), default=1) * (CELL + GAP) + GAP
    height = max(len(data), 1) * (CELL + GAP) + GAP
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             f'viewBox="0 0 {width} {height}" role="img" aria-label="woven record">',
             f'<rect width="{width}" height="{height}" fill="#1b1b19"/>']
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            fill = COLOURS.get(cell, "#3a3d42")
            px, py = GAP + x * (CELL + GAP), GAP + y * (CELL + GAP)
            parts.append(f'<rect x="{px}" y="{py}" width="{CELL}" height="{CELL}" fill="{fill}"/>')
    parts.append("</svg>")
    pathlib.Path("loom/cloth.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"woven {len(data)} row(s) -> loom/cloth.svg")

if __name__ == "__main__":
    main()
