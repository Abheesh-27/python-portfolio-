PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Payroll;
DROP TABLE IF EXISTS Attendance;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Departments;

-- ===== Creating Tables =====
-- Creating department table
CREATE TABLE Departments (
    Department_ID INTEGER PRIMARY KEY, -- No two departments can have the same ID
    Department_Name TEXT NOT NULL,
    Location TEXT
);

-- Creating Employees table
CREATE TABLE Employees (
    Employee_ID INTEGER PRIMARY KEY, 
    Name TEXT NOT NULL,
    Department_ID INTEGER,
    Job_Title TEXT,
    Salary REAL,
    Hire_Date DATE,
    Manager_ID INTEGER,

    FOREIGN KEY (Department_ID)
        REFERENCES Departments(Department_ID),
    
    FOREIGN KEY (Manager_ID)
        REFERENCES Employees(Employee_ID)
);

-- Creating Attendance table
CREATE TABLE Attendance (
    Attendance_ID INTEGER PRIMARY KEY,
    Employee_ID INTEGER,
    Date DATE,
    Status TEXT CHECK (
        Status IN ('Present', 'Absent', 'Leave') 
    ),
    
    FOREIGN KEY (Employee_ID)
        REFERENCES Employees(Employee_ID)
);

-- Creating Payroll table
CREATE TABLE Payroll (
    Payroll_ID INTEGER PRIMARY KEY,
    Employee_ID INTEGER,
    Month DATE,
    Basic_Pay REAL,
    Bonus REAL,
    Deductions REAL,
    Net_Pay REAL,
    
    FOREIGN KEY (Employee_ID)
        REFERENCES Employees(Employee_ID)
);

-- ===== Inserting Data =====

INSERT INTO Departments
(Department_ID, Department_Name, Location)
VALUES
(1, 'Engineering', 'Bangalore'),
(2, 'Finance', 'Mumbai'),
(3, 'Human Resources', 'Delhi'),
(4, 'Marketing', 'Bangalore'),
(5, 'Operations', 'Chennai'),
(6, 'Sales', 'Hyderabad');