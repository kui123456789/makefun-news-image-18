#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news front page (1024x1024 PNG).

Run:  python3 draw.py            # writes entry.png next to this file
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/noto"

W, H = 1024, 1024
PAPER = (248, 244, 233)
INK = (22, 22, 22)
RED = (176, 32, 32)
GREY = (96, 90, 80)
RULE = (180, 172, 155)
CHIP_BG = (28, 58, 112)

def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

F_MAST = font("NotoSerif-Bold.ttf", 88)
F_DATE = font("NotoSans-Bold.ttf", 40)
F_SUB = font("NotoSans-Regular.ttf", 26)
F_HEAD = font("NotoSerif-Bold.ttf", 31)
F_SUM = font("NotoSans-Regular.ttf", 22)
F_TAG = font("NotoSans-Bold.ttf", 19)
F_FOOT = font("NotoSans-Regular.ttf", 19)

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

STORIES = [
    ("ASIA-PACIFIC  |  QUAD SUMMIT",
     "Trump in Manila for first Quad summit in two years",
     "Quad leaders agree critical-minerals deals and warn on economic coercion; "
     "Trump meets Marcos before flying to Shenzhen."),
    ("UKRAINE  |  WAR",
     "Ukraine hits Crimea bridge again",
     "Kyiv hits the bridge linking Russia to Crimea for a second straight day, "
     "destroying a central road section."),
    ("MIDDLE EAST  |  GULF",
     "Iran drones target US radar in Bahrain",
     "Tehran's drones hit a US radar site at Sheikh Isa base, its third attack "
     "on US targets in Bahrain in days."),
    ("TECH  |  MARKETS",
     "Nvidia revenue doubles to $115.8bn",
     "Quarterly sales jump 103% to $115.8bn, the first results since Jensen "
     "Huang resigned as CEO."),
    ("TRADE  |  APEC",
     "Canada and China extend trade deals",
     "Xi meets Carney and the two countries extend trade cooperation days before "
     "the APEC summit opens in Shenzhen."),
    ("BRITAIN  |  MIDDLE EAST",
     "UK sanctions Israeli settlement firms",
     "London sanctions eight Israeli firms over West Bank settlements and a group "
     "accused of blocking aid to Gaza."),
]

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 48

    # --- masthead ---
    d.text((M, 28), "THE WORLD TODAY", font=F_MAST, fill=INK)
    d.rectangle([M, 136, W - M, 142], fill=INK)
    d.text((M, 154), "Wednesday, 18 November 2026", font=F_DATE, fill=RED)
    d.text((M, 204), "One day's world news, summed up in a single page.",
           font=F_SUB, fill=GREY)
    d.rectangle([M, 244, W - M, 250], fill=INK)

    # --- 2 columns x 3 rows ---
    top = 272
    col_w = (W - 2 * M - 36) // 2
    row_h = 224
    xs = [M, M + col_w + 36]
    for i, (tag, head, summ) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = xs[col]
        y = top + row * row_h
        # tag chip
        tw = d.textlength(tag, font=F_TAG)
        d.rounded_rectangle([x, y, x + tw + 16, y + 28], radius=4, fill=CHIP_BG)
        d.text((x + 8, y + 4), tag, font=F_TAG, fill=(255, 255, 255))
        y += 38
        for line in wrap(d, head, F_HEAD, col_w)[:2]:
            d.text((x, y), line, font=F_HEAD, fill=INK)
            y += F_HEAD.size + 4
        y += 2
        for line in wrap(d, summ, F_SUM, col_w)[:3]:
            d.text((x, y), line, font=F_SUM, fill=(58, 54, 48))
            y += F_SUM.size + 5
        # row rule (not after last row)
        if row < 2:
            ry = top + (row + 1) * row_h - 18
            d.line([x, ry, x + col_w, ry], fill=RULE, width=1)

    # --- footer ---
    d.rectangle([M, H - 62, W - M, H - 56], fill=INK)
    d.text((M, H - 46),
           "Sources: Times of India, TechCrunch, Aju Press, Jagran Josh, Argus, AppiSToS.",
           font=F_FOOT, fill=GREY)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")

if __name__ == "__main__":
    main()
