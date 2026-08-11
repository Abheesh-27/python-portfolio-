-- ===== 1. ORDER BY =====

-- Salaries from lowest to highest
SELECT *
FROM Employees 
ORDER BY Salary; -- similarly, ORDER BY Salary ASC (default) -> ascending

-- Highest salary first 
SELECT *
FROM Employees
ORDER BY Salary DESC; -- -> descending

-- Sort by Employee name i.e alphabetic order
SELECT *
FROM Employees
ORDER BY Name ASC;

-- Sort Employee name by reverse alphabetic order
SELECT *
FROM Employees 
ORDER BY Name DESC;

-- Sort using multiple columns
SELECT *
FROM Employees
ORDER BY Department ASC, Salary DESC; -- First sorts Department, then, within each department, it sorts by Salary.

-- Lowest to highest Salary in sorted department column
SELECT *
FROM Employees
ORDER BY Department ASC, Salary ASC;


-- ===== 2. Aggregate Functions =====

-- Count Employees
SELECT COUNT(*) AS Employee_Count  -- counts number of rows (including null rows)
FROM Employees;

-- COUNT Column
SELECT COUNT(Salary) AS Salary_Count  -- counts non-null salary values
FROM Employees;

-- Total Salary being paid to all employees
SELECT SUM(Salary) AS Total_Salary
FROM Employees;

-- Average Salary of all employees
SELECT AVG(Salary) AS Average_Salary  -- AVG return in decimal form
FROM Employees;

-- Average Salary rounded up-to 2 decimals
SELECT ROUND(AVG(Salary), 2) AS Average_Salary
FROM Employees;

-- Highest Salary 
SELECT MAX(Salary) AS Highest_Salary
FROM Employees;

-- Lowest Salary 
SELECT MIN(Salary) AS Lowest_Salary 
FROM Employees;

-- All together in one querry
SELECT 
    COUNT(*) AS Employee_Count,
    SUM(Salary) AS Total_Salary,
    ROUND(AVG(Salary), 2) AS Average_Salary,
    MAX(Salary) AS Highest_Salary,
    MIN(Salary) AS Lowest_Salary
FROM Employees;


-- ===== 3. Aggregate Functions with WHERE =====

-- Average salary of employees earning more than 60,000
SELECT ROUND(AVG(Salary), 2) AS Average_Salary
FROM Employees
WHERE Salary > 60000;

-- Highest salary above a threshold
SELECT MAX(Salary) AS Highest_Salary
FROM Employees
WHERE Salary > 60000;

-- COUNT employees above a threshold
SELECT COUNT(*) AS Employee_Count
FROM Employees
WHERE Salary > 60000;

-- Sort employees after filtering (Employees earning more than 50,000, highest salary first)
SELECT *
FROM Employees
WHERE Salary > 50000
ORDER BY Salary DESC;

-- Sort only selected columns
SELECT Name, Department , Salary
FROM Employees
ORDER BY Salary DESC;

-- difference between highest and lowest salary
SELECT 
    MAX(Salary) - MIN(Salary) AS Salary_Range
FROM Employees;

-- number of employees and average salary for employees earning more than 45,000
SELECT
    COUNT(*) AS Employee_Count,
    ROUND(AVG(Salary), 2) AS Avgerage_Salary
FROM Employees
WHERE Salary > 45000; 