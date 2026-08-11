-- ===== GROUP BY =====

-- GROUP BY + AVG() = Average salary by department 
SELECT Department, AVG(Salary) AS Average_Salary
FROM Employees
GROUP BY Department;

--  GROUP BY + COUNT() = Employees per department 
SELECT Department, COUNT(*) AS Employee_Count -- -> COUNT tells us how many rows are there in each group
FROM Employees
GROUP BY Department;

--  GROUP BY + SUM() = Total salary paid by department
SELECT 
    Department, 
    SUM(Salary) AS Total_Salary
FROM Employees
GROUP BY Department;

-- GROUP BY + MIN() = Lowest salary in each department 
SELECT 
    Department,
    MIN(Salary) AS Lowest_Salary
FROM Employees
GROUP BY Department;

-- GROUP BY + MAX() = Highest salary in each department 
SELECT
    Department,
    MAX(Salary) AS Highest_Salary
FROM Employees
GROUP BY Department;

-- Combining multiple aggregate functions 
SELECT
    Department,
    COUNT(*) AS Employee_Count,
    AVG(Salary) AS Average_Salary,
    MIN(Salary)AS Minimum_Salary,
    MAX(Salary) AS Maximum_Salary,
    SUM(Salary) AS Total_Salary
FROM Employees
GROUP BY Department;

-- GROUP BY + ORDER BY = Departments ordered by average salary
SELECT 
    Department, 
    AVG(Salary) AS Average_Salary
FROM Employees
GROUP BY Department 
ORDER BY Average_Salary DESC; -- highest paying department appers first

-- Largest department first
SELECT
    Department,
    COUNT(*) AS Employee_Count
FROM Employees
GROUP BY Department
ORDER BY Employee_Count DESC;

-- Highest total salary first
SELECT 
    Department, 
    SUM(Salary) AS Total_Salary
FROM Employees
GROUP BY Department
ORDER BY Total_Salary DESC;


-- ===== HAVING =====

-- Department with more than 5 employees
SELECT 
    Department, 
    COUNT(*) AS Employee_Count
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 5;

-- Department with less than 2 employees
SELECT 
    Department, 
    COUNT(*) AS Employee_Count
FROM Employees
GROUP BY Department
HAVING COUNT(*) < 2;

-- Departments with average salary more than 60,000
SELECT 
    Department, 
    AVG(Salary) AS Average_Salary
FROM Employees
GROUP BY Department 
HAVING AVG(Salary) > 60000;


-- ===== Multiple GROUP BY columns =====

-- Number of employees by department and job title
SELECT 
    Department,
    Job_Title,
    COUNT(*) AS Employee_Count
FROM Employees
GROUP BY Department, Job_Title;

-- Average salary by department and job title
SELECT 
    Department,
    Job_Title,
    AVG(Salary) AS Average_Salary
FROM Employees
GROUP BY Department, Job_Title
ORDER BY Average_Salary DESC;


-- ===== WHERE + GROUP BY + HAVING =====

-- Average salary of employees earning more than 50,000, department-wise
SELECT
    Department,
    AVG(Salary) AS Average_Salary
FROM Employees
WHERE Salary > 50000
GROUP BY Department;

-- Departments with more than 3 employees earning above 50,000
SELECT 
    Department,
    COUNT(*) AS Employee_Count
FROM Employees
WHERE Salary > 50000
GROUP BY Department
HAVING COUNT(*) > 3;

-- Departments whose average salary is greater than ₹60,000 among employees earning above 40,000
SELECT 
    Department,
    AVG(Salary) AS Average_Salary
FROM Employees
WHERE Salary > 40000
GROUP BY Department
HAVING AVG(Salary) > 60000;


-- ===== WHERE + GROUP BY + HAVING + ORDER BY =====

-- department-level salary report showing:
-- Department, Number of employees, Average salary, Lowest salary, Highest salary, Total salary
-- And departments with at least 3 employees and order by average salary from highest to lowest
SELECT
    Department,
    COUNT(*) AS Employee_Count,
    AVG(Salary) AS Average_Salary,
    MIN(Salary) AS Lowest_Salary,
    MAX(Salary) AS Highest_Salary,
    SUM(Salary) AS Total_Salary
FROM Employees
GROUP BY Department
HAVING COUNT(*) >= 3
ORDER BY Average_Salary DESC;