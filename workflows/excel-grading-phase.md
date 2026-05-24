# Workflow: Excel Grading Phase

## Trigger

```
/grade-excel-cohort <subject> <level> <cohort_id> <submissions_dir> [--assignments <assignments_dir>]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `subject` | yes | `excel`, `sql`, or `powerbi` |
| `level` | yes | `beginner`, `intermediate`, or `advanced` |
| `cohort_id` | yes | Short identifier for this cohort (e.g. `may-2026`) |
| `submissions_dir` | yes | Directory containing student `.xlsx` files |
| `--assignments` | no | Override assignments directory. Default: `assignments/` |

**Student ID derivation:** Strip the `.xlsx` extension from each filename, lowercase, replace spaces with hyphens. Example: `Leo Pham Lesson 1.xlsx` → `leo-pham-lesson-1`.

---

## Pre-Run Checks

Before processing any files, verify:

1. `submissions_dir` exists and contains at least one `.xlsx` file. If empty or missing → abort with error.
2. `assignments_dir` (default `assignments/`) exists and is not empty. If missing or empty → abort with error.
3. A rubric file matching `rubrics/[subject]-[level]-*-rubric.md` exists. If none found → warn instructor but continue (grading agent will note missing rubric).
4. Create directories if they do not exist:
   - `grades/`
   - `agents/excel-scanner/output/`
   - `agents/excel-reconciler/output/`

---

## Agent Sequence

```
For each .xlsx in submissions_dir:

  ┌─────────────────────────────────────────────────────────┐
  │ Step 1: Excel Scanner Agent                             │
  │   Input:  excel_file, student_id                        │
  │   Output: agents/excel-scanner/output/[sid]-scan.md     │
  └───────────────────────┬─────────────────────────────────┘
                          │ scan_file
  ┌───────────────────────▼─────────────────────────────────┐
  │ Step 2: Excel Reconciler Agent                          │
  │   Input:  scan_file, assignments_dir,                   │
  │           student_id, subject, level                    │
  │   Output: agents/excel-reconciler/output/[sid]-rec.md   │
  └───────────────────────┬─────────────────────────────────┘
                          │ reconciliation_file
  ┌───────────────────────▼─────────────────────────────────┐
  │ Step 3: Grading Agent                                   │
  │   Input:  reconciliation_file,                          │
  │           rubric_file (best match in rubrics/),         │
  │           student_id                                    │
  │   Output: grades/[subject]-[level]-[cid]-[sid]-         │
  │           feedback.md                                   │
  └─────────────────────────────────────────────────────────┘

After all students:

  ┌─────────────────────────────────────────────────────────┐
  │ Step 4: Cohort Feedback Agent                           │
  │   Input:  grades_dir=grades/,                           │
  │           filter=[subject]-[level]-[cohort_id]-*,       │
  │           topic=[subject]-[level],                      │
  │           cohort_id                                     │
  │   Output: log/cohort-[cid]-[subject]-[level]-           │
  │           feedback.md                                   │
  └─────────────────────────────────────────────────────────┘
```

Students are processed sequentially. Steps 1–3 are sequential per student (each step's output feeds the next). The Cohort Feedback Agent runs once after all students are done.

---

## Outputs

| File | Description |
|------|-------------|
| `agents/excel-scanner/output/[student-id]-scan.md` | Per-student sheet extraction report |
| `agents/excel-reconciler/output/[student-id]-reconciliation.md` | Per-student task reconciliation table |
| `grades/[subject]-[level]-[cohort-id]-[student-id]-feedback.md` | Per-student graded feedback |
| `log/cohort-[cohort-id]-[subject]-[level]-feedback.md` | Cohort weak-concept report |
| `log/excel-grading-phase.log` | Workflow run log (one entry per run) |

---

## Error Handling

| Failure | Action |
|---------|--------|
| Excel Scanner fails (corrupt file, missing openpyxl) | Log error. Write `grades/[subject]-[level]-[cid]-[sid]-ERROR.md` with reason. Skip to next student. |
| Reconciler finds no matching assignment for a sheet | Note in reconciliation report. Grade only matched sheets. Status: partial. |
| Rubric file not found for a student | Grading Agent proceeds without rubric; notes "no rubric — judgment-only grading" in feedback. |
| Grading Agent fails for a student | Log error. Write `grades/[subject]-[level]-[cid]-[sid]-ERROR.md`. Skip. Continue cohort. |
| Cohort Feedback Agent runs on < 3 students | Run normally; note small sample size in cohort report. Do not skip. |

The workflow never aborts mid-cohort due to a single student failure. All students are attempted; errors are logged and skipped.

---

## Logging

Append to `log/excel-grading-phase.log` on workflow completion:
```
[YYYY-MM-DD HH:MM] excel-grading-phase
  Input:   subject=[subject] level=[level] cohort=[cohort_id] submissions=[submissions_dir]
  Output:  [N] feedback files in grades/, cohort report at log/cohort-[cohort-id]-[subject]-[level]-feedback.md
  Status:  success | partial | failed
  Notes:   [N students processed, N errors, N unmatched sheets]
```

Each individual agent also appends its own entry to its own log file (`log/excel-scanner.log`, `log/excel-reconciler.log`, `log/grading-agent.log`, `log/cohort-feedback.log`).

---

## Example Run

```
/grade-excel-cohort excel beginner may-2026 submissions/may-2026/
```

With `submissions/may-2026/` containing:
- `ana-santos.xlsx`
- `david-kim.xlsx`
- `priya-mehta.xlsx`

Produces:
- `agents/excel-scanner/output/ana-santos-scan.md`
- `agents/excel-scanner/output/david-kim-scan.md`
- `agents/excel-scanner/output/priya-mehta-scan.md`
- `agents/excel-reconciler/output/ana-santos-reconciliation.md`
- `agents/excel-reconciler/output/david-kim-reconciliation.md`
- `agents/excel-reconciler/output/priya-mehta-reconciliation.md`
- `grades/excel-beginner-may-2026-ana-santos-feedback.md`
- `grades/excel-beginner-may-2026-david-kim-feedback.md`
- `grades/excel-beginner-may-2026-priya-mehta-feedback.md`
- `log/cohort-may-2026-excel-beginner-feedback.md`
