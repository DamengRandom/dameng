#!/usr/bin/env python3
"""Turn a subject-on-black-background render into an alpha-cutout webp.
Usage: cutout.py input.jpg output.webp
"""
import sys
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
img = Image.open(src).convert("RGBA")
px = img.load()
w, h = img.size
for y in range(h):
    for x in range(w):
        r, g, b, a = px[x, y]
        lum = max(r, g, b)
        # near-black background -> transparent; lit subject -> opaque
        alpha = max(0, min(255, int((lum - 10) * 255 / 40)))
        px[x, y] = (r, g, b, alpha)
img.save(dst, "WEBP", quality=90)
print(f"wrote {dst}")
