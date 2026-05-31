# Pitch Deck Template — Design Analysis
**Source:** `_template/Pitch-Deck-for-Startups-Small-Businesses.jpg`
**Template sample brand:** MaxLive — Health Insurance made Simple
**Analyzed:** 2026-05-24

> **Note:** This document captures design rationale and context only. All implementable values — hex codes, font sizes, coordinates, SVG rules — live exclusively in `svg-design-system.md`. Read that file before generating any slides.

---

## 1. Color System

### 1.1 Palette Overview

The template uses a strict monochromatic green palette with white as the only neutral. Every slide can be traced back to three base values: a deep forest green for dark backgrounds, a medium green for icons and accents, and a bright lime-green for gradient highlights and emphasis. White provides the neutral counterpoint; near-black and a muted grey-purple handle text on light slides.

### 1.2 Background Modes

Two distinct background modes alternate throughout the deck, creating visual rhythm:

**Mode A — Dark Green (immersive)**
Used on: Cover, Business Model, Product/Features slide
- Full-bleed radial gradient from bright green top-center to deep green at the edges
- Creates depth; white text reads cleanly at all sizes
- Signals importance — reserved for the highest-impact slides

**Mode B — White (clean)**
Used on: Competitive Landscape, Summary, Growth Strategy, Market Size, Opportunity
- Pure white background with green used only for headlines and icons
- Allows dense data (charts, tables, icon grids) to breathe
- Two-tone headline technique carries the brand color into every white slide

### 1.3 Gradient Technique

Two gradient types are visible:

1. **Radial background gradient** — a soft circle of bright green blooms from upper-center, fading to deep green at the edges. Adds atmosphere without texture.
2. **Frosted-card gradient** — a lighter green panel sits inside the darker background (Cover slide company card). The inner card uses a lighter version of the same green, creating a card-within-background layering effect.

### 1.4 Color Usage Rules

| Element | Treatment |
|---------|-----------|
| Dark slide background | Radial gradient: bright green center → deep green edges |
| White slide background | Pure white |
| Slide title (white slides) | Near-black for neutral word + accent green for accent word |
| Slide title (dark slides) | White for all words |
| Icon badge fill | Accent-green circle with white icon |
| Stat numbers (dark slides) | White, extra-bold |
| Stat numbers (white slides) | Deep green or near-black, extra-bold |
| Body text (white slides) | Muted grey-purple |
| Body text (dark slides) | White at reduced opacity |
| Arrow / connector | White (dark slides) or accent green (white slides) |
| Decorative gems | Semi-transparent bright green with inner highlight |

---

## 2. Typography

### 2.1 Font Choice

The template uses a single geometric sans-serif family throughout — likely **Poppins** or a similar rounded sans-serif (Inter, DM Sans). Key characteristics:
- Rounded terminals on letters like `a`, `e`, `g`
- Uniform stroke width (no thick/thin contrast)
- Tight default letter-spacing at large sizes, slightly looser at body sizes
- Works equally well at display scale and caption scale

### 2.2 Type Scale

The hierarchy moves from an extra-bold display title on the cover, down through bold slide titles and semi-bold section subheads, to regular-weight body text and small captions. KPI numbers use extra-bold weight to create visual dominance. See `svg-design-system.md` for the exact size values.

### 2.3 The Two-Tone Headline Technique

This is the single most distinctive typographic decision in the template. Every slide title on a white background splits into two colors:

```
"Competitive  Landscape"
 ^^^^^^^^^^^  ^^^^^^^^^^^
 near-black   accent green
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
| Cover display headline | Left-aligned, large |
| Icon + label pairs | Center-aligned within column |

### 2.5 Line Spacing and Hierarchy Spacing

- Slide titles have tight line height
- Body text has generous line height for readability
- Visual gap between title and content area is consistent across all slides
- KPI numbers and their labels are tightly stacked to read as a unit

---

## 3. Layout Patterns

### 3.1 Grid System

All slides use an implicit 12-column grid with generous margins on each side. Content never bleeds into the margin except background elements and decorative shapes.

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
- Left side holds a floating card on the gradient background
- Right side holds the large display title
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
- Left: oversized heading, optional one-liner
- Right: stacked rows of icon badge + label + short description
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
- Map fills the majority of the slide height, centered
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
- **Color:** Semi-transparent bright green with a bright specular highlight on one face
- **Size:** Small; never compete with content
- **Placement:** Corners (top-right, bottom-left most common), occasionally mid-edge
- **Purpose:** Adds a premium, modern feel; breaks the flatness of gradient backgrounds

**PPT replication:** Use 3D shape presets (PowerPoint has basic 3D shapes under Insert → 3D Models, or use SmartArt / shapes with bevel effects). Alternatively, import a transparent PNG of a crystal shape and apply a green color tint.

### 4.2 Frosted-Glass Cards

The Summary slide and Cover card use a frosted-glass (semi-transparent panel) effect:
- **Fill:** White or light green at low opacity
- **Border:** Thin white border at reduced opacity
- **Blur:** Background behind the card appears softly blurred
- **Drop shadow:** Very soft, large-radius shadow

**PPT replication:** In PowerPoint, use a rectangle shape → Format Shape → Fill: Solid, white at low transparency → Line: white at partial transparency → Shadow: Outer, soft, large blur. Background blur is not natively supported in PPT — simulate by placing a blurred copy of the background image clipped behind the card shape.

### 4.3 Circular Icon Badges

Every icon in the deck uses the same badge system:
- **Container:** Filled circle in accent green
- **Icon:** White line-art icon centered inside
- **Size:** Consistent badge diameter across all slides
- **Icon style:** Thin stroke, rounded line caps — no fills

**PPT replication:** Insert a circle shape (hold Shift to constrain), fill with accent green, no border. Insert an icon from PowerPoint's icon library (Insert → Icons) on top, set to white. Group the two. Resize maintaining proportions.

### 4.4 Gradient Arrow / Growth Motif

The Growth Strategy slide features an upward-pointing arrow graphic:
- Rendered as a gradient from bright green (bottom) to accent green (top)
- Appears organic / hand-drawn rather than a standard PowerPoint arrow
- Functions as a visual metaphor for upward growth

**PPT replication:** Use a custom arrow shape (or a chevron + triangle), apply a gradient fill from bottom to top matching the green palette. Add a soft glow effect (Format Shape → Glow) in bright green at low intensity.

### 4.5 Radial Soft-Light Circles

On dark-green background slides, soft blurred circular light spots appear in the upper area of the background:
- Appear as out-of-focus light sources in bright green
- Very low opacity, large radius
- Create a sense of depth and atmosphere in what would otherwise be a flat gradient

**PPT replication:** Insert a circle shape → Fill: bright green, no border → Soft Edges: set to a large value (Format Shape → Glow and Soft Edges) → set high transparency. Layer two or three of these at different sizes and opacities in the background.

### 4.6 Thin Accent Rules / Dividers

Horizontal lines appear beneath some section titles on white slides:
- **Weight:** Hairline to 2px
- **Color:** Accent green or bright green
- **Width:** Spans only the content column, not full slide width
- **Purpose:** Separates headline from body content area without adding visual weight

**PPT replication:** Insert → Shapes → Line. Set line color to accent green, hairline weight, length matching content column width.

### 4.7 Geographic Map with Color Wash

The Market Size slides use a US state map:
- Base map is a flat outline of US states
- Selected regions filled with accent or deep green to indicate market focus
- Non-highlighted states filled with a very light grey

**PPT replication:** Use a free SVG US map (editable state by state). Import as SVG, then break apart (right-click → Group → Ungroup) to recolor individual states. Alternatively use a PNG map and apply a green Duotone or Color Wash picture effect.

---

## 5. PPT Slide Design Principles Observed

### 5.1 Visual Rhythm via Alternating Backgrounds
Dark and white slides alternate deliberately — never more than two or three of the same mode in a row. This prevents fatigue and signals topic transitions without needing section-break slides.

### 5.2 The 1-Concept-Per-Slide Rule
Each slide communicates exactly one idea. Business Model = how money works. Opportunity = market size. The slide title is the conclusion; the content is the evidence. No slide tries to do two jobs.

### 5.3 Data Before Prose
Quantified statistics (numbers, percentages, dollar values) appear visually dominant — large, bold, high-contrast. Supporting prose is secondary in size and visual weight. In presentations, numbers land harder than sentences.

### 5.4 Consistent Slide Margin / Safe Zone
Content never reaches the slide edge. A consistent margin is maintained on all sides. Footer and slide number live inside this margin at small size. Maintain this safe zone to prevent projector/screen edge clipping.

### 5.5 Icon Language Consistency
All icons share the same stroke weight, style (line-only, no fill), and badge container. Mixing icon styles (some filled, some outlined, some colored) creates visual noise. Pick one icon library and use it exclusively.

### 5.6 Three-Column Maximum for Icon Grids
Feature slides use exactly three icon columns. Four or more columns at standard slide width compress each item below comfortable reading size and reduce impact.

### 5.7 Slide Number Placement
Slide numbers are positioned bottom-right at low opacity. They are present but not distracting — readable if needed, invisible if not. Standard placement for business presentations.

---

## 6. Elements Checklist for Recreating This Template in PowerPoint

| Element | PPT Method |
|---------|-----------|
| Dark green radial gradient background | Format Background → Gradient Fill → Radial, set color stops |
| Frosted-glass card | Rectangle shape → low-opacity white fill + partial-opacity white border + soft shadow |
| Two-tone headline | Single text box, select accent word, change font color only |
| Circular icon badge | Circle shape (green fill) + white icon from Insert → Icons |
| 3D gem decoration | Insert → 3D Models or custom gem PNG with transparency |
| Soft-light background circles | Circle shapes with Soft Edges + high transparency, stacked |
| KPI number + label | Two text boxes, grouped: large bold number above, small label below |
| Arrow connector between KPIs | Insert → Shapes → Arrow, match to slide color scheme |
| Horizontal divider line | Insert → Shapes → Line, hairline weight, accent green color |
| US map with state coloring | SVG map imported and ungrouped for per-state coloring |
| Quadrant matrix | Two crossing lines + four text boxes + image placeholders for logos |
| Slide footer + page number | Insert → Header & Footer, or text boxes in master slide |
