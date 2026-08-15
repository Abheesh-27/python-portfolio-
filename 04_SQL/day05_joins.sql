-- ===== INNER JOIN =====

-- Which department does each employee belong to
SELECT
    e.Name,
    d.Department_Name
FROM Employees e
INNER JOIN Departments d
    ON e.Department_ID = d.Department_ID;

-- Employee + department + location
SELECT
    e.Name,
    d.Department_Name,
    d.Location
FROM Employees e
INNER JOIN Departments d
    ON e.Department_ID = d.Department_ID;

-- Employees working in engineering
SELECT 
    e.Employee_ID,
    e.Name,
    d.Department_Name
FROM Employees e
INNER JOIN Departments d
    ON e.Department_ID = d.Department_ID
WHERE d.Department_Name = 'Engineering';

-- Employees earning more than 60,000 with department information
SELECT
    e.Employee_ID,
    e.Name,
    e.Salary,
    d.Department_Name
FROM Employees e
INNER JOIN Departments d
    ON e.Department_ID = d.Department_ID
WHERE e.Salary > 60000;

-- Employees ordered by department along with their job title
SELECT
    e.Name,
    e.Job_Title,
    d.Department_Name
FROM Employees e
INNER JOIN Departments d
    ON e.Department_ID = d.Department_ID
ORDER BY d.Department_Name;


-- ===== LEFT JOIN =====

-- Employees with or without their department names
SELECT
    e.Name,
    d.Department_Name
FROM Employees e
LEFT JOIN Departments d
    ON e.Department_ID = d.Department_ID;

-- Employees without departments
SELECT
    e.Employee_ID,
    e.Name
FROM Employees e
LEFT JOIN Departments d
    ON e.Department_ID = d.Department_ID
WHERE d.Department_Name IS NULL;

-- All employees whose department has a location
SELECT
    e.Name,
    d.Location
FROM Employees e
LEFT JOIN Departments d
    ON e.Department_ID = d.Department_ID
WHERE d.Location IS NOT NULL;

-- ALL Departments + employees
SELECT 
    e.Name,
    d.Department_Name
FROM Departments d
LEFT JOIN Employees e
    ON d.Department_ID = e.Department_ID;

-- Departments without employees
SELECT 
    e.Name,
    d.Department_ID,
    d.Department_Name
FROM Departments d
LEFT JOIN Employees e
    ON d.Department_ID = e.Department_ID
WHERE e.Employee_ID IS NULL;

-- Employees + Projects
SELECT 
    e.Name,
    p.Project_Name
FROM Employees e
LEFT JOIN Projects p
    ON e.Employee_ID = p.Employee_ID;

-- Employees who are not assigned to projects
SELECT 
    e.Employee_ID,
    e.Name
FROM Employees e
LEFT JOIN Projects p
    ON e.Employee_ID = p.Employee_ID
WHERE p.Project_ID IS NULL;


-- ===== SELF JOIN =====

-- Employees with or without manager
SELECT
    e.Name AS Employee,
    m.Name AS Manager
FROM Employees e
LEFT JOIN Employees m
    ON e.Manager_ID = m.Employee_ID;

-- Employees who have managers
SELECT
    e.Name AS Employee,
    m.Name AS Manager
FROM Employees e
INNER JOIN Employees m
    ON e.Manager_ID = m.Employee_ID;

-- Managers + their employees 
SELECT 
    m.Name AS Manager,
    e.Name AS Employee
FROM Employees m
LEFT JOIN Employees e
    ON m.Employee_ID =  e.Manager_ID;

-- Employees reporting to Alice
SELECT
    e.Name AS Employee,
    m.Name AS Manager
FROM Employees e
INNER JOIN Employees m
    ON e.Manager_ID = m.Employee_ID
WHERE m.Name = 'Alice';


-- ===== JOIN All 3 Tables =====

-- employee, their department, their project and the budget
SELECT
    e.Name,
    d.Department_Name,
    p.Project_Name,
    p.Budget
FROM Employees e
INNER JOIN Departments d
    ON e.Department_ID = d.Department_ID
INNER JOIN Projects p
    ON e.Employee_ID = p.Employee_ID;

-- projects whose assigned employee works in Engineering
SELECT
    p.Project_Name,
    d.Department_Name
FROM Projects p
INNER JOIN Employees e
    ON p.Employee_ID = e.Employee_ID
INNER JOIN Departments d
    ON e.Department_ID = d.Department_ID
WHERE d.Department_Name = 'Engineering';

-- Employees working on projects with budget > 100,000
SELECT
    e.Name,
    p.Project_Name,
    p.Budget
FROM Employees e
INNER JOIN Projects p
    ON e.Employee_ID = p.Employee_ID
WHERE p.Budget > 100000;

-- Department and the projects belonging to that department
SELECT
    d.Department_Name,
    p.Project_Name
FROM Departments d
INNER JOIN Employees e
    ON d.Department_ID = e.Department_ID
INNER JOIN Projects p
    ON e.Employee_ID = p.Employee_ID;