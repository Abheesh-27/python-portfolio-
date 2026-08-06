company.db

CREATE TABLE Employees(
    Employee_ID INTEGER PRIMARY KEY,

    Name TEXT,

    Age INTEGER,

    Department TEXT,

    Job_Title TEXT,

    Salary INTEGER,

    City TEXT,

    Experience INTEGER

);

INSERT INTO Employees VALUES
(1, 'Ajay', 25, 'HR', 'HR Executive', 42000, 'Chennai', 2),

(2, 'Bob', 31, 'Finance', 'Financial Analyst', 68000, 'Mumbai', 7),

(3, 'Charith', 28, 'IT', 'Software Engineer', 72000, 'Bangalore', 5),

(4, 'David', 23, 'Sales', 'Manager', 54000, 'Hyderabad', 0),

(5, 'Elvish', 38, 'Operations', 'Site Engineer', 80000, 'Pune', 9),

(6, 'Farhan', 35, 'IT', 'Software Developer', 75000, 'Mumbai', 3),

(7, 'Gagan', 40, 'Finance', 'Financial Executive', )