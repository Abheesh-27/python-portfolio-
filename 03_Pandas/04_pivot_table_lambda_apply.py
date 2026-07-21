import pandas as pd

print('\n===== PART 1: APPLY() =====')
df = pd.DataFrame({
    "Name": ['Abheesh', 'Rahul', 'kriti', 'SAMI'],
    "Marks": [87, 94, 76, 38]
})

def calculate_grade(marks):
    if marks >= 90:
        return "Grade A"
    elif marks >= 80:
        return "Grade B"
    elif marks >= 70:
        return "Grade C"
    else:
        return "Grade D"

df["Grade"] = df["Marks"].apply(calculate_grade) # Apply a custom function to each value in the Marks column
print('\nGrades of each student: ')
print(df[["Name", "Marks", "Grade"]])


print('\n===== PART 2: LAMBDA FUNCTIONS =====')

df["Pass"] = df["Marks"].apply( # Use lambda to classify students as Pass or Fail
    lambda x: "Pass" if x >= 40 else "Fail"
)

print('\nPass or Fail: ')
print(df[["Name", "Marks", "Pass"]])

df["Name"] = df["Name"].apply(lambda x: x.title())  # Use lambda with .title() to standardize names
print('\nStandardized Names: ')
print(df["Name"])


print('\n===== PART 3: APPLYING ON DATAFRAME ROWS =====')

df['Result'] = df.apply(
    lambda row: "Pass" if row['Marks'] >= 40 else "Fail",
    axis = 1 # axis 1 = operate row-wise
)            # axis 0 = operate column-wise

print('\nResults: ')
print(df[["Name", "Marks", "Result"]])


print('\n====== EXAMPLE =====')

students = pd.DataFrame({
    'Names': ['Jahnavi', 'Roshan', 'Joshi', 'Archit'],
    'Marks': [86, 75, 54, 38],
    'Attendance': [76, 54, 83, 64]
})

students['Eligible'] = students.apply(
    lambda row: 'Yes'
    if row['Marks'] >= 40 and row['Attendance'] >= 75
    else 'No',
    axis = 1
)

print('\nNumber of students eligible & not: ')
print(students['Eligible'].value_counts())


print('\n===== PART 4: PIVOT TABLES =====')
marks_data = pd.DataFrame({
    "Department": [
        "CSE", "CSE", "Civil",
        "Civil", "Mechanical", "Mechanical"
    ],
    "Gender": [
        "Male", "Female", "Male",
        "Female", "Male", "Female"
    ],
    "Marks": [83, 97, 75, 81, 77, 90]
})

piv_table = pd.pivot_table(
    marks_data,                   # Department         → Rows
    values = "Marks",        # Marks              → Values
    index = "Department",    # Default            → Mean
    aggfunc = "sum"          # aggregate function → Tells how to calculate the marks
)                            # like , sum , max , min, count 

print('\nTotal Makrs by Department: ')
print(piv_table)

piv_col = pd.pivot_table( # pivot with columns
    marks_data,
    values = "Marks",
    columns = "Gender",
    index = "Department",
    aggfunc = "mean"
)

print('\nPivot With Columns: ')
print(piv_col)

mult_agg = pd.pivot_table( # multiple aggregations
    marks_data,
    values = "Marks",
    index = "Department",
    aggfunc = ["mean", "max", "min"]
)
print('\nMultiple Aggregations: ')
print(mult_agg)

marks_data["Attendance"] = [90, 95, 80, 85, 75, 90]
add_attend = pd.pivot_table(
    marks_data,
    values = ["Marks", "Attendance"],
    index = "Department",
    aggfunc = "mean"
)

print('\nAfter adding attendance: ')
print(add_attend)