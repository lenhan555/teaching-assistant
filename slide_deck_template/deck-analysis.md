# Pitch Deck Template — Design Analysis
**Source:** `_template/Pitch-Deck-for-Startups-Small-Businesses.jpg`
**Template sample brand:** MaxLive — Health Insurance made Simple
**Analyzed:** 2026-05-24

---

## 1. Color System

### 1.1 Palette Overview

The template uses a strict monochromatic green palette with white as the only neutral. Every slide can be traced back to three base values:

| Token | Hex Estimate | Description |
|-------|-------------|-------------|
| `green-dark` | `#1A6B3A` | Deep forest green — primary background |
| `green-mid` | `#2EAA5E` | Medium green — icons, badges, borders |
| `green-light` | `#5CDB8F` | Lime/bright green — gradient top, headline accents |
| `white` | `#FFFFFF` | Text on dark slides, card backgrounds |
| `near-black` | `#1A1A2E` | Headings on white-background slides |
| `grey-body` | `#4A4A6A` | Body text on white slides |

### 1.2 Background Modes

Two distinct background modes alternate throughout the deck, creating visual rhythm:

**Mode A — Dark Green (immersive)**
Used on: Cover, Business Model, Product/Features slide
- Full-bleed radial gradient from `green-light` top-center to `green-dark` bottom
- Creates depth; white text reads cleanly at all sizes
- Signals importance — reserved for the highest-impact slides

**Mode B — White (clean)**
Used on: Competitive Landscape, Summary, Growth Strategy, Market Size, Opportunity
- Pure white background with green used only for headlines and icons
- Allows dense data (charts, tables, icon grids) to breathe
- Two-tone headline technique carries the brand color into every white slide

### 1.3 Gradient Technique

Two gradient types are visible:

1. **Radial background gradient** — soft circle of `green-light` blooms from upper-center, fading to `green-dark` at edges. Adds atmosphere without texture.
2. **Frosted-card gradient** — lighter green panel sits inside the darker background (Cover slide company card). The inner card uses a lighter version of the same green, creating a card-within-background layering effect.

### 1.4 Color Usage Rules (for PPT replication)

| Element | Color |
|---------|-------|
| Dark slide background | Radial gradient `green-light` → `green-dark` |
| White slide background | Pure white `#FFFFFF` |
| Slide title (white slides) | Near-black for neutral word + `green-mid` for accent word |
| Slide title (dark slides) | White for all words |
| Icon badge fill | `green-mid` circle with white icon |
| Stat numbers (dark slides) | White, extra-bold |
| Stat numbers (white slides) | `green-dark` or near-black, extra-bold |
| Body text (white slides) | `grey-body` |
| Body text (dark slides) | White at ~80% opacity |
| Arrow / connector | White (dark slides) or `green-mid` (white slides) |
| Decorative gems | Semi-transparent `green-light` with inner highlight |

---

## 2. Typography

### 2.1 Font Choice

The template uses a single geometric sans-serif family throughout — likely **Poppins** or a similar rounded sans-serif (Inter, DM Sans). Key characteristics:
- Rounded terminals on letters like `a`, `e`, `g`
- Uniform stroke width (no thick/thin contrast)
- Tight default letter-spacing at large sizes, slightly looser at body sizes
- Works equally well at display scale (80pt) and caption scale (9pt)

### 2.2 Type Scale

| Role | Weight | Size Estimate | Color |
|------|--------|--------------|-------|
| Cover display (`Pitch Deck`) | Extra-Bold / Black (900) | ~80pt | White |
| Cover subtitle | Regular (400) | ~22pt | White |
| Company name on cover card | Bold (700) | ~24pt | White |
| Tagline on cover card | Regular (400) | ~14pt | White |
| Slide title — neutral word | Bold (700) | ~32–40pt | Near-black |
| Slide title — accent word | Bold (700) | ~32–40pt | `green-mid` |
| Section subhead | Semi-Bold (600) | ~18pt | `green-mid` or near-black |
| KPI / stat number | Extra-Bold (800) | ~36–48pt | White or near-black |
| KPI label | Regular (400) | ~10pt | Grey or white |
| Body paragraph | Regular (400) | ~10–11pt | `grey-body` |
| Caption / footer | Regular (400) | ~8pt | Grey at 60% opacity |

### 2.3 The Two-Tone Headline Technique

This is the single most distinctive typographic decision in the template. Every slide title on a white background splits into two colors:

```
"Competitive  Landscape"
 ^^^^^^^^^^^  ^^^^^^^^^^^
 near-black   green-mid
```

Additional examples visible:
- "The **Summary**" — "The" in black, "Summary" in green
- "Business **Model**" — "Business" in black, "Model" in green
- "Growth **Strategy**" — "Growth" in black, "Strategy" in green
- "Market **Size**" — "Market" in black, "Size" in green
- "A huge **Opportunity** in health" — key noun in green, rest in black

**How to replicate in PowerPoint:**
Use two separate text boxes overlapping horizontally, or use a single text box with character-level color formatting (select specific words → change font color). Do NOT use two fonts — keep weight and size identical, only color changes.

### 2.4 Text Alignment

| Slide type | Alignment |
|-----------|-----------|
| Dark full-bleed slides | Center or left — varies by content |
| White content slides | Left-aligned throughout |
| KPI stat numbers | Center within their column |
| Cover display headline ("Pitch Deck") | Left-aligned, large |
| Icon + label pairs | Center-aligned within column |

### 2.5 Line Spacing and Hierarchy Spacing

- Slide titles have ~1.15× line height
- Body text has ~1.5–1.6× line height for readability
- Visual gap between title and content area: approximately 24–32pt equivalent
- KPI numbers and their labels are tightly stacked (~1.0× line height) to read as a unit

---

## 3. Layout Patterns

### 3.1 Grid System

All slides use an implicit **12-column grid** with generous margins (~5–7% of slide width on each side). Content never bleeds into the margin except background elements and decorative shapes.

### 3.2 Pattern A — Full-Bleed Split (Cover)

```
┌─────────────────────────────────────────┐
│  ┌──────────────┐                       │
│  │  BRAND CARD  │   DISPLAY HEADLINE    │
│  │  Company     │                       │
│  │  Tagline     │   Subtitle text       │
│  │  Mission     │                       │
│  └──────────────┘                       │
└─────────────────────────────────────────┘
```
- Left ~45% holds a floating card on the gradient background
- Right ~55% holds the large display title
- Background is full-bleed dark green gradient
- **PPT use:** Best for title/cover slides. The floating card can be a shape with a lighter fill and subtle drop shadow.

### 3.3 Pattern B — Left Title / Right Icon List (Summary, Growth Strategy)

```
┌─────────────────────────────────────────┐
│                                         │
│  Large Heading     [icon] Item text     │
│  Optional subtext  [icon] Item text     │
│                    [icon] Item text     │
│                                         │
└─────────────────────────────────────────┘
```
- Left 40%: oversized heading, optional one-liner
- Right 60%: stacked rows of icon badge + label + short description
- **PPT use:** Great for lists that need visual structure without bullet points. Replace bullets with circular icon badges.

### 3.4 Pattern C — Horizontal KPI Strip (Business Model)

```
┌─────────────────────────────────────────┐
│  Slide Title                            │
│  ─────────────────────────────────────  │
│  [ STAT A ] ──→ [ STAT B ] ──→ [ STAT C]│
│   label a         label b        label c │
│   body text       body text      body   │
└─────────────────────────────────────────┘
```
- Three equal columns, each with a large bold number, label, and supporting text
- Arrow connectors between columns suggest a flow or causal relationship
- **PPT use:** Use for before/after metrics, funnel stages, or cause→effect data. Keep to 3 stats maximum.

### 3.5 Pattern D — 2×2 Quadrant Matrix (Competitive Landscape)

```
┌─────────────────────────────────────────┐
│  Slide Title                            │
│         Y-AXIS LABEL                   │
│    ┌──────────┬──────────┐             │
│    │  logo    │  logo    │             │
│  X │  logo  ★ │  logo    │ X           │
│    │          │          │             │
│    └──────────┴──────────┘             │
│         Y-AXIS LABEL                   │
└─────────────────────────────────────────┘
```
- Four quadrants with competitor logos placed by position
- Company's own logo highlighted with a colored ring or larger treatment
- **PPT use:** Draw two crossing lines, add text boxes for axis labels, use image placeholders for logos. Highlight own company position with a circle shape + green fill.

### 3.6 Pattern E — Map + Stat Cards (Market Size)

```
┌─────────────────────────────────────────┐
│  Market  Size                           │
│  ┌────────────────────────┐            │
│  │    [US MAP GRAPHIC]    │            │
│  └────────────────────────┘            │
│  ┌──────────┐  ┌──────────┐            │
│  │  $789K   │  │  $674K   │            │
│  │  label   │  │  label   │            │
│  └──────────┘  └──────────┘            │
└─────────────────────────────────────────┘
```
- Map fills ~60% of slide height, centered
- Two stat callout cards sit below the map, side by side
- **PPT use:** Use a PNG/SVG map image as a picture placeholder, apply green-tint color wash. Place stat cards as rounded-rectangle shapes with bold text inside.

### 3.7 Pattern F — Dark Hero Slide (Product/Features)

```
┌─────────────────────────────────────────┐
│  [Full dark green background]           │
│                                         │
│    Main headline — white, bold          │
│    Sub-copy — white, smaller            │
│                                         │
│   [icon]     [icon]     [icon]          │
│   label      label      label           │
└─────────────────────────────────────────┘
```
- Full-bleed dark green, all text white
- Three icons centered in a row with labels below
- **PPT use:** Use as a visual "break" slide between sections. The contrast with surrounding white slides commands attention and signals a new topic.

### 3.8 Pattern G — Two-Stat Opportunity Slide

```
┌─────────────────────────────────────────┐
│  A huge Opportunity in health           │
│  Body text column left                  │
│                                         │
│  ┌─────────────┐   ┌─────────────┐     │
│  │  $36bn      │   │  96%        │     │
│  │  label text │   │  label text │     │
│  └─────────────┘   └─────────────┘     │
└─────────────────────────────────────────┘
```
- Two large stats side by side, each with an icon badge above
- Supporting paragraph text runs left of or above the stats
- **PPT use:** Effective for "size of prize" or impact slides. Keep to 2 stats max so each has room to breathe.

---

## 4. Decorative Elements

### 4.1 3D Gem / Crystal Shapes

Small translucent green 3D gemstone shapes appear at slide corners and edges throughout the deck. Characteristics:
- **Shape:** Multi-faceted low-poly crystal or gem — like a rounded diamond or emerald shape
- **Color:** Semi-transparent `green-light` with a bright specular highlight on one face
- **Size:** Small (roughly 40–80px at slide resolution); never compete with content
- **Placement:** Corners (top-right, bottom-left most common), occasionally mid-edge
- **Purpose:** Adds a premium, modern feel; breaks the flatness of gradient backgrounds

**PPT replication:** Use 3D shape presets (PowerPoint has basic 3D shapes under Insert → 3D Models, or use SmartArt / shapes with bevel effects). Alternatively, import a transparent PNG of a crystal shape and apply a green color tint.

### 4.2 Frosted-Glass Cards

The Summary slide and Cover card use a frosted-glass (semi-transparent panel) effect:
- **Fill:** White or light green at ~15–25% opacity
- **Border:** Thin 1px white border at ~40% opacity
- **Blur:** Background behind the card appears softly blurred
- **Drop shadow:** Very soft, large-radius shadow (outer, black at 18% opacity, 8px offset, 32px blur radius)

**PPT replication:** In PowerPoint, use a rectangle shape → Format Shape → Fill: Solid, white at 20% transparency → Line: white at 40% transparency → Shadow: Outer, soft, large blur. Background blur is not natively supported in PPT — simulate by placing a blurred copy of the background image clipped behind the card shape.

### 4.3 Circular Icon Badges

Every icon in the deck uses the same badge system:
- **Container:** Filled circle in `green-mid`
- **Icon:** White line-art icon centered inside (~50% of badge diameter)
- **Size:** Consistent badge diameter across all slides (~40–48pt)
- **Icon style:** Thin stroke, 2px line weight, rounded line caps — no fills

**PPT replication:** Insert a circle shape (hold Shift to constrain), fill with `green-mid`, no border. Insert an icon from PowerPoint's icon library (Insert → Icons) on top, set to white. Group the two. Resize maintaining proportions.

### 4.4 Gradient Arrow / Growth Motif

The Growth Strategy slide features an upward-pointing arrow graphic:
- Rendered as a gradient from `green-light` (bottom) to `green-mid` (top)
- Appears organic / hand-drawn rather than a standard PowerPoint arrow
- Functions as a visual metaphor for upward growth

**PPT replication:** Use a custom arrow shape (or a chevron + triangle), apply a gradient fill from bottom to top matching the green palette. Add a soft glow effect (Format Shape → Glow) in `green-light` at low intensity.

### 4.5 Radial Soft-Light Circles

On dark-green background slides, soft blurred circular light spots appear in the upper area of the background:
- Appear as out-of-focus light sources in `green-light`
- Very low opacity (~20–30%), large radius
- Create a sense of depth and atmosphere in what would otherwise be a flat gradient

**PPT replication:** Insert a circle shape → Fill: `green-light`, no border → Soft Edges: set to ~40–60pt (Format Shape → Glow and Soft Edges) → set transparency to 70–80%. Layer 2–3 of these at different sizes and opacities in the background.

### 4.6 Thin Accent Rules / Dividers

Horizontal lines appear beneath some section titles on white slides:
- **Weight:** 1–2px
- **Color:** `green-mid` or `green-light`
- **Width:** Spans only the content column, not full slide width
- **Purpose:** Separates headline from body content area without adding visual weight

**PPT replication:** Insert → Shapes → Line. Set line color to `green-mid`, weight 1.5pt, length matching content column width.

### 4.7 Geographic Map with Color Wash

The Market Size slides use a US state map:
- Base map is a flat outline of US states
- Selected regions filled with `green-mid` or `green-dark` to indicate market focus
- Non-highlighted states filled with a very light grey

**PPT replication:** Use a free SVG US map (editable state by state). Import as SVG, then break apart (right-click → Group → Ungroup) to recolor individual states. Alternatively use a PNG map and apply a green Duotone or Color Wash picture effect.

---

## 5. PPT Slide Design Principles Observed

Beyond the four areas above, this template demonstrates several best practices worth applying to any slide deck:

### 5.1 Visual Rhythm via Alternating Backgrounds
Dark and white slides alternate deliberately — never more than 2–3 of the same mode in a row. This prevents fatigue and signals topic transitions without needing section-break slides.

### 5.2 The 1-Concept-Per-Slide Rule
Each slide communicates exactly one idea. Business Model = how money works. Opportunity = market size. The slide title is the conclusion; the content is the evidence. No slide tries to do two jobs.

### 5.3 Data Before Prose
Quantified statistics (numbers, percentages, dollar values) appear visually dominant — large, bold, high-contrast. Supporting prose is secondary in size and visual weight. In presentations, numbers land harder than sentences.

### 5.4 Consistent Slide Margin / Safe Zone
Content never reaches the slide edge. Approximately 5–7% margin on all sides is maintained. Footer and slide number live inside this margin at ~8pt. Maintain this safe zone to prevent projector/screen edge clipping.

### 5.5 Icon Language Consistency
All icons share the same: stroke weight, style (line-only, no fill), and badge container. Mixing icon styles (some filled, some outlined, some colored) creates visual noise. Pick one icon library and use it exclusively.

### 5.6 Three-Column Maximum for Icon Grids
Feature slides use exactly three icon columns. Four or more columns at standard slide width compress each item below comfortable reading size and reduce impact.

### 5.7 Slide Number Placement
Slide numbers are positioned bottom-right at low opacity. They are present but not distracting — readable if needed, invisible if not. Standard placement for business presentations.

---

## 6. Elements Checklist for Recreating This Template in PowerPoint

| Element | PPT Method |
|---------|-----------|
| Dark green radial gradient background | Format Background → Gradient Fill → Radial, set color stops |
| Frosted-glass card | Rectangle shape → 20% white fill + 40% white border + soft shadow |
| Two-tone headline | Single text box, select accent word, change font color only |
| Circular icon badge | Circle shape (green fill) + white icon from Insert → Icons |
| 3D gem decoration | Insert → 3D Models or custom gem PNG with transparency |
| Soft-light background circles | Circle shapes with Soft Edges + high transparency, stacked |
| KPI number + label | Two text boxes, grouped: large bold number above, small label below |
| Arrow connector between KPIs | Insert → Shapes → Arrow, match to slide color scheme |
| Horizontal divider line | Insert → Shapes → Line, 1.5pt, green-mid color |
| US map with state coloring | SVG map imported and ungrouped for per-state coloring |
| Quadrant matrix | Two crossing lines + four text boxes + image placeholders for logos |
| Slide footer + page number | Insert → Header & Footer, or text boxes in master slide |
