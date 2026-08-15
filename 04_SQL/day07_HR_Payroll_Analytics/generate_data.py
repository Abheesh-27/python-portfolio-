import sqlite3
import random
from datetime import date, timedelta
from pathlib import Path

# ===== Configuration ======
NUM_EMPLOYEES = 50

BASE_DIR = Path(__file__).parent
DATABASE = BASE_DIR / 'company.db'
SETUP_FILE = BASE_DIR / 'setup.sql'

random.seed(42) # makes the random generation repeatable


# ===== Sample Data ===== 
first_names = [
    "Arjun", "Rahul", "Priya", "Ananya", "Vikram",
    "Neha", "Rohan", "Sneha", "Karan", "Meera",
    "Amit", "Kavya", "Aditya", "Ishita", "Nikhil",
    "Pooja", "Varun", "Divya", "Sanjay", "Riya",
    "Aarav", "Shreya", "Manish", "Tanvi", "Akash"
]

last_names = [
    "Sharma", "Patel", "Kumar", "Reddy", "Iyer",
    "Nair", "Singh", "Mehta", "Gupta", "Rao",
    "Verma", "Joshi", "Desai", "Malhotra", "Kapoor"
]

# Job titles by department
job_titles = {
    1: [
        "Software Engineer",
        "Data Analyst",
        "Senior Software Engineer",
        "Technical Lead"
    ],

    2: [
        "Financial Analyst",
        "Accountant",
        "Finance Manager",
        "Senior Financial Analyst"
    ],

    3: [
        "HR Executive",
        "HR Analyst",
        "HR Manager",
        "Recruitment Specialist"
    ],

    4: [
        "Marketing Executive",
        "Marketing Analyst",
        "Marketing Manager",
        "Content Specialist"
    ],

    5: [
        "Operations Executive",
        "Operations Analyst",
        "Operations Manager",
        "Process Specialist"
    ],

    6: [
        "Sales Executive",
        "Sales Analyst",
        "Sales Manager",
        "Business Development Executive"
    ]
}

# Salary ranges by department
salary_ranges = {
    1: (55000, 120000),   # Engineering
    2: (45000, 100000),   # Finance
    3: (40000, 90000),    # HR
    4: (40000, 95000),    # Marketing
    5: (45000, 95000),    # Operations
    6: (40000, 100000)    # Sales
}


# ===== Create Database =====
# Remove old database so the script can be
# safely executed again without duplicate data.

if DATABASE.exists():
    DATABASE.unlink()

connection = sqlite3.connect(DATABASE)

# Enable foreign key constraints
connection.execute("PRAGMA foreign_keys = ON")

cursor = connection.cursor()


# ===== Create tables =====

with open(SETUP_FILE, "r", encoding="utf-8") as file:
    setup_sql = file.read()

cursor.executescript(setup_sql)

# Generate employees
employees = []

start_date = date(2018, 1, 1)
end_date = date(2025, 1, 1)
payroll_year = end_date.year

for employee_id in range(1, NUM_EMPLOYEES + 1):

    name = (
        random.choice(first_names)
        + " "
        + random.choice(last_names)
    )

    department_id = random.randint(1, 6)

    job_title = random.choice(
        job_titles[department_id]
    )

    salary = random.randint(
        salary_ranges[department_id][0],
        salary_ranges[department_id][1]
    )

    random_days = random.randint(
        0,
        (end_date - start_date).days
    )

    hire_date = start_date + timedelta(
        days=random_days
    )

    # Manager_ID is initially NULL.
    # Managers are assigned only after
    # all employees have been inserted.
    manager_id = None

    employee = {
        "Employee_ID": employee_id,
        "Name": name,
        "Department_ID": department_id,
        "Job_Title": job_title,
        "Salary": salary,
        "Hire_Date": hire_date.isoformat(),
        "Manager_ID": manager_id
    }

    employees.append(employee)

# Insert employees
for employee in employees:

    cursor.execute(
        """
        INSERT INTO Employees
        (
            Employee_ID,
            Name,
            Department_ID,
            Job_Title,
            Salary,
            Hire_Date,
            Manager_ID
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            employee["Employee_ID"],
            employee["Name"],
            employee["Department_ID"],
            employee["Job_Title"],
            employee["Salary"],
            employee["Hire_Date"],
            employee["Manager_ID"]
        )
    )

# Assign managers 
for employee in employees:

    # Only employees with a lower Employee_ID
    # can become managers.
    #
    # This guarantees that the manager already
    # exists in the Employees table.

    possible_managers = [
        e for e in employees
        if e["Department_ID"] == employee["Department_ID"]
        and e["Employee_ID"] < employee["Employee_ID"]
    ]

    if possible_managers:

        manager = random.choice(possible_managers)

        cursor.execute(
            """
            UPDATE Employees
            SET Manager_ID = ?
            WHERE Employee_ID = ?
            """,
            (
                manager["Employee_ID"],
                employee["Employee_ID"]
            )
        )

# Generate attendance
attendance_id = 1

today = date.today()

for employee in employees:

    for days_ago in range(30):

        attendance_date = today - timedelta(
            days=days_ago
        )

        status = random.choices(
            ["Present", "Absent", "Leave"],
            weights=[0.85, 0.10, 0.05]
        )[0]

        cursor.execute(
            """
            INSERT INTO Attendance
            (
                Attendance_ID,
                Employee_ID,
                Date,
                Status
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                attendance_id,
                employee["Employee_ID"],
                attendance_date.isoformat(),
                status
            )
        )

        attendance_id += 1

# Generate payroll
payroll_id = 1

for employee in employees:

    monthly_basic_pay = employee["Salary"] / 12

    for month in range(1, 13):

        month_date = date(payroll_year, month, 1)

        bonus = monthly_basic_pay * random.uniform(
            0.00, 0.15
        )

        deductions = monthly_basic_pay * random.uniform(
            0.05, 0.12
        )

        net_pay = (
            monthly_basic_pay
            + bonus
            - deductions
        )

        cursor.execute(
            """
            INSERT INTO Payroll
            (
                Payroll_ID,
                Employee_ID,
                Month,
                Basic_Pay,
                Bonus,
                Deductions,
                Net_Pay
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                payroll_id,
                employee["Employee_ID"],
                month_date.isoformat(),
                round(monthly_basic_pay, 2),
                round(bonus, 2),
                round(deductions, 2),
                round(net_pay, 2)
            )
        )

        payroll_id += 1

# Save changes
connection.commit()

# Verify data
employee_count = cursor.execute(
    "SELECT COUNT(*) FROM Employees"
).fetchone()[0]

attendance_count = cursor.execute(
    "SELECT COUNT(*) FROM Attendance"
).fetchone()[0]

payroll_count = cursor.execute(
    "SELECT COUNT(*) FROM Payroll"
).fetchone()[0]


print("===== Data generation completed successfully! =====")

print(f"Employees generated: {employee_count}")
print(f"Attendance records:  {attendance_count}")
print(f"Payroll records:     {payroll_count}")
print()
print(f"Database created:")
print(DATABASE)

connection.close()