#!/usr/bin/env python3
"""
tools/blueprint_to_svg_pptx.py

Converts a slide-deck blueprint markdown to .pptx via the PPT Master SVG pipeline:
  1. Parse blueprint  → per-slide specs
  2. Claude API       → one SVG (1280×720) per slide, design-system compliant
  3. svg_to_pptx      → native DrawingML PPTX (fully editable shapes)

Usage:
    python3 tools/blueprint_to_svg_pptx.py <blueprint.md> [output.pptx]

Requires:
    pip3 install anthropic python-pptx Pillow
    ANTHROPIC_API_KEY environment variable
"""

from __future__ import annotations

import os
import re
import sys
import shutil
import tempfile
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic not installed.  Run: pip3 install anthropic")
    sys.exit(1)

# ── Path setup so svg_to_pptx package resolves ────────────────────────────────
TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

from svg_to_pptx import create_pptx_with_native_svg  # noqa: E402

# ── Design-system prompt (cached across slides) ────────────────────────────────
DESIGN_SYSTEM = """\
You are an SVG slide designer. Given a slide specification, produce a single
self-contained SVG that faithfully renders the slide at exactly 1280×720 px.

════════════════════════════════════════
CANVAS
════════════════════════════════════════
width="1280" height="720"
viewBox="0 0 1280 720"
Safe zone: 60px margin on all sides (content lives between x=60–1220, y=60–660)

════════════════════════════════════════
COLOR TOKENS  (use only hex, never rgb/rgba)
════════════════════════════════════════
GREEN_DARK   #1A6B3A  — dark slide backgrounds, dark text on light
GREEN_MID    #2EAA5E  — icon badges, divider lines, accent elements
GREEN_LIGHT  #5CDB8F  — gradient highlights, gem accents, cover accent word
WHITE        #FFFFFF
NEAR_BLACK   #1A1A2E  — neutral headline word on white slides, body on white
GREY_BODY    #4A4A6A  — body text on white slides, slide numbers, captions

For transparency use the SVG opacity attribute (e.g. opacity="0.2") — NEVER rgba().

════════════════════════════════════════
TYPOGRAPHY
════════════════════════════════════════
Font family: Poppins (always; fallbacks: DM Sans, Inter, sans-serif)
Write: font-family="Poppins, DM Sans, Inter, sans-serif"

Type scale:
  Cover display title  : font-size="80" font-weight="900"
  Slide headline       : font-size="36" font-weight="700"
  Section subhead      : font-size="18" font-weight="600"
  KPI number           : font-size="44" font-weight="700"
  Body / bullets       : font-size="16" font-weight="400"
  Caption / slide num  : font-size="11" font-weight="400"

Text color on DARK slides  : fill="#FFFFFF"
Neutral headline on WHITE  : fill="#1A1A2E"
Accent headline on WHITE   : fill="#2EAA5E"
Body on WHITE              : fill="#4A4A6A"

════════════════════════════════════════
LAYOUT PATTERNS  (select by the letter given in the spec)
════════════════════════════════════════

A — Cover / Full-bleed
  Background: radial gradient GREEN_LIGHT at top-center → GREEN_DARK at edges.
  Left panel (x=60–560, full height): frosted card — <rect rx="16" fill="#FFFFFF"
    opacity="0.18" stroke="#FFFFFF" stroke-opacity="0.4" stroke-width="1"/>.
    Inside: subtitle (13pt, white), audience/session badges.
  Right panel (x=580–1220): display headline, two lines if needed (80pt).
  Decorative: soft radial glow ellipse at top-right, opacity 0.15, GREEN_LIGHT fill.

B — Left title / right icon-row list
  Background: as specified (white or dark).
  Left (x=60–500): large headline (36pt, two-tone), one-line descriptor (13pt).
    Divider line on WHITE: <line x1="60" x2="500" stroke="#2EAA5E" stroke-width="1.5"/>
  Right (x=540–1220): stacked rows. Each row:
    Circle badge: <circle r="22" fill="#2EAA5E"/> + icon text inside (white, 14pt, centered)
    Label text: 20pt SemiBold, followed by descriptor 13pt GREY_BODY on same line.
    Row height: ~72px, first row starts at y=200.

C — Horizontal KPI strip (3 columns)
  Background: as specified.
  Three equal columns, each 360px wide.
    KPI number: 44pt Bold.
    KPI label: 11pt body color.
    Short description: 13pt body color.
  Separator arrows "→" in GREEN_MID between columns (centered vertically).

D — 2×2 Quadrant matrix
  Two crossing lines (horizontal + vertical) through slide center (640, 360).
  Axis labels 13pt at ends of each line.
  Content text in each quadrant, 13pt.

E — Chart + stat cards
  Top 55% (y=60–450): rounded-rect placeholder for chart/visual, dashed GREEN_MID border.
  Bottom 35% (y=460–660): two stat cards side-by-side, each with bold number (36pt)
    and label (11pt).

F — Dark hero / objectives
  Background: GREEN_DARK (solid or radial gradient → GREEN_MID at top).
  Headline centered, 36pt Bold White, y≈160.
  Three to five icon-badge rows centered at x=640, starting y≈260, spacing 72px.
    Circle badge r=22 GREEN_MID + white check/icon text, label 14pt white to the right.
  Soft radial glow at top-center, GREEN_LIGHT, opacity 0.12.

G — Two-stat opportunity
  Left 48% (x=60–580): paragraph body 13pt + optional subhead 18pt.
  Right 48% (x=620–1220): two stats stacked.
    Each: circle badge r=22 GREEN_MID above, bold number 40pt below, label 11pt.

════════════════════════════════════════
DIVIDER RULE (WHITE slides only)
════════════════════════════════════════
After the headline, draw:
  <line x1="60" y1="{headline_bottom+12}" x2="1220" y2="{headline_bottom+12}"
        stroke="#2EAA5E" stroke-width="1.5"/>

════════════════════════════════════════
SLIDE NUMBER
════════════════════════════════════════
Bottom-right, always:
  <text x="1215" y="700" font-family="Poppins, sans-serif" font-size="11"
        text-anchor="end" fill="{WHITE on dark / GREY_BODY on white}">{N}</text>

════════════════════════════════════════
SVG OUTPUT RULES  (non-negotiable)
════════════════════════════════════════
1. Return ONLY the SVG — no markdown fences, no explanation text.
2. Opening tag: <svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720"
   viewBox="0 0 1280 720">
3. ALL styles must be inline SVG presentation attributes — NO <style> tags,
   NO CSS classes, NO external references.
4. Never use rgb() or rgba() — hex colors only.
5. Never use <use>, <symbol>, <foreignObject>, <script>.
6. Gradients MUST be defined in <defs> and referenced via url(#id).
7. Fonts: write the full stack: font-family="Poppins, DM Sans, Inter, sans-serif"
8. Text must use <text> elements with explicit x, y, font-size, font-weight,
   font-family, fill. Use <tspan dy="1.4em"> for wrapped lines inside one <text>.
9. All coordinates are integers or at most 1 decimal place.
10. Keep file under 60 KB — no complex path data for decorative items.
"""


# ── Blueprint parser ───────────────────────────────────────────────────────────

def parse_blueprint(md_path: str) -> tuple[dict, list[dict]]:
    """Return (meta, slides) where each slide is a dict of its spec fields."""
    text = Path(md_path).read_text(encoding="utf-8")

    meta: dict[str, str] = {}
    for key in ("Topic", "Audience", "Style", "Slides"):
        m = re.search(rf"\*\*{key}:\*\*\s*(.*)", text)
        if m:
            meta[key.lower()] = m.group(1).strip()

    blocks = re.split(r"^## Slide (\d+):\s*(.*)", text, flags=re.MULTILINE)
    slides: list[dict] = []

    for idx in range(1, len(blocks) - 1, 3):
        num   = int(blocks[idx])
        title = blocks[idx + 1].strip()
        body  = blocks[idx + 2]

        def field(name: str) -> str:
            m = re.search(rf"\*\*{re.escape(name)}:\*\*\s*(.*?)(?=\n\s*-\s*\*\*|\Z)",
                          body, re.DOTALL)
            return m.group(1).strip() if m else ""

        slides.append({
            "n":       num,
            "title":   title,
            "layout":  field("Layout pattern").split("/")[0].strip().upper()[:1] or "B",
            "bg":      "dark" if "dark" in field("Background mode").lower() else "white",
            "headline": field("Headline"),
            "content":  field("Content"),
            "visual":   field("Visual spec"),
            "notes":    field("PPT build notes"),
        })

    return meta, slides


# ── SVG generation ─────────────────────────────────────────────────────────────

def _make_slide_prompt(meta: dict, slide: dict) -> str:
    bg_desc = "dark-green" if slide["bg"] == "dark" else "white"
    return f"""\
Generate a 1280×720 SVG for slide {slide['n']} of a {meta.get('style','training')} \
presentation titled "{meta.get('topic','')}".

Slide title   : {slide['title']}
Layout pattern: {slide['layout']}
Background    : {bg_desc}
Headline      : {slide['headline']}

Content spec:
{slide['content']}

Visual spec:
{slide['visual']}

Build notes:
{slide['notes']}

Follow the design system exactly. Return ONLY the SVG — no explanation."""


def _clean_svg(raw: str) -> str:
    """Strip markdown fences and leading/trailing whitespace."""
    text = raw.strip()
    text = re.sub(r'^```(?:svg|xml)?\s*\n?', '', text)
    text = re.sub(r'\n?```\s*$', '', text).strip()
    # If the SVG was truncated mid-tag, close it
    if not text.endswith("</svg>"):
        text = text.rstrip() + "\n</svg>"
    return text


def _is_valid_xml(text: str) -> bool:
    try:
        import xml.etree.ElementTree as ET
        ET.fromstring(text.encode("utf-8"))
        return True
    except Exception:
        return False


def generate_svgs(meta: dict, slides: list[dict], svg_dir: Path,
                  client: anthropic.Anthropic) -> None:
    total = len(slides)
    for slide in slides:
        n = slide["n"]
        print(f"  [{n}/{total}] Generating SVG for slide {n}: {slide['title']} ...", end=" ", flush=True)

        for attempt in range(1, 3):
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=6000,
                system=[{
                    "type": "text",
                    "text": DESIGN_SYSTEM,
                    "cache_control": {"type": "ephemeral"},
                }],
                messages=[{
                    "role": "user",
                    "content": _make_slide_prompt(meta, slide),
                }],
            )

            svg_text = _clean_svg(response.content[0].text)

            if not svg_text.startswith("<svg"):
                if attempt == 1:
                    print(f"retry(no <svg>)", end=" ", flush=True)
                    continue
                print(f"\nWARN: slide {n} still missing <svg> tag — writing anyway")

            if _is_valid_xml(svg_text):
                break
            if attempt == 1:
                # Try appending close tag and retry parsing before requesting again
                fixed = svg_text.rstrip() + "\n</svg>" if not svg_text.endswith("</svg>") else svg_text
                if _is_valid_xml(fixed):
                    svg_text = fixed
                    break
                print(f"retry(xml-err)", end=" ", flush=True)
            else:
                print(f"\nWARN: slide {n} SVG has XML errors — writing best-effort")

        out_file = svg_dir / f"slide{n:02d}.svg"
        out_file.write_text(svg_text, encoding="utf-8")
        print("done")


# ── Entry point ────────────────────────────────────────────────────────────────

def convert(md_path: str, out_path: str | None = None) -> str:
    if not out_path:
        out_path = str(Path(md_path).with_suffix(".svg_pptx.pptx"))

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
        sys.exit(1)

    print(f"\nPPT Master pipeline: {Path(md_path).name} → {Path(out_path).name}")
    print("=" * 60)

    meta, slides = parse_blueprint(md_path)
    if not slides:
        print("ERROR: No slides parsed from blueprint.")
        sys.exit(1)
    print(f"  Parsed {len(slides)} slides  |  topic: {meta.get('topic','')}  |  style: {meta.get('style','')}\n")

    client = anthropic.Anthropic(api_key=api_key)

    tmp_dir = Path(tempfile.mkdtemp(prefix="pptmaster_"))
    svg_dir = tmp_dir / "svg_output"
    svg_dir.mkdir()

    try:
        print("Step 1/2 — Generating SVGs via Claude API")
        generate_svgs(meta, slides, svg_dir, client)

        svg_files = sorted(svg_dir.glob("slide*.svg"))
        print(f"\nStep 2/2 — Converting {len(svg_files)} SVGs → PPTX (PPT Master native shapes)")
        ok = create_pptx_with_native_svg(
            svg_files=svg_files,
            output_path=Path(out_path),
            canvas_format="ppt169",
            verbose=True,
            transition="fade",
            use_compat_mode=False,   # pure SVG mode (no cairo required)
            use_native_shapes=True,  # DrawingML editable shapes
            enable_notes=False,
        )

        if ok:
            size_kb = Path(out_path).stat().st_size // 1024
            print(f"\noutput_path: {out_path}  ({size_kb} KB)")
        else:
            print("\nERROR: PPTX conversion reported failures — check output above.")
            sys.exit(1)

    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

    return out_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/blueprint_to_svg_pptx.py <blueprint.md> [output.pptx]")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
