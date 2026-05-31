# Workflow: Full Course Prep

## Purpose

End-to-end course material generation for a single topic and level. Runs: Researcher → Synthesizer → [Slide Generator + Assignment Generator in parallel] → Rubric Builder.

---

## Trigger

Instructor runs:
```
/course-prep <subject> <topic> <level> [--audience <audience>] [--style <style>]
```

**Example:**
```
/course-prep sql joins beginner --audience students --style training
```

---

## Parameters

| Parameter | Required | Values |
|-----------|----------|--------|
| `subject` | yes | `sql` / `excel` / `powerbi` |
| `topic` | yes | e.g. `joins`, `pivot tables`, `DAX CALCULATE` |
| `level` | yes | `beginner` / `intermediate` / `advanced` |
| `--audience` | no | `students` / `executives` / `clients` (default: `students`) |
| `--style` | no | `training` / `pitch` / `report` (default: `training`) |

---

## Agent Sequence

```
Step 1: Researcher
  → inputs:  subject, topic, level, --save
  → outputs: agents/researcher/output/[subject]-[level]-[topic-slug]-research.md
  → pass to Step 2: output_path from handoff block

Step 2: Synthesizer
  → inputs:  research_file=[Step 1 output_path], subject, topic, level
  → outputs: skills/[subject]-[level]-[topic-slug].md
  → pass to Steps 3a & 3b: output_path from handoff block

Step 3a (parallel): Slide Generator
  → inputs:  topic, audience, style, knowledge_doc=[Step 2 output_path], --save
             (slide count is topic-driven — agent generates as many as needed, no ceiling)
  → outputs: slide_deck_template/decks/[topic-slug].md

Step 3b (parallel): Assignment Generator — take-home
  → inputs:  subject, topic, level, --type=take-home, knowledge_doc=[Step 2 output_path], --save
  → outputs: assignments/[subject]-[level]-[topic-slug]-take-home.md

Step 3c (parallel): Assignment Generator — in-class
  → inputs:  subject, topic, level, --type=in-class, knowledge_doc=[Step 2 output_path], --save
  → outputs: assignments/[subject]-[level]-[topic-slug]-in-class.md

Step 4a (after Step 3a): Slide QC
  → inputs:  deck_path=[Step 3a output_path],
             design_references=[slide_deck_template/examples/deck-analysis.md,
                                slide_deck_template/examples/svg-design-system.md]
  → outputs: QC report inline; log/slide-qc.log entry appended
  → (blocks deck approval until Critical issues are resolved; does not block Step 4b)

Step 4b (after Step 3b): Rubric Builder
  → inputs:  assignment_file=[Step 3b output_path], subject, topic, level
  → outputs: rubrics/[subject]-[level]-[topic-slug]-rubric.md
  → (rubric is built from take-home assignment only; in-class practicals are instructor-led and ungraded)
```

---

## Data Flow

```
/course-prep sql joins beginner
        │
        ▼
  [Researcher] ──────────────────────────────────────────────────────┐
  agents/researcher/output/sql-beginner-joins-research.md            │
        │                                                             │
        ▼                                                             │
  [Synthesizer]                                                       │
  skills/sql-beginner-joins.md                                        │
        │                                                             │
        ├──────────────────────┬──────────────────────┐              │
        ▼                      ▼                      ▼              │
  [Slide Generator]   [Assignment Gen        [Assignment Gen         │
  decks/sql-          take-home]             in-class]               │
  training-for-       assignments/           assignments/            │
  beginners.md        sql-beginner-          sql-beginner-           │
        │             joins-take-home.md     joins-in-class.md       │
        ▼                   │                                         │
  [Slide QC]                ▼                                         │
  log/slide-qc.log    [Rubric Builder]                                │
                      rubrics/sql-beginner-joins-rubric.md           │
                                                                      │
  All agents log to log/ ◄────────────────────────────────────────────┘
```

---

## Error Handling

| Step | Failure | Action |
|------|---------|--------|
| Researcher | Web fetch fails for all sources | Abort workflow; notify instructor: "Research failed — check internet connection or try a different topic query" |
| Researcher | Partial fetch (some sources failed) | Continue with available data; log `Status: partial` and list failed URLs in Notes |
| Synthesizer | Output file write fails | Abort; notify instructor with file path and error |
| Slide Generator | Fails | Log failure; skip Slide QC; continue to Assignment Generator steps — deck can be regenerated separately |
| Slide QC | Finds Critical issues | Log issues to `log/slide-qc.log`; report inline; do not block other steps — instructor decides whether to regenerate before use |
| Slide QC | Agent fails to run | Log `Status: failed`; notify instructor; deck is usable but unreviewed |
| Assignment Generator | Fails | Log failure; continue to Rubric Builder if take-home assignment was written; skip rubric if not |
| Rubric Builder | No take-home assignment found | Skip and notify: "Rubric not generated — take-home assignment missing" |

---

## Outputs Summary

After a successful run, the instructor has:
- `skills/[subject]-[level]-[topic-slug].md` — structured knowledge doc
- `slide_deck_template/decks/[topic-slug].md` — slide deck blueprint
- `assignments/[subject]-[level]-[topic-slug]-take-home.md` — graded homework
- `assignments/[subject]-[level]-[topic-slug]-in-class.md` — live practicals
- `rubrics/[subject]-[level]-[topic-slug]-rubric.md` — grading rubric
- `log/slide-qc.log` — QC review of the deck (scores, issue log, top 3 priorities)
- Entries in `log/` for each agent that ran
