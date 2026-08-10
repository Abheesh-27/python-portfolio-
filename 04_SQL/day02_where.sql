-- Basic Where
SELECT '===== 1. BASIC WHERE =====' AS SECTION;

SELECT 'Employees with Salary > 70000' AS SECTION;
SELECT *
FROM Employees
WHERE Salary > 70000 ;

SELECT 'Employees in Sales' AS SECTION;
SELECT *
FROM Employees
WHERE Department = 'Sales' ;

SELECT 'Employees younger than 30 years' AS SECTION;
SELECT * 
FROM Employees 
WHERE Age < 30 ;

SELECT 'Employees from Hyderabad' AS SECTION;
SELECT * 
FROM Employees 
WHERE City = 'Hyderabad' ;

SELECT 'Employees earning atleast 80,000' AS SECTION;
SELECT *
FROM Employees
WHERE Salary >= 80000 ;


SELECT '===== 2. AND Operator =====' AS SECTION;

SELECT 'Sales employees earning more than 60,000' AS SECTION;
SELECT * 
FROM Employees
WHERE Department = 'Sales'
AND Salary > 60000 ;

SELECT 'IT employees older than 30 years' AS SECTION;
SELECT *
FROM Employees 
WHERE Department = 'IT'
AND Age > 30 ;

SELECT 'Employees from Mumbai earning more than 50,000' AS SECTION;
SELECT *
FROM Employees
WHERE City = 'Mumbai'
AND Salary > 50000 ;

SELECT 'Finance employees younger than 32 years' AS SECTION;
SELECT *
FROM Employees
WHERE Department = 'Finance'
AND Age < 32 ;

SELECT 'Emplyees from Bangalore earning atleast 55,000' AS SECTION;
SELECT * 
FROM Employees 
WHERE City = 'Bangalore'
AND Salary >= 55000 ;


SELECT '===== 3. OR Operator =====' AS SECTION;

SELECT 'Employees from Hyderabad or Chennai' AS SECTION;
SELECT *
FROM Employees 
WHERE City = 'Hyderabad' 
OR City = 'Chennai' ;

SELECT 'Employees from IT or Software' AS SECTION;
SELECT *
FROM Employees
WHERE Department = 'IT'
OR Department = 'Software' ;

SELECT 'Employees earning below 40,000 or above 90,000' AS SECTION;
SELECT *
FROM Employees
WHERE Salary < 40000
OR Salary > 90000 ;

SELECT 'Employees younger than 25 or older than 35' AS SECTION;
SELECT *
FROM Employees 
WHERE Age < 25
OR Age > 35 ;


SELECT '===== 4. NOT Operator =====' AS SECTION;

SELECT 'Employees not in IT' AS SECTION;
SELECT * 
FROM Employees 
WHERE NOT Department = 'Sales' ;     -- or WHERE Department != 'Sales';

SELECT 'Employees who are not from Chennai' AS SECTION;
SELECT * 
FROM Employees 
WHERE City != 'Chennai' ;

SELECT 'Employees Whose salary is not 60,000' AS SECTION;
SELECT *
FROM Employees 
WHERE Salary != 60000 ;


SELECT '===== 5. BETWEEN Operator =====' AS SECTION;

SELECT 'Salary between 60,000 & 80,000' AS SECTION;
SELECT *
FROM Employees 
WHERE Salary BETWEEN 60000 AND 70000 ;

SELECT 'Age between 25 & 30' AS SECTION;
SELECT *
FROM Employees 
WHERE Age BETWEEN 25 AND 30 ;

SELECT 'Employees IDs between 15 & 20' AS SECTION;
SELECT *
FROM Employees
WHERE Employee_ID BETWEEN 15 AND 20 ;


SELECT '===== 5. IN Operator =====' AS SECTION;

SELECT 'Employees from Bangalore, Hyderabad or Delhi' AS SECTION;
SELECT *
FROM Employees
WHERE City IN ('Bangalore', 'Hyderabad', 'Delhi') ;

SELECT 'Employees from IT, Finance or Marketing' AS SECTION;
SELECT *
FROM Employees
WHERE Department IN ('IT', 'Finance', 'Marketing') ;

SELECT 'Employees aged 30, 35 or 40' AS SECTION; 
SELECT *
FROM Employees 
WHERE Age IN (30, 35, 40) ;


SELECT '===== 6. LIKE Operator =====' AS SECTION;

SELECT 'Names starting with "P"' AS SECTION;
SELECT *
FROM Employees 
WHERE Name LIKE 'P%' ;

SELECT 'Names ending with "a"' AS SECTION;
SELECT * 
FROM Employees 
WHERE Name LIKE '%a' ;

SELECT 'Names containg "ar"' AS SECTION;
SELECT *
FROM Employees
WHERE Name LIKE '%ar%' ;


SELECT '===== 7. NULL Operator =====' AS SECTION;

SELECT 'Employees without a Department' AS SECTION;
SELECT *
FROM Employees 
WHERE Department IS NULL ;

SELECT 'Employees who have a Department' AS SECTION;
SELECT *
FROM Employees 
WHERE Email IS NOT NULL ;


SELECT '===== QUERRIES =====' AS SECTION;

SELECT 'IT Employees earning between 65,000 & 80,000' AS SECTION;
SELECT *
FROM Employees
WHERE Department = 'IT' 
AND Salary BETWEEN 65000 AND 80000 ;

SELECT 'Employees from Hyderbad or Chennai earning more than 70,000' AS SECTION;
SELECT *
FROM Employees 
WHERE City IN ('Hyderabad', 'Chennai')
AND Salary > 70000 ;

SELECT 'Employees who are not in HR Or Sales' AS SECTION;
SELECT *
FROM Employees
WHERE Department NOT IN ('HR', 'Sales') ;

SELECT 'Employees names start with A or J' AS SECTION;
SELECT *
FROM Employees 
WHERE Name LIKE 'A%' 
OR Name LIKE 'J%' ; 

SELECT 'Employees without a Department earning more than 45,000' AS SECTION;
SELECT *
FROM Employees
WHERE Department IS NULL
AND Salary > 45000 ;