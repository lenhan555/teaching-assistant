# Agent: Excel Reconciler

## Role

For each sheet in a scanned Excel workbook, locate the matching lesson assignment and judge whether each asked task was attempted and correct. Single responsibility: produce a per-lesson reconciliation table. Does not assign scores (that is the Grading Agent's job).

---

## Inputs

| Parameter | Required | Description |
|-----------|----------|-------------|
| `scan_file` | yes | Path to `[student-id]-scan.md` produced by Excel Scanner |
| `student_id` | yes | Unique student identifier |
| `subject` | yes | Subject area: `excel`, `sql`, or `powerbi` |
| `level` | yes | Skill level: `beginner`, `intermediate`, or `advanced` |
| `assignments_dir` | no | Directory containing assignment `.md` files. Default: `assignments/` |

---

## Outputs

**File:** `agents/excel-reconciler/output/[student-id]-reconciliation.md`

**Structure:**
```
# Reconciliation: [student-id]
Scan source: [scan_file]
Subject: [subject] | Level: [level]
Reconciled: [YYYY-MM-DD HH:MM]

---

## Lesson: <sheet_name> → Assignment: <assignment_filename>

| # | Task (from assignment) | Status | Notes |
|---|------------------------|--------|-------|
| 1 | [task description] | ✅ Complete | [one-line evidence note] |
| 2 | [task description] | ⚠️ Partial | [what was attempted and what is missing] |
| 3 | [task description] | ❌ Missing | [no evidence found] |

---

## Lesson: <sheet_name> → Assignment: NOT FOUND

No matching assignment file found in assignments/. Sheet content logged but not graded.

---

## Summary
Sheets processed: N
Sheets matched to assignments: N
Sheets unmatched: N
```

---

## Tools

- **Read** — read the scan file and each matched assignment file
- **Write** — write the reconciliation file

---

## Execution Steps

### Step 1 — Read the scan file

Read `scan_file`. Extract the list of sheet names from lines beginning with `## Sheet:`.

### Step 2 — For each sheet, find the matching assignment

For each sheet name:

1. Normalise the sheet name: lowercase, strip special characters, split into keywords (e.g. "Lesson 3 - VLOOKUP" → `["vlookup"]`; "PivotTable Basics" → `["pivottable", "basics"]`).
2. List all `.md` files in `assignments_dir`.
3. Score each file by how many keywords appear in its filename (case-insensitive). Also require the subject and level to appear in the filename (e.g. `excel-beginner-*`).
4. Select the highest-scoring file. If no file scores ≥ 1 keyword match, record "NOT FOUND" for this sheet.

### Step 3 — For each matched assignment, extract tasks

Read the matched assignment `.md` file. Extract numbered questions or tasks. Look for:
- Numbered lists (`1.`, `2.`, etc.)
- Task headings (`### Task 1`, `**Q1**`, etc.)

Collect each task's full description text.

### Step 4 — Reconcile sheet content against tasks

For each task in the assignment:

Read the corresponding sheet section from the scan file (the block under `## Sheet: <sheet_name>`).

Apply the following judgment:
- **✅ Complete** — the scan contains cells or formulas that clearly address the task. The student produced the expected output or used the expected function/approach. One-line note: cite the specific cell address and formula or value.
- **⚠️ Partial** — an attempt is visible (relevant formula types or table structures present) but something is incomplete, wrong type, or covering only part of the task. One-line note: describe what is present and what is missing.
- **❌ Missing** — no cells, formulas, charts, or pivot tables in the sheet relate to this task. One-line note: state what was expected but not found.

Do not penalise for formatting or naming choices not specified in the assignment. Judge only the substance of each task.

### Step 5 — Write reconciliation file

Write the full reconciliation report to `agents/excel-reconciler/output/{student_id}-reconciliation.md`.

Create the `agents/excel-reconciler/output/` directory if it does not exist.

### Step 6 — Log and hand off

Append to `log/excel-reconciler.log`:
```
[YYYY-MM-DD HH:MM] excel-reconciler
  Input:   scan=[scan_file] student=[student_id] subject=[subject] level=[level]
  Output:  agents/excel-reconciler/output/[student-id]-reconciliation.md
  Status:  success | partial | failed
  Notes:   [N sheets matched, N unmatched, any ambiguous task judgments]
```

Output the path on the final line:
```
output_path: agents/excel-reconciler/output/[student-id]-reconciliation.md
```

---

## Error Handling

| Condition | Action |
|-----------|--------|
| Scan file not found | Log status: failed. Abort. |
| No assignments in `assignments_dir` | Log status: failed. Note empty dir. Abort. |
| Sheet has no matching assignment | Record "NOT FOUND" in report. Continue to next sheet. Status: partial. |
| Assignment has no parseable tasks | Note "could not extract tasks" for that lesson. Mark all tasks as ❌ Missing. |
| Scan shows empty sheet | Mark all tasks for that lesson as ❌ Missing. Note "(empty sheet)" in Notes column. |
