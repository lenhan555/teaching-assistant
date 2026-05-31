# In-Class Practical: SQL — JOINs (Intermediate)
Duration: 50 minutes
Dataset / Setup: Instructor must have a live SQL environment (PostgreSQL or compatible) with the following tables pre-loaded and visible on screen:

```sql
-- employees (employee_id INT, employee_name VARCHAR, department_id INT, manager_id INT, hire_date DATE)
-- departments (department_id INT, department_name VARCHAR, location VARCHAR)
-- customers (customer_id INT, customer_name VARCHAR, email VARCHAR)
-- orders (order_id INT, customer_id INT, salesperson_id INT, amount DECIMAL, order_date DATE)
-- salespeople (salesperson_id INT, salesperson_name VARCHAR, region VARCHAR)
```

Sample row counts to mention aloud: employees (20 rows), departments (6 rows), customers (50 rows), orders (120 rows), salespeople (8 rows). Confirm with students they can see the schema before starting Practical 1.

---

## Instructor Notes

**Session objective (plain language):** By the end of this class, students can choose the right JOIN type for a business question, write the correct syntax from scratch, and explain in one sentence why an unmatched row appears or disappears in their results.

**Introduction script (3 minutes):**
"We have five tables in front of us today — they represent a small company's entire data world: its people, its structure, its customers, and its sales. Every practical we run today will ask you to connect two or more of those tables to answer a question a real manager might bring to your desk. Your job is to decide which JOIN type fits, write the query, and then explain your reasoning to the person next to you."

**Timing cues:**
- Practical 1 — 0:00 to 0:08 (8 min, including debrief)
- Practical 2 — 0:08 to 0:18 (10 min, including debrief)
- Practical 3 — 0:18 to 0:30 (12 min, including debrief)
- Practical 4 — 0:30 to 0:42 (12 min, including debrief)
- Practical 5 — 0:42 to 0:50 (8 min, including debrief)

**Discussion prompts to keep in your back pocket:**
- "What happens to an employee with no department if you switch LEFT to INNER here?"
- "Why is the date filter in the ON clause instead of the WHERE clause?"
- "What would the result look like if you used a RIGHT JOIN and swapped the table order?"
- "How would you know — without running it — whether this query could return duplicate rows?"

**What to watch for:**
- Students writing WHERE filters on right-table columns after a LEFT JOIN (silently converts to INNER JOIN)
- Forgetting to alias both sides of a SELF JOIN
- Using INNER JOIN when the question says "include employees with no manager"
- Not accounting for NULL when checking for missing records

---

## Practical 1
**Time box:** 6 minutes
**Scenario:** The HR manager needs a quick roster to verify every employee's department assignment before sending a company-wide announcement. Some new hires have not been assigned to a department yet, and they must still appear on the roster.

**Task:**
Complete the query below by filling in the blanks (`___`). Your result must include every employee, even those without a department assignment.

```sql
SELECT e.employee_name, ___.department_name
FROM employees ___
___ JOIN departments d ON e.department_id = d.department_id;
```

After running it, answer this question in one sentence: what does the `department_name` column show for employees who have no department assignment?

**Hint:** Think about which table must contribute all of its rows. That table goes on the side that matches the JOIN keyword you choose.

### Instructor Walkthrough
**Solution:**
```sql
SELECT e.employee_name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;
```

**Read aloud:** "We put `employees` on the left and `departments` on the right. LEFT JOIN says: keep every row from the left table — employees — whether or not a matching department exists. Employees with no department get a NULL in `department_name`."

**Talking points:**
- Swap the blank answers back to INNER JOIN and ask: "Who disappears?" — students should say unassigned employees vanish.
- Emphasize that the NULLs in `department_name` are not errors — they are information. They tell you exactly who has not been assigned yet.
- Common mistake to call out: writing `d.department_name` in the SELECT before aliasing `departments` as `d` in the FROM clause — always alias first, reference second.

---

## Practical 2
**Time box:** 8 minutes
**Scenario:** A sales analyst needs a report of all orders along with the name of the customer who placed each order. Only orders that are correctly linked to a customer record should appear — any orphaned order records without a matching customer must be excluded.

**Task:**
Fill in the blanks to complete the query. Then add one line to filter the results to orders placed on or after January 1, 2024.

```sql
SELECT o.order_id, ___.customer_name, o.amount, o.order_date
FROM orders ___
___ JOIN customers c ON ___.customer_id = c.customer_id
___; -- add your date filter here
```

**Hint:** When both sides must have a match, and rows without a match on either side should be dropped, there is only one JOIN type that fits.

### Instructor Walkthrough
**Solution:**
```sql
SELECT o.order_id, c.customer_name, o.amount, o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_date >= '2024-01-01';
```

**Read aloud:** "INNER JOIN is the right choice here because the question explicitly said to exclude orphaned orders. Every row in the result guaranteed has a real customer behind it. The WHERE clause then narrows down to 2024 orders only."

**Talking points:**
- Ask: "Where would the date filter go if we had used a LEFT JOIN and needed to keep all orders regardless of customer match?" — answer: it stays in WHERE because we still want to filter orders, not restrict the join.
- Ask: "What if a customer placed no orders? Would they appear here?" — no, because INNER JOIN works in both directions.
- Contrast with Practical 1: same two concepts (matching vs. preserving), now from the orders perspective instead of the employees perspective.

---

## Practical 3
**Time box:** 10 minutes
**Scenario:** The VP of Sales wants to know which customers have never placed an order — these customers will be targeted for a re-engagement campaign. The result must include every customer who has zero orders, and nothing else.

**Task:**
Fill in the blanks to complete the query. Do not use a subquery — use a JOIN approach only.

```sql
SELECT c.customer_id, c.customer_name
FROM customers ___
___ JOIN orders o ON c.customer_id = o.customer_id
WHERE o.___ IS NULL;
```

After filling in the blanks, explain to a partner: why does `WHERE o.order_id IS NULL` identify customers who have never ordered, rather than customers who placed an order with a NULL order ID?

**Hint:** An unmatched row from a LEFT JOIN shows up with NULLs on the right side. Use that NULL as your filter condition.

### Instructor Walkthrough
**Solution:**
```sql
SELECT c.customer_id, c.customer_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

**Read aloud:** "LEFT JOIN preserves every customer. For customers who have placed at least one order, `o.order_id` will have a real value. For customers who have never ordered, LEFT JOIN puts NULL in every `orders` column. The WHERE clause then keeps only the NULL rows — meaning: customers with no match in `orders`."

**Talking points:**
- This is the classic 'anti-join' pattern. Write it on the board: LEFT JOIN + WHERE right.col IS NULL = records that exist on the left but not the right.
- Ask: "What would happen if you changed WHERE to `WHERE o.order_id IS NOT NULL`?" — you would get customers who have ordered, which is the opposite of what we want.
- Common mistake to call out: using `WHERE o.customer_id IS NULL` instead of a non-nullable column like `order_id`. If `customer_id` in the orders table can legitimately be NULL due to a data issue, you might get false positives. Always filter on a NOT NULL column such as a primary key.

---

## Practical 4
**Time box:** 10 minutes
**Scenario:** The HR department stores each employee's manager inside the same `employees` table using the `manager_id` column. A new reporting tool needs to show each employee's name alongside their direct manager's name. Employees who report to no one (the CEO, for example) must still appear in the output — they should show NULL for manager name.

**Task:**
Complete the SELF JOIN query below. Both blanks use the same table name.

```sql
SELECT
    e.employee_name          AS employee,
    ___.employee_name        AS manager
FROM employees ___
LEFT JOIN employees ___ ON e.manager_id = m.employee_id
ORDER BY manager NULLS LAST, employee;
```

Bonus: Change the LEFT JOIN to an INNER JOIN and predict — before running — which rows will disappear and why.

**Hint:** A SELF JOIN requires two different aliases for the same table. Think of it as creating two "virtual copies" — one representing the employee, one representing the manager.

### Instructor Walkthrough
**Solution:**
```sql
SELECT
    e.employee_name     AS employee,
    m.employee_name     AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id
ORDER BY manager NULLS LAST, employee;
```

**Read aloud:** "We alias `employees` twice — `e` for the employee side, `m` for the manager side. The join condition says: match the employee's `manager_id` to the manager's `employee_id`. LEFT JOIN ensures that employees whose `manager_id` is NULL — the top of the hierarchy — still appear in the output with NULL in the manager column."

**Talking points:**
- Walk through the alias logic slowly. Draw a two-box diagram on the board: box 1 labeled `employees e`, box 2 labeled `employees m`, arrow from `e.manager_id` to `m.employee_id`.
- For the bonus: switching to INNER JOIN drops any employee whose `manager_id` is NULL — the CEO and any other top-level employee disappears from the report silently. This is the most common SELF JOIN mistake.
- Ask: "Could you write this as a RIGHT JOIN? How would you rewrite it?" — yes, swap `e` and `m` and change LEFT to RIGHT. Use this to reinforce that RIGHT JOIN is just a flipped LEFT JOIN.

---

## Practical 5
**Time box:** 6 minutes
**Scenario:** The finance team is auditing salesperson performance for Q1 2024 (January 1 through March 31). They need a list of every salesperson and their total sales during that period. Salespeople who made zero sales must appear in the report with a total of 0 — not be missing from the list.

**Task:**
A colleague wrote the query below but the manager flagged it: salespeople with zero Q1 sales are missing from the results. Find the two bugs and fix them.

```sql
-- Buggy version — fix it
SELECT
    s.salesperson_name,
    SUM(o.amount) AS total_sales
FROM salespeople s
INNER JOIN orders o ON s.salesperson_id = o.salesperson_id
WHERE o.order_date BETWEEN '2024-01-01' AND '2024-03-31'
GROUP BY s.salesperson_id, s.salesperson_name
ORDER BY total_sales DESC;
```

**Hint:** There are exactly two problems: one in the JOIN type, and one in where the date filter lives. Fix one at a time and think about what each change does to the row set.

### Instructor Walkthrough
**Corrected query:**
```sql
SELECT
    s.salesperson_name,
    COALESCE(SUM(o.amount), 0) AS total_sales
FROM salespeople s
LEFT JOIN orders o
    ON s.salesperson_id = o.salesperson_id
    AND o.order_date BETWEEN '2024-01-01' AND '2024-03-31'
GROUP BY s.salesperson_id, s.salesperson_name
ORDER BY total_sales DESC;
```

**Bug 1 — INNER JOIN → LEFT JOIN:** INNER JOIN drops salespeople with no Q1 orders entirely. LEFT JOIN keeps all salespeople and fills `orders` columns with NULL when there is no match.

**Bug 2 — WHERE filter → ON clause filter:** Moving the date filter to WHERE reinstates the INNER JOIN behavior even after switching to LEFT JOIN. The WHERE clause runs after the join and eliminates any row where `o.order_date` is NULL — which is every salesperson with zero sales. Moving the filter into the ON clause restricts which order rows attach to each salesperson, without affecting whether the salesperson row itself survives.

**Bonus fix — COALESCE:** `SUM(o.amount)` returns NULL (not 0) when a salesperson has no orders. Wrap it in `COALESCE(..., 0)` so zero-sales rows display cleanly as 0 rather than NULL.

**Talking points:**
- This is the most important pattern in the whole session. The LEFT JOIN + ON-clause filter combination appears in virtually every "include zero-value records" business report.
- Ask: "If you moved the COALESCE but kept the WHERE clause, would the zero-sales salespeople appear?" — no. COALESCE fixes display; the WHERE fix is what determines which rows survive.
- Close the session by asking students to summarize in one sentence when they would use LEFT JOIN vs INNER JOIN. Cold-call two or three students for different phrasings.

---

output_path: /Users/leopham/Documents/Teaching Assistant/assignments/sql-intermediate-joins-in-class.md
