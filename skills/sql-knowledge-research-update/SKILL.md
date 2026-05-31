---
name: sql-knowledge-research-update
description: Research SQL concepts at a specified skill level and optionally write or merge findings into the project's knowledge docs in skills/.
arguments: "[level] [topic] [--update]"
outputs:
  - skills/sql-[level]-[topic-slug].md
---

# Skill: sql-knowledge-research-update

## Usage

```
/sql-knowledge-research-update [level] [topic] [--update]
```

## Arguments

| Argument | Required | Values | Default |
|----------|----------|--------|---------|
| `level` | no | `beginner` / `intermediate` / `advanced` / `all` | `all` |
| `topic` | no | e.g. `joins`, `subqueries`, `window functions` | `general` |
| `--update` | no | flag — writes synthesized doc to `skills/` | off (print only) |

## Examples

```
/sql-knowledge-research-update beginner joins --update
/sql-knowledge-research-update intermediate subqueries
/sql-knowledge-research-update all window functions --update
```

---

## Execution Steps

### Step 1 — Parse arguments

Extract `level`, `topic`, and `--update` flag. Normalize `topic` to a slug (lowercase, spaces → hyphens). Default `level` to `all`, `topic` to `general` if omitted.

---

### Step 2 — Spawn Researcher agent

Use the Agent tool to spawn the `researcher` subagent with these inputs:

```
subject: sql
topic: [topic]
level: [level]
```

Wait for the agent to complete. It will write raw findings to:
`agents/researcher/output/sql-[level]-[topic-slug]-research.md`

Read the `output_path:` from the agent's final output to get the exact file path.

---

### Step 3a — If `--update`: Spawn Synthesizer agent

Use the Agent tool to spawn the `synthesizer` subagent with these inputs:

```
research_file: [output_path from Step 2]
subject: sql
topic: [topic]
level: [level]
```

Wait for the agent to complete. It will write the structured knowledge doc to:
`skills/sql-[level]-[topic-slug].md`

Confirm the output path to the instructor.

---

### Step 3b — If not `--update`: Print findings

Read and print the contents of the researcher's output file inline.

End with:
`Tip: run with --update to synthesize and save this to skills/sql-[level]-[topic-slug].md`
