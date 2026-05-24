# Skill: rubric-builder

## Usage

```
/rubric-builder "<topic>" --level <level> [--subject <subject>] [--assignment <path>] [--save]
```

## Arguments

| Argument | Required | Values | Default |
|----------|----------|--------|---------|
| `topic` | yes | e.g. `"SQL Joins"`, `"Excel PivotTables"` | — |
| `--level` | yes | `beginner` / `intermediate` / `advanced` | — |
| `--subject` | no | `sql` / `excel` / `powerbi` | inferred from topic |
| `--assignment` | no | path to assignment file in `assignments/` | auto-detect from topic + level |
| `--save` | no | flag | off (print only) |

## Examples

```
/rubric-builder "SQL Joins" --level beginner --save
/rubric-builder "Excel PivotTables" --level intermediate --assignment assignments/excel-intermediate-pivot-tables-take-home.md --save
/rubric-builder "DAX CALCULATE" --level advanced --subject powerbi --save
```

---

## Execution Steps

### Step 1 — Parse arguments

Extract `topic`, `level`, `subject`, `assignment`, and `--save` flag. Infer `subject` from topic text if not provided. Normalize topic to a slug.

---

### Step 2 — Load the assignment

If `--assignment` is provided, read that file directly. If not, look for `assignments/[subject]-[level]-[topic-slug]-take-home.md`. If neither is found, build the rubric from the topic and level alone (use knowledge of typical question types at that level for that subject).

---

### Step 3 — Extract questions and learning objectives

From the assignment file (or topic knowledge), identify:
- Each question or task
- The concept it tests
- Whether it allows partial credit (Practical and Short Answer: yes; MCQ: no)

---

### Step 4 — Build rubric

Produce a rubric table where all weights sum to exactly 100 points.

```
# Grading Rubric: [Topic] ([Level])
Subject: [subject]
Assignment: [assignment file name or "built from topic"]
Total marks: 100
Generated: [YYYY-MM-DD]

## Rubric Table

| # | Criterion | Weight | Full Marks | Partial Marks | Zero Marks |
|---|-----------|--------|------------|---------------|------------|
| 1 | [specific, observable criterion] | [N] pts | [what earns full credit — specific] | [condition for partial — specific] | [condition for zero] |
| 2 | ... | | | | |
| **Total** | | **100** | | | |

## Grading Notes
[Cross-cutting guidance: edge cases, acceptable alternative answers, common traps to watch for]

## Score Bands
| Grade | Range | Descriptor |
|-------|-------|------------|
| Excellent | 90–100% | Full mastery; no significant errors |
| Proficient | 75–89% | Solid understanding; minor gaps only |
| Developing | 60–74% | Partial understanding; notable gaps |
| Beginning | Below 60% | Foundational gaps; needs instructor review |
```

**Rubric rules:**
- MCQ questions: binary only (full or zero) — no partial credit column needed, write "N/A"
- Short Answer / Practical: must include partial credit condition
- Criterion names must be specific (e.g. "Correct JOIN type selected" not "Good answer")
- Full marks description must state exactly what correct looks like
- Partial marks must name the specific partial condition (e.g. "Correct approach but missing WHERE clause")

---

### Step 5 — Write or print (if `--save`)

**If `--save` is set:**
Write to `rubrics/[subject]-[level]-[topic-slug]-rubric.md`.
If the file already exists, confirm with the instructor before overwriting.

**If `--save` is not set:**
Print the full rubric inline.
End with: `Tip: run with --save to write to rubrics/[subject]-[level]-[topic-slug]-rubric.md`

---

### Step 6 — Respond and log

Return the full rubric. If `--save` was used, confirm the file path.

Append to `log/rubric-builder.log`:
```
[YYYY-MM-DD HH:MM] rubric-builder
  Input:   topic=[topic] level=[level] subject=[subject] assignment=[path or "none"]
  Output:  rubrics/[subject]-[level]-[topic-slug]-rubric.md (or "printed only")
  Status:  success | partial | failed
  Notes:   [criterion count, total weight confirmed 100, assignment used or not]
```
