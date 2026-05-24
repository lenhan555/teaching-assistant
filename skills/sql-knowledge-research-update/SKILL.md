# sql-knowledge-research-update

Research SQL knowledge at a specified skill level and save or update training documents in this project's `skills/` folder. Sources include live web research and any existing training files already in the project.

## Usage

```
/sql-knowledge-research-update [level] [topic] [--update]
```

**Arguments:**
- `level` — `beginner`, `intermediate`, `advanced`, or `all` (default: `all`)
- `topic` — specific SQL subject, e.g. `joins`, `indexes`, `window functions`, `transactions` (default: `general`)
- `--update` — write/merge the findings into the project's `skills/` folder

**Examples:**
```
/sql-knowledge-research-update beginner
/sql-knowledge-research-update intermediate joins
/sql-knowledge-research-update advanced window functions --update
/sql-knowledge-research-update all --update
```

---

## Execution Steps

### Step 1 — Parse the invocation

From the user's message extract:
- `LEVEL` → one of `beginner`, `intermediate`, `advanced`, `all`. Default: `all`.
- `TOPIC` → free-text SQL subject. Default: `general`.
- `UPDATE` → `true` if `--update` is present, otherwise `false`.

---

### Step 2 — Read existing training docs

Scan this path for existing content:
```
<PWD>/skills/
```
where `<PWD>` is the current project working directory (`/Users/leopham/Documents/Teaching Assistant`).

Full path: `/Users/leopham/Documents/Teaching Assistant/skills/`

List all `.md` and `.sql` files. For files that match the requested `LEVEL` and `TOPIC`, read them fully so you know what is already covered and can avoid redundancy.

---

### Step 3 — Web research

Use `WebSearch` and `WebFetch` to gather current, accurate SQL content for the requested level and topic.

**Preferred sources:** PostgreSQL docs, MySQL docs, SQL Server docs, SQLite docs, mode.com/sql-tutorial, use-the-index-luke.com, recent (≤2 years old) technical articles.

**Search queries to run (adapt to LEVEL and TOPIC):**
- `SQL [TOPIC] [LEVEL] tutorial 2024 2025`
- `SQL [TOPIC] best practices examples`
- `SQL [TOPIC] common mistakes pitfalls`

---

### Step 4 — Level scope

Apply these boundaries when deciding what to include per level:

#### Beginner
- SELECT, FROM, WHERE, ORDER BY, LIMIT/OFFSET
- Filtering: AND, OR, NOT, IN, BETWEEN, LIKE, IS NULL
- Basic data types: INT, VARCHAR, DATE, BOOLEAN, DECIMAL
- Aggregations: COUNT, SUM, AVG, MIN, MAX with GROUP BY and HAVING
- INNER JOIN and LEFT JOIN
- INSERT INTO, UPDATE, DELETE basics
- Simple subqueries in WHERE clause

#### Intermediate
- All JOIN types: RIGHT JOIN, FULL OUTER JOIN, CROSS JOIN, SELF JOIN
- Correlated subqueries and EXISTS / NOT EXISTS
- Common Table Expressions (CTEs) — WITH clause
- Window functions: ROW_NUMBER, RANK, DENSE_RANK, LEAD, LAG, OVER, PARTITION BY, ORDER BY
- CASE WHEN expressions
- String functions: CONCAT, SUBSTRING, TRIM, UPPER, LOWER, REPLACE, COALESCE
- Date/time functions: NOW, DATEADD, DATEDIFF, DATE_TRUNC, EXTRACT
- Views and their limitations
- Indexes: clustered vs non-clustered, when to add them
- EXPLAIN / EXPLAIN ANALYZE basics
- Transactions: BEGIN, COMMIT, ROLLBACK

#### Advanced
- Recursive CTEs
- Advanced window functions: NTILE, PERCENT_RANK, CUME_DIST, window frames (ROWS BETWEEN, RANGE BETWEEN)
- Query optimization: reading execution plans, index usage, covering indexes, partial indexes
- Table partitioning: range, list, hash
- JSON/JSONB querying (PostgreSQL: `->`, `->>`, `@>`, `jsonb_array_elements`; MySQL: `JSON_EXTRACT`, `JSON_TABLE`)
- Stored procedures, user-defined functions, triggers
- Isolation levels: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE; phantom reads, dirty reads
- Materialized views: refresh strategies, use cases
- Full-text search
- Replication basics: primary/replica, read replicas
- Dialect differences: PostgreSQL vs MySQL vs SQL Server vs SQLite

---

### Step 5 — Build the research report

Produce a structured markdown document using this exact template:

```markdown
# SQL Knowledge — [LEVEL] | [TOPIC]
**Generated:** [TODAY'S DATE]  
**Sources:** [list URLs or doc names used]

---

## Overview
[2–3 sentence summary of what this document covers and why it matters at this level]

---

## Concepts

### [Concept Name]
**What it is:** [one-sentence definition]

**When to use it:** [practical guidance]

**Syntax:**
```sql
-- minimal working example
```

**Real-world example:**
```sql
-- more complete, realistic query
```

**Common mistakes:**
- [mistake 1]
- [mistake 2]

---

[repeat ### Concept block for each concept — minimum 3 per level]

---

## Exercises

### Exercise 1 — [Short Title] *(Difficulty: Beginner/Intermediate/Advanced)*
[Problem statement — clear, realistic scenario]

<details>
<summary>Solution</summary>

```sql
-- solution query with brief inline comments explaining key lines
```

**Explanation:** [1–2 sentences on why this approach works]
</details>

---

[minimum 2 exercises per level covered]

---

## Quick Reference

| Concept | Syntax | Notes |
|---------|--------|-------|
| [name] | `[snippet]` | [when to use] |

---

## What Changed vs Existing Docs
- **New:** [concepts/exercises not previously in the doc]
- **Updated:** [items that were corrected or expanded]
- **Unchanged:** [items already well-covered — not re-added]
```

Always include at least 3 concepts and 2 exercises for each level being reported.

---

### Step 6 — Write or update files (only when `--update` is set)

Target directory: `/Users/leopham/Documents/Teaching Assistant/skills/`

**File naming:**
```
sql-[level]-[topic-slug].md
```
Examples:
- `sql-beginner-general.md`
- `sql-intermediate-joins.md`
- `sql-advanced-window-functions.md`
- `sql-all-general.md`

**Merge rules:**
- **File does not exist** → create it with the full report.
- **File exists** → append only new concepts and exercises not already present. Prepend an `## Updated [DATE]` section listing the changelog. Do not delete existing content. If existing content is factually wrong, add a `> ⚠️ Correction as of [DATE]:` callout inline rather than deleting.
- When `level = all`, write one file per level: `sql-beginner-[topic].md`, `sql-intermediate-[topic].md`, `sql-advanced-[topic].md`.

After writing, list every file path modified or created.

---

### Step 7 — Respond to the user

Always print the full research report in the conversation.

If `--update` was used, append:
```
Files written/updated:
- /Users/leopham/Documents/Teaching Assistant/skills/sql-[level]-[topic].md
```

If `--update` was NOT used, append:
```
Tip: Run `/sql-knowledge-research-update [level] [topic] --update` to save this to your training docs.
```
