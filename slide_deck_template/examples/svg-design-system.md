# SVG Slide Design System

This is the authoritative design specification for all SVG slides produced by the `/slide-deck` skill and `slide-generator` agent. Apply every rule below to every slide without exception.

---

## Canvas

```
width="1280" height="720" viewBox="0 0 1280 720"
```

Safe zone: 60 px margin on all sides — keep all content between x=60–1220, y=60–660.

---

## Color Tokens

Hex values only — **never** `rgb()` or `rgba()`.

| Token | Hex | Use |
|-------|-----|-----|
| `GREEN_DARK` | `#1A6B3A` | Dark slide backgrounds |
| `GREEN_MID` | `#2EAA5E` | Icon badges, divider lines, accent elements |
| `GREEN_LIGHT` | `#5CDB8F` | Gradient highlights, cover accent word |
| `WHITE` | `#FFFFFF` | Text and cards on dark slides |
| `NEAR_BLACK` | `#1A1A2E` | Neutral headline on white slides |
| `GREY_BODY` | `#4A4A6A` | Body text and captions on white slides |

For transparency use the SVG `opacity` attribute — **never** `rgba()`.

---

## Typography

Apply `font-family="Poppins, DM Sans, Inter, sans-serif"` to **every** text element.

| Role | `font-size` | `font-weight` |
|------|-------------|---------------|
| Cover display title | `80` | `900` |
| Slide headline | `36` | `700` |
| Section subhead | `18` | `600` |
| KPI number | `44` | `700` |
| Body / bullets | `16` | `400` |
| Caption / slide number | `11` | `400` |

**Text color:**
- Dark slides → `fill="#FFFFFF"` on all text
- White slides → headline `#1A1A2E`, accent word `#2EAA5E`, body `#4A4A6A`

---

## Layout Patterns

Use the pattern letter assigned in the blueprint spec. Never invent a new layout — choose the closest match.

### A — Cover / Full-bleed

Background: radial gradient `GREEN_LIGHT` at top-center → `GREEN_DARK` at edges (define in `<defs>`).

- **Left panel** (x=60–560): frosted card `<rect rx="16" fill="#FFFFFF" opacity="0.18" stroke="#FFFFFF" stroke-opacity="0.4" stroke-width="1"/>`. Contains subtitle and session badges.
- **Right panel** (x=580–1220): display headline 80pt.
- Add soft radial glow ellipse top-right, `opacity="0.15"`, `GREEN_LIGHT` fill.

### B — Left title / Right icon-row list

- **Left** (x=60–500): headline 36pt two-tone, one-line descriptor 13pt, divider line `GREEN_MID`.
- **Right** (x=540–1220): stacked rows, each `<circle r="22" fill="#2EAA5E"/>` badge + label 20pt SemiBold + descriptor 13pt. Row height ≈72px, first row y=200.

### C — Horizontal KPI strip (3 columns)

Three 360px-wide columns. Each: KPI number 44pt, label 11pt, description 13pt.
Separator arrows "→" in `GREEN_MID` centered between columns.

### D — 2×2 Quadrant matrix

Two crossing lines through center (640, 360). Axis labels 13pt at ends. Content 13pt in each quadrant.

### E — Chart + stat cards

- Top 55% (y=60–450): rounded-rect placeholder, dashed `GREEN_MID` border.
- Bottom 35% (y=460–660): two stat cards, each bold number 36pt + label 11pt.

### F — Dark hero / objectives

Background: `GREEN_DARK`. Headline centered 36pt Bold White y≈160.
3–5 icon-badge rows centered x=640 from y≈260, spacing 72px. Circle badge r=22 `GREEN_MID` + white label 14pt.
Soft radial glow top-center `GREEN_LIGHT` opacity 0.12.

### G — Two-stat opportunity

- **Left 48%** (x=60–580): body paragraph 13pt + optional subhead 18pt.
- **Right 48%** (x=620–1220): two stats stacked. Each: circle badge r=22 `GREEN_MID`, bold number 40pt, label 11pt.

---

## Recurring Elements

**Divider rule (white slides only)** — place after the headline:

```svg
<line x1="60" y1="{headline_bottom+12}" x2="1220" y2="{headline_bottom+12}"
      stroke="#2EAA5E" stroke-width="1.5"/>
```

**Slide number** — bottom-right on every slide:

```svg
<text x="1215" y="700" font-family="Poppins, sans-serif" font-size="11"
      text-anchor="end" fill="{#FFFFFF or #4A4A6A}">{N}</text>
```

---

## SVG Rules (non-negotiable)

1. Opening tag must be exactly: `<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">`
2. All styles must be inline SVG presentation attributes — **no** `<style>` tags, **no** CSS classes.
3. **Never** use `rgb()` or `rgba()` — hex colors only.
4. **Never** use `<use>`, `<symbol>`, `<foreignObject>`, or `<script>`.
5. Gradients **must** be defined in `<defs>` and referenced via `url(#id)`.
6. Text must use `<text>` elements with explicit `x`, `y`, `font-size`, `font-weight`, `font-family`, `fill`. Use `<tspan dy="1.4em">` for wrapped lines.
7. All coordinates are integers or at most 1 decimal place.
8. Keep each file under 60 KB.

---

## Background Alternation Rule

Dark-green and white slides must alternate throughout the deck. **Never place more than 2 consecutive slides of the same background mode.** Use this rhythm to signal topic transitions and prevent visual fatigue.
