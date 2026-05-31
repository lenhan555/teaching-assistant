---
name: power-bi-knowledge-research-update
description: Research Power BI and DAX concepts at a specified skill level and optionally write or merge findings into the project's knowledge docs in skills/.
arguments: "[level] [topic] [--update]"
outputs:
  - skills/powerbi-[level]-[topic-slug].md
---

# Skill: power-bi-knowledge-research-update

## Usage

```
/power-bi-knowledge-research-update [level] [topic] [--update]
```

## Arguments

| Argument | Required | Values | Default |
|----------|----------|--------|---------|
| `level` | no | `beginner` / `intermediate` / `advanced` / `all` | `all` |
| `topic` | no | e.g. `dax calculate`, `data modeling`, `report design` | `general` |
| `--update` | no | flag — writes synthesized doc to `skills/` | off (print only) |

## Examples

```
/power-bi-knowledge-research-update beginner report design --update
/power-bi-knowledge-research-update intermediate dax calculate
/power-bi-knowledge-research-update all data modeling --update
```

---

## Execution Steps

### Step 1 — Parse arguments

Extract `level`, `topic`, and `--update` flag. Normalize `topic` to a slug (lowercase, spaces → hyphens). Default `level` to `all`, `topic` to `general` if omitted.

---

### Step 2 — Spawn Researcher agent

Use the Agent tool to spawn the `researcher` subagent with these inputs:

```
subject: powerbi
topic: [topic]
level: [level]
```

Wait for the agent to complete. It will write raw findings to:
`agents/researcher/output/powerbi-[level]-[topic-slug]-research.md`

Read the `output_path:` from the agent's final output to get the exact file path.

---

### Step 3a — If `--update`: Spawn Synthesizer agent

Use the Agent tool to spawn the `synthesizer` subagent with these inputs:

```
research_file: [output_path from Step 2]
subject: powerbi
topic: [topic]
level: [level]
```

Wait for the agent to complete. It will write the structured knowledge doc to:
`skills/powerbi-[level]-[topic-slug].md`

Confirm the output path to the instructor.

---

### Step 3b — If not `--update`: Print findings

Read and print the contents of the researcher's output file inline.

End with:
`Tip: run with --update to synthesize and save this to skills/powerbi-[level]-[topic-slug].md`
