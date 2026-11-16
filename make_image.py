#!/usr/bin/env python3
"""Build entry.png for the ai-excited-01 entry.

Deterministic: opens the user-picked source artwork (a WEBP of a giant
fluffy Samoyed bursting through a shattered picture frame carrying a
birthday cake), converts it to RGB, and resizes it with LANCZOS
resampling. Widths from CANDIDATE_WIDTHS are tried in order and the
first whose PNG encoding fits within MAX_BYTES wins, so the output is
the largest version that satisfies the competition's size cap.
No randomness, no timestamps.
"""

import io
from pathlib import Path

from PIL import Image

SOURCE = Path(
    "/home/hatch/workspace/makefun/ai-excited-candidates/"
    "media-generation-excited-samoyed-0-b6e5f773-8a7f-41b0-bcba-994dbf8ceec1.webp"
)
CANDIDATE_WIDTHS = (1024, 960, 896, 832, 768)
MAX_BYTES = 1_048_576
OUTPUT = Path(__file__).resolve().parent / "entry.png"


def resized_to(rgb: Image.Image, width: int) -> Image.Image:
    src_w, src_h = rgb.size
    height = round(src_h * width / src_w)
    return rgb.resize((width, height), Image.LANCZOS)


def encode_png(im: Image.Image) -> bytes:
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=True)
    return buf.getvalue()


def main() -> None:
    with Image.open(SOURCE) as im:
        rgb = im.convert("RGB")
    for width in CANDIDATE_WIDTHS:
        candidate = resized_to(rgb, width)
        data = encode_png(candidate)
        if len(data) <= MAX_BYTES:
            OUTPUT.write_bytes(data)
            print(
                f"wrote {OUTPUT}: {candidate.size[0]}x{candidate.size[1]}, "
                f"{len(data)} bytes"
            )
            return
    raise SystemExit("no candidate width fits within the size cap")


if __name__ == "__main__":
    main()
