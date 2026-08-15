# SQL

Six days, zero to CTEs and window functions. Builds up SQL from `SELECT *` to production-grade analytical patterns — joins, subqueries, CTEs, ranking, and time-series window functions.

**Flagship project:** [`day07_HR_Payroll_Analytics/`](./day07_HR_Payroll_Analytics) — a standalone HR & Payroll analytics project applying everything from Days 1–6. 4 tables (Departments, Employees, Attendance, Payroll), 50 employees, ~2,150 rows of synthetic data, 13 analytical queries covering payroll rollups, attendance risk scoring, manager span-of-control, and month-over-month trend analysis via CTEs and window functions. Start there if you're short on time.

## Progression

| Day | File | Covers |
|---|---|---|
| 1 | [`day01_select_basics.sql`](./day01_select_basics.sql) | `SELECT`, `DISTINCT`, `AS`, `LIMIT` |
| 2 | [`day02_where.sql`](./day02_where.sql) | `WHERE`, `AND`/`OR`/`NOT`, `BETWEEN`, `IN`, `LIKE`, `NULL` checks |
| 3 | [`day03_order_by_aggregates.sql`](./day03_order_by_aggregates.sql) | `ORDER BY`, `COUNT`/`SUM`/`AVG`/`MIN`/`MAX` |
| 4 | [`day04_group_by_having.sql`](./day04_group_by_having.sql) | `GROUP BY`, `HAVING`, multi-column grouping |
| 5 | [`day05_joins.sql`](./day05_joins.sql) | `INNER`/`LEFT`/`SELF` joins, 3-table joins |
| 6 | [`day06_advanced_sql.sql`](./day06_advanced_sql.sql) | Subqueries, `EXISTS`, CTEs, `RANK()`/`ROW_NUMBER()`, `LAG()`/`LEAD()`, moving averages |
| 7 | [`day07_HR_Payroll_Analytics/`](./day07_HR_Payroll_Analytics) | Full project — schema design, synthetic data generation, 13-query HR & payroll analysis |

Each `dayNN_*.sql` file is self-contained: run the matching `_setup.sql` (or the setup block at the top of the file) to build the schema, then the queries below it. Day 7 is its own folder with its own README,