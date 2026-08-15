# HR & Employee Payroll Analytics (SQL)

SQL-only analytics project on a simulated 50-employee company database — salaries, payroll, and attendance across 6 departments. Built entirely in SQLite using joins, window functions, CTEs, and aggregation to answer real HR questions.

## Key Finding

Attendance risk scoring across departments (30-day window, 50 employees):

| Department | Total Days | Absent Days | Absence Rate | Risk |
|---|---|---|---|---|
| Marketing | 150 | 16 | 10.67% | High |
| Human Resources | 240 | 25 | 10.42% | High |
| Engineering | 330 | 34 | 10.30% | High |
| Finance | 300 | 28 | 9.33% | Medium |
| Operations | 210 | 19 | 9.05% | Medium |
| Sales | 270 | 23 | 8.52% | Medium |

3 of 6 departments cross the 10% absence threshold flagged as High Risk — Marketing, HR, and Engineering, despite Engineering having the largest headcount and payroll share. This is computed with a CTE-driven risk classifier (`workforce_risk` column), not a static label.

## Schema

4 tables, foreign-key constrained:

- **Departments** — Department_ID, Department_Name, Location
- **Employees** — Employee_ID, Name, Department_ID, Job_Title, Salary, Hire_Date, Manager_ID (self-referencing FK for reporting hierarchy)
- **Attendance** — Attendance_ID, Employee_ID, Date, Status (Present/Absent/Leave)
- **Payroll** — Payroll_ID, Employee_ID, Month, Basic_Pay, Bonus, Deductions, Net_Pay

Data is synthetically generated (`generate_data.py`) with seeded randomness for reproducibility — 50 employees, ~1,500 attendance records, 600 payroll records across 12 months.

## Queries Covered

- Top-paid employees, company-wide and per-department (`RANK() OVER (PARTITION BY ...)`)
- Employees earning above their department average and above company average (correlated subquery + CTE)
- Department-level payroll rollups (basic pay, bonus, deductions, net pay)
- Month-over-month payroll trend using `LAG()`
- Attendance rate per employee and absence rate per department
- Manager span-of-control (direct reports per manager)
- Department workforce risk classification based on absence rate thresholds

Full query set: [`queries.sql`](./queries.sql)
Schema + seed data: [`setup.sql`](./setup.sql)

## Stack

SQLite3, Python (data generation only — no pandas/ORM in the analysis layer, this is pure SQL).

## Run It

```bash
python3 generate_data.py        # builds company.db
sqlite3 company.db < queries.sql
```

## What This Demonstrates

Window functions, CTEs, correlated subqueries, multi-table joins, and threshold-based classification logic — the core SQL patterns used in HR analytics and payroll reporting pipelines.