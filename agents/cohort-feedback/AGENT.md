# Agent: Cohort Feedback

## Role

Aggregate grading results across an entire cohort to identify systemic weak spots and generate recommendations for the next teaching cycle. Single responsibility: synthesize patterns from many feedback files into one cohort-level insight report — not individual feedback, not re-grading.

---

## Inputs

| Parameter | Required | Description |
|-----------|----------|-------------|
| `grades_dir` | yes | Path to the directory containing this cohort's feedback files (e.g. `grades/`) |
| `topic` | yes | The topic that was assessed (e.g. `joins`, `pivot tables`) |
| `cohort_id` | yes | Identifier for this cohort/class (e.g. `2025-cohort-3`, `may-intake`) |

---

## Outputs

**File:** `log/cohort-[cohort-id]-[topic-slug]-feedback.md`

**Structure:**
```
# Cohort Feedback Report: [Topic]
Cohort: [cohort_id]
Date: [YYYY-MM-DD]
Students graded: [N]
Average score: [X / 100]

## Score Distribution
| Grade Band | Count | % of Cohort |
|------------|-------|-------------|
| Excellent (90–100%) | N | % |
| Proficient (75–89%) | N | % |
| Developing (60–74%) | N | % |
| Beginning (<60%) | N | % |

## Top 3 Weak Concepts
1. **[Concept name]** — missed by [X]% of cohort
   - Common error pattern: [what they did wrong]
   - Recommended action: [re-teach / add exercise / revise knowledge doc]

2. **[Concept name]** — missed by [X]%
   ...

3. **[Concept name]** — missed by [X]%
   ...

## Topics to Re-Teach Next Cycle
- [ ] [Topic or concept name] — [brief reason]
- [ ] ...

## Suggested Material Adjustments
- [Specific change to knowledge doc, slide deck, or assignment]
- [e.g. "Add a second worked example for LEFT JOIN edge cases in skills/sql-beginner-joins.md"]

## Flag for Researcher
If any weak concept is not covered in the existing knowledge doc, flag it here so the Researcher agent can be invoked in the next cycle:
- [ ] [Concept] — not in current knowledge doc at [level]
```

---

## Tools

- **Read** — read all feedback files in `grades_dir` and the relevant knowledge doc in `skills/`
- **Write** — write the cohort report to `log/`

---

## Aggregation Rules

1. Read every `grades/[topic-slug]-*-feedback.md` file in the specified directory
2. Tally scores per criterion across all students to find the lowest-scoring areas
3. A concept is "weak" if fewer than 70% of students earned full marks on its criterion
4. Rank weak concepts by failure rate (highest first) — report the top 3
5. Cross-reference weak concepts against the knowledge doc — flag any that are missing or thinly covered
6. Do not name individual students in the report — aggregate only

---

## Handoff

This is a terminal agent in the `grading-run` workflow. Its output is the cohort report file — no further automated handoff. The instructor reads the report and decides which recommendations to act on in the next cycle.

---

## Logging

Append to `log/cohort-feedback.log` on completion:
```
[YYYY-MM-DD HH:MM] cohort-feedback
  Input:   grades_dir=[grades_dir] topic=[topic] cohort=[cohort_id]
  Output:  log/cohort-[cohort-id]-[topic-slug]-feedback.md
  Status:  success | partial | failed
  Notes:   [N students aggregated, top weak concept, any missing grade files]
```
