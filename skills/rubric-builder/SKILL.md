---
name: rubric-builder
description: Generate a grading rubric from an assignment file; optionally save to rubrics/.
arguments: "<assignment_file> [--subject <subject>] [--level <level>] [--topic <topic>]"
outputs:
  - rubrics/[subject]-[level]-[topic-slug]-rubric.md
---

# Skill: rubric-builder

## Usage

```
/rubric-builder <assignment_/file> [--subject <subject>] [--level <level>] [--topic <topic>]
```

## Arguments

| Argument | Required | Values | Default |
|----------|----------|--------|---------|
| `assignment_file` | yes | path to file in `assignments/` | — |
| `--subject` | no | `sql` / `excel` / `powerbi` | inferred from filename |
| `--level` | no | `beginner` / `intermediate` / `advanced` | inferred from filename |
| `--topic` | no | topic slug | inferred from filename |

## Examples

```
/rubric-builder assignments/sql-beginner-joins-take-home.md
/rubric-builder assignments/excel-intermediate-pivot-tables-take-home.md --topic pivot-tables
```

---

## Execution Steps

### Step 1 — Parse arguments

Extract `assignment_file`, `subject`, `level`, and `topic`. Infer any missing values from the filename pattern `[subject]-[level]-[topic-slug]-[type].md`.

---

### Step 2 — Spawn Rubric Builder agent

Use the Agent tool to spawn the `rubric-builder` subagent with these inputs:

```
assignment_file: [assignment_file]
subject: [subject]
topic: [topic]
level: [level]
```

Wait for the agent to complete. It will write the rubric to:
`rubrics/[subject]-[level]-[topic-slug]-rubric.md`

---

### Step 3 — Report result

Confirm the rubric file path to the instructor.
