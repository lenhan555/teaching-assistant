#!/usr/bin/env python3
"""
tools/blueprint_to_html.py

Converts a slide-deck blueprint markdown to a self-contained HTML presentation.
No API calls. No dependencies. Pure Python standard library.

Features:
  - Full design system in CSS (radial gradients, frosted glass, two-tone headlines)
  - Layout patterns A–G rendered structurally
  - Keyboard navigation (← →, Space, F for fullscreen)
  - Print to PDF via browser: Ctrl+P → set margins to None → Save as PDF

Usage:
    python3 tools/blueprint_to_html.py <blueprint.md> [output.html]
"""

import html
import re
import sys
from pathlib import Path

# ── Parser (same logic as md_to_pptx.py) ─────────────────────────────────────
def _field(text: str, name: str) -> str:
    m = re.search(rf'\*\*{re.escape(name)}:\*\*\s*(.*)', text)
    return m.group(1).strip() if m else ""

def _parse_headline(raw: str) -> tuple[str, str]:
    parts = re.findall(r'"([^"]*)"', raw)
    if len(parts) >= 2:
        return parts[0].strip(), parts[1].strip()
    if len(parts) == 1:
        return parts[0].strip(), ""
    return raw.strip(), ""

def _parse_bullets(raw: str) -> list[str]:
    if not raw:
        return []
    items = []
    for line in raw.split("\n"):
        line = re.sub(r"^[\s•\-\*\[\]]+", "", line).strip()
        # Strip inline icon tags like [icon: book]
        line = re.sub(r"\[icon:[^\]]*\]", "", line).strip()
        if line:
            items.append(line)
    return items

def parse_blueprint(path: str) -> tuple[str, list[dict]]:
    text = Path(path).read_text(encoding="utf-8")

    # Extract deck title from H1 or first line
    title_m = re.search(r'^#\s+(.+)', text, re.MULTILINE)
    deck_title = title_m.group(1).strip() if title_m else Path(path).stem

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
    return deck_title, slides


# ── HTML helpers ──────────────────────────────────────────────────────────────
E = html.escape

def headline(neutral: str, accent: str, bg: str, size: str = "main") -> str:
    cls = f"headline headline-{size}"
    if bg == "dark":
        return f'<h1 class="{cls} dark-head">{E(neutral)} {E(accent)}</h1>'
    n = f'<span class="hl-neutral">{E(neutral)}</span>'
    a = f'<span class="hl-accent">{E(accent)}</span>'
    return f'<h1 class="{cls}">{n} {a}</h1>'

def divider(bg: str) -> str:
    return '<div class="divider"></div>' if bg == "white" else ""

def bullets_html(items: list[str], extra_class: str = "") -> str:
    if not items:
        return ""
    lis = "".join(f"<li>{E(b)}</li>" for b in items)
    return f'<ul class="bullets {extra_class}">{lis}</ul>'

def icon_badge(symbol: str = "◆", large: bool = False) -> str:
    cls = "badge badge-lg" if large else "badge"
    return f'<span class="{cls}">{symbol}</span>'

def stat_card(number: str, label: str, bg: str) -> str:
    return (
        f'<div class="stat-card">'
        f'<div class="stat-num">{E(number)}</div>'
        f'<div class="stat-label">{E(label)}</div>'
        f'</div>'
    )

def chart_placeholder(caption: str = "Chart / Visual") -> str:
    return f'<div class="chart-placeholder"><span>{E(caption)}</span></div>'

def slide_number(n: int) -> str:
    return f'<div class="slide-num">{n}</div>'


# ── Layout renderers ──────────────────────────────────────────────────────────
ICONS = ["◈", "◉", "◆", "◇", "○", "●", "◎", "▶", "★", "⬡"]

def _icon_for(i: int) -> str:
    return ICONS[i % len(ICONS)]


def layout_a(d: dict) -> str:
    """Full-bleed cover: frosted card left, display headline right."""
    bullets = d["bullets"]
    card_lines = "".join(f"<p>{E(b)}</p>" for b in bullets[:4]) if bullets else ""
    return f"""
    <div class="glow glow-top"></div>
    <div class="glow glow-mid"></div>
    <div class="layout-a-inner">
      <div class="frosted-card">
        <div class="badge-pill">SQL · Training</div>
        {card_lines}
      </div>
      <div class="cover-hero">
        <h1 class="display-headline">{E(d["neutral"])}<br><span class="display-accent">{E(d["accent"])}</span></h1>
        <p class="cover-sub">{E(d["title"])}</p>
      </div>
    </div>
    {slide_number(d["n"])}"""


def layout_b(d: dict) -> str:
    """Left title / right icon list."""
    bullets = d["bullets"]
    rows = ""
    for i, b in enumerate(bullets):
        rows += f"""
        <div class="icon-row">
          {icon_badge(_icon_for(i))}
          <span class="icon-label">{E(b)}</span>
        </div>"""
    return f"""
    <div class="layout-b-inner">
      <div class="b-left">
        {headline(d["neutral"], d["accent"], d["bg"])}
        {divider(d["bg"])}
      </div>
      <div class="b-right">
        {rows}
      </div>
    </div>
    {slide_number(d["n"])}"""


def layout_c(d: dict) -> str:
    """Horizontal KPI strip — 3 columns with arrows between."""
    bullets = d["bullets"]
    cols = []
    for i, b in enumerate(bullets[:3]):
        parts = b.split("—", 1) if "—" in b else b.split(":", 1) if ":" in b else [b, ""]
        num   = parts[0].strip()
        label = parts[1].strip() if len(parts) > 1 else ""
        cols.append(
            f'<div class="kpi-col">'
            f'<div class="kpi-num">{E(num)}</div>'
            f'<div class="kpi-lbl">{E(label)}</div>'
            f'</div>'
        )
    # Interleave arrows
    strip = ""
    for i, col in enumerate(cols):
        strip += col
        if i < len(cols) - 1:
            strip += '<div class="kpi-arrow">→</div>'
    if not strip and bullets:
        # Fallback: just show bullets
        strip = bullets_html(bullets)
    return f"""
    {headline(d["neutral"], d["accent"], d["bg"])}
    {divider(d["bg"])}
    <div class="kpi-strip">{strip}</div>
    {slide_number(d["n"])}"""


def layout_d(d: dict) -> str:
    """2×2 quadrant matrix."""
    bullets = d["bullets"]
    quads = bullets[:4] + [""] * (4 - len(bullets[:4]))
    return f"""
    {headline(d["neutral"], d["accent"], d["bg"])}
    {divider(d["bg"])}
    <div class="quadrant-grid">
      <div class="quad q-tl"><span>{E(quads[0])}</span></div>
      <div class="quad q-tr"><span>{E(quads[1])}</span></div>
      <div class="quad q-bl"><span>{E(quads[2])}</span></div>
      <div class="quad q-br"><span>{E(quads[3])}</span></div>
      <div class="quad-h-line"></div>
      <div class="quad-v-line"></div>
    </div>
    {slide_number(d["n"])}"""


def layout_e(d: dict) -> str:
    """Chart placeholder + stat cards."""
    bullets = d["bullets"]
    stats = []
    for b in bullets[:2]:
        parts = b.split("—", 1) if "—" in b else b.split(":", 1) if ":" in b else [b, ""]
        stats.append((parts[0].strip(), parts[1].strip() if len(parts) > 1 else ""))
    stat_cards = "".join(stat_card(s[0], s[1], d["bg"]) for s in stats) if stats else ""
    caption = d["visual"] or "Chart / Visual"
    return f"""
    {headline(d["neutral"], d["accent"], d["bg"])}
    {divider(d["bg"])}
    {chart_placeholder(caption[:80])}
    <div class="stat-row">{stat_cards}</div>
    {slide_number(d["n"])}"""


def layout_f(d: dict) -> str:
    """Dark hero: headline + 3 icon columns."""
    bullets = d["bullets"]
    cols = ""
    for i, b in enumerate(bullets[:3]):
        cols += f"""
        <div class="f-col">
          {icon_badge(_icon_for(i), large=True)}
          <div class="f-label">{E(b)}</div>
        </div>"""
    return f"""
    <div class="glow glow-top"></div>
    <div class="layout-f-inner">
      {headline(d["neutral"], d["accent"], d["bg"])}
      <div class="f-icons">{cols}</div>
    </div>
    {slide_number(d["n"])}"""


def layout_g(d: dict) -> str:
    """Two-stat opportunity: text left, two big stats right."""
    bullets = d["bullets"]
    body_bullets = bullets[:-2] if len(bullets) > 2 else bullets[:1]
    stat_bullets  = bullets[-2:] if len(bullets) >= 2 else bullets[-1:]

    stats_html = ""
    for b in stat_bullets:
        parts = b.split("—", 1) if "—" in b else b.split(":", 1) if ":" in b else [b, ""]
        num   = parts[0].strip()
        label = parts[1].strip() if len(parts) > 1 else ""
        stats_html += f"""
        <div class="g-stat">
          {icon_badge(_icon_for(0), large=True)}
          <div class="g-num">{E(num)}</div>
          <div class="g-lbl">{E(label)}</div>
        </div>"""

    return f"""
    <div class="layout-g-inner">
      <div class="g-left">
        {headline(d["neutral"], d["accent"], d["bg"])}
        {divider(d["bg"])}
        {bullets_html(body_bullets)}
      </div>
      <div class="g-right">{stats_html}</div>
    </div>
    {slide_number(d["n"])}"""


def layout_default(d: dict) -> str:
    """Generic layout for any unlisted pattern."""
    return f"""
    {headline(d["neutral"], d["accent"], d["bg"])}
    {divider(d["bg"])}
    {bullets_html(d["bullets"])}
    {slide_number(d["n"])}"""


LAYOUT_FN = {
    "A": layout_a,
    "B": layout_b,
    "C": layout_c,
    "D": layout_d,
    "E": layout_e,
    "F": layout_f,
    "G": layout_g,
}

def render_slide(d: dict, active: bool) -> str:
    fn    = LAYOUT_FN.get(d["layout"], layout_default)
    inner = fn(d)
    cls   = f'slide {"dark" if d["bg"] == "dark" else "white"} layout-{d["layout"].lower()}'
    if active:
        cls += " active"
    return f'<div class="{cls}" id="slide-{d["n"]}">{inner}</div>'


# ── CSS ───────────────────────────────────────────────────────────────────────
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --green-dark:  #1A6B3A;
  --green-mid:   #2EAA5E;
  --green-light: #5CDB8F;
  --white:       #FFFFFF;
  --near-black:  #1A1A2E;
  --grey-body:   #4A4A6A;
  --font: 'Poppins', 'DM Sans', 'Inter', system-ui, sans-serif;
  --margin: 5.6%;  /* ~0.75" on 13.33" slide */
}

/* ── Viewport wrapper ── */
body { background: #111; font-family: var(--font); overflow: hidden; }

.deck-wrapper {
  width: 100vw; height: 100vh;
  display: flex; align-items: center; justify-content: center;
}

/* ── Slide base ── */
.slide {
  position: absolute;
  width:  min(100vw, 177.78vh);
  height: min(56.25vw, 100vh);
  display: none;
  flex-direction: column;
  padding: var(--margin);
  overflow: hidden;
  font-family: var(--font);
}
.slide.active { display: flex; }

.slide.dark  { background: radial-gradient(ellipse at 50% 15%, #3a9a6044 0%, var(--green-dark) 65%); color: #fff; }
.slide.white { background: var(--white); color: var(--grey-body); }

/* ── Headlines ── */
.headline { font-weight: 700; line-height: 1.1; margin-bottom: 0.15em; }
.headline-main { font-size: clamp(1.6rem, 4.2vh, 2.4rem); }
.headline-large { font-size: clamp(2rem, 5.5vh, 3.2rem); }

.dark-head  { color: #fff; }
.hl-neutral { color: var(--near-black); }
.hl-accent  { color: var(--green-mid); }

/* ── Divider ── */
.divider {
  height: 2px; width: 100%;
  background: var(--green-mid);
  margin: 0.5em 0 0.8em;
  border-radius: 1px;
}

/* ── Bullets ── */
.bullets { list-style: none; padding: 0; }
.bullets li {
  padding: 0.28em 0 0.28em 1.2em;
  font-size: clamp(0.75rem, 1.8vh, 1rem);
  line-height: 1.55;
  position: relative;
}
.bullets li::before { content: "◆"; position: absolute; left: 0; color: var(--green-mid); font-size: 0.65em; top: 0.42em; }
.dark  .bullets li { color: rgba(255,255,255,0.88); }
.white .bullets li { color: var(--grey-body); }

/* ── Icon badge ── */
.badge {
  display: inline-flex; align-items: center; justify-content: center;
  width: clamp(28px, 4.5vh, 36px); height: clamp(28px, 4.5vh, 36px);
  border-radius: 50%;
  background: var(--green-mid); color: #fff;
  font-size: clamp(0.65rem, 1.6vh, 0.9rem);
  flex-shrink: 0;
}
.badge-lg {
  width: clamp(40px, 6.5vh, 52px); height: clamp(40px, 6.5vh, 52px);
  font-size: clamp(0.9rem, 2vh, 1.2rem);
}

/* ── Slide number ── */
.slide-num {
  position: absolute; bottom: 1.8%; right: 2.2%;
  font-size: clamp(0.5rem, 1.2vh, 0.65rem);
  opacity: 0.5;
}
.dark  .slide-num { color: #fff; }
.white .slide-num { color: var(--grey-body); }

/* ═══════════════════════════════════════
   LAYOUT A — Cover
════════════════════════════════════════ */
.layout-a { padding: 0; }

.glow {
  position: absolute; border-radius: 50%;
  background: radial-gradient(circle, var(--green-light), transparent 70%);
  pointer-events: none;
}
.glow-top  { width: 55%; height: 55%; top: -15%; left: 20%; opacity: 0.18; }
.glow-mid  { width: 30%; height: 30%; bottom: 5%; left: 3%; opacity: 0.12; }

.layout-a-inner {
  display: flex; width: 100%; height: 100%;
  align-items: center; padding: var(--margin);
}

.frosted-card {
  width: 40%; min-height: 60%;
  background: rgba(255,255,255,0.14);
  border: 1px solid rgba(255,255,255,0.32);
  border-radius: 1.2em;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding: 8% 7%;
  display: flex; flex-direction: column; justify-content: center; gap: 0.6em;
  flex-shrink: 0;
}
.frosted-card p { color: rgba(255,255,255,0.85); font-size: clamp(0.65rem, 1.6vh, 0.9rem); line-height: 1.55; }

.badge-pill {
  display: inline-block;
  background: var(--green-mid); color: #fff;
  border-radius: 2em; padding: 0.25em 0.9em;
  font-size: clamp(0.55rem, 1.3vh, 0.75rem); font-weight: 600;
  margin-bottom: 0.5em;
}

.cover-hero {
  flex: 1; display: flex; flex-direction: column;
  justify-content: center; padding-left: 7%;
}
.display-headline {
  font-size: clamp(2.4rem, 9vh, 5.5rem);
  font-weight: 900; color: #fff; line-height: 1.0;
  letter-spacing: -0.02em;
}
.display-accent { color: var(--green-light); }
.cover-sub { color: rgba(255,255,255,0.7); font-size: clamp(0.7rem, 1.8vh, 1rem); margin-top: 0.6em; }

/* ═══════════════════════════════════════
   LAYOUT B — Left title / right icon list
════════════════════════════════════════ */
.layout-b-inner {
  display: grid; grid-template-columns: 38% 1fr;
  gap: 5%; width: 100%; height: 100%; align-items: center;
}
.b-left { display: flex; flex-direction: column; justify-content: center; }
.b-right { display: flex; flex-direction: column; gap: 1.2vh; justify-content: center; }

.icon-row { display: flex; align-items: flex-start; gap: 0.7em; }
.icon-label { font-size: clamp(0.7rem, 1.8vh, 1rem); line-height: 1.5; padding-top: 0.1em; }
.dark  .icon-label { color: rgba(255,255,255,0.88); }
.white .icon-label { color: var(--grey-body); }

/* ═══════════════════════════════════════
   LAYOUT C — KPI strip
════════════════════════════════════════ */
.kpi-strip {
  display: flex; align-items: center; justify-content: space-between;
  flex: 1; margin-top: 1.5vh;
}
.kpi-col { flex: 1; text-align: center; padding: 0 2%; }
.kpi-num {
  font-size: clamp(1.6rem, 5.5vh, 3.2rem); font-weight: 800; line-height: 1;
  color: var(--green-mid);
}
.dark .kpi-num { color: var(--green-light); }
.kpi-lbl { font-size: clamp(0.6rem, 1.4vh, 0.8rem); margin-top: 0.3em; opacity: 0.75; }
.kpi-arrow {
  font-size: clamp(1rem, 2.8vh, 1.6rem); color: var(--green-mid);
  padding: 0 1%; flex-shrink: 0;
}

/* ═══════════════════════════════════════
   LAYOUT D — Quadrant matrix
════════════════════════════════════════ */
.quadrant-grid {
  position: relative; flex: 1; margin-top: 1.5vh;
  display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr;
  gap: 2px;
}
.quad {
  display: flex; align-items: center; justify-content: center;
  padding: 4%; font-size: clamp(0.65rem, 1.6vh, 0.9rem);
  text-align: center;
}
.dark  .quad { background: rgba(255,255,255,0.06); color: rgba(255,255,255,0.85); }
.white .quad { background: rgba(0,0,0,0.03); color: var(--grey-body); }

.quad-h-line, .quad-v-line {
  position: absolute; background: var(--green-mid); opacity: 0.5; pointer-events: none;
}
.quad-h-line { top: 50%; left: 0; right: 0; height: 1px; transform: translateY(-50%); }
.quad-v-line { left: 50%; top: 0; bottom: 0; width: 1px; transform: translateX(-50%); }

/* ═══════════════════════════════════════
   LAYOUT E — Chart + stat cards
════════════════════════════════════════ */
.chart-placeholder {
  flex: 1; margin: 1.5vh 0;
  border: 2px dashed var(--green-mid);
  border-radius: 0.8em; display: flex; align-items: center; justify-content: center;
  opacity: 0.5;
}
.dark  .chart-placeholder { background: rgba(255,255,255,0.04); }
.white .chart-placeholder { background: rgba(46,170,94,0.05); }
.chart-placeholder span { font-size: clamp(0.65rem, 1.5vh, 0.85rem); font-style: italic; }

.stat-row { display: flex; gap: 3%; margin-top: 1.2vh; }
.stat-card {
  flex: 1; border-radius: 0.8em; padding: 5% 6%;
  text-align: center;
}
.dark  .stat-card { background: rgba(255,255,255,0.12); }
.white .stat-card { background: rgba(46,170,94,0.08); border: 1px solid rgba(46,170,94,0.25); }
.stat-num { font-size: clamp(1.2rem, 4vh, 2.2rem); font-weight: 800; color: var(--green-mid); }
.dark .stat-num { color: var(--green-light); }
.stat-label { font-size: clamp(0.55rem, 1.3vh, 0.75rem); margin-top: 0.25em; opacity: 0.7; }

/* ═══════════════════════════════════════
   LAYOUT F — Dark hero
════════════════════════════════════════ */
.layout-f { align-items: center; justify-content: center; }
.layout-f-inner {
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  width: 100%; gap: 4vh; text-align: center;
}
.f-icons { display: flex; gap: 5%; justify-content: center; width: 70%; }
.f-col { display: flex; flex-direction: column; align-items: center; gap: 1.2vh; flex: 1; }
.f-label { font-size: clamp(0.65rem, 1.6vh, 0.9rem); color: rgba(255,255,255,0.88); text-align: center; }

/* ═══════════════════════════════════════
   LAYOUT G — Two-stat opportunity
════════════════════════════════════════ */
.layout-g-inner {
  display: grid; grid-template-columns: 52% 1fr;
  gap: 4%; width: 100%; height: 100%; align-items: center;
}
.g-left { display: flex; flex-direction: column; justify-content: center; }
.g-right { display: flex; flex-direction: column; gap: 4%; justify-content: center; }
.g-stat { display: flex; flex-direction: column; align-items: flex-start; gap: 0.4vh; }
.g-num { font-size: clamp(1.4rem, 4.5vh, 2.6rem); font-weight: 800; color: var(--green-mid); }
.dark .g-num { color: var(--green-light); }
.g-lbl { font-size: clamp(0.6rem, 1.4vh, 0.8rem); opacity: 0.75; }

/* ── Controls ── */
.controls {
  position: fixed; bottom: 1.2rem; left: 50%; transform: translateX(-50%);
  display: flex; align-items: center; gap: 1rem;
  background: rgba(0,0,0,0.55); backdrop-filter: blur(8px);
  border-radius: 2em; padding: 0.4em 1.1em;
  z-index: 100;
}
.controls button {
  background: none; border: none; color: #fff; font-size: 1.1rem;
  cursor: pointer; padding: 0.2em 0.5em; border-radius: 0.4em;
  transition: background 0.15s;
}
.controls button:hover { background: rgba(255,255,255,0.15); }
#counter { color: rgba(255,255,255,0.7); font-size: 0.8rem; min-width: 4.5em; text-align: center; font-family: var(--font); }

/* ── Print / PDF ── */
@media print {
  body { background: none; overflow: visible; }
  .deck-wrapper { display: block; width: 100%; height: auto; }
  .slide {
    display: flex !important;
    position: relative;
    width: 100%; height: auto;
    min-height: 56.25vw;
    page-break-after: always;
    break-after: page;
  }
  .controls { display: none; }
}
"""

# ── JS ────────────────────────────────────────────────────────────────────────
JS = """
const slides = document.querySelectorAll('.slide');
let cur = 0;

function show(n) {
  cur = Math.max(0, Math.min(n, slides.length - 1));
  slides.forEach((s, i) => s.classList.toggle('active', i === cur));
  document.getElementById('counter').textContent = (cur + 1) + ' / ' + slides.length;
}

function next() { show(cur + 1); }
function prev() { show(cur - 1); }

document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight' || e.key === ' ')  { e.preventDefault(); next(); }
  if (e.key === 'ArrowLeft')                    { e.preventDefault(); prev(); }
  if (e.key === 'f' || e.key === 'F')           { document.documentElement.requestFullscreen?.(); }
  if (e.key === 'Home')                          { show(0); }
  if (e.key === 'End')                           { show(slides.length - 1); }
});

// Click right half to advance, left half to go back
document.querySelector('.deck-wrapper').addEventListener('click', e => {
  const mid = window.innerWidth / 2;
  e.clientX > mid ? next() : prev();
});

show(0);
"""

# ── HTML template ─────────────────────────────────────────────────────────────
def build_html(deck_title: str, slides: list[dict]) -> str:
    slide_html = "\n".join(render_slide(d, i == 0) for i, d in enumerate(slides))
    total = len(slides)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(deck_title)}</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="deck-wrapper">
{slide_html}
</div>
<div class="controls">
  <button onclick="prev()" title="Previous (←)">&#8592;</button>
  <span id="counter">1 / {total}</span>
  <button onclick="next()" title="Next (→)">&#8594;</button>
</div>
<script>
{JS}
</script>
</body>
</html>"""


# ── Entry point ───────────────────────────────────────────────────────────────
def convert(md_path: str, out_path: str | None = None) -> str:
    if not out_path:
        out_path = str(Path(md_path).with_suffix(".html"))

    deck_title, slides = parse_blueprint(md_path)
    if not slides:
        print("ERROR: No slides found in blueprint.")
        sys.exit(1)

    html_out = build_html(deck_title, slides)
    Path(out_path).write_text(html_out, encoding="utf-8")

    size_kb = Path(out_path).stat().st_size // 1024
    print(f"output_path: {out_path}  ({size_kb} KB, {len(slides)} slides)")
    return out_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/blueprint_to_html.py <blueprint.md> [output.html]")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
