-- ===== Database Setup =====

-- ===== 1. Drop Existing Table =====
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Departments;


-- ===== 2. Create Tables =====
CREATE TABLE Departments (
    Department_ID INTEGER PRIMARY KEY,
    Department_Name TEXT NOT NULL,
    Location TEXT
);

CREATE TABLE Employees (
    Employee_ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Department_ID INTEGER,
    Manager_ID INTEGER,
    Salary REAL,
    Job_Title TEXT,
    FOREIGN KEY (Department_ID) REFERENCES Departments(Department_ID),
    FOREIGN KEY (Manager_ID) REFERENCES Employees(Employee_ID)
);

CREATE TABLE Projects (
    Project_ID INTEGER PRIMARY KEY,
    Project_Name TEXT NOT NULL,
    Department_ID INTEGER,
    Employee_ID INTEGER,
    Budget REAL,
    FOREIGN KEY (Department_ID) REFERENCES Departments(Department_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employees(Employee_ID)
);


-- ===== 3. Insert Data Into Tables =====
INSERT INTO Departments
    (Department_ID, Department_Name, Location)
VALUES
    (1, 'Engineering', 'Building A'),
    (2, 'Finance', 'Building B'),
    (3, 'Human Resources', 'Building C'),
    (4, 'Marketing', 'Building D'),
    (5, 'Operations', 'Building E'),
    (6, 'Research', 'Building F'),
    (7, 'Legal', 'Building G');

INSERT INTO Employees
    (Employee_ID, Name, Department_ID, Manager_ID, Salary, Job_Title)
VALUES
    (101, 'Alice',   1, NULL, 90000, 'Engineering Manager'),
    (102, 'Bob',     1, 101, 70000, 'Engineer'),
    (103, 'Charlie', 2, NULL, 80000, 'Finance Manager'),
    (104, 'Diana',   3, NULL, 75000, 'HR Manager'),
    (105, 'Ethan',   4, NULL, 72000, 'Marketing Manager'),
    (106, 'Frank',   5, NULL, 78000, 'Operations Manager'),
    (107, 'Grace',   1, 101, 68000, 'Engineer'),
    (108, 'Henry',   NULL, 101, 45000, 'Intern'),
    (109, 'Irene',   2, 103, 65000, 'Analyst'),
    (110, 'Jack',    NULL, NULL, 60000, 'Consultant');

INSERT INTO Projects
    (Project_ID, Project_Name, Department_ID, Employee_ID)
VALUES
    (201, 'Metro Project',       1, 101),
    (202, 'Database Upgrade',   1, 102),
    (203, 'Budget Analysis',    2, 103),
    (204, 'Recruitment Drive',  3, 104),
    (205, 'Marketing Campaign', 4, 105),
    (206, 'Operations Audit',   5, 106),
    (207, 'AI Research',         6, NULL);


-- ===== 4. Verify Data =====
SELECT '===== DEPARTMENTS =====' AS Section;
SELECT *
FROM Departments;
SELECT COUNT(*) FROM Departments;

SELECT '===== EMPLOYEES =====' AS Section;
SELECT *
FROM Employees;
SELECT COUNT(*) FROM Employees;

SELECT '===== PROJECTS =====' AS Section;
SELECT *
FROM Projects;
SELECT COUNT(*) FROM Projects;