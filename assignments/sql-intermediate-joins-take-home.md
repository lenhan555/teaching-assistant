# Take-Home Assignment: SQL — JOINs (Intermediate)
Due: _______________
Student name: _______________

---

## Instructions

Using the SQL script provided in the **Dataset Setup** section below, create all tables and insert the sample data in your local database (PostgreSQL or any ANSI SQL-compatible engine). Write your queries in a `.sql` file, one clearly labelled section per question. Submit your `.sql` file via the course portal before the due date. Each question states exactly what your query must return; include a screenshot or copy-paste of the output alongside each query.

---

## Dataset Setup

Run the script below to set up your working schema. Do not modify the data — questions are calibrated against these exact rows.

```sql
-- ============================================================
-- DATASET: Acme Corp HR & Sales
-- ============================================================

-- 1. Departments
CREATE TABLE departments (
    department_id   INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL,
    location        VARCHAR(50) NOT NULL
);

INSERT INTO departments VALUES
    (1,  'Engineering',  'Austin'),
    (2,  'Marketing',    'New York'),
    (3,  'Sales',        'Chicago'),
    (4,  'HR',           'Austin'),
    (5,  'Legal',        'New York');   -- no employees assigned

-- 2. Employees
CREATE TABLE employees (
    employee_id   INT PRIMARY KEY,
    employee_name VARCHAR(60) NOT NULL,
    department_id INT,                  -- NULL = not yet assigned
    manager_id    INT,                  -- NULL = top of hierarchy
    hire_date     DATE NOT NULL,
    salary        NUMERIC(10,2) NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (manager_id)    REFERENCES employees(employee_id)
);

INSERT INTO employees VALUES
    (1,  'Alice Nguyen',    1, NULL, '2019-03-15', 120000),  -- CTO, no manager
    (2,  'Bob Okafor',      1,    1, '2020-07-01',  95000),
    (3,  'Carol Smith',     1,    1, '2021-01-10',  88000),
    (4,  'David Lee',       2,    NULL, '2018-11-20', 105000), -- CMO, no manager
    (5,  'Eva Patel',       2,    4, '2022-03-05',  72000),
    (6,  'Frank Torres',    3,    NULL, '2017-06-30', 110000), -- VP Sales, no manager
    (7,  'Grace Kim',       3,    6, '2021-09-15',  68000),
    (8,  'Henry Chan',      3,    6, '2022-05-20',  65000),
    (9,  'Iris Johansson',  4,    NULL, '2020-02-14',  90000), -- HR Director
    (10, 'Jake Williams',   NULL, NULL,'2023-08-01',  60000);  -- not yet assigned to a dept

-- 3. Customers
CREATE TABLE customers (
    customer_id   INT PRIMARY KEY,
    customer_name VARCHAR(80) NOT NULL,
    city          VARCHAR(50) NOT NULL
);

INSERT INTO customers VALUES
    (101, 'Pinnacle Tech',    'Austin'),
    (102, 'Bright Solutions', 'New York'),
    (103, 'Oakwood Group',    'Chicago'),
    (104, 'Sunrise Media',    'Austin'),
    (105, 'ClearPath Inc',    'Denver');   -- has never placed an order

-- 4. Orders
CREATE TABLE orders (
    order_id      INT PRIMARY KEY,
    customer_id   INT NOT NULL,
    employee_id   INT NOT NULL,   -- salesperson who handled the order
    order_date    DATE NOT NULL,
    amount        NUMERIC(10,2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

INSERT INTO orders VALUES
    (1001, 101, 7, '2024-01-15',  1500.00),
    (1002, 102, 7, '2024-02-10',   850.00),
    (1003, 103, 8, '2024-01-28',  2200.00),
    (1004, 101, 8, '2024-03-05',   400.00),
    (1005, 104, 7, '2024-03-22',  3100.00),
    (1006, 102, 8, '2024-04-11',  1750.00),
    (1007, 103, 7, '2024-05-03',   620.00),
    (1008, 101, 8, '2023-11-19',  5500.00);  -- pre-2024 order
```

---

## Questions

---

### Q1 — Type: Practical | Difficulty: Easy

**Topic: INNER JOIN**

The Sales team wants a report of all orders alongside the name of the customer who placed each order. Only orders with a valid matching customer record should appear.

Write a query that returns the following columns:

| order_id | customer_name | order_date | amount |
|---|---|---|---|

Sort the results by `order_date` ascending.

**Expected row count:** 8 rows (all orders have a matching customer in this dataset).

**Sample answer:**
```sql
SELECT
    o.order_id,
    c.customer_name,
    o.order_date,
    o.amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
ORDER BY o.order_date;
```

---

### Q2 — Type: Practical | Difficulty: Easy

**Topic: LEFT JOIN**

HR needs a complete employee directory that shows each employee's department name. Employees who have not yet been assigned to a department must still appear in the list, with `department_name` showing as NULL.

Write a query that returns the following columns:

| employee_name | department_name | location |
|---|---|---|

Sort by `department_name` ascending, with unassigned employees at the bottom.

**Expected row count:** 10 rows (Jake Williams appears with NULL department and location).

**Sample answer:**
```sql
SELECT
    e.employee_name,
    d.department_name,
    d.location
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name ASC NULLS LAST;
```

---

### Q3 — Type: Short Answer + Practical | Difficulty: Medium

**Topic: RIGHT JOIN / FULL OUTER JOIN**

**Part A — Short Answer (no code required):**

The query below was written to show all departments and any employees assigned to them, including departments with no employees. A colleague claims it has a bug. Identify the bug and explain in one or two sentences what result it actually produces instead of the intended result.

```sql
SELECT e.employee_name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > 80000;
```

**Sample answer (Part A):**
The `WHERE e.salary > 80000` filter references a column on the left (NULL-padded) side of the RIGHT JOIN. When a department has no employees, `e.salary` is NULL, and `NULL > 80000` evaluates to false, so those departments are silently dropped. The query effectively becomes an INNER JOIN that also filters by salary, producing only employees earning above $80,000 — not all departments. To preserve departments with no employees, the salary filter must move into the ON clause, or be applied as `WHERE e.salary > 80000 OR e.salary IS NULL`.

**Part B — Practical:**

Rewrite the query correctly so that it returns every department (including those with no employees) along with any employees earning above $80,000. Departments with no qualifying employees should still appear with `employee_name` as NULL.

| department_name | employee_name | salary |
|---|---|---|

**Sample answer (Part B):**
```sql
SELECT
    d.department_name,
    e.employee_name,
    e.salary
FROM employees e
RIGHT JOIN departments d
    ON e.department_id = d.department_id
    AND e.salary > 80000
ORDER BY d.department_name;
```

---

### Q4 — Type: Practical | Difficulty: Medium

**Topic: SELF JOIN**

Management wants a report showing the full employee hierarchy: each employee's name and the name of their direct manager. Employees at the top of the hierarchy (those with no manager) must still appear, with `manager_name` showing as NULL.

Write a query that returns the following columns:

| employee_name | manager_name |
|---|---|

Sort by `manager_name` ascending, with top-level employees (NULL manager) listed last.

**Expected row count:** 10 rows.

**Sample answer:**
```sql
SELECT
    e.employee_name,
    m.employee_name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id
ORDER BY m.employee_name ASC NULLS LAST, e.employee_name;
```

---

### Q5 — Type: Practical | Difficulty: Medium

**Topic: LEFT JOIN — Finding Missing Records**

The customer success team wants to know which customers have never placed an order so they can follow up. Return only customers with no order history.

Write a query using a LEFT JOIN (do not use a subquery or NOT IN) that returns:

| customer_id | customer_name | city |
|---|---|---|

**Expected row count:** 1 row (ClearPath Inc).

**Sample answer:**
```sql
SELECT
    c.customer_id,
    c.customer_name,
    c.city
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

---

### Q6 — Type: Practical | Difficulty: Hard

**Topic: Multi-Table JOIN + Aggregation + Date Filtering**

The VP of Sales needs a Q1 2024 (January 1 – March 31) performance summary. The report must list every salesperson in the Sales department (department_id = 3), their total sales amount for Q1 2024, and the number of orders they handled. Salespeople who handled zero orders in Q1 2024 must still appear with totals of 0.

Write a query that returns:

| employee_name | order_count | total_sales |
|---|---|---|

Sort by `total_sales` descending.

**Important:** Place the date filter in the ON clause, not in the WHERE clause. Explain in a comment inside your SQL why this matters.

**Expected rows:** Grace Kim and Henry Chan both appear. At least one should have a non-zero total.

**Sample answer:**
```sql
SELECT
    e.employee_name,
    COUNT(o.order_id)       AS order_count,
    COALESCE(SUM(o.amount), 0) AS total_sales
FROM employees e
-- Date filter in ON clause preserves employees with zero Q1 orders.
-- Moving it to WHERE would silently convert this LEFT JOIN into an INNER JOIN,
-- dropping any salesperson with no Q1 orders.
LEFT JOIN orders o
    ON  e.employee_id = o.employee_id
    AND o.order_date BETWEEN '2024-01-01' AND '2024-03-31'
WHERE e.department_id = 3
GROUP BY e.employee_id, e.employee_name
ORDER BY total_sales DESC;
```

---

### Q7 — Type: Practical | Difficulty: Hard

**Topic: Correlated Subquery → JOIN Rewrite + Performance**

**Part A — Rewrite:**

The following correlated subquery finds customers whose single largest order exceeded $1,000. Rewrite it as a JOIN without using a subquery in the WHERE clause. Your rewrite must produce identical results.

```sql
-- Original (do not modify this)
SELECT c.customer_name
FROM customers c
WHERE (
    SELECT MAX(amount)
    FROM orders o
    WHERE o.customer_id = c.customer_id
) > 1000;
```

**Expected row count:** 3 rows (Pinnacle Tech, Oakwood Group, Sunrise Media).

**Part B — Performance Explanation:**

In two to four sentences, explain why the original correlated subquery can be significantly slower than the JOIN rewrite on a large `orders` table, and name at least one concrete technique (other than the rewrite itself) you would apply to make the JOIN run faster on a production table with millions of rows.

**Sample answer (Part A):**
```sql
SELECT c.customer_name
FROM customers c
INNER JOIN (
    SELECT customer_id, MAX(amount) AS max_order
    FROM orders
    GROUP BY customer_id
) top_orders ON c.customer_id = top_orders.customer_id
WHERE top_orders.max_order > 1000;
```

**Sample answer (Part B):**
The correlated subquery re-executes the inner `SELECT MAX(amount)` once for every row in the `customers` table, resulting in N full scans (or index seeks) of the `orders` table where N is the number of customers. The JOIN rewrite aggregates `orders` a single time and then performs one join operation, which is far cheaper at scale. On a production table, you would add a composite index on `orders(customer_id, amount)` so the database can satisfy the `MAX(amount)` per customer using an index-only scan without touching the full row data. You can verify the improvement by running `EXPLAIN ANALYZE` before and after adding the index and comparing the execution plans.

---

## Submission Instructions

1. Save all seven queries in a single file named `[YourName]-sql-joins.sql` with clearly labelled comments (e.g., `-- Q1`, `-- Q2 Part A`, etc.).
2. For each query, paste the output (as a comment block or screenshot) immediately below the query.
3. For short-answer sections (Q3 Part A, Q7 Part B), write your explanation as a SQL comment (`-- ...`) directly in the file.
4. Upload your `.sql` file to the course portal submission link before the due date. Late submissions will not be accepted without prior approval from the instructor.

---

output_path: /Users/leopham/Documents/Teaching Assistant/assignments/sql-intermediate-joins-take-home.md
