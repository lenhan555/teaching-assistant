# Skill: assignment-generator

## Usage

```
/assignment-generator "<topic>" --level <level> [--type <type>] [--questions N] [--subject <subject>] [--save]
```

## Arguments

| Argument | Required | Values | Default |
|----------|----------|--------|---------|
| `topic` | yes | e.g. `"SQL Joins"`, `"Excel PivotTables"` | — |
| `--level` | yes | `beginner` / `intermediate` / `advanced` | — |
| `--type` | no | `take-home` / `in-class` | `take-home` |
| `--questions` | no | integer | 5 (take-home) / 2 (in-class) |
| `--subject` | no | `sql` / `excel` / `powerbi` | inferred from topic |
| `--save` | no | flag | off (print only) |

## Examples

```
/assignment-generator "SQL Joins" --level beginner --type take-home --questions 5 --save
/assignment-generator "Excel PivotTables" --level intermediate --type in-class --save
/assignment-generator "DAX CALCULATE" --level advanced --type take-home --save
```

---

## Execution Steps

### Step 1 — Parse arguments

Extract `topic`, `level`, `type`, `questions`, `subject`, and `--save` flag. Infer `subject` from `topic` if not stated (e.g. topic contains "SQL" → sql, "Excel" → excel, "Power BI" or "DAX" → powerbi). Normalize `topic` to a slug for file naming.

---

### Step 2 — Load source material

Check if a knowledge doc exists at `skills/[subject]-[level]-[topic-slug].md`. If found, read it — use it as the content source. If not found, proceed from the topic name alone (no web research at this step; the assignment-generator is a content-shaping skill, not a research skill).

---

### Step 3 — Generate assignment

#### Take-Home format

Produce `num_questions` questions. Vary types: at least one MCQ, at least one Short Answer, at least one Practical (for N ≥ 3). Escalate difficulty Easy → Hard across the set.

```
# Take-Home Assignment: [Topic] ([Level])
Subject: [subject]
Due: _______________
Student name: _______________

## Instructions
Submit your answers as a document or file. Show your work for practical questions.
For SQL questions, include your query. For Excel, describe your steps or paste formulas.

## Questions

### Q1 — MCQ [Easy]
[Stem]
A) ...  B) ...  C) ...  D) ...
**Sample answer:** [letter] — [explanation]

### Q2 — Short Answer [Medium]
[Stem]
**Sample answer:** [full answer]

### Q3 — Practical [Hard]
[Realistic scenario + task]
**Sample answer:** [complete solution with code/formula/steps]
```

#### In-Class format

Produce `num_questions` practicals (default 2). Each is time-boxed, scenario-driven, and ends with an instructor-only walkthrough.

```
# In-Class Practical: [Topic] ([Level])
Subject: [subject]
Duration: [total estimated time] mins
Setup: [what the instructor needs ready on screen: dataset, file, query window, etc.]

## Instructor Introduction
[2–3 sentences to say to the class to frame the exercise]

## Practical 1
**Time box:** [X] minutes
**Scenario:** [real-world context]
**Task:** [step-by-step instruction to students]
**Hint:** [one nudge — no answer]

### Instructor Walkthrough (after time is up)
[Step-by-step solution]
**Key talking points:**
- [What to emphasize]
- [Common mistakes to call out]
```

---

### Step 4 — Write or print (if `--save`)

**If `--save` is set:**
Write to `assignments/[subject]-[level]-[topic-slug]-[type].md`.
If the file already exists, confirm with the instructor before overwriting.

**If `--save` is not set:**
Print the full assignment inline.
End with: `Tip: run with --save to write to assignments/[subject]-[level]-[topic-slug]-[type].md`

---

### Step 5 — Respond and log

Return the full assignment. If `--save` was used, confirm the file path.

Append to `log/assignment-generator.log`:
```
[YYYY-MM-DD HH:MM] assignment-generator
  Input:   topic=[topic] level=[level] type=[type] questions=[N]
  Output:  assignments/[subject]-[level]-[topic-slug]-[type].md (or "printed only")
  Status:  success | partial | failed
  Notes:   [knowledge doc used or not, question types generated]
```
