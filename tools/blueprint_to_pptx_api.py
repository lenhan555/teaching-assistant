#!/usr/bin/env python3
"""
tools/blueprint_to_pptx_api.py

Converts a slide-deck blueprint markdown to .pptx using the Claude API.
Claude generates a bespoke python-pptx script for the specific deck; we run it.

Why: The mechanical parser (md_to_pptx.py) can only place text boxes.
     Claude reasons about layout patterns (A-G), gradients, frosted cards,
     KPI columns, icon badges, and the full design system — producing rich slides.

Usage:
    python3 tools/blueprint_to_pptx_api.py <blueprint.md> [output.pptx]

Requires:
    pip3 install anthropic python-pptx
    ANTHROPIC_API_KEY environment variable
"""

import os
import re
import subprocess
import sys
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic not installed. Run: pip3 install anthropic")
    sys.exit(1)

# ── Design system prompt (cached via prompt caching) ─────────────────────────
DESIGN_SYSTEM = """\
You are a PowerPoint generation expert. Given a slide deck blueprint in markdown format, \
generate a complete, self-contained Python script using python-pptx that faithfully \
implements every slide with high visual fidelity to the design system below.

════════════════════════════════════════
DESIGN SYSTEM
════════════════════════════════════════

Slide dimensions: 13.333" × 7.5"  (set prs.slide_width / prs.slide_height)
Content margin:   0.75" on all sides
Content width:    13.333 - 1.5 = 11.833"

Color tokens (use RGBColor from pptx.dml.color):
  GREEN_DARK  = RGBColor(0x1A, 0x6B, 0x3A)   ← dark slide backgrounds
  GREEN_MID   = RGBColor(0x2E, 0xAA, 0x5E)   ← accents, divider lines, icon badges
  GREEN_LIGHT = RGBColor(0x5C, 0xDB, 0x8F)   ← gradient highlight, gem accents
  WHITE       = RGBColor(0xFF, 0xFF, 0xFF)
  NEAR_BLACK  = RGBColor(0x1A, 0x1A, 0x2E)   ← neutral headline word on white slides
  GREY_BODY   = RGBColor(0x4A, 0x4A, 0x6A)   ← body text on white slides

Font: "Poppins" throughout (single family, no mixing). Set on every run.

Type scale:
  Cover display headline : Bold,      ~72-80pt,  white
  Slide title (white bg) : Bold,      36pt,      two-tone runs (see rule 3)
  Slide title (dark bg)  : Bold,      36pt,      all white
  Section subhead        : SemiBold,  18pt,      GREEN_MID or NEAR_BLACK
  KPI stat number        : Bold,      44pt
  KPI label              : Regular,   10pt
  Body / bullets         : Regular,   13pt
  Caption / slide number : Regular,   8pt

════════════════════════════════════════
LAYOUT PATTERNS  (apply by the letter in the blueprint)
════════════════════════════════════════

A — Cover / Full-bleed:
    Background: GREEN_DARK (solid).
    Left 45%: frosted card — RoundedRectangle shape, white fill at 20% transparency,
              1pt white border at 40% transparency. Contains: course badge text, subtitle.
    Right 55%: display headline text box, Poppins Bold 72pt, white.
    Decorative: add a semi-transparent GREEN_LIGHT ellipse (soft glow) in upper area,
                and a smaller one in lower-left, both with high transparency (70%+).

B — Left title / right icon list:
    Background: white or dark per spec.
    Left 38%: large heading (Poppins Bold 40pt) + one-liner (13pt body color).
    Right 60%: stacked rows — for each bullet, draw a filled GREEN_MID circle (icon badge,
               0.35" diameter) + text label to its right (Poppins SemiBold 14pt).

C — Horizontal KPI strip:
    3 equal columns across the content area (each ~3.9" wide).
    Each column: large stat number (Bold 44pt, GREEN_DARK on white / white on dark) +
    stat label (10pt, body color) + short description (12pt, body color).
    Between columns: small right-arrow "→" in GREEN_MID at center height.

D — 2×2 Quadrant matrix:
    Draw two crossing lines (horizontal + vertical) in GREY_BODY at slide center.
    Axis labels (12pt) at each end of both lines.
    Content text boxes in each quadrant.

E — Map / chart + stat cards:
    Top ~55%: a rounded-rect placeholder labeled "[CHART / VISUAL]" in GREY_BODY 10pt,
              dashed GREEN_MID border, light grey fill.
    Bottom ~35%: two rounded-rect stat cards side-by-side, each with bold number (36pt)
                 and label (10pt).

F — Dark hero slide:
    Background: GREEN_DARK.
    Centered headline (Bold 40pt, white) in upper third.
    Three icon badges (GREEN_MID filled circles, 0.5") in a row at center, with
    label text (14pt, white) beneath each.

G — Two-stat opportunity:
    Left 48%: paragraph body text (13pt, body color) + optional subhead.
    Right 48%: two stats stacked — each with GREEN_MID filled circle badge (0.45") above,
               bold number (40pt) below badge, label (10pt) beneath number.

════════════════════════════════════════
DESIGN RULES  (non-negotiable)
════════════════════════════════════════

1. All slides use prs.slide_layouts[6]  (blank layout).

2. Background:
     dark-green → slide.background.fill.solid(); .fore_color.rgb = GREEN_DARK
     white      → slide.background.fill.solid(); .fore_color.rgb = WHITE

3. Two-tone headline on WHITE slides:
     Single text box, two text runs in the same paragraph:
       run 1: neutral words  → NEAR_BLACK, Bold, 36pt, font "Poppins"
       run 2: accent words   → GREEN_MID,  Bold, 36pt, font "Poppins"
     One space between them.

4. Headline on DARK slides: all one color (WHITE), same size/weight.

5. Divider line on WHITE slides: thin rectangle shape (height 0.022") at GREEN_MID
   fill, no border, positioned just below the title text box.

6. Slide number: text box at bottom-right (x≈12.6", y≈7.1", w=0.55", h=0.28"),
   8pt, right-aligned, GREY_BODY (white slides) / WHITE (dark slides).

7. Bullets: prefix each with "•  ", 13pt, Poppins, body color for the slide mode.
   word_wrap = True on the text frame.

8. Frosted card (Pattern A): use MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE via add_shape.
   Set shape.fill.solid(), fore_color.rgb = WHITE, then adjust transparency via XML:
     sp_tree = slide.shapes._spTree
     (or set shape.fill.fore_color.theme_color approach is less reliable —
      prefer setting transparency on the fill element directly via lxml)

9. Icon badge (circle): add_shape(MSO_AUTO_SHAPE_TYPE.OVAL, ...) → fill GREEN_MID,
   line.fill.background().

10. Keep ALL content inside the 0.75" margin safe zone.

════════════════════════════════════════
OUTPUT FORMAT
════════════════════════════════════════

Return ONLY a complete Python script. No markdown fences. No explanation text.

The script must:
  - Start with necessary imports (pptx, pptx.util, pptx.dml.color, pptx.enum.text,
    pptx.enum.shapes, lxml if needed, sys, os)
  - Define constants for colors, dimensions
  - Implement a helper to set fill transparency via lxml if needed for frosted glass
  - Accept output path from sys.argv[1] (default: 'output.pptx')
  - Create Presentation, set dimensions, add every slide, save
  - Be runnable standalone: python3 <script>.py output.pptx
"""


def _strip_fences(code: str) -> str:
    code = code.strip()
    code = re.sub(r'^```(?:python)?\s*\n?', '', code)
    code = re.sub(r'\n?```\s*$', '', code)
    return code.strip()


def convert(md_path: str, out_path: str | None = None) -> str:
    if not out_path:
        out_path = str(Path(md_path).with_suffix(".pptx"))

    blueprint = Path(md_path).read_text(encoding="utf-8")
    slug = Path(md_path).stem

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    print(f"Generating bespoke python-pptx script for '{slug}' via Claude API...")

    chunks: list[str] = []
    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        system=[{
            "type": "text",
            "text": DESIGN_SYSTEM,
            "cache_control": {"type": "ephemeral"},   # cache the design system across calls
        }],
        messages=[{
            "role": "user",
            "content": (
                f"Generate a complete python-pptx script for this slide deck blueprint. "
                f"The script must save to: '{out_path}'\n\n"
                f"{blueprint}"
            ),
        }],
    ) as stream:
        for text in stream.text_stream:
            chunks.append(text)
            print(".", end="", flush=True)

    print()  # newline after progress dots

    code = _strip_fences("".join(chunks))

    # Save the generated script so it's inspectable and re-runnable
    py_path = str(Path(md_path).with_suffix(".generated.py"))
    Path(py_path).write_text(code, encoding="utf-8")
    print(f"Generated script: {py_path}")

    # Run the generated script to produce the .pptx
    print("Running generated script...")
    result = subprocess.run(
        [sys.executable, py_path, out_path],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(Path(md_path).parent),
    )

    if result.returncode != 0:
        print("\nERROR: Generated script failed. Stderr:\n")
        print(result.stderr[-3000:])
        print(f"\nInspect and fix: {py_path}")
        sys.exit(1)

    if result.stdout:
        print(result.stdout.strip())

    size_kb = Path(out_path).stat().st_size // 1024
    print(f"output_path: {out_path}  ({size_kb} KB)")
    return out_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/blueprint_to_pptx_api.py <blueprint.md> [output.pptx]")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
