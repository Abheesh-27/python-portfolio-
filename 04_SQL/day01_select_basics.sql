-- Show all employees
SELECT *
FROM Employees;

-- Show employee names
SELECT Name
FROM Employees;

-- Show employee salaries
SELECT Salary
FROM Employees;

-- Show employee departments
SELECT Department
FROM Employees;

-- Show employee job titles
SELECT Job_Title
FROM Employees;

-- Show employee cities
SELECT City
FROM Employees;

-- Show employee experience
SELECT Experience
FROM Employees;

-- Show employee names and salaries
SELECT Name, Salary
FROM Employees;

-- Show employee names and departments
SELECT Name, Department
FROM Employees;

-- Show employee names, cities, and salaries
SELECT Name, City, Salary
FROM Employees;

-- Show unique departments
SELECT DISTINCT Department
FROM Employees;

-- Show unique cities
SELECT DISTINCT City
FROM Employees;

-- Show unique job titles
SELECT DISTINCT Job_Title
FROM Employees;

-- Rename Salary column as MonthlySalary
SELECT Salary AS Monthly_Salary
FROM Employees;

-- Rename Department column as Team
SELECT Department AS Team
FROM Employees;

-- Rename Job_Title column as Position
SELECT Job_Title AS Position
FROM Employees;

-- Show the first 5 employees
SELECT *
FROM Employees
LIMIT 5;

-- Show the first 10 employee names
SELECT Name
FROM Employees
LIMIT 10;

-- Show the first 3 salaries
SELECT Salary
FROM Employees
LIMIT 3;

-- Show Employee ID, Name and Salary
SELECT Employee_ID, Name, Salary
FROM Employees;