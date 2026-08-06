-- Show all employees
SELECT '===== ALL Employees =====' AS Section;
SELECT *
FROM Employees;

-- Show employee names
SELECT '===== Employee Names =====' AS Section;
SELECT Name
FROM Employees;

-- Show employee salaries
SELECT '===== Employee Salaries =====' AS Section;
SELECT Salary
FROM Employees;

-- Show employee departments
SELECT '===== Employee Department =====' AS Section;
SELECT Department
FROM Employees;

-- Show employee job titles
SELECT '===== Employee Job Title =====' AS Section;
SELECT Job_Title
FROM Employees;

-- Show employee cities
SELECT '===== Employee Cities =====' AS Section;
SELECT City
FROM Employees;

-- Show employee experience
SELECT '===== Employee Experience =====' AS Section;
SELECT Experience
FROM Employees;

-- Show employee names and salaries
SELECT '===== Employee Names & Salaries =====' AS Section;
SELECT Name, Salary
FROM Employees;

-- Show employee names and departments
SELECT '===== Employee Names & Departments =====' AS Section;
SELECT Name, Department
FROM Employees;

-- Show employee names, cities, and salaries
SELECT '===== Employee Names, Cities & Salaries =====' AS Section;
SELECT Name, City, Salary
FROM Employees;

-- Show unique departments
SELECT '===== Unique Departments =====' AS Section;
SELECT DISTINCT Department
FROM Employees;

-- Show unique cities
SELECT '===== Unique Cities =====' AS Section;
SELECT DISTINCT City
FROM Employees;

-- Show unique job titles
SELECT '===== Unique Job Titles =====' AS Section;
SELECT DISTINCT Job_Title
FROM Employees;

-- Rename Salary column as MonthlySalary
SELECT '===== Rename Salary Column =====' AS Section;
SELECT Salary AS Monthly_Salary
FROM Employees;

-- Rename Department column as Team
SELECT '===== Rename Department Column =====' AS Section;
SELECT Department AS Team
FROM Employees;

-- Rename Job_Title column as Position
SELECT '===== Rename Job_Title Column =====' AS Section;
SELECT Job_Title AS Position
FROM Employees;

-- Show the first 5 employees
SELECT '===== Show First 5 Employees =====' AS Section;
SELECT *
FROM Employees
LIMIT 5;

-- Show the first 10 employee names
SELECT '===== Show First 10 Employees =====' AS Section;
SELECT Name
FROM Employees
LIMIT 10;

-- Show the first 3 salaries
SELECT '===== Show First 2 Salaries =====' AS Section;
SELECT Salary
FROM Employees
LIMIT 3;

-- Show Employee ID, Name and Salary
SELECT '===== Show Employee ID, Name & Salary =====' AS Section;
SELECT Employee_ID, Name, Salary
FROM Employees;