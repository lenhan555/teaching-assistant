# Skill: excel-knowledge-research-update

## Usage

```
/excel-knowledge-research-update [level] [topic] [--update]
```

## Arguments

| Argument | Required | Values | Default |
|----------|----------|--------|---------|
| `level` | no | `beginner` / `intermediate` / `advanced` / `all` | `all` |
| `topic` | no | e.g. `vlookup`, `pivot tables`, `power query` | `general` |
| `--update` | no | flag | off (print only) |

## Examples

```
/excel-knowledge-research-update beginner vlookup --update
/excel-knowledge-research-update intermediate pivot tables
/excel-knowledge-research-update all power query --update
```

---

## Execution Steps

### Step 1 — Parse invocation

Extract `level`, `topic`, and `--update` flag from the command. Normalize `topic` to a slug (lowercase, spaces → hyphens). If `level` is omitted, default to `all`. If `topic` is omitted, default to `general`.

---

### Step 2 — Check existing content

Read any existing file at `skills/excel-[level]-[topic-slug].md`. Note which concepts are already covered so research avoids duplication and only fills gaps.

---

### Step 3 — Web research

Search for authoritative content using the query templates below. Fetch at least 3 sources per level included.

**Query templates:**
- `Excel [topic] [level] tutorial 2024 2025`
- `Excel [topic] formula examples`
- `Excel [topic] best practices common mistakes`
- `site:support.microsoft.com Excel [topic]`
- `site:exceljet.net [topic]`

**Preferred sources (in priority order):**
1. support.microsoft.com/excel — official Microsoft documentation
2. exceljet.net — formula reference and examples
3. chandoo.org — tutorials and real-world use cases
4. contextures.com — detailed how-to guides
5. Recent articles (≤ 2 years) from reputable Excel blogs

---

### Step 4 — Apply level boundaries

Filter content to the appropriate level(s):

| Level | Include |
|-------|---------|
| `beginner` | SUM, AVERAGE, COUNT, IF, VLOOKUP / XLOOKUP, basic charts (bar, line, pie), table formatting, sorting & filtering, basic cell references (absolute vs relative) |
| `intermediate` | PivotTables, Power Query (import, transform, load), nested IFs, SUMIF / COUNTIF, named ranges, conditional formatting, data validation, INDEX/MATCH |
| `advanced` | Power Pivot / DAX basics, array formulas (FILTER, UNIQUE, SORT, SPILL), dynamic arrays, VBA intro (record macro, simple Sub), large-dataset performance (data model vs worksheet), LAMBDA |
| `all` | Union of all three levels — organize output into separate level sections |

---

### Step 5 — Build structured report

Produce a markdown document with this structure:

```
# Excel: [Topic] — [Level]
Last updated: [YYYY-MM-DD]
Sources: [comma-separated URLs]

## Overview
[2–3 sentences: what this concept is and when Excel users reach for it]

## Concepts
### [Concept / Function Name]
- **Definition:** ...
- **When to use:** ...
- **Syntax:** `=FUNCTION(arg1, arg2, ...)`
- **Real example:** [realistic business scenario with formula and result]
- **Common mistakes:** ...

## Worked Examples
[Full step-by-step example with a realistic dataset described in text]

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
- If `skills/excel-[level]-[topic-slug].md` does not exist: create it with the full report
- If it exists: append new sections only; never overwrite existing content; mark corrections as `> ⚠️ Correction as of [DATE]: [note]`; add `## Updated [YYYY-MM-DD]` header before appended content

**If `--update` is not set:**
- Print the full report inline; do not write any file
- End response with: `Tip: run with --update to save this to skills/excel-[level]-[topic-slug].md`

---

### Step 7 — Respond and log

Return the full report to the instructor. If `--update` was used, confirm the file path written.

Append to `log/excel-knowledge-research-update.log`:
```
[YYYY-MM-DD HH:MM] excel-knowledge-research-update
  Input:   level=[level] topic=[topic] update=[true/false]
  Output:  skills/excel-[level]-[topic-slug].md (or "printed only")
  Status:  success | partial | failed
  Notes:   [sources used, sections added or merged]
```
