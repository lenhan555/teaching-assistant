# Grading Rubric: SQL — JOINs (Intermediate)

**Assignment:** sql-intermediate-joins-take-home.md  
**Total marks:** 100  
**Generated:** 2026-05-25

---

## Rubric Table

| Criterion | Weight | Full Marks | Partial Marks | Zero Marks |
|-----------|--------|------------|---------------|------------|
| **Q1: INNER JOIN query** | 10 pts | Correct INNER JOIN between orders and customers on customer_id; returns exactly 4 columns (order_id, customer_name, order_date, amount); all 8 rows returned; sorted correctly by order_date ascending; correct syntax; output screenshot/paste provided. | Correct structure and 8 rows, but missing sort order (5 pts); OR correct sort and columns but 1-2 rows missing or extra (6-7 pts); OR correct logic but minor syntax error that would still execute (7 pts). | Incorrect JOIN type used (e.g. LEFT JOIN instead of INNER); missing required columns; rows incorrect; no output provided; query does not execute. |
| **Q2: LEFT JOIN query** | 10 pts | Correct LEFT JOIN between employees and departments on department_id; returns exactly 3 columns (employee_name, department_name, location); all 10 rows returned including Jake Williams with NULLs; sorted by department_name ascending with NULL values last; correct syntax; output screenshot/paste provided. | Correct structure and 10 rows, but missing or incorrect sort (NULL order wrong or not sorted by department) (5-7 pts); OR correct columns and LEFT JOIN but 1 row missing/extra (6-7 pts); OR correct logic but minor syntax issue like missing NULLS LAST that affects sort (7 pts). | Missing LEFT JOIN (uses INNER or other type); fewer than 10 rows (Jake filtered out); incorrect columns; NULLs not handled; no output provided; query does not execute. |
| **Q3 Part A: Conceptual explanation of RIGHT JOIN bug** | 8 pts | Correctly identifies that WHERE clause filters on NULL values from right-padded side; explains that NULL > 80000 evaluates to false, causing departments with no employees to be silently dropped; states that query produces INNER JOIN-like result (only employees > 80k); response is clear and concise (1-2 sentences). | Identifies that WHERE causes filtering but explanation is unclear or incomplete (e.g. mentions NULL but doesn't explain the evaluation to false); mentions the bug exists but doesn't fully explain the mechanism (4-5 pts); OR correct explanation but slightly verbose/unclear wording (6 pts). | No answer provided; identifies no bug; incorrect explanation (e.g. claims the query is correct or blames the JOIN keyword itself); confuses LEFT/RIGHT/INNER semantics. |
| **Q3 Part B: Corrected RIGHT JOIN query** | 9 pts | Correct RIGHT JOIN from employees to departments; date/salary filter moved into ON clause (e.g. AND e.salary > 80000); returns exactly 3 columns (department_name, employee_name, salary); all 5 departments appear (including Legal with NULL); employees > 80k shown, others as NULL; sorted correctly; output provided. | Correct JOIN and all 5 departments returned, but minor sort issue or missing output (6-7 pts); OR filter in ON clause but column order different from spec (still full logic) (8 pts); OR correct logic but 1 minor syntax error that doesn't affect execution (8 pts). | Filter remains in WHERE clause (silently drops depts with no high-earners); fewer than 5 departments; incorrect columns or column order; wrong JOIN type; no output; query does not execute. |
| **Q4: SELF JOIN (employee hierarchy)** | 10 pts | Correct LEFT JOIN of employees table to itself on manager_id; alias used clearly (e.g. e and m); returns exactly 2 columns (employee_name, manager_name); all 10 rows returned; 4 top-level employees show with manager_name = NULL; sorted by manager_name ascending, NULL last, then by employee_name; correct syntax; output provided. | Correct structure and all 10 rows, but sort order incorrect or incomplete (5-7 pts); OR correct join and columns but 1-2 rows missing/extra (6-7 pts); OR correct logic but minor syntax issue (7 pts). | Missing self-join (joins employees to departments instead); fewer than 10 rows; incorrect columns; managers not named correctly; alias inconsistency prevents code clarity; no output; query does not execute. |
| **Q5: LEFT JOIN to find missing customers** | 10 pts | Correct LEFT JOIN from customers to orders on customer_id; WHERE clause filters on o.order_id IS NULL (or equivalent); returns exactly 3 columns (customer_id, customer_name, city); exactly 1 row returned (ClearPath Inc, 105, Denver); no subquery used; correct syntax; output provided. | Correct logic (1 row, no subquery) but wrong IS NULL column tested (e.g. IS NULL on wrong field but still gets 1 row) (7-8 pts); OR correct approach but minor syntax error (8 pts); OR correct structure but 2 rows returned due to misunderstanding NULL semantics (5-6 pts). | Uses subquery or NOT IN (violates constraint); returns 0 rows or >1 rows; uses INNER/RIGHT JOIN instead of LEFT; missing columns; no output; query does not execute. |
| **Q6: Multi-table JOIN + aggregation + date in ON clause** | 17 pts | **Structure (8 pts):** LEFT JOIN from employees → orders on employee_id AND date filter in ON clause (not WHERE); WHERE clause filters on department_id = 3 only; **Correctness (7 pts):** Returns Grace Kim and Henry Chan; totals non-zero for at least one; rows grouped correctly; COALESCE or SUM handling ensures 0 totals appear, not NULL; 2 rows returned; columns: employee_name, order_count, total_sales; sorted by total_sales DESC; date range correct (2024-01-01 to 2024-03-31); **Output (2 pts):** Result screenshot/paste provided; comment explains why date filter must be in ON clause (prevents LEFT JOIN → INNER JOIN conversion). | Correct date filter in ON clause and department filter in WHERE, but minor aggregation issue (e.g. totals off by small amount due to rounding/coercion) (12-14 pts); OR structure correct but comment missing or unclear (14-15 pts); OR structure and logic correct but only 1 row returned (one salesperson has no Q1 orders but is missing from output) (12-14 pts); OR correct output but syntax error that doesn't affect execution (15 pts). | Date filter in WHERE clause (converts LEFT to INNER, drops 0-order salespeople) (0-5 pts); wrong department ID or logic; aggregation clearly wrong (negative totals, wrong count); fewer than 2 rows when both should appear; missing GROUP BY or COALESCE; no output; query does not execute. |
| **Q7 Part A: Correlated subquery rewrite** | 13 pts | Rewrite uses INNER JOIN from customers to a derived table/CTE that performs GROUP BY customer_id with MAX(amount); WHERE clause filters on max_order > 1000 (after join); returns exactly 1 column (customer_name) or uses SELECT DISTINCT; exactly 3 rows returned (Pinnacle Tech, Oakwood Group, Sunrise Media); no subquery in WHERE clause; identical results to original query; syntax correct; output provided. | Correct derived table/GROUP BY/MAX approach and 3 correct rows, but missing SELECT DISTINCT when duplicate customer_names appear (still correct logic) (10-11 pts); OR correct approach with 3 rows but includes extra columns (11-12 pts); OR uses CTE instead of derived table (still correct) but structure less efficient (11 pts); OR correct logic but 1 minor syntax issue (12 pts). | Still contains subquery in WHERE clause (not rewritten); fewer than 3 rows or more than 3 rows; uses NOT IN or other forbidden approach; results do not match original query (wrong customers returned); no output; query does not execute. |
| **Q7 Part B: Performance explanation** | 12 pts | Clearly explains that correlated subquery re-executes for N customers (O(N) passes over orders); states JOIN rewrites aggregates orders once (O(1) passes); names at least one concrete optimization (index on (customer_id, amount), EXPLAIN ANALYZE usage, or query plan inspection); explains how that optimization helps (index-only scan, avoids full table scan); answer is 2-4 sentences, technically accurate. | Correctly identifies re-execution vs. single-pass but explanation lacks clarity or depth (e.g. doesn't name why: N executions) (7-9 pts); OR names optimization but doesn't explain how it helps (8-10 pts); OR mentions EXPLAIN but not how to interpret it; general answer but missing concrete technique name (8-10 pts); OR answer slightly verbose or wandering (9-10 pts). | No answer provided; incorrect claim (e.g. says correlated subquery is faster); vague answer with no technical content; does not mention performance at all; suggests optimization unrelated to the problem (e.g. query caching). |
| **Submission format (all sections present)** | 1 pt | All 7 questions (Q1–Q7) present in single `.sql` file with clear section comments (e.g. `-- Q1`, `-- Q3 Part A`); output for each practical query included as screenshot or pasted result; short-answer sections written as SQL comments; file is properly formatted and readable. | One section missing (output or comment); file structure present but one question's output unclear or incomplete; minor formatting issue (0.5 pts). | Multiple sections missing; unrelated or incorrectly labeled sections; no outputs provided; file is unreadable or not .sql format. |

---

## Grading Notes

### Key Concepts to Verify

1. **INNER JOIN (Q1):** All 8 orders should appear. If only 7 appear, the student may have filtered incorrectly. Verify the ON clause matches customer_id, not a different field.

2. **LEFT JOIN (Q2):** Jake Williams (employee_id 10) must appear with NULLs. If 9 rows only, Jake was lost — likely the student used INNER JOIN by accident. Check the sort order carefully: NULL values should sort last when using `NULLS LAST`.

3. **RIGHT JOIN Bug (Q3 Part A):** Common misconceptions:
   - "The query is correct" → no credit.
   - "RIGHT JOIN is wrong" → partial credit; they must explain the WHERE clause is the actual problem.
   - Correct answer must mention NULL evaluation: `NULL > 80000 → FALSE`, causing departments with no employees to vanish.

4. **SELF JOIN (Q4):** Students often forget the alias on the second reference to employees. Verify the manager_name column pulls from the second alias (m.employee_name), not e.employee_name. All 4 top-level employees (Alice, David, Frank, Iris) should have NULL manager_name.

5. **Missing Records (Q5):** COMMON ERROR: Students may use `o.customer_id IS NULL` instead of `o.order_id IS NULL`. Both produce the same result here (1 row) but the question specifies looking for missing orders, so `order_id IS NULL` is semantically correct.
   - FORBIDDEN: If subquery or NOT IN is used, automatic zero; the question explicitly forbids these approaches to test LEFT JOIN mastery.

6. **Q6 Date Filter Placement:** This is a **critical concept**. 
   - If the date filter is in the WHERE clause instead of the ON clause, the LEFT JOIN converts to an INNER JOIN and Grace/Henry with zero Q1 orders disappear (wrong answer, 0–5 pts for this criterion).
   - The comment explaining why is mandatory; if missing, deduct points.
   - COALESCE or SUM(...) must handle NULL; students who forget this may see NULL totals instead of 0 (partial credit).
   - Grace Kim: 3 orders in Q1 2024 (order_ids 1001, 1005, 1007), total $5,220.
   - Henry Chan: 2 orders in Q1 2024 (order_ids 1003, 1004), total $2,600.

7. **Q7 Correlated Subquery Rewrite:**
   - The original query is a correlated subquery: `SELECT MAX(amount) FROM orders WHERE o.customer_id = c.customer_id` runs once per customer row.
   - Correct rewrite uses a derived table (or CTE) that groups orders and computes MAX per customer, then JOINs back.
   - WRONG: If the student still uses a subquery in the WHERE clause, zero credit — the question asks for a JOIN rewrite.
   - Expected customers: Pinnacle Tech (max order $5,500), Oakwood Group (max $2,200), Sunrise Media (max $3,100). ClearPath and Bright Solutions do not appear (max orders $850 and $1,750, both ≤ $1,000).

8. **Edge Cases:**
   - NULL values in sorts: PostgreSQL (and some other engines) put NULLs first by default unless `NULLS LAST` is used. Accept either if the sort is stable and reasonable.
   - COALESCE vs. IFNULL: Both are acceptable; SQL dialect may vary.
   - Derived table vs. CTE: Both are acceptable; no style preference.
   - Column order: Accept any order except where a question explicitly specifies (e.g., Q3 Part B specifies department_name, employee_name, salary).

### Common Errors (Deduction Guidance)

- **Wrong row count without output screenshot:** Difficult to debug; ask student to resubmit output. If row count is verifiably wrong, deduct based on cause (missing/extra rows = partial).
- **Syntax error that prevents execution:** Zero for that query; acceptable if the logic is obvious and only punctuation is wrong (then 7–8 pts).
- **Wildcard SELECT (SELECT \*):** Acceptable only if the columns returned match the spec. Deduct 1 pt if columns are unclear.
- **Missing aliases:** If the query is ambiguous (e.g., two tables have the same column and no alias clarifies which one), deduct 1 pt for clarity.
- **EXPLAIN ANALYZE not provided for Q7 Part B:** Not mandatory, but accepting it as additional evidence of performance improvement is encouraged.

---

## Score Bands

| Grade | Score Range | Descriptor |
|-------|-------------|------------|
| Excellent | 90–100% | Mastery of all JOIN types; correct date/filter placement; clear explanations of concepts; all outputs provided; no syntax errors. |
| Proficient | 75–89% | Solid understanding of INNER, LEFT, and SELF JOINs; minor gaps in advanced topics (Q6 date placement, Q7 optimization); most outputs present; 1–2 minor errors. |
| Developing | 60–74% | Basic JOIN syntax correct; some conceptual gaps (e.g., confuses LEFT/RIGHT, or misses ON clause placement); partial credit on Q3 and Q7 explanations; missing some outputs. |
| Beginning | Below 60% | Foundational gaps in JOIN mechanics; queries do not execute or return incorrect data; explanations missing or incorrect; multiple missing outputs or incomplete sections. |

---

output_path: /Users/leopham/Documents/Teaching Assistant/rubrics/sql-intermediate-joins-rubric.md
