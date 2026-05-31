#!/usr/bin/env python3
"""
Convert a slide-deck markdown blueprint to a .pptx file.

Applies the project design system:
  - Two-tone headlines (near-black + green-mid on white; all-white on dark)
  - Alternating dark-green / white backgrounds
  - Poppins font, green palette, divider lines, slide numbers

Usage:
    python3 tools/md_to_pptx.py <blueprint.md> [output.pptx]
"""

import re
import sys
from pathlib import Path

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN
except ImportError:
    print("ERROR: python-pptx not installed. Run: pip3 install python-pptx")
    sys.exit(1)

# ── Design tokens ─────────────────────────────────────────────────────────────
C = {
    "green_dark":  RGBColor(0x1A, 0x6B, 0x3A),
    "green_mid":   RGBColor(0x2E, 0xAA, 0x5E),
    "green_light": RGBColor(0x5C, 0xDB, 0x8F),
    "white":       RGBColor(0xFF, 0xFF, 0xFF),
    "near_black":  RGBColor(0x1A, 0x1A, 0x2E),
    "grey_body":   RGBColor(0x4A, 0x4A, 0x6A),
}

SLIDE_W   = Inches(13.333)
SLIDE_H   = Inches(7.5)
MARGIN    = Inches(0.75)
CONTENT_W = SLIDE_W - 2 * MARGIN
FONT      = "Poppins"


# ── Parser ────────────────────────────────────────────────────────────────────
def _field(text: str, name: str) -> str:
    m = re.search(rf'\*\*{re.escape(name)}:\*\*\s*(.*)', text)
    return m.group(1).strip() if m else ""


def _parse_headline(raw: str) -> tuple[str, str]:
    """Parse '"neutral" + "accent"' → (neutral, accent)."""
    parts = re.findall(r'"([^"]*)"', raw)
    if len(parts) >= 2:
        return parts[0].strip(), parts[1].strip()
    if len(parts) == 1:
        return parts[0].strip(), ""
    return raw.strip(), ""


def _parse_bullets(raw: str) -> list[str]:
    """Turn content string into a list of bullet strings."""
    if not raw:
        return []
    items = []
    for line in raw.replace(";", "\n").split("\n"):
        line = re.sub(r"^[\s•\-\*]+", "", line).strip()
        if line:
            items.append(line)
    return items


def parse_blueprint(path: str) -> list[dict]:
    text = Path(path).read_text(encoding="utf-8")
    blocks = re.split(r"^## Slide \d+:\s*", text, flags=re.MULTILINE)

    slides = []
    for i, block in enumerate(blocks[1:], 1):
        lines = block.strip().split("\n")
        title = lines[0].strip()
        rest  = "\n".join(lines[1:])

        layout_raw = _field(rest, "Layout pattern").split("/")[0].strip().upper()
        layout = layout_raw[0] if layout_raw else "B"

        bg_raw = _field(rest, "Background mode").lower()
        bg = "dark" if "dark" in bg_raw else "white"

        neutral, accent = _parse_headline(_field(rest, "Headline"))
        if not neutral:
            neutral = title

        slides.append({
            "n":       i,
            "title":   title,
            "layout":  layout,
            "bg":      bg,
            "neutral": neutral,
            "accent":  accent,
            "bullets": _parse_bullets(_field(rest, "Content")),
            "visual":  _field(rest, "Visual spec"),
            "notes":   _field(rest, "PPT build notes"),
        })

    return slides


# ── Shape helpers ─────────────────────────────────────────────────────────────
def _apply_background(slide, bg: str):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = C["green_dark"] if bg == "dark" else C["white"]


def _two_tone_title(slide, neutral: str, accent: str, bg: str) -> float:
    """Add headline; return bottom-y (in Inches float) for next element."""
    top = Inches(0.55)
    tb  = slide.shapes.add_textbox(MARGIN, top, CONTENT_W, Inches(1.1))
    tf  = tb.text_frame
    tf.word_wrap = False
    p   = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT

    nc = C["white"]     if bg == "dark" else C["near_black"]
    ac = C["white"]     if bg == "dark" else C["green_mid"]

    if neutral:
        r = p.add_run()
        r.text = neutral + (" " if accent else "")
        r.font.size = Pt(36)
        r.font.bold = True
        r.font.name = FONT
        r.font.color.rgb = nc

    if accent:
        r = p.add_run()
        r.text = accent
        r.font.size = Pt(36)
        r.font.bold = True
        r.font.name = FONT
        r.font.color.rgb = ac

    return top + Inches(1.15)


def _divider(slide, y_inches: float):
    """Thin green-mid horizontal rule (white slides only)."""
    rect = slide.shapes.add_shape(
        1,  # MSO_AUTO_SHAPE_TYPE.RECTANGLE
        MARGIN,
        Inches(y_inches),
        CONTENT_W,
        Inches(0.025),
    )
    rect.fill.solid()
    rect.fill.fore_color.rgb = C["green_mid"]
    rect.line.fill.background()


def _bullets(slide, items: list[str], y: float, bg: str):
    if not items:
        return
    color   = C["white"] if bg == "dark" else C["grey_body"]
    avail_h = SLIDE_H - Inches(y) - MARGIN

    tb = slide.shapes.add_textbox(MARGIN, Inches(y + 0.18), CONTENT_W, avail_h)
    tf = tb.text_frame
    tf.word_wrap = True

    for i, text in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_before = Pt(7)
        p.alignment    = PP_ALIGN.LEFT
        run = p.add_run()
        run.text           = f"•  {text}"
        run.font.size      = Pt(13)
        run.font.name      = FONT
        run.font.color.rgb = color


def _slide_number(slide, n: int, bg: str):
    color = C["white"] if bg == "dark" else C["grey_body"]
    tb    = slide.shapes.add_textbox(
        SLIDE_W - Inches(0.65),
        SLIDE_H - Inches(0.38),
        Inches(0.5),
        Inches(0.28),
    )
    tf  = tb.text_frame
    p   = tf.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    run = p.add_run()
    run.text           = str(n)
    run.font.size      = Pt(8)
    run.font.name      = FONT
    run.font.color.rgb = color


# ── Slide builder ─────────────────────────────────────────────────────────────
def _build_slide(prs: Presentation, data: dict):
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank layout
    bg    = data["bg"]

    _apply_background(slide, bg)
    y = _two_tone_title(slide, data["neutral"], data["accent"], bg)

    # Convert Emu → float inches for subsequent helpers
    y_in = y / 914400.0  # 1 inch = 914400 EMU

    if bg == "white":
        _divider(slide, y_in)
        y_in += 0.11

    _bullets(slide, data["bullets"], y_in, bg)
    _slide_number(slide, data["n"], bg)


# ── Entry point ───────────────────────────────────────────────────────────────
def convert(md_path: str, out_path: str | None = None) -> str:
    if not out_path:
        out_path = str(Path(md_path).with_suffix(".pptx"))

    slides = parse_blueprint(md_path)
    if not slides:
        print("ERROR: No slides parsed from blueprint.")
        sys.exit(1)

    prs = Presentation()
    prs.slide_width  = SLIDE_W
    prs.slide_height = SLIDE_H

    for data in slides:
        _build_slide(prs, data)

    prs.save(out_path)
    print(f"output_path: {out_path}")
    print(f"Slides: {len(slides)}")
    return out_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/md_to_pptx.py <blueprint.md> [output.pptx]")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
