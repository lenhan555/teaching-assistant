---
name: pattern-sql-headline-size-drift
description: Dark-slide headline font sizes frequently drift below the 36pt spec in SQL decks — affects visual authority and hierarchy consistency
metadata:
  type: project
---

In the sql-joins-for-beginners deck (34 slides, reviewed 2026-05-31), 13 of 17 dark slides used headline font sizes below the 36pt specification defined in svg-design-system.md. Sizes observed: 22pt, 24pt, 26pt, 28pt, 30pt, 32pt, 34pt — none consistently reaching the mandated 36pt for both headline lines.

**Why:** The slide generator reduces font size when the headline text is long (e.g., "FULL OUTER JOIN —" / "Worked Example") to prevent overflow. This is a collision-avoidance workaround but violates the spec.

**How to apply:** During any SQL deck review, check dark slides with long JOIN-type names in the headline — these are the highest-risk candidates for font-size drift. Flag as Major if below 32pt, Critical if below 28pt. Recommend the generator split long headlines across two lines within the 36pt size instead of reducing font size.

See also: [[pattern-sql-off-palette-colors]]
