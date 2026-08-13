-- ===== Sub Querries =====

-- Employees earning above average
SELECT 
    Name, 
    Salary
FROM Employees 
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employees
);

-- Highest paid employee
SELECT 
    Name,
    Salary
FROM Employees
WHERE Salary = (
    SELECT MAX(Salary)
    FROM Employees 
);

-- Employees earning more than Bob
SELECT 
    Name,
    Salary
FROM Employees
WHERE Salary = (
    SELECT Salary
    FROM Employees
    WHERE Name = 'Bob'
);

-- Second highest salary
SELECT 
    Name,
    Salary
FROM Employees
WHERE Salary = (
    SELECT MAX(Salary)
    FROM Employees
    WHERE Salary < (
        SELECT MAX(Salary)
        FROM Employees
    )
);


-- ===== IN, EXISTS, ANY, ALL =====

-- IN -> is the value contained in the set of value?
-- Employees in Engineering or Finance
SELECT 
    Name,
    Department_ID
FROM Employees
WHERE Department_ID IN (
    SELECT Department_ID 
    FROM Departments
    WHERE Department_Name IN ('Engineering', 'Finance')
);

-- Employees belonging to departments with salaries above 70,000
SELECT
    Name,
    Department_ID
FROM Employees
WHERE Department_ID IN (
    SELECT DISTINCT Department_ID
    FROM Employees
    WHERE Salary > 70000
);

-- EXISTS -> Does at least one matching row exist?
-- departments for which at least one employee exists
SELECT d.Department_Name
FROM Departments d
WHERE EXISTS (
    SELECT 1
    FROM Employees e
    WHERE e.Department_ID = d.Department_ID
);

-- Departments with employees earning above 80,000
SELECT d.Department_Name
FROM Departments d
WHERE EXISTS (
    SELECT 1
    FROM Employees e
    WHERE e.Department_ID = d.Department_ID
      AND e.Salary > 80000
);


-- NOT EXISTS -> Does no matching row exist?
-- Departments with no employees
SELECT d.Department_Name
FROM Departments d
WHERE NOT EXISTS (
    SELECT 1
    FROM Employees e
    WHERE e.Department_ID = d.Department_ID
);

-- ANY -> Compare against atleast one value
-- Salary greater than ANY Engineering salary
SELECT 
    Name,
    Salary
FROM Employees
WHERE Salary > ANY (
    SELECT e.Salary 
    FROM Employees e
    JOIN Departments d
        ON e.Department_ID = d.Department_ID
    WHERE d.Department_Name = 'Engineering'
);

-- ALL -> Compare against every value
-- Salary greater than ALL Engineering salaries
SELECT
    Name,
    Salary
FROM Employees
WHERE Salary > ALL (
    SELECT e.Salary
    FROM Employees e
    JOIN Departments d
        ON e.Department_ID = d.Department_ID
    WHERE d.Department_Name = 'Engineering'
);


-- ===== CTE: Common Table Expression =====

-- Average salary CTE 
WITH average_salary AS (
    SELECT AVG(Salary) AS avg_salary
    FROM Employees
)
SELECT 
    Name,
    Salary
FROM Employees, average_salary
WHERE Salary > avg_salary;

-- Department salary statistics 
WITH department_stats AS (
    SELECT 
        Department_ID,
        AVG(Salary) AS avg_salary,
        MAX(Salary) AS max_salary,
        MIN(Salary) AS min_salary
    FROM Employees
    GROUP BY Department_ID
)
SELECT *
FROM department_stats;

-- Department statistics + names
WITH department_stats AS (
    SELECT
        Department_ID,
        AVG(Salary) AS avg_salary,
        MAX(Salary) AS max_salary,
        MIN(Salary) AS min_salary
    FROM Employees
    GROUP BY Department_ID
)
SELECT
    d.Department_Name,
    ds.avg_salary,
    ds.max_salary
FROM department_stats ds
JOIN Departments d
    ON ds.Department_ID = d.Department_ID;

-- Departments with average salary above 60k
WITH department_stats AS (
    SELECT
        Department_ID,
        AVG(Salary) AS avg_salary
    FROM Employees
    GROUP BY Department_ID
)
SELECT
    d.Department_Name,
    ds.avg_salary
FROM department_stats ds
JOIN Departments d
    ON ds.Department_ID = d.Department_ID
WHERE ds.avg_salary > 60000;

-- Highest salary per department  
WITH department_max AS (
    SELECT
        Department_ID,
        MAX(Salary) AS max_salary
    FROM Employees
    GROUP BY Department_ID
)
SELECT 
    e.Name,
    e.Department_ID,
    e.Salary
FROM Employees e
JOIN department_max dm
    ON e.Department_ID = dm.Department_ID
    AND e.Salary = dm.max_salary;


-- ===== Window Functions =====
-- A normal aggregate collapses rows 
-- But a window function does not collapse rows
-- It calculates something while keeping every employee row

-- Department average beside every employee
SELECT 
    Name, 
    Department_ID,
    Salary, 
    AVG(Salary) OVER( 
        PARTITION BY Department_ID 
    ) AS Department_avg_salary 
FROM Employees; 
-- PARTITION BY -> -- Split the employees into separate groups by department, but dont collapse those groups


-- ===== ROW_NUMBER, RANK, DENSE_RANK =====

-- Row number for all employees -> Gives everyone a unique position
SELECT
    Name,
    Salary,
    ROW_NUMBER() OVER (
        ORDER BY Salary DESC
    ) AS salary_position
FROM Employees;

-- Rank employees -> Give people with the same score the same position and skip numbers
SELECT
    Name,
    Salary,
    RANK() OVER (
        ORDER BY Salary DESC
    ) AS salary_rank
FROM Employees;

-- Dense rank employees -> Give people with the same score the same position without skipping numbers
SELECT
    Name,
    Salary,
    DENSE_RANK() OVER (
        ORDER BY Salary DESC
    ) AS salary_rank
FROM Employees;

-- Rank employees within each department
SELECT 
    Name,
    Department_ID,
    Salary,
    RANK() OVER (
        PARTITION BY Department_ID
        ORDER BY Salary DESC
    ) AS department_rank -- each department starts at rank 1
FROM Employees

-- Top salary per department
WITH ranked_employees AS(
    SELECT 
        Name,
        Department_ID,
        Salary,
        RANK() OVER (
            PARTITION BY Department_ID
            ORDER BY Salary DESC
        ) AS salary_rank 
    FROM Employees
)
SELECT
    Name,
    Department_ID,
    Salary
FROM ranked_employees
WHERE salary_rank = 1;

-- Top 3 employees per department
WITH ranked_employees AS(
    SELECT 
        Name,
        Department_ID,
        Salary,
        ROW_NUMBER() OVER (
            PARTITION BY Department_ID
            ORDER BY Salary DESC
        ) AS salary_rank 
    FROM Employees
)
SELECT
    Name,
    Department_ID,
    Salary,
    salary_rank
FROM ranked_employees
WHERE salary_rank <= 3;


-- ===== LAG() & LEAD() =====
-- LAG() -> Compare with previous row
-- LEAD() -> Compare with next row

-- Previous employee salary
SELECT
    Name,
    Salary,
    LAG(Salary) OVER (
        ORDER BY Salary
    ) AS previous_salary
FROM Employees;

-- Next employee salary
SELECT
    Name,
    Salary,
    LEAD(Salary) OVER (
        ORDER BY Salary
    ) AS next_salary
FROM Employees;

-- Salary difference from previous employee
SELECT 
    Name, 
    Salary,
    LAG(Salary) OVER (
        ORDER BY Salary
    ) AS previous_salary,
    Salary - LAG(salary) OVER (
        ORDER BY Salary
    ) AS salary_difference
FROM Employees;


-- ===== Sales Querries =====
-- Running total
SELECT
    Sale_Date,
    Amount,
    SUM(Amount) OVER (
        ORDER BY Sale_Date
    ) AS running_total
FROM Sales;

-- Monthly sales
WITH monthly_sales AS (
    SELECT
        strftime('%Y-%m', Sale_Date) AS month,
        SUM(Amount) AS sales
    FROM Sales
    GROUP BY month
)
SELECT
    month,
    sales,
    LAG(sales) OVER (
        ORDER BY month
    ) AS previous_month_sales
FROM monthly_sales;

-- Month-over-month change
WITH monthly_sales AS (
    SELECT
        strftime('%Y-%m', Sale_Date) AS month,
        SUM(Amount) AS sales
    FROM Sales
    GROUP BY month
)
SELECT
    month,
    sales,
    LAG(sales) OVER (
        ORDER BY month
    ) AS previous_month_sales,
    sales - LAG(sales) OVER (
        ORDER BY month
    ) AS sales_change
FROM monthly_sales;

-- Moving average
WITH monthly_sales AS (
    SELECT
        strftime('%Y-%m', Sale_Date) AS month,
        SUM(Amount) AS sales
    FROM Sales
    GROUP BY month
)
SELECT
    month,
    sales,
    AVG(sales) OVER (
        ORDER BY month
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW 
    ) AS moving_average
FROM monthly_sales;