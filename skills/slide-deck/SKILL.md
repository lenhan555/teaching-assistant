# slide-deck

Generate a fully structured PowerPoint slide deck for this project. Combines the visual design system from `slide_deck_template/deck-analysis.md` with agent-researched content to produce a slide-by-slide blueprint ready to build in PowerPoint.

## Usage

```
/slide-deck "<topic>" [--slides N] [--audience <audience>] [--style <style>] [--save]
```

**Arguments:**
- `topic` — required. What the deck is about. E.g. `"SQL Training Program"`, `"Startup Pitch for EdTech"`, `"Q3 Business Review"`
- `--slides N` — target slide count (default: 10). Min 5, max 20.
- `--audience <audience>` — who will see this. E.g. `investors`, `students`, `executives`, `clients` (default: `general`)
- `--style <style>` — `pitch` (investor/startup narrative), `training` (educational, step-by-step), `report` (data-heavy, business review) (default: `pitch`)
- `--save` — write the output to `slide_deck_template/decks/<topic-slug>.md`

**Examples:**
```
/slide-deck "SQL Training for Beginners" --style training --audience students --slides 12 --save
/slide-deck "Startup Pitch — EdTech Platform" --style pitch --audience investors --save
/slide-deck "Q3 Teaching Assistant Review" --style report --audience executives --slides 8
```

---

## Execution Steps

### Step 1 — Parse Arguments

Extract from the user's invocation:
- `TOPIC` — the deck subject (required)
- `SLIDES` — target count (default 10)
- `AUDIENCE` — who it's for (default: general)
- `STYLE` — `pitch`, `training`, or `report` (default: pitch)
- `SAVE` — boolean, true if `--save` is present

---

### Step 2 — Load the Design System

Read the full design reference:
```
/Users/leopham/Documents/Teaching Assistant/slide_deck_template/deck-analysis.md
```

Internalize and apply throughout generation:
- **Color system** — dark green mode vs white mode slides; color token usage per element
- **Typography** — type scale, two-tone headline technique, font weight rules
- **Layout patterns** — Pattern A through G (Cover, Icon List, KPI Strip, Quadrant, Map, Dark Hero, Two-Stat)
- **Decorative elements** — gem shapes, frosted cards, icon badges, soft-light circles, accent lines
- **PPT principles** — 1 concept per slide, data before prose, alternating background rhythm, 3-column max

---

### Step 3 — Research Content (Agent Phase)

Use `WebSearch` and `WebFetch` to gather current, accurate content relevant to `TOPIC` and `AUDIENCE`.

**Research goals:**
- Key facts, statistics, and data points that can anchor slides
- Industry context and market sizing (for pitch style)
- Structured learning objectives and concept breakdowns (for training style)
- KPIs, trends, and performance data (for report style)

**Search queries (adapt to TOPIC):**
- `"[TOPIC] statistics [current year]"`
- `"[TOPIC] market size trends"`
- `"[TOPIC] best practices overview"`
- `"[TOPIC] for [AUDIENCE] introduction"`

Also check for any existing content files under:
```
/Users/leopham/Documents/Teaching Assistant/
```
If relevant files exist (e.g. SQL training docs in `skills/`), read them as primary source material.

---

### Step 4 — Select the Slide Structure

Based on `STYLE`, use the appropriate narrative structure:

#### Pitch Structure
```
1.  Cover               → Company / topic + tagline
2.  Problem             → Pain point with data
3.  Solution            → How this addresses the problem
4.  Opportunity         → Market size / why now
5.  Product / Features  → What it does (3-feature hero slide)
6.  Business Model      → How money is made (KPI strip)
7.  Market Size         → TAM / SAM with visual
8.  Competitive         → Quadrant positioning
9.  Traction            → Proof points / milestones
10. Growth Strategy     → Scale plan (3 pillars)
11. Team                → Key people
12. The Ask             → Raise amount, use of funds
```

#### Training Structure
```
1.  Cover               → Course title + instructor / program
2.  Agenda              → What we will cover today (icon list)
3.  Learning Objectives → 3 outcomes students will achieve
4.  Context / Why       → Why this topic matters (two-stat)
5+. Concept Slides      → One concept per slide (dark hero for key concepts)
N-2. Practice / Exercises → Hands-on activity prompt
N-1. Summary / Recap    → Key takeaways (icon list)
N.  Next Steps          → What comes next / resources
```

#### Report Structure
```
1.  Cover               → Report title + period + team
2.  Executive Summary   → 3-5 bullet highlights (icon list)
3+. Section Slides      → One metric area per slide (KPI strip or two-stat)
N-2. Analysis           → Trends, observations, root causes
N-1. Recommendations    → Action items (3-column icon grid)
N.  Appendix / Sources  → Supporting data
```

Adjust slide count to match `--slides N` by expanding or contracting concept/section slides.

---

### Step 5 — Generate the Slide Blueprint

For every slide produce a complete specification block using this format:

```
---
## Slide [N] — [Slide Title]

**Layout Pattern:** [Pattern name from deck-analysis.md — e.g. Pattern C: KPI Strip]
**Background Mode:** [Dark Green | White]
**Headline:** [Exact headline text — apply two-tone technique: mark accent word with **bold**]

### Content
[Structured content for this slide — bullet points, stats, table, or prose as appropriate]

### Visual Spec
- **Left zone:** [what goes here]
- **Right zone / main area:** [what goes here]
- **Icons:** [which icon concepts to use, e.g. "shield icon for security, chart icon for growth"]
- **Stats to highlight:** [any numbers that should be displayed in large bold KPI format]
- **Decorative:** [gem corner, soft-light circle, frosted card, accent line, etc.]

### PPT Build Notes
[Specific PowerPoint instructions for this slide — shape types, layout, any non-obvious steps]
---
```

Apply these rules across all slides:
- Never use the same Background Mode on more than 2 consecutive slides
- Every white-background slide title uses the two-tone headline technique
- Every dark-green slide title is fully white
- Include at least one data point (stat, percentage, or figure) on every slide except Cover and Team
- Icon badges: use consistent circular badge style throughout
- Slide footer: include topic name left, slide number right, at ~8pt grey

---

### Step 6 — Produce the Full Output Document

Structure the final output as:

```markdown
# [TOPIC] — Slide Deck Blueprint
**Style:** [pitch | training | report]
**Audience:** [audience]
**Slide count:** [N]
**Generated:** [DATE]
**Design system:** slide_deck_template/deck-analysis.md

---

## Design Tokens (apply throughout)
| Token | Value |
|-------|-------|
| green-dark | #1A6B3A |
| green-mid | #2EAA5E |
| green-light | #5CDB8F |
| white | #FFFFFF |
| near-black | #1A1A2E |
| grey-body | #4A4A6A |
| Font | Poppins (or system substitute: DM Sans, Inter) |

---

## Slide-by-Slide Blueprint
[all slide blocks from Step 5]

---

## Build Checklist
- [ ] Set slide dimensions to 33.87cm × 19.05cm (16:9 widescreen) in PowerPoint
- [ ] Install or match font: Poppins / DM Sans / Inter
- [ ] Create Slide Master with dark-green and white layout variants
- [ ] Define color theme with the 6 design tokens above
- [ ] Build reusable icon badge component (circle shape + white icon, grouped)
- [ ] Add gem decoration PNGs to slide master as background elements
- [ ] Set default footer: topic name left, slide number right, 8pt grey
- [ ] Apply soft-light circle shapes to all dark-green slide masters

## Content Sources
[list of URLs or local files used for research]
```

---

### Step 7 — Save (only if `--save` is set)

Write the output to:
```
/Users/leopham/Documents/Teaching Assistant/slide_deck_template/decks/<topic-slug>.md
```

Where `<topic-slug>` is the TOPIC converted to lowercase with spaces replaced by hyphens.

Example: `"SQL Training for Beginners"` → `sql-training-for-beginners.md`

Create the `decks/` subfolder if it does not exist.

After saving, report the full file path.

If `--save` is not set, remind the user:
```
Tip: Run with --save to write this blueprint to slide_deck_template/decks/.
```

---

### Step 8 — Respond

Print the full blueprint in the conversation. Always end with a one-paragraph summary of:
- How many slides were generated
- Which layout patterns were used and on which slides
- Which content sources were used
- What the next step is (open PowerPoint, install font, start with the Slide Master)
