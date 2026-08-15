.headers on
.mode column

-- Top 10 highest paid employees
SELECT 
    Employee_ID,
    Name,
    Department_ID,
    Salary
FROM Employees
ORDER BY Salary DESC
LIMIT 10;

-- Which employee earns more than 70,000
SELECT 
    Employee_ID,
    Name,
    Department_ID,
    Salary
FROM Employees
WHERE Salary > 70000
ORDER BY Salary DESC;

-- Average salary in each department
SELECT
    d.Department_Name,
    COUNT(e.Employee_ID) AS headcount,
    ROUND(AVG(Salary), 2) AS average_salary,
    ROUND(MAX(Salary), 2) AS maximum_salary,
    ROUND(MIN(Salary), 2) AS minimum_salary
FROM Employees e
JOIN Departments d
    ON e.Department_ID = d.Department_ID
GROUP BY d.Department_ID, d.Department_Name
ORDER BY average_salary DESC;

-- Departments have more than 5 employees and an average salary above 50,000 
SELECT
    d.Department_Name,
    COUNT(e.Employee_ID) AS headcount,
    ROUND(AVG(e.Salary), 2) AS average_salary
FROM Employees e
JOIN Departments d
    ON e.Department_ID = d.Department_ID
GROUP BY d.Department_ID, d.Department_Name
HAVING COUNT(e.Employee_ID) > 5
   AND AVG(e.Salary) > 50000
ORDER BY average_salary DESC;

-- Employee's department and total payroll compensation
SELECT 
    e.Employee_ID,
    e.Name,
    d.Department_Name,
    ROUND(SUM(p.Basic_Pay), 2) AS total_basic_salary,
    ROUND(SUM(p.Bonus), 2) AS total_bonus,
    ROUND(SUM(p.Deductions), 2) AS total_deductions,
    ROUND(SUM(p.Net_Pay), 2) AS total_net_salary
FROM Employees e
JOIN Departments d
    ON e.Department_ID = d.Department_ID
JOIN Payroll p
    ON e.Employee_ID = p.Employee_ID
GROUP BY
    e.Employee_ID,
    e.Name,
    d.Department_Name
ORDER BY total_net_salary DESC;

-- Highest paid employees within each department
SELECT 
    e.Name,
    d.Department_Name,
    e.Salary,
    RANK() OVER (
        PARTITION BY e.Department_ID
        ORDER BY e.Salary DESC
    ) AS salary_rank
FROM Employees e
JOIN Departments d
    ON e.Department_ID = d.Department_ID
ORDER BY
    d.Department_Name,
    salary_rank;

-- Employees earning more than the average salary of their own department
WITH department_salary AS (
    SELECT 
        Department_ID,
        AVG(Salary) AS average_salary
    FROM Employees
    GROUP BY Department_ID
)
SELECT 
    e.Employee_ID,
    e.Name,
    d.Department_ID,
    e.Salary
FROM Employees e
JOIN Departments d
    ON e.Department_ID = d.Department_ID
JOIN department_salary ds
    ON e.Department_ID = ds.Department_ID
WHERE e.Salary > ds.average_salary
ORDER BY
    d.Department_Name,
    e.Salary DESC;

-- Employees earning more than the company's overall average salary
SELECT
    Employee_ID,
    Name,
    Salary
FROM Employees
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employees
)
ORDER BY Salary DESC;

-- Attendance rate by employee
SELECT
    e.Employee_ID,
    e.Name,
    COUNT(a.Attendance_ID) AS total_days,
    SUM(
        CASE
            WHEN a.Status = 'Present' THEN 1
            ELSE 0
        END
    ) AS present_days,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN a.Status = 'Present' THEN 1
                ELSE 0
            END
        ) / COUNT(a.Attendance_ID),
        2
    ) AS attendance_rate
FROM Employees e
JOIN Attendance a
    ON e.Employee_ID = a.Employee_ID
GROUP BY
    e.Employee_ID,
    e.Name
ORDER BY attendance_rate ASC;

-- Departments having the highest absence rates
SELECT
    d.Department_Name,
    COUNT(a.Attendance_ID) AS total_attendance_records,
    SUM(
        CASE
            WHEN a.Status = 'Absent' THEN 1
            ELSE 0
        END
    ) AS absent_days,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN a.Status = 'Absent' THEN 1
                ELSE 0
            END
        ) / COUNT(a.Attendance_ID),
        2
    ) AS absence_rate
FROM Employees e
JOIN Departments d
    ON e.Department_ID = d.Department_ID
JOIN Attendance a
    ON e.Employee_ID = a.Employee_ID
GROUP BY
    d.Department_ID,
    d.Department_Name
ORDER BY absence_rate DESC;

-- Monthly payroll trend
SELECT
    Month,
    ROUND(SUM(Basic_Pay), 2) AS total_basic_salary,
    ROUND(SUM(Bonus), 2) AS total_bonus,
    ROUND(SUM(Deductions), 2) AS total_deductions,
    ROUND(SUM(Net_Pay), 2) AS total_net_salary
FROM Payroll
GROUP BY Month
ORDER BY Month;

-- Compared with the previous month
WITH monthly_payroll AS (
    SELECT
        Month,
        SUM(Net_Pay) AS total_net_salary
    FROM Payroll
    GROUP BY Month
)
SELECT
    Month,
    ROUND(total_net_salary, 2) AS total_net_salary,
    ROUND(
        total_net_salary
        - LAG(total_net_salary) OVER (
            ORDER BY Month
        ),
        2
    ) AS payroll_change
FROM monthly_payroll
ORDER BY Month;

-- Headcount reporting to each manager
SELECT
    m.Employee_ID AS manager_id,
    m.Name AS manager_name,
    COUNT(e.Employee_ID) AS direct_reports
FROM Employees m
JOIN Employees e
    ON e.Manager_ID = m.Employee_ID
GROUP BY
    m.Employee_ID,
    m.Name
ORDER BY direct_reports DESC;

-- Department workforce risk indicator based on absence rate
WITH department_attendance AS (
    SELECT
        e.Department_ID,
        COUNT(a.Attendance_ID) AS total_days,
        SUM(
            CASE
                WHEN a.Status = 'Absent' THEN 1
                ELSE 0
            END
        ) AS absent_days
    FROM Employees e
    JOIN Attendance a
        ON e.Employee_ID = a.Employee_ID
    GROUP BY e.Department_ID
)
SELECT
    d.Department_Name,
    da.total_days,
    da.absent_days,
    ROUND(
        100.0 * da.absent_days / da.total_days,
        2
    ) AS absence_rate,
    CASE
        WHEN 100.0 * da.absent_days / da.total_days >= 10
            THEN 'High Risk'
        WHEN 100.0 * da.absent_days / da.total_days >= 5
            THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS workforce_risk
FROM department_attendance da
JOIN Departments d
    ON da.Department_ID = d.Department_ID
ORDER BY absence_rate DESC;