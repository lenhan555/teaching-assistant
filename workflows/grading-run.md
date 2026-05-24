# Workflow: Grading Run

## Purpose

Grade an entire cohort's submissions for one assignment and produce a cohort-level insight report. Runs: Grading Agent (once per student, sequential) → Cohort Feedback Agent.

---

## Trigger

Instructor runs:
```
/grade-cohort <topic> <level> <submissions-dir>
```

**Example:**
```
/grade-cohort joins beginner submissions/may-cohort-joins/
```

The `submissions-dir` must contain one file per student, named `[student-id].[ext]` (e.g. `student-001.md`, `nguyen-thi-lan.sql`).

---

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `topic` | yes | Must match an existing rubric in `rubrics/` |
| `level` | yes | `beginner` / `intermediate` / `advanced` |
| `submissions_dir` | yes | Path to the folder containing all student submissions |
| `subject` | no | `sql` / `excel` / `powerbi` — inferred from rubric file if omitted |
| `cohort_id` | no | Identifier for this cohort (default: directory name of `submissions_dir`) |

---

## Pre-Run Check

Before starting, verify:
1. A rubric file exists at `rubrics/[subject]-[level]-[topic-slug]-rubric.md` — abort if missing and notify instructor
2. The `submissions_dir` is not empty — abort if no files found
3. The `grades/` directory exists — create it if not

---

## Agent Sequence

```
For each student file in submissions_dir:
  Step 1: Grading Agent
    → inputs:  submission_file=[student file], rubric_file=[matching rubric], student_id=[filename stem]
    → outputs: grades/[topic-slug]-[student-id]-feedback.md
    → continue to next student on failure (do not abort entire run)

After all students:
  Step 2: Cohort Feedback Agent
    → inputs:  grades_dir=grades/, topic=[topic], cohort_id=[cohort_id]
    → outputs: log/cohort-[cohort-id]-[topic-slug]-feedback.md
```

Students are graded **sequentially** (not in parallel) to keep log output readable and avoid file write conflicts.

---

## Data Flow

```
/grade-cohort joins beginner submissions/may-cohort/
        │
        ├── student-001.md ──► [Grading Agent] ──► grades/joins-student-001-feedback.md
        ├── student-002.md ──► [Grading Agent] ──► grades/joins-student-002-feedback.md
        ├── student-003.md ──► [Grading Agent] ──► grades/joins-student-003-feedback.md
        │   ... (one per student)
        │
        └── all grade files ──► [Cohort Feedback Agent]
                                 └──► log/cohort-may-cohort-joins-feedback.md
```

---

## Error Handling

| Step | Failure | Action |
|------|---------|--------|
| Pre-run: rubric missing | No rubric found | Abort workflow; notify instructor: "No rubric found for [subject]-[level]-[topic]. Run rubric-builder first." |
| Pre-run: empty submissions | No files in dir | Abort workflow; notify instructor |
| Grading Agent: file unreadable | Submission is empty or corrupt | Log `Status: failed` for that student; skip to next; note in cohort report |
| Grading Agent: ambiguous answer | Student answer is unclear | Grade conservatively (award partial marks where rubric allows); note in feedback file |
| Cohort Feedback: insufficient data | Fewer than 3 graded files | Run cohort feedback anyway; note low sample size in report |

---

## Outputs Summary

After a successful run, the instructor has:
- `grades/[topic-slug]-[student-id]-feedback.md` — one file per student
- `log/cohort-[cohort-id]-[topic-slug]-feedback.md` — cohort-wide insight report with weak concepts and re-teach recommendations
- Entries in `log/grading-agent.log` and `log/cohort-feedback.log`
