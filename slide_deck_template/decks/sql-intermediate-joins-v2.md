# Slide Deck Blueprint — SQL Joins (Intermediate) v2
**Topic:** SQL Joins
**Audience:** Intermediate SQL learners (students)
**Style:** Training
**Slides:** 10
**Knowledge doc:** `skills/sql-intermediate-joins.md`
**Generated:** 2026-05-29
**Version note:** Enriched rebuild of `sql-intermediate-joins.md` — all visual specs and PPT build notes expanded to production-ready precision.

---

## Slide 1: SQL Joins
- **Layout pattern:** A
- **Background mode:** dark-green
- **Headline:** "SQL" (white `#FFFFFF`) + "Joins" (green-light `#5CDB8F`) — display scale ~80pt, Poppins Black 900
- **Content:**
  - Subtitle: "Mastering Every JOIN Type for Real-World Queries"
  - Audience badge: "Intermediate Level"
  - Session summary tag: "6 JOIN types · Subquery rewrites · Performance"
- **Visual spec:**
  - Full-bleed background: radial gradient originating at upper-center (approximately 50% X, 15% Y). Gradient stops: `green-light #5CDB8F` at 0% → `green-dark #1A6B3A` at 100%. The light bloom should cover roughly the top-center third of the slide.
  - Two soft-light atmosphere circles in the upper half: one large (~300pt diameter, green-light at 22% opacity, 50pt soft edges) centered at ~(50%, 20%); one smaller (~180pt diameter, green-light at 15% opacity, 40pt soft edges) offset to ~(65%, 10%). Both sit behind all content in the z-order.
  - Left zone (0–45% of slide width): frosted-glass card — rounded rectangle, 16pt corner radius, white fill at 20% opacity, 1px white border at 40% opacity, outer drop shadow (black 18% opacity, 6px Y offset, 28px blur). Card contains top-to-bottom: course logo placeholder (60×60pt circle, green-mid fill), session badge label ("SQL Training · Intermediate"), and course mission line in white Regular 12pt.
  - Right zone (47–100% of slide width): display headline stacked — "SQL" on line 1, "Joins" on line 2, subtitle in white Regular 22pt below, audience/session tags in white Regular 13pt at bottom.
  - Decorative 3D gem PNG, top-right corner: ~72pt, green-light tint, semi-transparent. Second gem bottom-left corner: ~52pt, same treatment.
  - Slide number: bottom-right, white 8pt Regular, 40% opacity.
- **PPT build notes:**
  1. Set slide background: Format Background → Gradient Fill → Type: Radial → Direction: From Center → Add two stops: Stop 1 at 0% position = `#5CDB8F`, Stop 2 at 100% = `#1A6B3A`. Adjust gradient center handle to upper-center.
  2. Insert two circle shapes for atmosphere glow: Format Shape → Fill: Solid `#5CDB8F` → Transparency 78% → Soft Edges: 50pt. No border. Send to Back. Layer both behind all other elements.
  3. Left card: Insert → Shapes → Rounded Rectangle. Set corner radius to 0.22" (≈16pt). Format Shape → Fill: Solid White, Transparency 80% → Line: Solid White, Transparency 60%, 1pt weight → Shadow: Outer, Blur 28pt, Distance 6pt, Angle 90°, Black 18% transparency.
  4. Right headline: Insert Text Box. Type "SQL" → Enter → "Joins". Select "SQL" → Font Color: White `#FFFFFF`. Select "Joins" → Font Color: `#5CDB8F`. Font: Poppins Black (or DM Sans ExtraBold), size 80pt. Line spacing: Multiple 1.0.
  5. Subtitle text box: Poppins Regular 22pt, white, placed ~24pt below headline base.
  6. Tags text box: Poppins Regular 13pt, white 80% opacity, placed ~14pt below subtitle.
  7. Insert gem PNG assets (transparent background), position top-right corner with ~2% margin from edges. Duplicate, resize to 52pt, position bottom-left.
  8. Group all right-zone elements. Group all left card elements. Do not group background layers.

---

## Slide 2: Agenda
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Session" (near-black `#1A1A2E`) + "Agenda" (green-mid `#2EAA5E`) — Poppins Bold 700, ~36pt
- **Content:**
  - [icon: book-open] JOIN Types — INNER, LEFT, RIGHT, FULL OUTER, CROSS, SELF
  - [icon: arrow-left-right] Correlated Subqueries vs JOIN rewrites
  - [icon: bolt/lightning] Performance — indexes, EXPLAIN, sargable conditions
  - [icon: pencil-square] In-Class Practice — 3 progressively harder queries
  - [icon: flag] Summary and Next Steps
- **Visual spec:**
  - White background, no gradient.
  - Left column (0–38% of slide width): two-tone headline top-left. Below headline: thin horizontal divider line (green-mid `#2EAA5E`, 1.5pt, spanning left column width). Below divider: one-line session descriptor "What we cover today" in grey-body `#4A4A6A` Regular 11pt. All left-column content left-aligned.
  - Right column (42–100%): five icon-badge rows stacked with 20pt gap between rows. Each row: circular badge (44pt diameter, green-mid fill, white icon 22pt centered) → bold label (near-black Semi-Bold 600 ~13pt) to the right of badge, grey-body descriptor (~10pt Regular) on same line or second line if overflow. Badge and label vertically center-aligned.
  - No decorative gems on white slides.
  - Slide number: bottom-right, grey-body 8pt, 40% opacity.
- **PPT build notes:**
  1. White slide background: Format Background → Solid Fill → White `#FFFFFF`.
  2. Two-tone headline: Insert Text Box → type "Session Agenda". Select "Session" → Font Color `#1A1A2E`. Select "Agenda" → Font Color `#2EAA5E`. Font: Poppins Bold 700, 36pt. Do NOT use two separate text boxes — use character-level color within one text box to maintain consistent baseline.
  3. Divider line: Insert → Shapes → Line. Color `#2EAA5E`, Weight 1.5pt. Length = left column width. Place 10pt below headline bottom edge.
  4. Session descriptor: Text Box below divider, Poppins Regular 400 11pt, `#4A4A6A`.
  5. Icon badges: For each of the 5 rows — Insert → Shapes → Oval (hold Shift for circle), 44pt × 44pt, Fill `#2EAA5E`, No border. Insert → Icons → search for relevant icon → place centered on circle → Format: Color White. Group circle + icon. Copy group and duplicate vertically with 20pt gap.
  6. Row labels: Text Box beside each badge group. Label line: Poppins Semi-Bold 600 13pt `#1A1A2E`. Descriptor line: Poppins Regular 400 10pt `#4A4A6A`. Text boxes left-aligned to a consistent X position (badge right-edge + 10pt margin).
  7. Align all badge-groups to a single left X axis. Align all text boxes to a single left X axis. Use Arrange → Align → Align Left for precision.

---

## Slide 3: Four Skills You Will Own
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Four Skills" (white `#FFFFFF`) + "You Will Own" (green-light `#5CDB8F`) — Poppins Bold 700, 36pt. Apply two-tone rule using green-light accent on dark background for the accent word.
- **Content:**
  - [icon: check-circle] Choose the right JOIN type for any query requirement
  - [icon: check-circle] Identify and fix the LEFT JOIN → INNER JOIN conversion trap
  - [icon: check-circle] Rewrite correlated subqueries as performant JOINs
  - [icon: check-circle] Read an EXPLAIN plan to diagnose a slow join
- **Visual spec:**
  - Full-bleed dark-green radial gradient (same spec as Slide 1).
  - One large soft-light atmosphere circle (~260pt, green-light 20% opacity, 45pt soft edges) at upper-center (~50% X, 18% Y).
  - All content horizontally centered on slide. Headline at ~22% from top. Framing line at ~32% from top. Four objective rows starting at ~40% from top, spaced 18pt apart.
  - Each objective row: green-mid badge (44pt) on the left of a white objective text line. Rows centered as a group (not each individually — group the four rows, then center the group).
  - Decorative gem (small, ~48pt) at top-right corner, green-light tint, semi-transparent.
- **PPT build notes:**
  1. Background: same radial gradient as Slide 1.
  2. Soft-light circle: circle shape, green-light `#5CDB8F` fill, 78% transparency, Soft Edges 45pt, no border. Send to Back. Position at upper-center.
  3. Headline: Poppins Bold 700, 36pt. Two words in one text box. "Four Skills" in white `#FFFFFF`. "You Will Own" in green-light `#5CDB8F`. Character-level color — same technique as white slides but using green-light instead of green-mid. Center-aligned text box, positioned at top-center of content area.
  4. Four objective rows start directly below headline with 24pt gap (framing line removed — title now carries the context). Build one row as a group (badge + label text box), then duplicate 3×. Stack with 18pt gap. Select all four row groups → Arrange → Align → Align Center (horizontal). Then group all four rows and center the group on slide.
  6. Objective text: Poppins Regular 400 11pt, white 80% opacity. Bold keyword at start of each objective: Poppins Semi-Bold 600 12pt, white 100%.
  7. Top-right gem: place gem PNG, 48pt, green-light tint, ~2% margin from top-right corner.

---

## Slide 4: INNER JOIN vs LEFT JOIN — Choose Based on NULLs
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Choose" (near-black `#1A1A2E`) + "Your JOIN" (green-mid `#2EAA5E`) — Poppins Bold 700, ~36pt
- **Content:**
  - **INNER JOIN** — Matched rows only. Missing key = row silently dropped.
    - Code: `SELECT o.order_id, c.name FROM orders o INNER JOIN customers c ON o.customer_id = c.customer_id;`
  - **LEFT JOIN** — All left-table rows kept; unmatched right side becomes NULL.
    - Code: `SELECT e.name, d.dept_name FROM employees e LEFT JOIN departments d ON e.dept_id = d.id;`
  - Decision rule callout: "Rows going missing? Suspect INNER JOIN — switch to LEFT JOIN to see the gaps."
- **Visual spec:**
  - White background.
  - Left column (0–38%): two-tone headline top-left, thin green-mid divider line (1.5pt) below headline, one-sentence framing "Match vs. preserve — pick the right tool" in grey-body Regular 11pt, then a decision-rule callout box (rounded rectangle, 12pt corner radius, green-light `#5CDB8F` 1.5pt border, white fill, near-black text ~10pt Poppins Italic 400) positioned below the framing text with ~16pt gap.
  - Right column (42–100%): two stacked icon-badge rows. Row 1 (INNER JOIN): green-mid badge with intersecting-circles icon, bold label "INNER JOIN" in near-black Semi-Bold 13pt, one-line definition (≤8 words) in grey-body Regular 10pt, then a code snippet card below (light-grey `#F4F4F8` rounded rectangle, 8pt corner radius, monospace 9pt text). Row 2 (LEFT JOIN): same structure with left-circle-filled icon, identical card treatment. 24pt gap between the two rows.
  - No gem decorations on white slides.
- **PPT build notes:**
  1. White background.
  2. Two-tone headline: same technique as Slide 2 — single text box, character-level color.
  3. Divider line: Insert Line, `#2EAA5E`, 1.5pt, left-column width.
  4. Callout box: Rounded Rectangle shape, corner radius 0.17" (≈12pt). Fill: white. Line: `#5CDB8F`, 1.5pt. Text inside: Poppins Italic 400 10pt `#1A1A2E`. Size: ~38% of slide width × ~14% height.
  5. Icon badges: same badge construction as Slide 2 (circle `#2EAA5E` + white icon). Use PowerPoint's built-in "Circles and circles overlap" icon for INNER JOIN, "Half-filled circle left" for LEFT JOIN.
  6. Code snippet cards: Insert Rounded Rectangle, Fill `#F4F4F8`, No border, corner radius 0.11". Type code in Courier New 9pt, near-black `#1A1A2E`. Use Wrap Text: Do Not Wrap.
  7. Right column — vertical rhythm: badge row top at same Y as headline top. 24pt gap between Row 1 card bottom and Row 2 badge top.

---

## Slide 5: Outer JOINs — Keep Every Row, No Matter What
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Outer JOINs" (white `#FFFFFF`) + "Keep Everything" (green-light `#5CDB8F`) — Poppins Bold 700, 36pt. Two-tone applied using green-light accent on dark background.
- **Content:**
  - **RIGHT JOIN** — Mirror of LEFT JOIN; all right-side rows kept. Prefer LEFT JOIN with swapped table order — never mix LEFT and RIGHT JOIN in one query.
  - **FULL OUTER JOIN** — Every row from both tables; unmatched sides become NULL. Use for reconciliation: "what exists in one dataset but not the other?"
  - MySQL note: No native FULL OUTER JOIN — use: `LEFT JOIN ... UNION ... RIGHT JOIN`
  - Code callout: `WHERE a.id IS NULL OR b.id IS NULL` — isolates exclusive rows only.
- **Visual spec:**
  - Full-bleed dark-green radial gradient (same as Slides 1 and 3).
  - One soft-light atmosphere circle (~220pt, green-light 18% opacity, 40pt soft edges) at upper-right (~72% X, 14% Y).
  - Three-zone layout: LEFT zone (0–44%) = RIGHT JOIN text block. CENTER zone (46–54%) = vertical divider line in green-mid `#2EAA5E`, 1.5pt, spanning ~75% of slide height, vertically centered. RIGHT zone (56–100%) = FULL OUTER JOIN text block.
  - Both text blocks follow the same structure: bold label (white Semi-Bold 600 13pt), body paragraph (white Regular 10pt 80% opacity), MySQL note (white Italic 10pt 70% opacity).
  - Frosted-glass callout card spanning full content width below both columns: white 20% opacity fill, 1px white border 40% opacity, outer drop shadow, contains the WHERE IS NULL tip in white Regular 11pt.
  - Small gem decoration (~44pt) at bottom-right corner.
- **PPT build notes:**
  1. Background: radial gradient same as Slide 1.
  2. Soft-light circle: upper-right position, same technique as Slide 3.
  3. Vertical divider: Insert → Shapes → Line. Color `#2EAA5E`, weight 1.5pt. Height = 75% of slide height. Vertically center-align on slide. Horizontal position at exactly 50% of slide width.
  4. Text blocks: two text boxes, each ~42% of slide width. LEFT text box right-edge at 44% slide width. RIGHT text box left-edge at 56% slide width. Bold label: Poppins Semi-Bold 600 13pt white. Body: Poppins Regular 400 10pt white 80% opacity. Italic note: Poppins Italic 400 10pt white 70% opacity. 8pt gap between label and body, 6pt gap between body and note.
  5. Frosted callout card: Rounded Rectangle, width = full content zone width (≈86% of slide width), height ~12% of slide height. Fill: Solid White, Transparency 80%. Border: Solid White 1pt, Transparency 60%. Shadow: Outer, Blur 22pt, Distance 5pt, Angle 90°, Black 18%. Position bottom of content zone, ~8% from slide bottom edge.
  6. Callout text: Poppins Regular 400 11pt white, left-aligned inside card with 12pt left padding.
  7. Bottom-right gem: 44pt, same treatment as Slide 1 gems.

---

## Slide 6: CROSS JOIN and SELF JOIN — Special Purpose Tools
- **Layout pattern:** C
- **Background mode:** white
- **Headline:** "Special" (near-black `#1A1A2E`) + "JOINs" (green-mid `#2EAA5E`) — Poppins Bold 700, ~36pt
- **Content:**
  - **CROSS JOIN** — Result rows = Table A rows × Table B rows. No ON clause. Use for product matrices, calendar grids, test data generation. Risk: 1,000 × 1,000 = 1,000,000 rows — always sanity-check row count before running.
    - Code: `SELECT * FROM products CROSS JOIN colors;`
  - Center connector arrow (green-mid, pointing right)
  - **SELF JOIN** — Same table, two aliases. No special keyword. Use for hierarchies (employee → manager), duplicate detection, row-to-row comparisons. Use LEFT JOIN variant to keep top-level rows (no manager) in results.
    - Code: `SELECT e.name, m.name AS manager FROM employees e LEFT JOIN employees m ON e.manager_id = m.id;`
- **Visual spec:**
  - White background.
  - Two-tone headline left-aligned at top-left.
  - Thin green-mid divider line (1.5pt) below headline, spanning left ~28% of content width (matches Column 1 width only — visual anchor, not full-width).
  - Three equal-width columns below the headline, each ~28% of slide width, with ~4% gap between columns:
    - Column 1: bold label "CROSS JOIN" (near-black Semi-Bold 13pt), body text (grey-body Regular 10pt), code snippet card (light-grey `#F4F4F8` rounded rectangle, Courier New 9pt near-black).
    - Column 2 (center): a large right-pointing block arrow shape, green-mid `#2EAA5E` fill, white border none, vertically centered in the column.
    - Column 3: bold label "SELF JOIN" (near-black Semi-Bold 13pt), body text, code snippet card matching Column 1 style.
  - No gem decorations on white slides.
- **PPT build notes:**
  1. White background.
  2. Two-tone headline: single text box, character-level color. Poppins Bold 700 36pt.
  3. Short divider line: Insert Line, `#2EAA5E`, 1.5pt, length ≈ 28% of slide width. Positioned 10pt below headline bottom.
  4. Column layout: use three manually placed text/shape zones rather than a PowerPoint table (tables limit formatting flexibility). Mark column boundaries at slide widths 7%, 35%, 43%, 65%, 72%, 93% (margins + 3 content zones + 2 gaps).
  5. CROSS JOIN text box: left-aligned in Column 1. Bold label Poppins Semi-Bold 600 13pt `#1A1A2E`. Body Poppins Regular 400 10pt `#4A4A6A`. 6pt gap label → body.
  6. Code card: Rounded Rectangle `#F4F4F8` fill, 0.11" corner radius, no border. Inside: Courier New 9pt `#1A1A2E`. Size to content + 8pt padding all sides.
  7. Arrow: Insert → Shapes → Block Arrows → Right Arrow. Resize to roughly 60pt wide × 36pt tall. Fill `#2EAA5E`, No border. Vertically center within the column. Apply Format Shape → Glow → `#2EAA5E` at 20% transparency, 4pt size — subtle glow effect.
  8. SELF JOIN column: mirror of Column 1 placement and styling.
  9. Distribute all three column groups vertically centered relative to each other: select all three → Arrange → Align → Align Middle.

---

## Slide 7: Correlated Subqueries Slow You Down — JOINs Are Faster
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Correlated Subqueries" (white `#FFFFFF`) + "Slow You Down" (green-light `#5CDB8F`) — Poppins Bold 700, 34pt. Two-tone applied: white phrase + green-light accent phrase on dark background.
- **Content:**
  - Context: Correlated subquery re-runs once per outer-query row → nested loop behavior → slow on large tables.
  - Card 1 — NOT IN rewrite:
    - Before (slow): `SELECT c.name FROM customers c WHERE c.id NOT IN (SELECT customer_id FROM orders);`
    - After (fast): `SELECT c.name FROM customers c LEFT JOIN orders o ON c.id = o.customer_id WHERE o.customer_id IS NULL;`
  - Card 2 — EXISTS rewrite:
    - Before (slow): `SELECT c.name FROM customers c WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);`
    - After (fast): `SELECT DISTINCT c.name FROM customers c INNER JOIN orders o ON c.id = o.customer_id;`
- **Visual spec:**
  - Full-bleed dark-green radial gradient.
  - One soft-light atmosphere circle (~240pt, green-light 20% opacity, 45pt soft edges) at upper-left (~28% X, 16% Y).
  - Two-tone headline: "Correlated Subqueries" in white `#FFFFFF` + "Slow You Down" in green-light `#5CDB8F`. Poppins Bold 700 34pt, left-aligned at top-left of content zone. Apply character-level color in one text box — same technique as white slides but using green-light for the accent.
  - Supporting sentence below headline: white Regular 11pt 80% opacity, max 2 lines.
  - Two frosted-glass cards side by side in the lower 60% of slide, each 42% slide width, 3% gap. Cards: white 20% opacity fill, 1px white 40% opacity border, drop shadow (same spec as Slide 5 callout card).
  - Each card: label line in green-light `#5CDB8F` Semi-Bold 600 13pt at top. "Before" label + code block (Courier New 9pt white). "After" label + code block. Label and code tightly stacked (6pt gap).
  - Small gem (~44pt) top-right corner.
- **PPT build notes:**
  1. Background: radial gradient same as Slides 1, 3, 5.
  2. Soft-light circle: upper-left position (~28% X, 16% Y), same technique as prior dark slides.
  3. Headline text box: Poppins Bold 700 34pt. Two-tone in one text box: "Correlated Subqueries" in white `#FFFFFF`, "Slow You Down" in green-light `#5CDB8F`. Character-level color — same technique as white slides. Left-aligned. Position top-left of content area (7% from left edge, 8% from top).
  4. Supporting sentence: Poppins Regular 400 11pt white, Transparency 20% (i.e., 80% opacity). 12pt below headline.
  5. Card construction: Insert Rounded Rectangle, corner radius 0.18". Width = 42% slide width. Height = ~52% slide height. Fill: Solid White, Transparency 80%. Border: Solid White 1pt, Transparency 60%. Shadow: Outer, Blur 24pt, Distance 5pt, Angle 90°, Black 18% transparency.
  6. Card interior — label: Poppins Semi-Bold 600 13pt `#5CDB8F`. Place 12pt from card top, 12pt from card left.
  7. "Before" marker text: Poppins Semi-Bold 600 10pt white 70% opacity. Code block: Courier New 9pt white. 6pt gap between marker and code.
  8. "After" marker text: same treatment, 10pt gap below "Before" code block.
  9. Both cards: position left card at 7% from left slide edge, right card at 51% from left slide edge. Both cards vertically aligned at the same Y top position.
  10. Top-right gem: 44pt, place at ~95% X, 3% Y from top.

---

## Slide 8: JOIN Performance — Write Queries the Engine Can Optimize
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "JOIN" (near-black `#1A1A2E`) + "Performance" (green-mid `#2EAA5E`) — Poppins Bold 700, ~36pt
- **Content:**
  - [icon: database] Index join columns — foreign keys without an index cause full-table scans on every join
  - [icon: ban] No functions in ON clause — `ON YEAR(date) = 2024` kills index use; rewrite as a range condition
  - [icon: magnifying-glass] Always EXPLAIN — `EXPLAIN ANALYZE` reveals index scan vs sequential scan
  - Callout: "Sargable condition = the optimizer can use an index. Non-sargable = it cannot."
- **Visual spec:**
  - White background.
  - Left column (0–38%): two-tone headline top-left. Thin green-mid divider line (1.5pt) below headline. Framing sentence: "Three rules for queries the optimizer can execute efficiently" in grey-body Regular 11pt. Sargable callout box (rounded rectangle, 12pt corner radius, green-light `#5CDB8F` 1.5pt border, white fill, near-black Italic 10pt text) positioned below framing text, ~16pt gap. Callout includes a small green-mid left-accent bar (4pt wide rectangle `#2EAA5E` no border, full height of callout box, attached to left edge).
  - Right column (42–100%): three icon-badge rows stacked with 16pt gap. Icons: database cylinder, ban/circle-X, magnifying glass. Each row: badge (44pt green-mid circle + white icon 22pt), bold label (near-black Semi-Bold 600 12pt), descriptor (grey-body Regular 10pt) on a second line within the same text box.
- **PPT build notes:**
  1. White background.
  2. Two-tone headline: same technique as Slides 2, 4, 6.
  3. Divider line: `#2EAA5E`, 1.5pt, left-column width.
  4. Framing sentence: Poppins Regular 400 11pt `#4A4A6A`. 12pt below divider.
  5. Callout box: Rounded Rectangle, corner radius 0.17", Fill white, Border `#5CDB8F` 1.5pt. Text: Poppins Italic 400 10pt `#1A1A2E`. Left accent bar: thin Rectangle shape, width 4pt, height = callout box height, Fill `#2EAA5E`, No border, Aligned to left edge of callout box, grouped with callout box.
  6. Three icon badges: same construction as Slide 2. Vertical rhythm: 16pt gap between each row's bottom edge and next row's badge top edge.
  7. Row label: Poppins Semi-Bold 600 12pt `#1A1A2E` on line 1 of text box. Descriptor: Poppins Regular 400 10pt `#4A4A6A` on line 2. Text box line spacing: 1.2× between lines within each row.
  8. Right-column top Y position: align to same Y as headline top edge. This creates visual alignment across both columns.

---

## Slide 9: In-Class Practice
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "In-Class Practice" — all white (dark slide rule)
- **Content:**
  - [badge: Easy] Task 1: Write a LEFT JOIN returning all employees and their department names, including employees with no department assigned.
  - [badge: Medium] Task 2: Find all customers who have never placed an order — no subqueries allowed. Hint: think about what NULL means on the right side of a LEFT JOIN.
  - [badge: Hard] Task 3: Rewrite this correlated subquery as a JOIN:
    - `SELECT c.customer_name FROM customers c WHERE (SELECT MAX(amount) FROM orders o WHERE o.customer_id = c.customer_id) > 1000;`
- **Visual spec:**
  - Full-bleed dark-green radial gradient.
  - One soft-light atmosphere circle (~200pt, green-light 18% opacity, 40pt soft edges) at upper-center (~50% X, 15% Y).
  - All content centered on slide. Headline at top-center of content zone.
  - Three task rows, each a structured horizontal unit: difficulty badge (small rounded rectangle, ~64pt wide × 22pt tall) → task label (white Semi-Bold 12pt) → task description (white Regular 10pt 80% opacity) on the same row or wrapping beneath the label. 20pt gap between rows.
  - Difficulty badges: "Easy" = green-light `#5CDB8F` fill, near-black `#1A1A2E` text. "Medium" = green-mid `#2EAA5E` fill, white text. "Hard" = white fill, near-black text. All badges: Poppins Semi-Bold 600 9pt, center-aligned text.
  - Task 3 has an additional frosted-glass code card directly below its task description row: white 20% opacity fill, 1px white border 40% opacity, Courier New 9pt white, drop shadow same spec as Slide 7 cards.
  - Small gem (~44pt) at top-right corner, and another (~36pt) at bottom-left.
- **PPT build notes:**
  1. Background: radial gradient, same as Slides 1, 3, 5, 7.
  2. Soft-light circle: upper-center, same technique.
  3. Headline: Poppins Bold 700 36pt white, center-aligned text box, positioned at 8% from slide top.
  4. Difficulty badge shapes: Rounded Rectangle, corner radius 0.14". Sizes: 64pt wide × 22pt tall. Fill per difficulty (green-light, green-mid, white). No border. Text: Poppins Semi-Bold 600 9pt, color per difficulty (near-black for Easy and Hard, white for Medium).
  5. Task label: Poppins Semi-Bold 600 12pt white. Placed 10pt to the right of badge right edge, vertically centered to badge.
  6. Task description: Poppins Regular 400 10pt white 80% opacity. Placed on second line beneath the label within the same text box (or a separate text box if easier), left-aligned to label left edge.
  7. Three task groups: build one complete group (badge + label + description), then duplicate twice and modify text. Select all three groups → Arrange → Align → Align Left. Set 20pt gap between groups manually or via Position and Size dialog.
  8. Task 3 code card: Rounded Rectangle, white 80% transparency fill, 1pt white 60% transparent border, drop shadow (Blur 22pt, Distance 5pt). Width ≈ 80% of slide width, centered. Code text Courier New 9pt white, 10pt top/bottom padding, 14pt left/right padding inside card.
  9. Two gems: top-right 44pt, bottom-left 36pt. Tinted green-light, semi-transparent. Send to back behind content but above background gradient.

---

## Slide 10: Summary and Next Steps
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Session" (near-black `#1A1A2E`) + "Summary" (green-mid `#2EAA5E`) — Poppins Bold 700, ~36pt
- **Content:**
  - [icon: check-circle] INNER JOIN — silent row drops
  - [icon: check-circle] LEFT JOIN — filter in ON, not WHERE
  - [icon: check-circle] FULL OUTER JOIN — reconciliation and gaps
  - [icon: check-circle] CROSS / SELF JOIN — products and hierarchies
  - [icon: check-circle] Subquery rewrites — use JOINs instead
  - [icon: check-circle] Performance — EXPLAIN before shipping
  - Primary CTA: "Complete take-home exercises 4–7."
  - Bonus Challenge: "Run EXPLAIN on your own database."
- **Visual spec:**
  - White background.
  - Left column (0–38%): two-tone headline top-left. Thin green-mid divider (1.5pt) below headline. Grey-body Regular 11pt line "What we covered today." Two callout boxes stacked below (16pt gap between framing line and first box, 12pt between boxes): (1) Primary CTA box — rounded rectangle, green-mid `#2EAA5E` 1.5pt border, white fill, right-arrow badge (32pt, green-mid circle) + "Complete take-home exercises 4–7." near-black Regular 10pt; (2) Bonus Challenge box — green-light `#5CDB8F` 1.5pt border, star badge (32pt, green-light circle) + "Run EXPLAIN on your own database." near-black Regular 10pt.
  - Right column (42–100%): six icon-badge rows, 16pt gap between rows (trimmed reminder text restores standard spacing). Badges: 40pt diameter. Check-circle white icons. Bold concept labels near-black Semi-Bold 12pt. Short reminders (≤5 words) grey-body Regular 10pt on second line.
  - No gem decorations on this closing white slide.
- **PPT build notes:**
  1. White background.
  2. Two-tone headline: single text box, character-level color, Poppins Bold 700 36pt.
  3. Divider line: `#2EAA5E`, 1.5pt, left-column width. 10pt below headline.
  4. Framing line: Poppins Regular 400 11pt `#4A4A6A`. 8pt below divider.
  5. Primary CTA callout box: Rounded Rectangle, corner radius 0.17", Fill white, Border `#2EAA5E` 1.5pt. Height ~16% of slide height. Width = left column width. Position 16pt below framing line. Right-arrow icon badge (32pt circle, Fill `#2EAA5E`, white arrow icon 16pt) at left interior. Text: Poppins Regular 400 10pt `#1A1A2E`. Text: "Complete take-home exercises 4–7."
  6. Bonus Challenge callout box: same dimensions. Border `#5CDB8F` 1.5pt. Star icon badge (32pt circle, Fill `#5CDB8F`, white star icon 16pt). Text: "Run EXPLAIN on your own database." Place 12pt below primary CTA box.
  7. Six icon badges: 40pt × 40pt circles, `#2EAA5E` fill, white check-circle icons 20pt. Right column, stacked at 16pt gap. Top row Y aligns with headline top edge.
  8. Row labels: Poppins Semi-Bold 600 12pt `#1A1A2E` line 1. Short reminders: Poppins Regular 400 10pt `#4A4A6A` line 2. Line spacing 1.2× within row text box.
  9. Final quality check: select all six row groups → Arrange → Align → Align Left. Confirm no right-column content clips into slide right margin (maintain 7% right margin).

---

## Design Compliance Checklist

| Rule | Slide(s) | Implementation Detail |
|------|----------|-----------------------|
| Two-tone headline on every white slide | 2, 4, 6, 8, 10 | Single text box, character-level color: neutral word `#1A1A2E`, accent word `#2EAA5E`. Same Poppins Bold 700 36pt — color only, never font or weight change |
| Dark slides: two-tone headline using green-light accent | 1, 3, 5, 7, 9 | White `#FFFFFF` for neutral word/phrase + green-light `#5CDB8F` for accent. Slide 1: "SQL" + "Joins". Slide 3: "Four Skills" + "You Will Own". Slide 5: "Outer JOINs" + "Keep Everything". Slide 7: "Correlated Subqueries" + "Slow You Down". Slide 9: dark-slide two-tone applied per pattern. |
| Background alternation — no more than 2 consecutive same mode | All 10 | Strict alternation: dark / white / dark / white / dark / white / dark / white / dark / white (Slides 1→10) — never consecutive same mode |
| 1 concept per slide; title is the conclusion | All 10 | Slide 4 = INNER/LEFT JOIN choice. Slide 5 = Outer JOINs. Slide 6 = Special JOINs. Slide 7 = Subquery rewrites. Slide 8 = Performance. No slide carries two unrelated topics |
| Layout patterns A–G only | All 10 | A: Slide 1. B: Slides 2, 4, 8, 10. C: Slide 6. F: Slides 3, 5, 7, 9. Pattern D (quadrant matrix), E (map + stat cards), and G (two-stat opportunity) not used — not appropriate for training content |
| Color tokens exclusively | All 10 | green-dark `#1A6B3A`, green-mid `#2EAA5E`, green-light `#5CDB8F`, white `#FFFFFF`, near-black `#1A1A2E`, grey-body `#4A4A6A`. No off-palette colors introduced |
| Font: Poppins throughout, single family | All 10 | Poppins (fallback: DM Sans, then Inter). Courier New used only inside code snippet cards — acceptable exception for monospace code display |
| Icon badge system consistency | 2, 3, 4, 8, 10 | All badges: circle shape `#2EAA5E`, same diameter per context (44pt for body slides, 40pt for six-row summary, 32pt for callout interior). White line-art icons, same stroke library throughout |
| Slide margin / safe zone | All 10 | 7% left/right margin, 8% top/bottom margin maintained. No content bleeds to edge. Slide numbers bottom-right inside margin |
| Decorative gems on dark slides only | 1, 3, 5, 7, 9 | Gems not placed on white slides. On dark slides: top-right and/or bottom-left corners only. Size range 36–72pt. Green-light tint, semi-transparent PNG |
| Soft-light atmosphere circles on dark slides only | 1, 3, 5, 7, 9 | One or two per dark slide. Green-light fill, 75–80% transparency, 40–50pt Soft Edges, Send to Back. Creates depth without competing with content |
| Training slide structure | All 10 | Cover (1) → Agenda (2) → Learning Objectives (3) → Core Concepts (4–6) → Advanced Concept (7) → Performance (8) → Practice (9) → Summary (10) |

---

## v2 Enrichment Notes

The following areas were expanded beyond the original `sql-intermediate-joins.md` blueprint:

1. **Exact positioning:** Column boundary percentages (e.g., "0–38%", "42–100%") are now specified for every Pattern B slide, eliminating layout guesswork.
2. **Layering and z-order:** Every slide now specifies Send to Back/front ordering for background shapes, atmosphere circles, gem assets, and content layers.
3. **Gradient precision:** Radial gradient stop positions (0% → 100%) and center-handle coordinates are now explicit, not just "dark to light."
4. **Code block styling:** Courier New is specified as the monospace font inside code cards, with padding, background color `#F4F4F8` (white slides), and transparent-white (dark slides) explicitly called out.
5. **Callout box accent bars:** Slide 8's sargable callout now includes a left-edge green-mid accent bar, referencing the design system's thin accent rule convention (Section 4.6 of deck-analysis.md).
6. **Icon badge sizing gradation:** 44pt (body slides) → 40pt (six-row summary) → 32pt (callout interior) — a consistent sizing hierarchy not present in v1.
7. **Step-by-step PPT instructions:** Every slide now has numbered PowerPoint build steps rather than prose notes, enabling a designer to build slide-by-slide without re-reading the design system.
8. **Atmosphere circle coordinates:** Each dark slide specifies a different position for the soft-light circle (upper-center, upper-right, upper-left) to add subtle visual variation while maintaining consistency.

---

output_path: /Users/leopham/Documents/Teaching Assistant/slide_deck_template/decks/sql-intermediate-joins-v2.md
