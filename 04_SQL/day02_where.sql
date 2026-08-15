-- ===== 1. Basic WHERE =====

-- Employees with Salary > 70000
SELECT *
FROM Employees
WHERE Salary > 70000 ;

-- Employees in Sales
SELECT *
FROM Employees
WHERE Department = 'Sales' ;

-- Employees younger than 30 years
SELECT * 
FROM Employees 
WHERE Age < 30 ;

-- Employees from Hyderabad
SELECT * 
FROM Employees 
WHERE City = 'Hyderabad' ;

-- Employees earning atleast 80,000
SELECT *
FROM Employees
WHERE Salary >= 80000 ;


-- ===== 2. AND Operator =====

-- Sales employees earning more than 60,000
SELECT * 
FROM Employees
WHERE Department = 'Sales'
AND Salary > 60000 ;

-- IT employees older than 30 years
SELECT *
FROM Employees 
WHERE Department = 'IT'
AND Age > 30 ;

-- Employees from Mumbai earning more than 50,000
SELECT *
FROM Employees
WHERE City = 'Mumbai'
AND Salary > 50000 ;

-- Finance employees younger than 32 years
SELECT *
FROM Employees
WHERE Department = 'Finance'
AND Age < 32 ;

-- Employees from Bangalore earning atleast 55,000
SELECT * 
FROM Employees 
WHERE City = 'Bangalore'
AND Salary >= 55000 ;


-- ===== 3. OR Operator =====

-- Employees from Hyderabad or Chennai
SELECT *
FROM Employees 
WHERE City = 'Hyderabad' 
OR City = 'Chennai' ;

-- Employees from IT or Software
SELECT *
FROM Employees
WHERE Department = 'IT'
OR Department = 'Software' ;

-- Employees earning below 40,000 or above 90,000
SELECT *
FROM Employees
WHERE Salary < 40000
OR Salary > 90000 ;

-- Employees younger than 25 or older than 35
SELECT *
FROM Employees 
WHERE Age < 25
OR Age > 35 ;


-- ===== 4. NOT Operator =====

-- Employees not in IT
SELECT * 
FROM Employees 
WHERE NOT Department = 'Sales' ;     -- or WHERE Department != 'Sales';

-- Employees who are not from Chennai
SELECT * 
FROM Employees 
WHERE City != 'Chennai' ;

-- Employees Whose salary is not 60,000
SELECT *
FROM Employees 
WHERE Salary != 60000 ;


-- ===== 5. BETWEEN Operator =====

-- Salary between 60,000 & 80,000
SELECT *
FROM Employees 
WHERE Salary BETWEEN 60000 AND 70000 ;

-- Age between 25 & 30
SELECT *
FROM Employees 
WHERE Age BETWEEN 25 AND 30 ;

-- Employees IDs between 15 & 20
SELECT *
FROM Employees
WHERE Employee_ID BETWEEN 15 AND 20 ;


-- ===== 5. IN Operator =====

-- Employees from Bangalore, Hyderabad or Delhi
SELECT *
FROM Employees
WHERE City IN ('Bangalore', 'Hyderabad', 'Delhi') ;

-- Employees from IT, Finance or Marketing
SELECT *
FROM Employees
WHERE Department IN ('IT', 'Finance', 'Marketing') ;

-- Employees aged 30, 35 or 40
SELECT *
FROM Employees 
WHERE Age IN (30, 35, 40) ;


-- ===== 6. LIKE Operator =====

-- Names starting with "P"
SELECT *
FROM Employees 
WHERE Name LIKE 'P%' ;

-- Names ending with "a"
SELECT * 
FROM Employees 
WHERE Name LIKE '%a' ;

-- Names containg "ar"
SELECT *
FROM Employees
WHERE Name LIKE '%ar%' ;


-- ===== 7. NULL Operator =====

-- Employees without a Department
SELECT *
FROM Employees 
WHERE Department IS NULL ;

-- Employees who have a Department
SELECT *
FROM Employees 
WHERE Department IS NOT NULL ;


-- ===== QUERRIES =====

-- IT Employees earning between 65,000 & 80,000
SELECT *
FROM Employees
WHERE Department = 'IT' 
AND Salary BETWEEN 65000 AND 80000 ;

-- Employees from Hyderbad or Chennai earning more than 70,000
SELECT *
FROM Employees 
WHERE City IN ('Hyderabad', 'Chennai')
AND Salary > 70000 ;

-- Employees who are not in HR Or Sales
SELECT *
FROM Employees
WHERE Department NOT IN ('HR', 'Sales') ;

-- Employees names start with A or J
SELECT *
FROM Employees 
WHERE Name LIKE 'A%' 
OR Name LIKE 'J%' ; 

-- Employees without a Department earning more than 45,000
SELECT *
FROM Employees
WHERE Department IS NULL
AND Salary > 45000 ;