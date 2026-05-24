# Skill: power-bi-knowledge-research-update

## Usage

```
/power-bi-knowledge-research-update [level] [topic] [--update]
```

## Arguments

| Argument | Required | Values | Default |
|----------|----------|--------|---------|
| `level` | no | `beginner` / `intermediate` / `advanced` / `all` | `all` |
| `topic` | no | e.g. `measures`, `relationships`, `CALCULATE` | `general` |
| `--update` | no | flag | off (print only) |

## Examples

```
/power-bi-knowledge-research-update beginner measures --update
/power-bi-knowledge-research-update intermediate CALCULATE
/power-bi-knowledge-research-update all relationships --update
```

---

## Execution Steps

### Step 1 — Parse invocation

Extract `level`, `topic`, and `--update` flag. Normalize `topic` to a slug. Default `level` to `all` and `topic` to `general` if omitted.

---

### Step 2 — Check existing content

Read any existing file at `skills/powerbi-[level]-[topic-slug].md`. Note covered concepts to avoid duplication.

---

### Step 3 — Web research

Search for authoritative Power BI content using the query templates below. Fetch at least 3 sources per level included.

**Query templates:**
- `Power BI [topic] [level] tutorial 2024 2025`
- `DAX [topic] examples explained`
- `Power BI [topic] best practices`
- `site:learn.microsoft.com power-bi [topic]`
- `site:dax.guide [topic]`
- `site:sqlbi.com [topic]`

**Preferred sources (in priority order):**
1. learn.microsoft.com/power-bi — official Microsoft documentation
2. dax.guide — authoritative DAX function reference
3. sqlbi.com — advanced DAX patterns and data modeling
4. youtube.com/guyinacube — practical tutorials (summarize — do not embed video)
5. Recent articles (≤ 2 years) from reputable Power BI community blogs

---

### Step 4 — Apply level boundaries

Filter content to the appropriate level(s):

| Level | Include |
|-------|---------|
| `beginner` | Import data (Excel, CSV, SQL), basic visuals (bar, line, card, table), report filters and slicers, simple measures (SUM, COUNT, AVERAGE), publish to Power BI Service, basic page navigation |
| `intermediate` | DAX (CALCULATE, SUMX, FILTER, time intelligence functions: TOTALYTD, SAMEPERIODLASTYEAR), many-to-one relationships, star schema basics, data model design, row-level security (static), drill-through and bookmarks |
| `advanced` | Query folding in Power Query, incremental refresh, composite models (DirectQuery + Import), advanced DAX patterns (RANKX, TOPN, virtual tables, context transition), deployment pipelines, dynamic RLS, calculation groups |
| `all` | Union of all three levels — organize output into separate level sections |

---

### Step 5 — Build structured report

Produce a markdown document with this structure:

```
# Power BI: [Topic] — [Level]
Last updated: [YYYY-MM-DD]
Sources: [comma-separated URLs]

## Overview
[2–3 sentences: what this concept is and when Power BI users need it]

## Concepts
### [Concept / DAX Function / Feature Name]
- **Definition:** ...
- **When to use:** ...
- **Syntax:** `FUNCTION(parameters)`
- **Real example:** [realistic business scenario with DAX expression or step-by-step]
- **Common mistakes:** ...

## Worked Examples
[Full step-by-step example with a realistic data model described in text]

## Exercises
### Exercise 1 — [Easy / Medium / Hard]
[Problem stem]
**Sample answer:** ...

### Exercise 2 — ...

## Quick Reference
| Function / Feature | Purpose | Example |
|--------------------|---------|---------|
| ... | ... | ... |
```

---

### Step 6 — Write or merge (if `--update`)

**If `--update` is set:**
- If `skills/powerbi-[level]-[topic-slug].md` does not exist: create it with the full report
- If it exists: append new sections only; never overwrite existing content; mark corrections as `> ⚠️ Correction as of [DATE]: [note]`; add `## Updated [YYYY-MM-DD]` header before appended content

**If `--update` is not set:**
- Print the full report inline; do not write any file
- End response with: `Tip: run with --update to save this to skills/powerbi-[level]-[topic-slug].md`

---

### Step 7 — Respond and log

Return the full report to the instructor. If `--update` was used, confirm the file path written.

Append to `log/power-bi-knowledge-research-update.log`:
```
[YYYY-MM-DD HH:MM] power-bi-knowledge-research-update
  Input:   level=[level] topic=[topic] update=[true/false]
  Output:  skills/powerbi-[level]-[topic-slug].md (or "printed only")
  Status:  success | partial | failed
  Notes:   [sources used, sections added or merged]
```
