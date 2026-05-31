---
description: Run the full course preparation pipeline for a single topic. Arguments: $ARGUMENTS
---

Run the full course preparation pipeline for a single topic. Arguments: $ARGUMENTS

Expected format: `<subject> <topic> <level> [--audience <audience>] [--style <style>]`

Examples:
- `sql joins beginner`
- `excel vlookup beginner --audience students --style training`
- `powerbi CALCULATE intermediate`

---

## What to do

Parse the arguments above to extract:
- `subject` — `sql`, `excel`, or `powerbi`
- `topic` — e.g. `joins`, `pivot tables`, `DAX CALCULATE`
- `level` — `beginner`, `intermediate`, or `advanced`
- `--audience` — default: `students`
- `--style` — default: `training`

Then execute the following agent sequence:

---

## Agent Sequence

### Step 1 — Researcher agent
Invoke the `researcher` sub-agent with:
- Input: `subject`, `topic`, `level`, `--save`
- Output: `agents/researcher/output/[subject]-[level]-[topic-slug]-research.md`

### Step 2 — Synthesizer agent
Invoke the `synthesizer` sub-agent with:
- Input: `research_file` = Step 1 output, `subject`, `topic`, `level`
- Output: `skills/[subject]-[level]-[topic-slug].md`

### Steps 3a, 3b, 3c — Run in parallel

**3a — Slide Generator agent**
- Input: `topic`, `audience`, `style`, `slides=10`, `knowledge_doc` = Step 2 output, `--save`
- Output: `slide_deck_template/decks/[topic-slug].md`

**3b — Assignment Generator agent (take-home)**
- Input: `subject`, `topic`, `level`, `--type=take-home`, `knowledge_doc` = Step 2 output, `--save`
- Output: `assignments/[subject]-[level]-[topic-slug]-take-home.md`

**3c — Assignment Generator agent (in-class)**
- Input: `subject`, `topic`, `level`, `--type=in-class`, `knowledge_doc` = Step 2 output, `--save`
- Output: `assignments/[subject]-[level]-[topic-slug]-in-class.md`

### Step 4 — Rubric Builder agent
- Input: `assignment_file` = Step 3b output, `subject`, `topic`, `level`
- Output: `rubrics/[subject]-[level]-[topic-slug]-rubric.md`

---

## Error Handling

| Step | Failure | Action |
|------|---------|--------|
| Researcher | All web fetches fail | Abort; notify instructor |
| Researcher | Partial fetch | Continue with available data; log partial |
| Synthesizer | Write fails | Abort; notify instructor |
| Slide Generator | Fails | Log failure; continue to Steps 3b/3c |
| Assignment Generator | Fails | Log failure; continue to Step 4 if take-home was written |
| Rubric Builder | No take-home found | Skip; notify instructor |

---

## Outputs Summary
After a successful run, confirm to the instructor:
- `skills/[subject]-[level]-[topic-slug].md` — knowledge doc
- `slide_deck_template/decks/[topic-slug].md` — slide deck blueprint
- `assignments/[subject]-[level]-[topic-slug]-take-home.md` — graded homework
- `assignments/[subject]-[level]-[topic-slug]-in-class.md` — live practicals
- `rubrics/[subject]-[level]-[topic-slug]-rubric.md` — grading rubric
