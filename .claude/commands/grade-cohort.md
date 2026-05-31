---
description: Grade an entire cohort's text or SQL submissions for one assignment. Arguments: $ARGUMENTS
---

Grade an entire cohort's text or SQL submissions for one assignment. Arguments: $ARGUMENTS

Expected format: `<topic> <level> <submissions-dir>`

Example: `joins beginner submissions/may-cohort-joins/`

Student files must be named `[student-id].md` or `[student-id].sql` (e.g. `ana-santos.md`).

---

## What to do

Parse the arguments to extract:
- `topic` — must match an existing rubric in `rubrics/`
- `level` — `beginner`, `intermediate`, or `advanced`
- `submissions_dir` — path to the folder containing all student files
- `cohort_id` — default: the directory name of `submissions_dir`

---

## Pre-Run Checks

1. Find rubric at `rubrics/[subject]-[level]-[topic-slug]-rubric.md`. If missing, abort and tell the instructor to run `/rubric-builder` first.
2. Check `submissions_dir` is not empty. If empty, abort.
3. Create `grades/` directory if it does not exist.

---

## Agent Sequence

**For each student file in `submissions_dir`:**

**Step 1 — Grading Agent**
Invoke the `grading-agent` sub-agent with:
- `submission_file` = path to student file
- `rubric_file` = matching rubric
- `student_id` = filename stem (no extension)
- Output: `grades/[topic-slug]-[student-id]-feedback.md`

On failure for a single student: log the error, skip to the next student. Do not abort the entire cohort.

**After all students:**

**Step 2 — Cohort Feedback Agent**
Invoke the `cohort-feedback` sub-agent with:
- `grades_dir` = `grades/`
- `topic` = topic slug
- `cohort_id`
- Output: `log/cohort-[cohort-id]-[topic-slug]-feedback.md`

---

## Outputs Summary

Confirm to the instructor:
- `grades/[topic-slug]-[student-id]-feedback.md` — one file per student
- `log/cohort-[cohort-id]-[topic-slug]-feedback.md` — cohort weak-concept report
