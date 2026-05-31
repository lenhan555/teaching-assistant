# Slide Deck Blueprint — SQL Joins (Intermediate)
**Topic:** SQL Joins
**Audience:** Intermediate SQL learners (students)
**Style:** Training
**Slides:** 12
**Knowledge doc:** `skills/sql-intermediate-joins.md`
**Generated:** 2026-05-25
**Updated:** 2026-05-31 — Slides 4/5 split into single-concept slides (4–7); slide count 10 → 12; two-tone headline specs added to dark slides; slide 8 reduced to 3 performance rules; slide 11 title made declarative; slide 12 summary consolidated.

---

## Slide 1: SQL Joins
- **Layout pattern:** A
- **Background mode:** dark-green
- **Headline:** "SQL" (white `#FFFFFF`) + "Joins" (green-light `#5CDB8F`) — display scale ~80pt, Poppins Black 900
- **Content:**
  - Subtitle: "Mastering Every JOIN Type for Real-World Queries"
  - Audience tag: Intermediate Level
  - Session length cue: "6 JOIN types · Subquery rewrites · Performance"
- **Visual spec:** Floating frosted-glass card on the left (45%) containing the session badge and course logo placeholder. Right side (55%) holds the display headline at ~80pt. Decorative 3D gem shapes at top-right and bottom-left corners. Soft radial light circle blooms from upper-center in green-light at 25% opacity.
- **PPT build notes:** Full-bleed radial gradient background — green-light `#5CDB8F` at top-center fading to green-dark `#1A6B3A` at edges. Left card: rounded rectangle, white fill at 20% opacity, 1px white border at 40% opacity, subtle drop shadow. Headline text box: "SQL" white, "Joins" green-light `#5CDB8F`, Poppins Black 900 ~80pt. Insert 3D gem PNGs at corners with green-light tint.

---

## Slide 2: Agenda
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Session" (near-black `#1A1A2E`) + "Agenda" (green-mid `#2EAA5E`) — Poppins Bold 700, ~36pt
- **Content:**
  - [icon: book] JOIN Types — INNER, LEFT, RIGHT, FULL OUTER, CROSS, SELF
  - [icon: arrow-swap] Subquery Rewrites — rewrite correlated subqueries as JOINs
  - [icon: lightning] Performance — indexes, EXPLAIN, sargable conditions
  - [icon: pencil] In-Class Practice — 3 progressively harder queries
  - [icon: flag] Summary & Next Steps
- **Visual spec:** Left column (40%) holds the two-tone headline and a one-line session description in grey-body. Right column (60%) is a stacked list of five rows, each with a circular green-mid icon badge (white line-art icon) followed by a bold label and a short grey-body descriptor on the same line.
- **PPT build notes:** White background. Two-tone headline: "Session" near-black `#1A1A2E`, "Agenda" green-mid `#2EAA5E`, both Poppins Bold 700 ~36pt. Icon badges: circle shape green-mid `#2EAA5E`, 44pt diameter, white icon from Insert → Icons. Row spacing: 20pt between rows. Thin horizontal divider line (green-mid, 1.5pt) between headline and icon list.

---

## Slide 3: Learning Objectives
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Learning" (white `#FFFFFF`) + "Objectives" (green-light `#5CDB8F`) — Poppins Bold 700, ~36pt. Two-tone applied: white neutral word + green-light accent word using character-level color in one text box.
- **Content:**
  - [icon: check] Choose the right JOIN type for any query requirement
  - [icon: check] Identify and fix the LEFT JOIN → INNER JOIN conversion trap
  - [icon: check] Rewrite correlated subqueries as performant JOINs
  - [icon: check] Read an EXPLAIN plan to diagnose a slow join
- **Visual spec:** Full-bleed dark-green gradient. Centered layout. Two-tone headline at top. Four icon-badge + objective rows centered horizontally below, equal spacing. Decorative soft-light circle in upper background at 20% opacity.
- **PPT build notes:** Background: radial gradient green-light → green-dark. Headline: Poppins Bold 700 ~36pt. "Learning" white `#FFFFFF`, "Objectives" green-light `#5CDB8F` — character-level color in one text box. Objective rows: green-mid circle badges (44pt) with white check icons, label text Poppins Regular 400 ~11pt white at 80% opacity. Vertical spacing between rows: 18pt. Center-align all elements on slide.

---

## Slide 4: INNER JOIN Silently Drops Unmatched Rows
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "INNER" (near-black `#1A1A2E`) + "JOIN" (green-mid `#2EAA5E`) — Poppins Bold 700, ~36pt
- **Content:**
  - **INNER JOIN** — Matched rows only. If a key is missing on either side, that row is silently dropped.
    - `SELECT o.order_id, c.customer_name FROM orders o INNER JOIN customers c ON o.customer_id = c.customer_id;`
  - Callout: "Rows going missing? Suspect INNER JOIN — switch to LEFT JOIN to see the gaps."
- **Visual spec:** Left column (40%) — two-tone headline, one-line framing "Set-based matching — no match, no row" in grey-body, decision callout box (rounded rectangle, green-light `#5CDB8F` border). Right column (60%) — one icon-badge row: intersecting-circles icon, bold label "INNER JOIN" near-black Semi-Bold 13pt, one-line definition, code snippet in a light-grey monospace card below.
- **PPT build notes:** White background. Two-tone headline Poppins Bold 700 ~36pt. Body text grey-body `#4A4A6A` Regular 400 ~10pt. Code snippet: Courier New ~9pt, light-grey `#F4F4F4` rounded rectangle container. Icon badge green-mid `#2EAA5E` 44pt. Callout box: green-light `#5CDB8F` 1.5pt border, white fill, ~10pt Italic near-black text.

---

## Slide 5: LEFT JOIN Keeps Every Left Row — Filter in ON, Not WHERE
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "LEFT" (white `#FFFFFF`) + "JOIN" (green-light `#5CDB8F`) — Poppins Bold 700, ~36pt. Two-tone applied on dark background.
- **Content:**
  - **LEFT JOIN** — All left-table rows kept; unmatched right-table columns become NULL.
    - Classic use: all customers, with or without orders.
  - **Warning:** Filtering on a nullable right-table column in WHERE silently converts LEFT JOIN → INNER JOIN. Move the filter into the ON clause.
    - `SELECT e.name, d.dept_name FROM employees e LEFT JOIN departments d ON e.dept_id = d.id;`
  - Callout: "Filter in the ON clause — not the WHERE — to keep the LEFT JOIN intact."
- **Visual spec:** Full-bleed dark-green gradient. Two-tone headline top-left. Centered content below: one icon-badge row for LEFT JOIN (half-filled left circle icon), bold label, definition, code card in frosted-glass style. Warning callout card below code block spanning content width.
- **PPT build notes:** Background: radial gradient green-light → green-dark. Headline: "LEFT" white, "JOIN" green-light `#5CDB8F`, character-level color one text box, Poppins Bold 700 ~36pt. Icon badge: green-mid `#2EAA5E` 44pt, white left-circle-filled icon. Code card: white 20% opacity rounded rectangle, 1pt white border 40% opacity, Courier New ~9pt white. Warning callout: frosted-glass card spanning content width, green-light `#5CDB8F` 1.5pt border, white text ~10pt.

---

## Slide 6: RIGHT JOIN Is a LEFT JOIN in Reverse — Just Rewrite It
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "RIGHT" (near-black `#1A1A2E`) + "JOIN" (green-mid `#2EAA5E`) — Poppins Bold 700, ~36pt
- **Content:**
  - **RIGHT JOIN** — Mirror of LEFT JOIN. All right-table rows; NULLs fill the left side. Almost always rewritable as LEFT JOIN with swapped table order.
  - Rule: Avoid mixing LEFT and RIGHT JOIN in the same query — pick one direction and swap table order instead.
    - Rewrite: `SELECT c.name, o.order_id FROM orders o RIGHT JOIN customers c ON o.customer_id = c.id;`
    - Better: `SELECT c.name, o.order_id FROM customers c LEFT JOIN orders o ON c.id = o.customer_id;`
- **Visual spec:** Left column (40%) — two-tone headline, one-line framing "Prefer LEFT JOIN for consistency" in grey-body, rewrite-tip callout box (rounded rectangle, green-light border). Right column (60%) — one icon-badge row: right-circle-filled icon, bold label "RIGHT JOIN", definition, then before/after code snippet cards stacked vertically below.
- **PPT build notes:** White background. Two-tone headline Poppins Bold 700 ~36pt. Body text grey-body `#4A4A6A` Regular 400 ~10pt. Code cards: Courier New ~9pt, light-grey `#F4F4F4` rounded rectangle. Callout box: green-light `#5CDB8F` 1.5pt border, white fill, ~10pt Italic near-black text.

---

## Slide 7: FULL OUTER JOIN Finds What Exists in One Dataset But Not the Other
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "FULL OUTER" (white `#FFFFFF`) + "JOIN" (green-light `#5CDB8F`) — Poppins Bold 700, ~36pt. Two-tone applied on dark background.
- **Content:**
  - **FULL OUTER JOIN** — Every row from both tables. Unmatched sides get NULL. The tool for reconciliation: "Which records exist in one dataset but not the other?"
  - MySQL workaround: No native FULL OUTER JOIN — use UNION of LEFT JOIN + RIGHT JOIN.
  - Key filter: `WHERE a.id IS NULL OR b.id IS NULL` isolates the exclusive rows only.
    - Code: `SELECT a.id, b.id FROM table_a a FULL OUTER JOIN table_b b ON a.id = b.id WHERE a.id IS NULL OR b.id IS NULL;`
- **Visual spec:** Full-bleed dark-green gradient. Two-tone headline top-left. Two-column content below: LEFT column — FULL OUTER JOIN definition and MySQL note; RIGHT column — code card in frosted-glass style. Frosted callout card spanning full width at bottom: WHERE IS NULL filter tip.
- **PPT build notes:** Background: radial gradient. Headline: "FULL OUTER" white, "JOIN" green-light `#5CDB8F`, character-level color, Poppins Bold 700 ~36pt. Text: Regular 400 ~10pt white 80% opacity. Bold labels: Semi-Bold 600 ~12pt white. Code card: frosted-glass rounded rectangle, Courier New ~9pt white. Callout card: white 20% opacity fill, white 1px border 40% opacity, drop shadow, white text ~11pt.

---

## Slide 8: CROSS JOIN Multiplies Rows; SELF JOIN Reflects a Table on Itself
- **Layout pattern:** C
- **Background mode:** white
- **Headline:** "Special" (near-black `#1A1A2E`) + "JOINs" (green-mid `#2EAA5E`) — Poppins Bold 700, ~36pt
- **Content:**
  - **CROSS JOIN** → A × B rows. No ON clause. Use for product matrices, calendar grids, test data. Risk: 1,000 × 1,000 = 1,000,000 rows — sanity-check row counts first.
  - **→**
  - **SELF JOIN** → Same table, two aliases. No special keyword. Use for hierarchies (employee → manager), duplicate detection, row comparisons.
- **Visual spec:** Pattern C three-column layout: Column 1 — CROSS JOIN definition + code snippet card. Center column — right-pointing block arrow in green-mid. Column 3 — SELF JOIN definition + code snippet card. Two-tone headline above, left-aligned.
- **PPT build notes:** White background. Two-tone headline Poppins Bold 700 ~36pt. Three equal columns (~28% each) using manually placed text boxes. Arrow shape: Insert → Shapes → Block Arrow, green-mid fill. Code snippet cards: light-grey `#F4F4F4` rounded rectangle, Courier New ~9pt near-black. Bold concept labels: near-black Semi-Bold 600 ~13pt.

---

## Slide 9: Subquery Rewrites
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Subquery" (white `#FFFFFF`) + "Rewrites" (green-light `#5CDB8F`) — Poppins Bold 700, ~34pt. Two-tone applied on dark background.
- **Content:**
  - Correlated subquery re-runs once per outer-query row → behaves like a nested loop → slow on large tables.
  - Card 1 — NOT IN → LEFT JOIN + IS NULL:
    - Before (slow): `SELECT c.name FROM customers c WHERE c.id NOT IN (SELECT customer_id FROM orders);`
    - After (fast): `SELECT c.name FROM customers c LEFT JOIN orders o ON c.id = o.customer_id WHERE o.customer_id IS NULL;`
  - Card 2 — EXISTS → INNER JOIN + DISTINCT:
    - Before (slow): `SELECT c.name FROM customers c WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);`
    - After (fast): `SELECT DISTINCT c.name FROM customers c INNER JOIN orders o ON c.id = o.customer_id;`
- **Visual spec:** Full-bleed dark-green gradient. Two-tone headline left-aligned. Supporting sentence in white at 80% opacity beneath the headline. Two frosted-glass comparison cards side by side (~42% slide width each, 3% gap). Each card: green-light label, Before/After code blocks.
- **PPT build notes:** Background: radial gradient. Headline: "Subquery" white `#FFFFFF`, "Rewrites" green-light `#5CDB8F`, character-level color, Poppins Bold 700 ~34pt. Cards: white 20% opacity fill, 1px white border 40% opacity, drop shadow. Card label: green-light `#5CDB8F` Semi-Bold 600 ~13pt. Code text: Courier New ~9pt white. Supporting sentence: Regular 400 ~11pt white 80% opacity.

---

## Slide 10: JOIN Performance — Three Rules That Matter
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "JOIN" (near-black `#1A1A2E`) + "Performance" (green-mid `#2EAA5E`) — Poppins Bold 700, ~36pt
- **Content:**
  - [icon: database] Index join columns — foreign keys without an index cause full-table scans
  - [icon: ban] No functions in ON clause — `ON YEAR(date) = 2024` kills index use; use a range condition instead
  - [icon: search] Always EXPLAIN — `EXPLAIN ANALYZE` reveals whether an index scan or sequential scan is running
  - Callout: "Sargable condition = the optimizer can use an index. Non-sargable = it cannot."
- **Visual spec:** Left column (40%) — two-tone headline + one-sentence framing "Three rules for queries the optimizer can execute efficiently" + sargable callout box (rounded rectangle, green-light `#5CDB8F` border). Right column (60%) — three stacked icon-badge rows (icons: database, ban/x, magnify), each with bold label and grey-body descriptor.
- **PPT build notes:** White background. Two-tone headline Poppins Bold 700 ~36pt. Three icon badges: green-mid `#2EAA5E` circle 44pt, white icons. Bold labels: near-black Semi-Bold 600 ~12pt. Descriptors: grey-body `#4A4A6A` Regular 400 ~10pt. Callout box: green-light `#5CDB8F` 1.5pt border, white fill, near-black text ~10pt Italic. Row gap 16pt. Thin green-mid divider line beneath headline.

---

## Slide 11: Apply Every JOIN Type in Three Escalating Queries
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "In-Class" (white `#FFFFFF`) + "Practice" (green-light `#5CDB8F`) — Poppins Bold 700, ~36pt. Two-tone applied on dark background.
- **Content:**
  - Task 1 (Easy): Write a LEFT JOIN returning all employees and their department names, including employees with no department.
  - Task 2 (Medium): Find all customers who have never placed an order — no subqueries allowed.
  - Task 3 (Hard): Rewrite this correlated subquery as a JOIN: `SELECT c.customer_name FROM customers c WHERE (SELECT MAX(amount) FROM orders o WHERE o.customer_id = c.customer_id) > 1000;`
- **Visual spec:** Full-bleed dark-green background. Three task rows centered: each has a difficulty badge (green-light for Easy, green-mid for Medium, white for Hard) followed by the task label and a one-line description. Task 3 includes a frosted-glass code card below its row.
- **PPT build notes:** Background: radial gradient. Headline: "In-Class" white, "Practice" green-light `#5CDB8F`, character-level color, Poppins Bold 700 ~36pt. Difficulty badges: small rounded rectangles ~9pt Poppins Semi-Bold — green-light (Easy), green-mid (Medium), white + near-black text (Hard). Task labels: Semi-Bold 600 ~12pt white. Descriptions: Regular 400 ~10pt white 80% opacity. Frosted code card for Task 3: white 20% opacity, 1px white border, Courier New ~9pt white. Row spacing: 20pt.

---

## Slide 12: Now Apply What You Learned Before Next Session
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Session" (near-black `#1A1A2E`) + "Summary" (green-mid `#2EAA5E`) — Poppins Bold 700, ~36pt
- **Content:**
  - [icon: check-circle] Outer JOINs preserve rows — LEFT, RIGHT, FULL OUTER all keep unmatched rows
  - [icon: check-circle] Special JOINs have specific patterns — CROSS multiplies, SELF aliases
  - [icon: check-circle] Correlated subqueries are slow — rewrite as LEFT JOIN + IS NULL or INNER JOIN + DISTINCT
  - [icon: check-circle] Performance: index join columns; write sargable conditions; run EXPLAIN
  - Primary CTA: "Complete take-home exercises 4–7."
  - Bonus Challenge: "Run EXPLAIN on a query from your own database."
- **Visual spec:** Left column (40%) — two-tone headline, "What we covered today" grey-body, then two stacked callout boxes: (1) Primary CTA (green-mid border, right-arrow badge), (2) Bonus Challenge (green-light border, star badge). Right column (60%) — four icon-badge rows with check-circle icons, bold concept labels, grey-body one-line reminders.
- **PPT build notes:** White background. Two-tone headline Poppins Bold 700 ~36pt. Four icon badges: green-mid `#2EAA5E` circle 44pt (larger badges due to fewer rows), white check-circle icons. Concept labels: near-black Semi-Bold 600 ~12pt. Reminders: grey-body `#4A4A6A` Regular 400 ~10pt. Primary CTA callout: green-mid `#2EAA5E` 1.5pt border, right-arrow badge, action text. Bonus Challenge callout: green-light `#5CDB8F` 1.5pt border, star badge, action text. Row gap 18pt (generous spacing since only 4 rows). Thin green-mid divider line beneath headline.

---

## Design Compliance Checklist

| Rule | Status |
|------|--------|
| Two-tone headline on every white slide | Slides 2, 4, 6, 8, 10, 12 — neutral word near-black `#1A1A2E`, accent word green-mid `#2EAA5E` |
| Dark slides: two-tone headline using green-light accent | Slides 1, 3, 5, 7, 9, 11 — white `#FFFFFF` for neutral + green-light `#5CDB8F` for accent word |
| Background alternation (no more than 2 consecutive same mode) | dark / white / dark / white / dark / white / dark / white / dark / white / dark / white — strictly alternating across all 12 slides |
| 1 concept per slide; title is the conclusion | Each slide carries a single JOIN type or topic: S4 = INNER JOIN, S5 = LEFT JOIN, S6 = RIGHT JOIN, S7 = FULL OUTER JOIN, S8 = Special JOINs, S9 = Subquery rewrites, S10 = Performance |
| Layout patterns A–G only | A: S1. B: S2, S4, S6, S10, S12. C: S8. F: S3, S5, S7, S9, S11. Patterns D, E, G not used — not appropriate for training content |
| Color tokens only | green-dark `#1A6B3A`, green-mid `#2EAA5E`, green-light `#5CDB8F`, white `#FFFFFF`, near-black `#1A1A2E`, grey-body `#4A4A6A` |
| Font: Poppins throughout | Poppins (fallback: DM Sans, Inter) — Courier New inside code cards only |

---

output_path: /Users/leopham/Documents/Teaching Assistant/slide_deck_template/decks/sql-intermediate-joins.md
