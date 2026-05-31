---
name: pattern-sql-density-end-slides
description: Beginner SQL decks exceed 30-word body limit on wrap-up slides (Exercises, Best Practices, Summary) — density spike at session end is a recurring structural pattern
metadata:
  type: project
---

In sql-joins-for-beginners (reviewed 2026-05-31), three consecutive end-of-session slides violated the density rule:

- Slide 29 (Duplicate Rows): two full code blocks + multi-sentence explanation (~80 words body)
- Slide 30 (Best Practices): 8 checklist items (~90 words body)
- Slide 31 (Comprehensive Practice): 4 exercises in a 2×2 grid (~150+ words total)

Root cause: instructors tend to front-load exercises and summaries near the end of a session, treating slides as a handout rather than a presentation screen.

**Fixes applied:**
- Slide 29: reduced to 1 code block + 1 key-insight sentence
- Slide 30: trimmed from 8 to 5 checklist items; items 6-8 moved to speaker notes
- Slide 31: split into Slide 31 (2 exercises) + Slide 31b (2 exercises + bonus)

**How to apply:** When reviewing the final 20% of a deck:
- Flag any slide with more than 3 bullet points as density risk
- Practice slides with more than 2 exercises per slide must be flagged for splitting
- Checklist slides with more than 5 items must be flagged — excess items go to speaker notes or a handout

See also: [[pattern-sql-off-palette-colors]]
