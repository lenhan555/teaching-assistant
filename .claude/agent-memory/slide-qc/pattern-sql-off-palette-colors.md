---
name: pattern-sql-off-palette-colors
description: SQL decks repeatedly introduce off-palette colors — blue/purple/amber tints for zone tables, and red (#CC3333) in "Watch Out" slide headlines — both violating the two-tone rule
metadata:
  type: project
---

Two distinct off-palette color patterns confirmed in sql-joins-for-beginners:

**Pattern A — Summary/zone table row tints (Slides 14, 16, 32):**
- slide14: light-blue and light-yellow row tints for INNER/RIGHT JOIN rows
- slide16: blue zone bar for FULL OUTER JOIN left-only rows
- slide32: six off-palette tints (blue, yellow, purple, orange, grey) for six JOIN type rows
Root cause: generator reaches for rainbow differentiation when the palette tint options are exhausted.

**Pattern B — "Watch Out" slide red headlines (Slides 13, 27):**
- Headline accent word set to RED (#CC3333) on both "Watch Out —" callout slides
- Warning badge also specified as red circle (#CC3333)
Root cause: generator associates "danger/warning" semantic with red, overriding the two-tone headline rule.

**Fixes applied (2026-05-31):**
- All table row tints corrected to: white (#FFFFFF) / very-light-green (#E8F8EE) / light-grey (#F4F4F4)
- Headline accent corrected to GREEN_LIGHT (#5CDB8F) on both "Watch Out" slides
- Warning badges changed to GREEN_LIGHT; WRONG-panel headers changed to NEAR_BLACK (#1A1A2E)

**How to apply:** In any SQL deck, proactively check:
1. All "Watch Out" / callout slides — headline must use GREEN_MID or GREEN_LIGHT, never red
2. Any summary or comparison table — row tints limited to white, #E8F8EE, #F4F4F4 from approved palette
3. Zone-coded result tables — use left-border bars in GREEN_MID / GREY_BODY / GREEN_LIGHT instead of fill colors

See also: [[pattern-sql-headline-size-drift]]
