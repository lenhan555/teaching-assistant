# SQL Joins for Beginners — Slide Blueprint

**Topic:** SQL Joins for Beginners
**Audience:** Students
**Style:** Training
**Generated:** 2026-05-31

---

## Slide 1: SQL Joins for Beginners
- **Layout pattern:** A
- **Background mode:** dark-green
- **Headline:** "SQL" + "Joins for Beginners"
- **Content:**
  - Frosted card (left panel): "SQL Training Series" badge, "Session 3 of 6", "Prerequisite: Basic SELECT & WHERE"
  - Right panel display headline: "SQL Joins for Beginners"
  - Subtext: "Combine data from multiple tables — the most essential skill in SQL"
- **Visual spec:** Full-bleed radial gradient (GREEN_LIGHT top-center → GREEN_DARK edges). Frosted card left panel. Soft glow ellipse top-right. Two small decorative gem shapes at bottom-right corner.
- **Image query:** database tables connecting diagram
- **Image style:** diagram
- **PPT build notes:**
  1. Set slide background to radial gradient: GREEN_LIGHT (#5CDB8F) at center top → GREEN_DARK (#1A6B3A) at edges.
  2. Insert rectangle shape left panel (x=60–560), fill white at 18% opacity, border white at 40% opacity, corner radius 16px.
  3. Inside card: "SQL Training Series" in Poppins 18pt SemiBold white; "Session 3 of 6" in Poppins 13pt white 70% opacity; "Prerequisite: Basic SELECT & WHERE" in Poppins 11pt white 60% opacity.
  4. Right panel: "SQL" in Poppins 80pt Black white; new line "Joins for Beginners" in Poppins 80pt Black GREEN_LIGHT (#5CDB8F).
  5. Subtext below headline: Poppins 16pt white 80% opacity.
  6. Add soft-glow ellipse top-right: GREEN_LIGHT fill, 15% opacity, large radius, no border.
  7. Slide number bottom-right: Poppins 11pt white 40% opacity. Value: "01".

---

## Slide 2: Agenda
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Today's" + "Agenda"
- **Content:**
  - What is a JOIN and why it matters
  - Section 1 — INNER JOIN: matching rows only
  - Section 2 — LEFT & RIGHT JOIN: preserving all rows
  - Section 3 — FULL OUTER JOIN: both sides
  - Section 4 — CROSS JOIN & Self-Join: special cases
  - Section 5 — Multiple JOINs and best practices
  - Wrap-up: common mistakes, review, next steps
- **Visual spec:** Left column: two-tone headline + green-mid divider line + "What you will be able to do by end of class" subtext in grey-body. Right column: 7 stacked icon-badge rows, each with green circle badge + agenda item label.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. White slide background.
  2. Left panel (x=60–480): "Today's" in Poppins 36pt Bold NEAR_BLACK; "Agenda" in same size GREEN_MID. Green-mid divider line below at y≈160, width 420px. Subtext "What you will be able to do by end of class" Poppins 13pt GREY_BODY.
  3. Right panel (x=520–1220): 7 rows starting y=160, row height 70px. Each row: green circle badge r=22 GREEN_MID, white icon inside, label text Poppins 14pt NEAR_BLACK beside badge.
  4. Slide number bottom-right: Poppins 11pt GREY_BODY 40% opacity. Value: "02".

---

## Slide 3: Why JOINs Matter
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Why" + "JOINs Matter"
- **Content:**
  - Every real database splits data across multiple tables to avoid repetition
  - Without JOINs, each table is an island — you cannot cross-reference data
  - JOINs are the bridge that connects tables and unlocks real business answers
  - Example: "Which customers placed an order last month?" — impossible without a JOIN
  - Master JOINs and you can answer almost any data question
- **Visual spec:** Dark hero slide. Headline centered white + GREEN_LIGHT. 5 icon-badge rows centered x=640, each with GREEN_MID circle badge r=22 and white label. Soft radial glow top-center GREEN_LIGHT opacity 0.12. Center: simple three-table "island" icon with a bridge/arrow motif between them.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. Dark green background (#1A6B3A).
  2. Add soft glow circle top-center: GREEN_LIGHT (#5CDB8F) fill, opacity 12%, large radius, no border.
  3. Headline: "Why" Poppins 36pt Bold White, centered x=640 y=100. Second line: "JOINs Matter" Poppins 36pt Bold GREEN_LIGHT, centered.
  4. 5 icon-badge rows centered x=640, starting y=220, spacing 70px. Badge: circle r=22 GREEN_MID, white icon. Label: Poppins 14pt White beside badge, left-aligned from badge.
  5. Slide number: "03" bottom-right Poppins 11pt white 40% opacity.
- **QC note:** Replaces redundant Learning Objectives slide (duplicate of Agenda). Provides motivating "why" context instead.

---

## Slide 4: Why Do Multiple Tables Exist?
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Why" + "Multiple Tables?"
- **Content:**
  - Real databases split data into separate tables to avoid repetition — this is called **normalization**
  - Tables connect via a shared column called a **foreign key**
  - A JOIN tells SQL: "combine rows from both tables where the keys match"
- **Visual spec:** Left panel: two-tone headline + GREEN_MID divider + 3 bullets. Right panel: two-table diagram — Customers table (CustomerID, Name) linked by green arrow to Orders table (OrderID, CustomerID, Amount), arrow labeled "JOIN on CustomerID". Callout boxes with GREEN_MID border highlight the terms "normalization" (left panel) and "foreign key" (arrow label).
- **Image query:** database normalization two tables relationship
- **Image style:** diagram
- **PPT build notes:**
  1. White background.
  2. Left panel (x=60–520): two-tone headline Poppins 36pt Bold. GREEN_MID divider line. Body bullets Poppins 14pt GREY_BODY, line spacing 1.5. Max 3 bullets.
  3. Right panel (x=560–1220): draw two table shapes (rounded rectangles, thin GREEN_MID border). Left table "Customers" with rows: CustomerID | Name. Right table "Orders" with rows: OrderID | CustomerID | Amount. Green arrow connecting CustomerID columns, labeled "JOIN on CustomerID" Poppins 11pt GREEN_MID.
  4. Add callout box (small rounded rect, GREEN_MID border, no fill) around "normalization" in bullet 1 and around "foreign key" in bullet 2 to visually distinguish key terms.
  5. Slide number: "04" bottom-right GREY_BODY 40% opacity.
- **QC note:** Reduced from 6 bullets (~65 words) to 3 bullets to meet the 30-word body limit.

---

## Slide 5: The JOIN Syntax Blueprint
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "The" + "JOIN Syntax Blueprint"
- **Content:**
  - Every JOIN follows the same skeleton:
  ```sql
  SELECT table1.column, table2.column
  FROM   table1
  [JOIN TYPE] table2
    ON table1.shared_key = table2.shared_key;
  ```
  - Four parts to remember:
    1. SELECT — which columns you want
    2. FROM — your starting (left) table
    3. JOIN TYPE + table name — which table to combine and how
    4. ON — the condition that links the two tables
- **Visual spec:** Dark hero slide. Headline white. Code block displayed as a monospaced white-on-dark-card rectangle (Courier New 15pt, white text, semi-transparent white background panel). Below the code block: 4 numbered icon-badge rows explaining each part, each badge GREEN_MID.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. Dark green background.
  2. Soft glow top-center GREEN_LIGHT 12% opacity.
  3. Headline: "The" Poppins 36pt Bold White + "JOIN Syntax Blueprint" GREEN_LIGHT, centered y=100.
  4. Code block panel: rounded rectangle x=200–1080 y=160–320, fill white 15% opacity, border white 30% opacity. Inside: Courier New 15pt White, the SQL skeleton above. Highlight [JOIN TYPE] in GREEN_LIGHT.
  5. Below code block (y=350): 4 icon-badge rows, badge r=22 GREEN_MID, label Poppins 13pt White. Center-align the block at x=640.
  6. Slide number: "05" Poppins 11pt white 40%.

---

## Slide 6: Our Sample Data — Meet the Tables
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Our" + "Sample Data"
- **Content:**
  **Customers table**
  | CustomerID | Name       | City     |
  |------------|------------|----------|
  | 1          | Alice       | London   |
  | 2          | Bob         | Paris    |
  | 3          | Carol       | Berlin   |
  | 4          | Dan         | Madrid   |

  **Orders table**
  | OrderID | CustomerID | Product   | Amount |
  |---------|------------|-----------|--------|
  | 101     | 1          | Laptop    | 1200   |
  | 102     | 2          | Phone     | 800    |
  | 103     | 1          | Mouse     | 25     |
  | 104     | 5          | Keyboard  | 75     |

  Note: Customer 5 does not exist in Customers. Dan (CustomerID=4) has no orders. These gaps are intentional — they show the difference between join types.
- **Visual spec:** Left panel: two-tone headline + divider + brief intro text. Right panel: two formatted tables rendered as PowerPoint table shapes. Use alternating light-green row shading. Highlight CustomerID column header in GREEN_MID. Add annotation box pointing to CustomerID=5 in Orders: "No matching customer!" and pointing to Dan (ID=4): "No orders!".
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. White background.
  2. Left panel (x=60–440): headline + divider + intro text Poppins 13pt GREY_BODY "We will use these two tables for every example in this session."
  3. Right panel (x=460–1220): two PPT table shapes stacked vertically. Header row fill GREEN_MID, white text Poppins 11pt Bold. Alternating data rows: white / very-light-green (#E8F8EE). Cell text Poppins 11pt GREY_BODY.
  4. Add call-out annotation boxes (small rectangle + arrow, GREEN_MID border) pointing to CustomerID=5 and CustomerID=4.
  5. Slide number: "06" GREY_BODY 40%.

---

## Slide 7: Section 1 — INNER JOIN
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Section 1 —" + "INNER JOIN"
- **Content:**
  - Returns only rows where the join condition matches in BOTH tables
  - Think of it as the intersection in a Venn diagram
  - Unmatched rows from either side are silently dropped
  - Most commonly used JOIN type
  - Use when: you only want confirmed pairs
- **Visual spec:** Dark hero slide. Large Venn diagram in the center of the slide: two overlapping circles in white outline, the overlapping region filled GREEN_MID. Label left circle "Customers", right circle "Orders", overlap "Matched rows only". Below: three icon-badge bullets on use cases.
- **Image query:** Venn diagram inner join SQL overlap
- **Image style:** diagram
- **PPT build notes:**
  1. Dark green background with soft glow.
  2. Headline centered white + GREEN_LIGHT accent, y=80.
  3. Draw Venn diagram: two circle shapes (no fill, WHITE border 2pt, 50% opacity) centered at x=480 and x=800, y=380, radius ~130px. Overlap region: custom overlap shape, fill GREEN_MID, 80% opacity.
  4. Circle labels: "Customers" Poppins 14pt White outside left circle; "Orders" Poppins 14pt White outside right circle. Overlap label: "Matched rows" Poppins 12pt NEAR_BLACK inside overlap fill.
  5. Right of diagram: 3 icon-badge bullet rows from y=280, badge r=18 GREEN_MID.
  6. Slide number: "07" white 40%.

---

## Slide 8: INNER JOIN — Syntax and Worked Example
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "INNER JOIN —" + "Worked Example"
- **Content:**
  **Query:**
  ```sql
  SELECT Customers.Name, Orders.Product, Orders.Amount
  FROM   Customers
  INNER JOIN Orders
    ON Customers.CustomerID = Orders.CustomerID;
  ```

  **Result:**
  | Name  | Product  | Amount |
  |-------|----------|--------|
  | Alice | Laptop   | 1200   |
  | Bob   | Phone    | 800    |
  | Alice | Mouse    | 25     |

  What happened:
  - Carol (no orders) → excluded
  - Dan (no orders) → excluded
  - OrderID 104 (CustomerID=5, no customer) → excluded
  - Only Alice and Bob appear because they have matching records in BOTH tables
- **Visual spec:** Left panel: two-tone headline + divider + code block (Courier New, light grey background #F4F4F8, NEAR_BLACK text, GREEN_MID for keywords). Right panel: result table with green header, followed by annotation list explaining what was excluded and why. Draw a small "excluded" stamp icon (red-X or strikethrough line) beside Carol, Dan, and OrderID 104.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. White background.
  2. Left panel (x=60–560): headline Poppins 36pt two-tone + divider. Code block rectangle fill #F4F4F8, rounded corners 8px. Code text Courier New 13pt NEAR_BLACK. Keywords SELECT/FROM/INNER JOIN/ON in GREEN_MID Bold.
  3. Right panel (x=580–1220): result table (PPT table shape), header GREEN_MID. Below table: annotation list with red-X shape + Poppins 12pt GREY_BODY explanation per excluded row.
  4. Slide number: "08" GREY_BODY 40%.

---

## Slide 9: Practice — Try It Yourself (INNER JOIN)
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "In-Class" + "Practice: INNER JOIN"
- **Content:**
  Using the Customers and Orders tables from Slide 6:

  **Exercise 1 (Warm-up):**
  Write a query that returns each customer's Name and the Amount they spent. Only include customers who have at least one order.

  **Exercise 2 (Stretch):**
  Modify Exercise 1 to also include the Product column. Sort the results by Amount descending.

  **Expected output for Exercise 1:**
  | Name  | Amount |
  |-------|--------|
  | Alice | 1200   |
  | Bob   | 800    |
  | Alice | 25     |

  Hint: Start with SELECT, then FROM Customers, then INNER JOIN Orders ON …
- **Visual spec:** Dark hero slide. Headline centered white. Two exercise panels rendered as frosted cards (white 18% opacity, rounded corners) stacked vertically left-of-center. Expected output table to the right as a smaller card. Hint text in GREEN_LIGHT italic below the cards.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. Dark green background with soft glow.
  2. Headline centered white + GREEN_LIGHT, y=80.
  3. Exercise 1 card: rounded rectangle x=80–620 y=160–360, fill white 18% opacity. Inside: "Exercise 1 (Warm-up)" Poppins 14pt Bold GREEN_LIGHT; exercise text Poppins 13pt White.
  4. Exercise 2 card: x=80–620 y=380–520, same style. Label: "Exercise 2 (Stretch)" in GREEN_LIGHT.
  5. Expected output table: x=660–1200 y=200–400, card background white 15% opacity, table text Courier New 12pt White.
  6. Hint text: x=80 y=545, Poppins 12pt GREEN_LIGHT italic.
  7. Slide number: "09" white 40%.

---

## Slide 10: Section 2 — LEFT JOIN
- **Layout pattern:** G
- **Background mode:** white
- **Headline:** "Section 2 —" + "LEFT JOIN"
- **Content:**
  - Returns ALL rows from the left table + matching rows from the right table
  - If the right table has no match, the right-side columns are filled with NULL
  - The left table is never filtered — every row appears in the result
  - Use when: you have a master list and want to see what is (and is not) matched
  - Real-world example: "Show me all customers, even those who have never placed an order"

  **Stats:**
  - Left table rows always preserved: 100%
  - Right-side NULLs reveal unmatched records
- **Visual spec:** Left panel: two-tone headline + body text + use-case bullets. Right panel: two stat callout cards (100% / NULL pattern) with GREEN_MID badge icons. Below stat cards: small Venn diagram showing full left circle + partial right overlap.
- **Image query:** Venn diagram left join SQL all left rows
- **Image style:** diagram
- **PPT build notes:**
  1. White background.
  2. Left panel (x=60–580): headline Poppins 36pt + divider + body bullets Poppins 14pt GREY_BODY.
  3. Right panel (x=620–1220): two stat cards (rounded rect, thin GREEN_MID border). Top card: "100%" Poppins 40pt Bold NEAR_BLACK, label "Left table rows always kept" Poppins 11pt GREY_BODY. Bottom card: "NULL" Poppins 40pt Bold GREEN_MID, label "Fills unmatched right-side columns" Poppins 11pt GREY_BODY.
  4. Small Venn diagram at bottom-right corner (decorative): full left circle filled GREEN_MID, right circle outline only white with overlap region slightly lighter.
  5. Slide number: "10" GREY_BODY 40%.

---

## Slide 11: LEFT JOIN — Syntax and Worked Example
- **Layout pattern:** B
- **Background mode:** dark-green
- **Headline:** "LEFT JOIN —" + "Worked Example"
- **Content:**
  **Query:**
  ```sql
  SELECT Customers.Name, Orders.Product, Orders.Amount
  FROM   Customers
  LEFT JOIN Orders
    ON Customers.CustomerID = Orders.CustomerID;
  ```

  **Result:**
  | Name  | Product  | Amount |
  |-------|----------|--------|
  | Alice | Laptop   | 1200   |
  | Alice | Mouse    | 25     |
  | Bob   | Phone    | 800    |
  | Carol | NULL     | NULL   |
  | Dan   | NULL     | NULL   |

  Key insight: Carol and Dan now appear with NULL — the LEFT JOIN preserved them. OrderID 104 (CustomerID=5) is still excluded because its customer does not exist in the left table.
- **Visual spec:** Left panel: headline both words white (dark-slide rule) + code block (dark card, Courier New, white text, GREEN_LIGHT keywords). Right panel: result table with GREEN_MID header, NULL cells highlighted in a very light tint using WHITE at 10% opacity to draw attention — no off-palette colors. Annotation arrow in GREEN_LIGHT pointing to Carol/Dan rows: "Preserved by LEFT JOIN".
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. Dark green background.
  2. Headline on dark slide: BOTH parts "LEFT JOIN —" and "Worked Example" in Poppins 36pt Bold White (#FFFFFF), left-aligned x=80. Dark slides use all-white headlines per design system.
  3. Left panel code block: rounded rect fill BLACK 30% opacity, border WHITE 20%. Code text Courier New 13pt WHITE, keywords (LEFT JOIN, ON, SELECT, FROM) in GREEN_LIGHT Bold.
  4. Right panel (x=640–1220): PPT table, header GREEN_MID. NULL cells: apply subtle white-fill highlight (White 10% opacity rectangle overlay) to distinguish NULL from data values — no red or yellow fills.
  5. Annotation: small text box + arrow GREEN_LIGHT pointing to Carol/Dan rows: "Preserved by LEFT JOIN".
  6. Slide number: "11" white 40%.
- **QC note:** Both headline words corrected to white — dark slides must not apply two-tone coloring per deck-analysis.md rule.

---

## Slide 12: RIGHT JOIN — The Mirror Image
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "RIGHT JOIN —" + "The Mirror Image"
- **Content:**
  - Returns ALL rows from the right table + matching rows from the left table
  - If the left table has no match, left-side columns fill with NULL
  - Prefer LEFT JOIN for portability — swap table order to get the same result (SQLite does not support RIGHT JOIN)
- **Visual spec:** Left panel: two-tone headline + GREEN_MID divider + 3 bullets Poppins 14pt GREY_BODY. Right panel: small Venn diagram showing full right circle filled GREEN_MID, left circle outline only WHITE. Below Venn: a single annotation callout "Prefer: swap tables and use LEFT JOIN" in GREEN_MID Bold.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. White background.
  2. Left panel (x=60–500): headline Poppins 36pt two-tone ("RIGHT JOIN —" NEAR_BLACK, "The Mirror Image" GREEN_MID) + GREEN_MID divider + 3 bullets Poppins 13pt GREY_BODY.
  3. Right panel (x=540–1220): Venn diagram centered — right circle fill GREEN_MID 80% opacity, left circle outline only (GREEN_MID stroke, no fill). Circle labels Poppins 13pt NEAR_BLACK. Below diagram: callout box (rounded rect, GREEN_MID border) labeled "Tip: Swap tables → use LEFT JOIN instead" Poppins 13pt GREEN_MID Bold.
  4. Slide number: "12" GREY_BODY 40%.
- **QC note:** Removed inline code block (moved to speaker notes) to reduce density below 30 words. Core concept preserved in 3 focused bullets. Equivalence code: speaker notes read "SELECT * FROM Customers RIGHT JOIN Orders ON … equals SELECT * FROM Orders LEFT JOIN Customers ON …"

---

## Slide 13: Common Mistake — The NULL Trap
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Watch Out —" + "The NULL Trap"
- **Content:**
  **The mistake:** Filtering a LEFT JOIN result with WHERE on a right-table column.

  ```sql
  -- WRONG: This silently converts LEFT JOIN into INNER JOIN
  SELECT Customers.Name, Orders.Amount
  FROM   Customers
  LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
  WHERE  Orders.Amount > 100;   -- <-- kills NULL rows!

  -- CORRECT: Move the filter to the ON clause
  SELECT Customers.Name, Orders.Amount
  FROM   Customers
  LEFT JOIN Orders
    ON Customers.CustomerID = Orders.CustomerID
    AND Orders.Amount > 100;
  ```

  Result: In the WRONG version, Carol and Dan disappear. In the CORRECT version, they remain with NULL.
- **Visual spec:** Dark hero "callout" slide. Warning icon badge (GREEN_LIGHT circle r=28, white "!" icon) at top-center above the headline. Two code block panels side by side: "WRONG" with NEAR_BLACK header bar, "CORRECT" with GREEN_MID header bar. Annotation below each panel in WHITE.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. Dark green background.
  2. Warning badge: circle r=28 fill GREEN_LIGHT (#5CDB8F), white "!" text centered Poppins 20pt Bold. Position x=640 y=70.
  3. Headline: "Watch Out —" Poppins 36pt Bold White (#FFFFFF) + "The NULL Trap" in GREEN_LIGHT (#5CDB8F), centered y=130. No red in headline text — approved palette only.
  4. Two code block panels x=80–600 (WRONG) and x=680–1200 (CORRECT), y=210–510. WRONG panel: header bar fill NEAR_BLACK (#1A1A2E), label "WRONG" Poppins 12pt White Bold. CORRECT panel: header bar fill GREEN_MID (#2EAA5E), label "CORRECT" White Bold. Code: Courier New 12pt White.
  5. Annotation below panels: Poppins 11pt WHITE 80% explaining what each version returns.
  6. Slide number: "13" white 40%.
- **QC note:** Critical fix — headline accent changed from off-palette RED (#CC3333) to GREEN_LIGHT (#5CDB8F). WRONG panel header now uses NEAR_BLACK (on-palette).

---

## Slide 14: Section 1 & 2 Summary
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Section" + "Summary"
- **Content:**
  | JOIN Type   | Left rows kept? | Right rows kept? | Use when...                      |
  |-------------|-----------------|------------------|----------------------------------|
  | INNER JOIN  | Only matched    | Only matched     | You need confirmed pairs only    |
  | LEFT JOIN   | All             | Only matched     | Preserve master list on the left |
  | RIGHT JOIN  | Only matched    | All              | Preserve master list on the right (prefer LEFT instead) |

  Key takeaways:
  - INNER = intersection only
  - LEFT = left table is the boss
  - RIGHT = right table is the boss (but just swap tables and use LEFT)
  - NULL in result = "no match found on that side"
- **Visual spec:** Left panel: two-tone headline + GREEN_MID divider + "Key takeaways" bullets. Right panel: summary comparison table, column headers GREEN_MID. INNER JOIN row: white (#FFFFFF). LEFT JOIN row: very-light-green (#E8F8EE). RIGHT JOIN row: light grey (#F4F4F4). No blue or yellow tints — approved palette only.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. White background.
  2. Left panel (x=60–480): headline + divider + key takeaways as 4 bullet rows Poppins 13pt GREY_BODY.
  3. Right panel (x=500–1220): 4-row comparison table (header + 3 join types). Header: fill GREEN_MID, white text Poppins 12pt Bold. INNER row: white (#FFFFFF). LEFT row: light green (#E8F8EE). RIGHT row: light grey (#F4F4F4). Cell text Poppins 11pt NEAR_BLACK.
- **QC note:** Row tints corrected — removed off-palette blue and yellow fills; now uses white, light-green, and light-grey within approved palette.
  4. Slide number: "14" GREY_BODY 40%.

---

## Slide 15: Section 3 — FULL OUTER JOIN
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Section 3 —" + "FULL OUTER JOIN"
- **Content:**
  - Returns ALL rows from BOTH tables
  - Where there is no match on either side, NULL fills those columns
  - Combines the behavior of LEFT JOIN + RIGHT JOIN
  - Think of it as: "Show me everything, gaps and all"
  - Use when: comparing two datasets, finding mismatches, reconciling data
  - Note: Not supported in SQLite or older MySQL — use UNION of LEFT + RIGHT JOIN instead
- **Visual spec:** Dark hero slide. Large Venn diagram centered: BOTH circles fully filled (left circle GREEN_MID, right circle lighter green #5CDB8F, overlap region WHITE outline). Label: "All rows from both tables". Three icon-badge use-case bullets below. Warning badge (small, amber #E89C20) noting database compatibility.
- **Image query:** Venn diagram full outer join both circles filled SQL
- **Image style:** diagram
- **PPT build notes:**
  1. Dark green background with soft glow.
  2. Headline centered white + GREEN_LIGHT, y=80.
  3. Venn diagram: left circle fill GREEN_MID opacity 80%, right circle fill GREEN_LIGHT opacity 70%, overlap slightly blended. Both circles outlined white 1.5pt. Circle labels Poppins 13pt White.
  4. 3 icon-badge rows centered, y=480–580, badge r=18 GREEN_MID.
  5. Compatibility warning: amber circle badge r=18 (#E89C20), text Poppins 12pt White "Not supported in SQLite / older MySQL".
  6. Slide number: "15" white 40%.

---

## Slide 16: FULL OUTER JOIN — Syntax and Worked Example
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "FULL OUTER JOIN —" + "Worked Example"
- **Content:**
  **Query:**
  ```sql
  SELECT Customers.Name, Orders.Product, Orders.Amount
  FROM   Customers
  FULL OUTER JOIN Orders
    ON Customers.CustomerID = Orders.CustomerID;
  ```

  **Result:**
  | Name  | Product  | Amount |
  |-------|----------|--------|
  | Alice | Laptop   | 1200   |
  | Alice | Mouse    | 25     |
  | Bob   | Phone    | 800    |
  | Carol | NULL     | NULL   |
  | Dan   | NULL     | NULL   |
  | NULL  | Keyboard | 75     |

  Three zones in the result:
  1. Matched rows (Alice, Bob) — appear with full data
  2. Left-only rows (Carol, Dan) — Name filled, Orders = NULL
  3. Right-only rows (CustomerID=5) — Name = NULL, Orders filled
- **Visual spec:** Left panel: two-tone headline + code block. Right panel: result table with three zones differentiated by a thin left-border bar: zone 1 (matched) GREEN_MID, zone 2 (left-only) GREY_BODY (#4A4A6A), zone 3 (right-only) GREEN_LIGHT (#5CDB8F). Legend below the table using palette-compliant colors only.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. White background.
  2. Left panel code block: Courier New 13pt NEAR_BLACK, keywords GREEN_MID, fill #F4F4F8.
  3. Right panel table: standard PPT table, header GREEN_MID. Apply left-border bar (4px wide colored rectangle) overlapping first cell of each zone group: GREEN_MID (#2EAA5E) for rows 1–2 (matched), GREY_BODY (#4A4A6A) for rows 3–4 (left-only), GREEN_LIGHT (#5CDB8F) for row 5 (right-only). No blue or amber fills — approved palette only.
  4. Legend: three small colored squares (GREEN_MID, GREY_BODY, GREEN_LIGHT) + label text Poppins 11pt GREY_BODY below table.
- **QC note:** Zone color bars corrected — removed off-palette blue and amber; now uses GREEN_MID, GREY_BODY, GREEN_LIGHT.
  5. Slide number: "16" GREY_BODY 40%.

---

## Slide 17: FULL OUTER JOIN — The UNION Workaround
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "FULL OUTER JOIN —" + "The UNION Workaround"
- **Content:**
  When your database does not support FULL OUTER JOIN (SQLite, MySQL <8.0), combine LEFT and RIGHT JOINs with UNION:

  ```sql
  SELECT Customers.Name, Orders.Product, Orders.Amount
  FROM   Customers
  LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID

  UNION

  SELECT Customers.Name, Orders.Product, Orders.Amount
  FROM   Customers
  RIGHT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
  ```

  UNION automatically removes duplicate rows from the overlap region — so the result is identical to a FULL OUTER JOIN.
- **Visual spec:** Dark hero slide. Headline centered white + GREEN_LIGHT. Large code block card centered (Courier New 14pt White on semi-transparent dark panel). "UNION" keyword highlighted in GREEN_LIGHT Bold, large. Below code block: annotation Poppins 12pt White "UNION removes duplicates — result is identical to FULL OUTER JOIN."
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. Dark green background.
  2. Headline centered y=80.
  3. Code block: rounded rect x=120–1160 y=160–500, fill black 25% opacity, border white 20% opacity. Code Courier New 14pt white. "UNION" in a separate text box: Poppins 18pt Bold GREEN_LIGHT, centered between the two query blocks.
  4. Annotation text below: Poppins 12pt White, centered x=640 y=540.
  5. Slide number: "17" white 40%.

---

## Slide 18: Practice — LEFT & FULL OUTER JOIN
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "In-Class" + "Practice: LEFT & FULL OUTER JOIN"
- **Content:**
  **Exercise 3 — LEFT JOIN:**
  Write a query using the Customers and Orders tables that lists ALL customers, including those who have never placed an order. Show Name and Amount. Customers with no orders should show NULL in the Amount column.

  **Exercise 4 — FULL OUTER JOIN:**
  Extend Exercise 3 to also show orders that have no matching customer (CustomerID=5). What do you expect to see in the Name column for that row?

  **Bonus challenge:**
  How would you rewrite Exercise 4 using UNION if your database does not support FULL OUTER JOIN?
- **Visual spec:** Left panel: two-tone headline + divider + intro sentence. Right panel: three exercise cards stacked (rounded rect, GREEN_MID left accent bar 4px wide, Poppins 13pt GREY_BODY body text, exercise title in NEAR_BLACK Bold 14pt).
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. White background.
  2. Left panel (x=60–440): headline + divider + intro "Work through these exercises in your SQL editor. Raise your hand when done with Exercise 3."
  3. Right panel (x=460–1220): 3 cards stacked, y=140/340/520. Each card: rounded rect fill #F4F4F8, left accent bar 4px GREEN_MID. Title Poppins 14pt Bold NEAR_BLACK. Body Poppins 13pt GREY_BODY.
  4. Slide number: "18" GREY_BODY 40%.

---

## Slide 19: Section 4 — CROSS JOIN
- **Layout pattern:** G
- **Background mode:** dark-green
- **Headline:** "Section 4 —" + "CROSS JOIN"
- **Content:**
  - Produces the Cartesian product: every row in Table A paired with every row in Table B
  - No ON condition needed — every possible combination is included automatically
  - Result rows = (rows in Table A) × (rows in Table B): our example gives 4 × 4 = 16 rows
  - Real use case: generate all size × color product variants in a catalog

  **Warning:** Large tables explode — 1,000 × 1,000 = 1,000,000 rows. Always test with small data first.
- **Visual spec:** Left panel: headline white + GREEN_LIGHT + body text white + use-case bullets with GREEN_MID badges. Right panel: two stat callout cards — "No ON clause needed" (top card) and "Rows = A × B" (bottom card, large formula). Warning badge amber at bottom.
- **Image query:** Cartesian product grid matrix all combinations
- **Image style:** diagram
- **PPT build notes:**
  1. Dark green background.
  2. Left panel (x=60–580): headline Poppins 36pt white + GREEN_LIGHT + divider green-mid. Body bullets Poppins 13pt white 85% opacity. Badge rows r=18 GREEN_MID for use cases.
  3. Right panel (x=620–1220): two rounded rect cards. Top card: "No ON clause" Poppins 24pt Bold WHITE. Bottom card: "Rows = A × B" Poppins 36pt Bold GREEN_LIGHT. Small formula note Poppins 13pt White.
  4. Warning line at bottom: amber (#E89C20) left-accent bar + Poppins 12pt White warning text.
  5. Slide number: "19" white 40%.

---

## Slide 20: CROSS JOIN — Syntax and Worked Example
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "CROSS JOIN —" + "Worked Example"
- **Content:**
  **Query:**
  ```sql
  SELECT Customers.Name, Orders.Product
  FROM   Customers
  CROSS JOIN Orders;
  ```

  **Partial Result (first 8 of 16 rows shown):**
  | Name  | Product  |
  |-------|----------|
  | Alice | Laptop   |
  | Alice | Phone    |
  | Alice | Mouse    |
  | Alice | Keyboard |
  | Bob   | Laptop   |
  | Bob   | Phone    |
  | Bob   | Mouse    |
  | Bob   | Keyboard |

  Observation: Alice is paired with every single order product — even those not hers. This is intentional in a CROSS JOIN.
- **Visual spec:** Left panel: headline + code block. Right panel: partial result table, header GREEN_MID. Below table: a 4×4 grid illustration (matrix diagram) showing Customers on rows, Products on columns, each cell = one result row.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. White background.
  2. Left panel code block: Courier New 13pt NEAR_BLACK, keywords GREEN_MID.
  3. Right panel table: PPT table, 8 rows shown, note "(8 of 16 rows)" in Poppins 10pt GREY_BODY italic below.
  4. Matrix diagram: below or beside table — 4 column headers (products), 4 row headers (customer names), grid cells all filled very light green with small dot indicating "paired". Poppins 10pt GREY_BODY labels. Draw this as a PPT table with colored cells.
  5. Slide number: "20" GREY_BODY 40%.

---

## Slide 21: Section 4 (Part 2) — Self-Join
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Section 4 (Part 2) —" + "Self-Join"
- **QC note:** Renamed from "Section 4 — Self-Join" to distinguish from Slide 19 "Section 4 — CROSS JOIN". Agenda (Slide 2) should be updated to reflect 4A/4B naming.
- **Content:**
  - A Self-Join joins a table to itself
  - Requires table aliases to distinguish the two "copies"
  - Useful for hierarchical data: employees and their managers (both in the same table)

  **Example table: Employees**
  | EmployeeID | Name    | ManagerID |
  |------------|---------|-----------|
  | 1          | Sara    | NULL      |
  | 2          | Tom     | 1         |
  | 3          | Uma     | 1         |
  | 4          | Vic     | 2         |

  ManagerID references EmployeeID in the same table.
- **Visual spec:** Dark hero slide. Headline centered white. Center: org-chart tree diagram (Sara at top, Tom & Uma below, Vic at bottom under Tom) drawn with circle nodes (GREEN_MID fill, white name text) and white connecting lines. Below diagram: annotation explaining ManagerID = EmployeeID self-reference.
- **Image query:** employee manager hierarchy org chart database
- **Image style:** diagram
- **PPT build notes:**
  1. Dark green background with soft glow.
  2. Headline centered y=80.
  3. Org-chart: draw circle shapes (r=36, fill GREEN_MID) for each employee node. White connecting lines (2pt) from manager circle to report circles. Names: Poppins 13pt Bold White inside circles. Position Sara x=640 y=220; Tom x=480 y=360; Uma x=800 y=360; Vic x=480 y=500.
  4. Table: small card bottom-left showing Employees table, Courier New 11pt White, card fill white 15% opacity.
  5. Annotation: "ManagerID references EmployeeID in the same table" Poppins 12pt GREEN_LIGHT, centered y=600.
  6. Slide number: "21" white 40%.

---

## Slide 22: Self-Join — Syntax and Worked Example
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Self-Join —" + "Worked Example"
- **Content:**
  **Query:**
  ```sql
  SELECT e.Name AS Employee, m.Name AS Manager
  FROM   Employees AS e
  LEFT JOIN Employees AS m
    ON e.ManagerID = m.EmployeeID;
  ```

  **Result:**
  | Employee | Manager |
  |----------|---------|
  | Sara     | NULL    |
  | Tom      | Sara    |
  | Uma      | Sara    |
  | Vic      | Tom     |

  Key points:
  - "e" is the employee copy; "m" is the manager copy — same physical table
  - LEFT JOIN is used so Sara (no manager) still appears with NULL
  - Without aliases (e, m), SQL would not know which copy of Employees each column refers to
- **Visual spec:** Left panel: headline + code block with aliases highlighted in GREEN_MID. Right panel: result table + annotation callouts. Arrow from "e.ManagerID" in code → "m.EmployeeID" annotation showing the self-referential link.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. White background.
  2. Left panel: code block fill #F4F4F8, Courier New 13pt. Highlight "AS e" and "AS m" in GREEN_MID Bold. Highlight ON clause in a light yellow highlight rectangle behind the text.
  3. Right panel: PPT result table, header GREEN_MID. Below table: 3 annotation bullet points Poppins 12pt GREY_BODY with key insight icons (small green circles r=10).
  4. Arrow callout: draw a curved arrow from the code ON clause to a small annotation box: "Same table, two aliases".
  5. Slide number: "22" GREY_BODY 40%.

---

## Slide 23: Section 4 Summary — CROSS JOIN & Self-Join
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Section 4" + "Summary"
- **Content:**
  | Type       | ON clause? | Typical use                        | Watch out for               |
  |------------|------------|------------------------------------|-----------------------------|
  | CROSS JOIN | No         | All combinations, test data, grids | Row explosion on large tables|
  | Self-Join  | Yes        | Hierarchical data, comparisons     | Must use table aliases       |

  Remember:
  - CROSS JOIN has no condition — every row meets every other row
  - Self-Join is not a JOIN type — it is a technique using any JOIN type on the same table
  - Always use LEFT JOIN for self-referential hierarchy so top-level rows (no manager) are preserved
- **Visual spec:** Dark hero slide. Summary table rendered as a styled card (white 15% opacity rounded rect). Three icon-badge "remember" bullets below the table. Soft glow atmosphere.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. Dark green background.
  2. Headline centered white + GREEN_LIGHT, y=80.
  3. Summary table card: rounded rect x=80–1200 y=160–400, fill white 15% opacity. Inside: draw PPT table — header row GREEN_MID White text, data rows Courier New 12pt White.
  4. Three icon-badge "Remember" bullets below card: badge r=18 GREEN_LIGHT, label Poppins 13pt White.
  5. Slide number: "23" white 40%.

---

## Slide 24: Practice — CROSS JOIN & Self-Join
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "In-Class" + "Practice: CROSS JOIN & Self-Join"
- **Content:**
  **Exercise 5 — CROSS JOIN:**
  Using the Customers table (4 rows) and a new Colors table with 3 rows (Red, Blue, Green), write a CROSS JOIN query. How many rows will the result have? Write the query and verify.

  **Exercise 6 — Self-Join:**
  Using the Employees table from Slide 21, write a query that lists every employee alongside their manager's name. Employees with no manager (Sara) should still appear in the result with NULL in the Manager column.

  **Reflection question:** Why do we need two aliases (e and m) in a self-join? What would happen if we wrote FROM Employees JOIN Employees ON … without aliases?
- **Visual spec:** Left panel: headline + divider + intro sentence. Right panel: exercise cards with green left-accent bar, plus reflection question card with amber left-accent bar to signal it is conceptual rather than coding.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. White background.
  2. Left panel (x=60–440): headline + divider + "Work through each exercise. Check your results with your neighbor." Poppins 13pt GREY_BODY.
  3. Right panel (x=460–1220): Exercise 5 card y=140–300 (GREEN_MID left bar). Exercise 6 card y=320–480 (GREEN_MID left bar). Reflection card y=500–620 (amber #E89C20 left bar, label "Think & Discuss").
  4. Slide number: "24" GREY_BODY 40%.

---

## Slide 25: Section 5 — Joining More Than Two Tables
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Section 5 —" + "Multiple JOINs"
- **Content:**
  - You can chain as many JOINs as needed in a single query
  - Each JOIN adds one more table to the result set
  - SQL processes JOINs from top to bottom — each JOIN builds on the previous result

  **Extended schema for this section:**
  - Customers (CustomerID, Name, City)
  - Orders (OrderID, CustomerID, ProductID, Amount)
  - Products (ProductID, ProductName, Category)

  **Concept:** Order → Customer + Product
  A single order row can be enriched with both customer name and product name in one query.
- **Visual spec:** Dark hero slide. Headline centered. Center: chain diagram — three table boxes (rounded rectangles, GREEN_MID outline, white text labels) connected by right-pointing arrows labeled "JOIN". Table boxes: Customers → Orders → Products. Below chain diagram: three icon-badge bullets explaining the sequential enrichment concept.
- **Image query:** multiple SQL tables join chain three tables
- **Image style:** diagram
- **PPT build notes:**
  1. Dark green background with soft glow.
  2. Headline centered white + GREEN_LIGHT, y=80.
  3. Chain diagram: three rounded rect boxes y=280 centered. Customers x=120–400; Orders x=500–760; Products x=860–1160. Each box: fill white 15% opacity, border GREEN_MID 2pt, label Poppins 14pt Bold White. Arrows: right-pointing arrow shapes GREEN_LIGHT between boxes, label "JOIN" Poppins 11pt WHITE above arrows.
  4. Three bullet rows below diagram y=450–560, badge r=18 GREEN_MID.
  5. Slide number: "25" white 40%.

---

## Slide 26: Multiple JOINs — Syntax and Worked Example
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Multiple JOINs —" + "Worked Example"
- **Content:**
  **Query — 3 tables joined:**
  ```sql
  SELECT Customers.Name,
         Products.ProductName,
         Orders.Amount
  FROM   Orders
  INNER JOIN Customers
    ON Orders.CustomerID = Customers.CustomerID
  INNER JOIN Products
    ON Orders.ProductID = Products.ProductID;
  ```

  **Result:**
  | Name  | ProductName | Amount |
  |-------|-------------|--------|
  | Alice | Laptop      | 1200   |
  | Bob   | Phone       | 800    |
  | Alice | Mouse       | 25     |

  Pattern to notice:
  - Start FROM the "fact" table (Orders) — the one with foreign keys
  - Add one INNER JOIN per dimension table (Customers, Products)
  - Each ON clause maps back to the fact table's foreign key
- **Visual spec:** Left panel: headline + code block with each JOIN line highlighted in different shade (first JOIN line slightly highlighted, second JOIN line slightly different shade). Right panel: result table + "Pattern" annotation box with 3 numbered steps in NEAR_BLACK Bold.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. White background.
  2. Left panel code block (x=60–580): Courier New 13pt, keywords GREEN_MID. Draw subtle left-accent rectangles behind each JOIN block in alternating very light green and very light blue to show the two JOINs visually.
  3. Right panel (x=600–1220): result table top half. Below table: "Pattern" card — rounded rect fill #F4F4F8, header bar GREEN_MID, 3 numbered steps Poppins 12pt NEAR_BLACK.
  4. Slide number: "26" GREY_BODY 40%.

---

## Slide 27: Common Mistake — Ambiguous Column Names
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Watch Out —" + "Ambiguous Column Names"
- **Content:**
  **The mistake:** When two tables share a column name (like CustomerID), SQL does not know which one you mean.

  ```sql
  -- WRONG: Which CustomerID?
  SELECT CustomerID, Name, Amount
  FROM   Customers
  INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

  -- CORRECT: Always prefix with table name (or alias)
  SELECT Customers.CustomerID, Customers.Name, Orders.Amount
  FROM   Customers
  INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
  ```

  **Best practice:** Use table aliases for shorter, cleaner queries:
  ```sql
  SELECT c.CustomerID, c.Name, o.Amount
  FROM   Customers AS c
  INNER JOIN Orders AS o ON c.CustomerID = o.CustomerID;
  ```
- **Visual spec:** Dark callout slide. Warning badge (GREEN_LIGHT circle r=28, white "!" icon) above headline. Three code block panels: WRONG (NEAR_BLACK header), CORRECT (GREEN_MID header), BEST PRACTICE (GREEN_MID header, GREEN_LIGHT star badge). Each panel Courier New 13pt White.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. Dark green background.
  2. Warning badge: circle fill GREEN_LIGHT (#5CDB8F), white "!" Poppins 20pt Bold. x=640 y=70.
  3. Headline: "Watch Out —" White (#FFFFFF) + "Ambiguous Column Names" GREEN_LIGHT (#5CDB8F). Centered y=130. No red in headline — approved palette only.
  4. Three code panels arranged x=60–400 / x=440–780 / x=820–1220, y=200–560. WRONG: NEAR_BLACK (#1A1A2E) header bar. CORRECT: GREEN_MID header. BEST PRACTICE: GREEN_MID header + small GREEN_LIGHT star badge top-right corner.
  5. Slide number: "27" white 40%.
- **QC note:** Critical fix — headline accent and badge changed from off-palette RED (#CC3333) to GREEN_LIGHT (#5CDB8F). WRONG panel header uses NEAR_BLACK (on-palette).

---

## Slide 28: Common Mistake — Joining on the Wrong Column
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Watch Out —" + "Wrong Join Key"
- **Content:**
  **The mistake:** Joining on a column that looks like a key but is not the right relationship.

  Example of WRONG join:
  ```sql
  -- WRONG: joining on Name instead of CustomerID
  SELECT *
  FROM Customers
  INNER JOIN Orders ON Customers.Name = Orders.CustomerID;
  ```
  This returns zero rows (or nonsense) because Name is a text column and CustomerID is a number.

  **How to find the correct join key:**
  1. Look at the ERD (Entity-Relationship Diagram) for your database
  2. The foreign key in one table always points to the primary key of another
  3. Ask: "What column in Table B references Table A's primary key?"
- **Visual spec:** Left panel: headline + code block showing the WRONG query with a large red "X" overlay on it. Right panel: simple ERD diagram showing Customers (PK: CustomerID) → Orders (FK: CustomerID) with the correct join column circled in GREEN_MID.
- **Image query:** entity relationship diagram ERD primary foreign key SQL
- **Image style:** diagram
- **PPT build notes:**
  1. White background.
  2. Left panel (x=60–560): code block fill #F4F4F8. Draw a large red diagonal cross (X) shape over the code block to mark it WRONG. Small label "Result: 0 rows or nonsense" Poppins 11pt RED below.
  3. Right panel (x=580–1220): ERD diagram — two rounded table cards connected by an arrow. Arrow labeled "CustomerID (FK → PK)". Circle GREEN_MID highlight drawn around the CustomerID cell in each table. Below: 3 numbered steps Poppins 12pt GREY_BODY.
  4. Slide number: "28" GREY_BODY 40%.

---

## Slide 29: Common Mistake — Duplicate Rows from One-to-Many
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Watch Out —" + "Unexpected Duplicate Rows"
- **Content:**
  **The situation:** Alice has TWO orders, so she appears TWICE in a JOIN result — one row per order. This is correct behavior, not a bug.

  ```sql
  SELECT Customers.Name, Orders.Amount
  FROM   Customers
  INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
  ```

  Result: Alice appears twice (Laptop $1200, Mouse $25). If you need one row per customer, use GROUP BY with SUM — covered in the next session.

  **Key insight:** Always check row count before and after a JOIN. Unexpected duplicates signal a one-to-many relationship.
- **Visual spec:** Dark hero slide. Warning badge (GREEN_LIGHT circle r=28, white "!" icon) above headline. Single code block card centered (x=100–1180), result snippet below showing Alice twice with annotation arrows. Key insight callout at bottom in GREEN_LIGHT italic.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. Dark green background.
  2. Warning badge: circle r=28 GREEN_LIGHT (#5CDB8F), white "!" Poppins 20pt Bold. Centered above headline.
  3. Headline: "Watch Out —" White (#FFFFFF) + "Unexpected Duplicate Rows" GREEN_LIGHT (#5CDB8F). Centered.
  4. Single code block card x=100–1180 y=190–360: rounded rect fill white 15% opacity. Code Courier New 13pt White, keywords GREEN_LIGHT.
  5. Result snippet below code: small table showing Alice x2. Annotation arrow (GREEN_LIGHT) pointing to duplicate rows with label "One order = one row".
  6. Key insight box at bottom: rounded rect GREEN_MID border, Poppins 13pt WHITE "Always check row count — duplicates mean one-to-many". Center x=640 y=560.
  7. Slide number: "29" white 40%.
- **QC note:** Removed second GROUP BY code block (moved to speaker notes) to reduce density. Core insight preserved in one code block + annotation.

---

## Slide 30: Best Practices Checklist
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Best" + "Practices"
- **Content:**
  - Always prefix columns with table name or alias: write c.Name, not just Name
  - Use meaningful aliases: c for Customers, o for Orders — never a and b
  - Start FROM the "fact" table — the one that holds the foreign keys
  - Verify your join key in the ERD before writing the query
  - Move right-table filters to the ON clause, not WHERE (prevents the NULL trap)

  **Speaker notes (items 6–8 for instructor reference):** Use LEFT JOIN to preserve all rows from one side. Check row count before and after every JOIN. Test with small datasets before running on production tables.
- **Visual spec:** Left panel: two-tone headline + GREEN_MID divider + intro sentence. Right panel: 5 checklist rows, each with a green checkmark circle badge (r=20, fill GREEN_MID, white checkmark icon) + label text Poppins 13pt NEAR_BLACK. Adequate whitespace between rows — no crowding.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. White background.
  2. Left panel (x=60–440): headline + divider + "Apply these habits from day one." Poppins 13pt GREY_BODY.
  3. Right panel (x=460–1220): 5 icon-badge rows, badge r=20 GREEN_MID, checkmark icon white inside. Label Poppins 13pt NEAR_BLACK. Row height 80px, start y=160 — generous whitespace.
- **QC note:** Reduced from 8 to 5 checklist items to respect cognitive load limit. Items 6–8 moved to speaker notes for instructor reference.
  4. Slide number: "30" GREY_BODY 40%.

---

## Slide 31: Comprehensive Practice — Part 1
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Putting It" + "All Together (Part 1)"
- **Content:**
  Use the extended schema: Customers, Orders, Products.

  **Exercise 7 (INNER JOIN × 2):**
  Write a query returning each customer's Name, the ProductName they ordered, and the Amount. Only include orders where both the customer and product exist.

  **Exercise 8 (LEFT JOIN):**
  Modify Exercise 7 to also show customers with no orders. Which columns will be NULL for those customers?
- **Visual spec:** Dark hero slide. Headline centered white + GREEN_LIGHT. Two exercise cards centered vertically (one per row), each a frosted panel (white 18% opacity, rounded corners 12px). Card header bar GREEN_MID. Exercise text Poppins 13pt White. Adequate padding inside each card.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. Dark green background with soft glow.
  2. Headline centered y=80.
  3. Exercise 7 card: x=100–1180 y=180–390, rounded rect fill white 18% opacity, header bar GREEN_MID. Title Poppins 14pt Bold WHITE. Body Poppins 13pt White 85% opacity.
  4. Exercise 8 card: x=100–1180 y=420–600, same style.
  5. Slide number: "31" white 40%.
- **QC note:** Split from 4-exercise 2×2 grid into two slides. This slide covers Exercises 7–8 (INNER + LEFT JOIN). See Slide 31b for Exercises 9–10.

---

## Slide 31b: Comprehensive Practice — Part 2
- **Layout pattern:** F
- **Background mode:** dark-green
- **Headline:** "Practice —" + "Self-Join & GROUP BY"
- **Content:**
  Use the Employees table for Exercise 9 and Customers/Orders for Exercise 10.

  **Exercise 9 (Self-Join):**
  Write a query listing every employee and their manager's name. Employees with no manager (Sara) should show NULL in the Manager column.

  **Exercise 10 (GROUP BY + JOIN — Stretch):**
  Write a query showing each customer's Name and total amount spent (SUM). Include customers who have never ordered — their total should show NULL.

  **Bonus (fast finishers):** Replace NULL totals with 0 using COALESCE. Note: COALESCE will be covered fully in Session 5.
- **Visual spec:** Dark hero slide. Headline centered. Two exercise cards + one bonus card. Main cards: frosted panel white 18% opacity, GREEN_MID header bar. Bonus card: GREEN_LIGHT left-accent bar, slightly smaller text, labeled "Bonus — fast finishers".
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. Dark green background with soft glow.
  2. Headline centered y=80.
  3. Exercise 9 card: x=100–1180 y=160–340, rounded rect fill white 18% opacity, header bar GREEN_MID. Title Poppins 14pt Bold WHITE. Body Poppins 13pt White 85% opacity.
  4. Exercise 10 card: x=100–1180 y=360–520, same style.
  5. Bonus card: x=100–1180 y=535–630, rounded rect fill white 12% opacity, left-accent bar 4px GREEN_LIGHT. Title "Bonus" Poppins 12pt Bold GREEN_LIGHT. Body Poppins 12pt White 70% opacity.
  6. Slide number: "31b" white 40%.
- **QC note:** Split from 4-exercise grid. COALESCE removed from main exercises (intermediate concept) and demoted to labeled Bonus. Audience alignment fix for beginner level.

---

## Slide 32: Session Summary — All JOIN Types
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Session" + "Summary"
- **Content:**
  | JOIN Type      | Returns                                          | NULL appears when...              |
  |----------------|--------------------------------------------------|-----------------------------------|
  | INNER JOIN     | Rows matched in BOTH tables                      | Never — unmatched rows excluded   |
  | LEFT JOIN      | All left rows + matched right rows               | Right side has no match           |
  | RIGHT JOIN     | All right rows + matched left rows               | Left side has no match            |
  | FULL OUTER JOIN| All rows from both tables                        | Either side has no match          |
  | CROSS JOIN     | Every combination (no ON clause)                 | Never — all combinations included |
  | Self-Join      | A table joined to itself (any type)              | Depends on JOIN type used         |
- **Visual spec:** Left panel: two-tone headline + GREEN_MID divider + "You now know all six JOIN types" subtext. Right panel: 6-row comparison table, column headers GREEN_MID. Row tints: alternate white (#FFFFFF) and very-light-green (#E8F8EE) only — no blue, yellow, purple, or orange. Palette-compliant only.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. White background.
  2. Left panel (x=60–420): headline + divider + "You now know all six JOIN types. Use this table as your reference sheet." Poppins 13pt GREY_BODY.
  3. Right panel (x=440–1220): PPT table 7 rows (1 header + 6 join types). Header: GREEN_MID fill, White text. Alternating row fills: odd rows white (#FFFFFF), even rows very-light-green (#E8F8EE). Cell text Poppins 11pt NEAR_BLACK. Column width: 180px | 380px | 280px.
- **QC note:** Six off-palette row tints (blue, yellow, purple, orange) replaced with alternating white / light-green within approved palette.
  4. Slide number: "32" GREY_BODY 40%.

---

## Slide 33: JOIN Quick Reference
- **Layout pattern:** C
- **Background mode:** dark-green
- **Headline:** "JOIN" + "Quick Reference"
- **Content:**
  **Column 1 — JOIN Selection Guide:**
  - Need only matched rows? → INNER JOIN
  - Keep all from left? → LEFT JOIN
  - Keep all from right? → RIGHT JOIN (or swap to LEFT)
  - Keep everything? → FULL OUTER JOIN
  - All combinations? → CROSS JOIN
  - Query same table? → Self-Join (LEFT JOIN with alias)

  **Column 2 — Syntax Skeleton:**
  ```
  SELECT t1.col, t2.col
  FROM   table1 AS t1
  [JOIN] table2 AS t2
    ON t1.key = t2.key;
  ```

  **Column 3 — Danger Checklist:**
  - Prefix all columns with alias
  - Check join key in ERD first
  - Move right-table filters to ON
  - Expect duplicates in 1-to-many
  - Test row count before/after
- **Visual spec:** Three-column horizontal strip on dark green. Each column has a GREEN_MID icon badge at top, bold white column header, and content as tight bullet list in white body text. Column separators: thin WHITE vertical lines at 20% opacity. Top-right decorative gem shapes.
- **Image query:** none
- **Image style:** none
- **PPT build notes:**
  1. Dark green background.
  2. Headline centered white + GREEN_LIGHT, y=60. Thin GREEN_LIGHT underline at y=110.
  3. Three columns each ~360px wide: Column 1 x=80–400, Column 2 x=460–800, Column 3 x=860–1200.
  4. Each column: icon badge r=22 GREEN_MID at top, header Poppins 16pt Bold White, body bullets Poppins 11pt White 85% opacity. Column 2 code block: Courier New 11pt White on dark panel.
  5. Vertical divider lines: x=440 and x=840, y=140–680, stroke WHITE 20% opacity, 1px.
  6. Slide number: "33" white 40%.

---

## Slide 34: Next Steps
- **Layout pattern:** B
- **Background mode:** white
- **Headline:** "Next" + "Steps"
- **Content:**
  **Practice:**
  - Complete the take-home assignment (link/handout provided)
  - Run all 10 exercises in your own SQL editor against the class dataset
  - For each exercise, compare INNER vs LEFT JOIN and observe the difference in row counts

  **Coming up in Session 4:**
  - Subqueries — another way to filter and shape data
  - When to use a subquery vs a JOIN
  - EXISTS and IN operators

  **Resources:**
  - W3Schools SQL JOIN reference (w3schools.com/sql/sql_join.asp)
  - SQLZoo interactive JOIN exercises (sqlzoo.net)
  - Your class dataset is in the shared folder: [Instructor: update shared folder path before class]
- **Visual spec:** Left panel: two-tone headline + divider + "What to do before Session 4" subtext. Right panel: 3 icon-badge sections stacked — Practice (book icon badge), Coming Up (calendar icon badge), Resources (link icon badge). Each section has a GREEN_MID badge + bold label + 2-3 sub-bullets.
- **Image query:** student studying SQL computer desk learning
- **Image style:** photo
- **PPT build notes:**
  1. White background.
  2. Left panel (x=60–440): headline + divider + "What to do before Session 4" Poppins 14pt NEAR_BLACK.
  3. Right panel (x=460–1220): 3 section rows, each: GREEN_MID badge r=22 + section label Poppins 16pt Bold NEAR_BLACK + sub-bullets Poppins 12pt GREY_BODY with hanging indent. Row spacing 160px, start y=160.
  4. Slide number: "34" GREY_BODY 40%.

---

## Image Manifest
```json
[
  {"slide_id": "slide01", "query": "database tables connecting diagram", "style_hint": "diagram"},
  {"slide_id": "slide04", "query": "database normalization two tables relationship", "style_hint": "diagram"},
  {"slide_id": "slide07", "query": "Venn diagram inner join SQL overlap", "style_hint": "diagram"},
  {"slide_id": "slide10", "query": "Venn diagram left join SQL all left rows", "style_hint": "diagram"},
  {"slide_id": "slide15", "query": "Venn diagram full outer join both circles filled SQL", "style_hint": "diagram"},
  {"slide_id": "slide19", "query": "Cartesian product grid matrix all combinations", "style_hint": "diagram"},
  {"slide_id": "slide21", "query": "employee manager hierarchy org chart database", "style_hint": "diagram"},
  {"slide_id": "slide25", "query": "multiple SQL tables join chain three tables", "style_hint": "diagram"},
  {"slide_id": "slide28", "query": "entity relationship diagram ERD primary foreign key SQL", "style_hint": "diagram"},
  {"slide_id": "slide34", "query": "student studying SQL computer desk learning", "style_hint": "photo"}
]
```

output_path: slide_deck_template/decks/sql/sql-joins-for-beginners.md
