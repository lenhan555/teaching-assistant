---
description: Grade an entire cohort's Excel workbook submissions. Arguments: $ARGUMENTS
---

Grade an entire cohort's Excel workbook submissions. Arguments: $ARGUMENTS

Expected format: `<subject> <level> <cohort_id> <submissions_dir> [--assignments <assignments_dir>]`

Example: `excel beginner may-2026 submissions/may-2026/`

Each student submits one `.xlsx` file with one sheet per completed lesson. Student ID is derived from the filename: strip `.xlsx`, lowercase, spaces → hyphens. Example: `Ana Santos.xlsx` → `ana-santos`.

---

## What to do

Parse the arguments to extract:
- `subject` — `excel`, `sql`, or `powerbi`
- `level` — `beginner`, `intermediate`, or `advanced`
- `cohort_id` — short identifier, e.g. `may-2026`
- `submissions_dir` — folder containing student `.xlsx` files
- `assignments_dir` — default: `assignments/`

---

## Pre-Run Checks

1. `submissions_dir` exists and contains at least one `.xlsx` file. If not, abort with error.
2. `assignments_dir` exists and is not empty. If not, abort with error.
3. Warn (but continue) if no rubric matches `rubrics/[subject]-[level]-*-rubric.md`.
4. Create if missing: `grades/`, `agents/excel-scanner/output/`, `agents/excel-reconciler/output/`

---

## Agent Sequence

**For each `.xlsx` in `submissions_dir`:**

**Step 1 — Excel Scanner agent**
Invoke the `excel-scanner` sub-agent with:
- `excel_file` = path to `.xlsx`
- `student_id` = derived from filename
- Output: `agents/excel-scanner/output/[student-id]-scan.md`

On failure (corrupt file, missing openpyxl): write `grades/[subject]-[level]-[cohort_id]-[student-id]-ERROR.md`, skip to next student.

**Step 2 — Excel Reconciler agent**
Invoke the `excel-reconciler` sub-agent with:
- `scan_file` = Step 1 output
- `assignments_dir`, `student_id`, `subject`, `level`
- Output: `agents/excel-reconciler/output/[student-id]-reconciliation.md`

If no assignment matches a sheet: note in reconciliation, continue with matched sheets.

**Step 3 — Grading Agent**
Invoke the `grading-agent` sub-agent with:
- `reconciliation_file` = Step 2 output
- `rubric_file` = best match in `rubrics/` for subject + level
- `student_id`
- Output: `grades/[subject]-[level]-[cohort_id]-[student-id]-feedback.md`

On failure: write `grades/[subject]-[level]-[cohort_id]-[student-id]-ERROR.md`, skip to next student.

**After all students:**

**Step 4 — Cohort Feedback Agent**
Invoke the `cohort-feedback` sub-agent with:
- `grades_dir` = `grades/`
- Filter files matching `[subject]-[level]-[cohort_id]-*`
- `topic` = `[subject]-[level]`
- `cohort_id`
- Output: `log/cohort-[cohort_id]-[subject]-[level]-feedback.md`

---

## Logging

Append to `log/excel-grading-phase.log`:
```
[YYYY-MM-DD HH:MM] excel-grading-phase
  Input:   subject=[subject] level=[level] cohort=[cohort_id] submissions=[submissions_dir]
  Output:  [N] feedback files in grades/, cohort report at log/cohort-[cohort_id]-[subject]-[level]-feedback.md
  Status:  success | partial | failed
  Notes:   [N students processed, N errors, N unmatched sheets]
```

---

## Outputs Summary

Confirm to the instructor:
- `agents/excel-scanner/output/[student-id]-scan.md` — one per student
- `agents/excel-reconciler/output/[student-id]-reconciliation.md` — one per student
- `grades/[subject]-[level]-[cohort_id]-[student-id]-feedback.md` — one per student
- `log/cohort-[cohort_id]-[subject]-[level]-feedback.md` — cohort weak-concept report
