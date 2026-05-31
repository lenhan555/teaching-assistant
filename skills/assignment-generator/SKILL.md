---
name: assignment-generator
description: Generate a take-home or in-class assignment for a given topic and level; optionally save to assignments/.
arguments: '"<topic>" --level <level> [--type <type>] [--questions N] [--subject <subject>] [--save]'
outputs:
  - assignments/[subject]-[level]-[topic-slug]-[type].md
---

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

Extract `topic`, `level`, `type`, `questions`, `subject`, and `--save` flag. Infer `subject` from `topic` if not stated (SQL → `sql`, Excel → `excel`, Power BI / DAX → `powerbi`). Normalize `topic` to a slug.

---

### Step 2 — Check for knowledge doc

Look for an existing knowledge doc at `skills/[subject]-[level]-[topic-slug].md`. Note the path if found — pass it to the agent as `knowledge_doc`.

---

### Step 3 — Spawn Assignment Generator agent

Use the Agent tool to spawn the `assignment-generator` subagent with these inputs:

```
subject: [subject]
topic: [topic]
level: [level]
--type: [type]
num_questions: [questions]
knowledge_doc: [path if found, omit if not]
--save: [true if --save flag was set]
```

Wait for the agent to complete. It will write to (if --save):
`assignments/[subject]-[level]-[topic-slug]-[type].md`

---

### Step 4 — Report result

If `--save` was used, confirm the file path written.
If not, the agent's output is already printed inline.
