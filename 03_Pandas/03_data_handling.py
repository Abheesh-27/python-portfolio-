import pandas as pd
import numpy as np

# creating a messy dataset 
df = pd.DataFrame({
    'Name': [
        'Rahul',
        'Neha',
        'AJAY',
        np.nan,
        'kriti',
        'Ramesh'
    ],
    
    'Department': [
        'CSE',
        'Civil',
        np.nan,
        'Mechanical',
        ' CSE',
        'civil'
    ],

    'Marks':[ 
        85,
        np.nan,
        92,
        76,
        np.nan,
        88
    ],

    "Joining_Date": [
        "2024-01-15",
        "2024/02/18",
        "15-03-2024",
        None,
        "April 5 2024",
        "2024-06-01"
    ]
})

# detect missing values
print('\n===== PART 1: MISSING DATA =====')
print('===== isnull() =====')
print(df.isnull()) # returns True/False
print('\n', df.isnull().sum()) # total number of missing values in each category
print('\n', df.isnull().sum().sum()) # total missing values in dataset
print('\n', df.isnull().values.any()) # returns true even if there's 1 value missing 

print('\n===== dropna() =====')
print(df.dropna()) # rows contain any NaN disappear
print('\n', df.dropna(axis=1)) # columns having missing values disappear
print('\n', df.dropna(how = "all")) # drop only if all values are missing
print('\n', df.dropna(thresh=3)) # keep rows having at-least 3 non-null values

print('\n===== fillna() =====')
print(df.fillna(0)) # filling empty spaces with constant
print('\n', df.fillna("Unknown")) # filling empty spaces with strings

df["Marks"] = df["Marks"].fillna(0) # fill only 1 column

df = df.fillna({ # fill multiple columns
    "Department": "Unknown",
    "Name": "Not Available"
})

forward_fill = df.ffill() # copies previous value
backward_fill = df.bfill() # copies next value

print('\n', df.replace('civil', 'Civil')) # replacing values
print('\n', df.replace({ # replacing multiple values
    'civil': 'Civil',
    'CSE': 'Computer Science'
}))


print('\n===== PART 2: STRING OPERATIONS =====')

print('Names in Title: ')
print(df['Name'].str.title()) # first letter of each word in caps

print('\nLength of each name: ')
print(df['Name'].str.len()) # length of string

print('\nRemoving extra spaces:')
print(df['Department'].str.strip()) # removes spaces, similarly lstrip() and rstrip()

print('\nReplacing Values: ')
print(df['Department'].str.replace('Civil', 'CE'))

print('\nDepartment names in caps: ')
print(df['Department'].str.upper()) # all letters in caps

print('\nStudents in cse department: ')
print(df["Department"].str.contains("cse", case = False, na = False)) # case = False , doesnt check if its in upper/lowercase.

print('\nNames starting with "R": ')
print(df['Name'].str.startswith('R'))

print('\nNames ending with "h": ')
print(df['Name'].str.endswith('h'))

emails = pd.Series([
    "rahul@gmail.com",
    "ajay@yahoo.com"
])

print('\nSplit: ')
print(emails.str.split("@"))

print('\nAccessing split parts: ')
print(emails.str.split("@").str[0]) # accessing split parts
print(emails.str.split("@").str[1])


print("\n===== PART 3: DATE-TIME HANDLING =====")

df['Joining_Date'] = pd.to_datetime(
    df['Joining_Date'],
    errors='coerce',
    format='mixed'
)

print('\nData Type of each column: ')
print(df.dtypes) # printing datatypes

current_date = pd.Timestamp.today() # current date
print("\nToday's Date: ")
print(current_date)

#similarly
year = df["Joining_Date"].dt.year
month = df["Joining_Date"].dt.month
day = df["Joining_Date"].dt.day
weekday = df["Joining_Date"].dt.day_name()
month_name = df["Joining_Date"].dt.month_name()
quarter = df["Joining_Date"].dt.quarter

print(df["Joining_Date"].dt.is_month_end)
print(df["Joining_Date"].dt.is_month_start)

print('\nSort by Date: ')
print(df.sort_values("Joining_Date"))

today = pd.Timestamp.today()

df["Days_Worked"] = (
    today - df["Joining_Date"]
).dt.days

print('\nNumber of days worked: ')
print(df['Days_Worked'])

print('\nFiltering by date: ')
print(df[df["Joining_Date"] > "2024-03-01"])

print('\nFormating Date: ')
print(df["Joining_Date"].dt.strftime("%d-%m-%Y"))