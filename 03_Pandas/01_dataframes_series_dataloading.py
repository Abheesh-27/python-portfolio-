import pandas as pd
import numpy as np

print('\n==== Series ====') # Series = similar to a NumPy array, but with labels (index).
# from list - default indexing 0,1,2...
series_list = pd.Series([10,20,30])
print(series_list)

# from dictionary - keys become the index
series_dict = pd.Series({
    'a':10,
    'b':20,
    'c':30
})
print(series_dict)

# customised index
series = pd.Series([1,2,3,4], index = ['k','l','m','n'])
print(series)

print('\n==== Data Frames ====') # A DataFrame is a collection of Series sharing the same index.
# from list of lists: specification of columns is important

dframe_list = pd.DataFrame([['Abheesh', 20], ['Archit', 21]], columns = ['Name', 'Age'])
print(dframe_list)

# from dictionary
dframe_dict = pd.DataFrame({
    'Name': ['Ajay', 'Roshan', 'Kashi'],
    'Age': [20, 22, 21]
})
print(dframe_dict)

# from numpy array
dframe_array = pd.DataFrame(np.random.randint(1, 100, (5, 3)), columns = ['x', 'y', 'z'])
print(dframe_array)

# reading and writing files

# df = pd.read_csv('students.csv')
# df = pd.read_excel('students.xlsx')

# df.to_csv('Output.csv', index = False)         [index = False , doesn't give index as an extra column]
# df.to_excel('Output.xlsx', index = False)

# exploring datasets

# df.head()        first 5 rows
# df.tail()        last 5 rows
#df.sample(3)      3 random rows
#df.shape          (rows, columns)
#df.columns        column names
#df.index          row index
#df.dtypes         data type per column
#df.info()         tells you no. of rows & columns , missing values, data types, memory usage;
#                  mostly used before running any new dataset.
# df.describe()    stats (mean, std, min, max, quartiles) for numeric columns only

print('\n==== Example 1 ====')
data = {
    'Name': ['Aditi', 'Rohan', 'Neel', 'Kiran', 'Meera', 'Arjun'],
    'Age': [20, 21, 20, 22, 21, 20],
    'Department': ['CSE', 'Civil', 'CSE', 'Mech', 'Civil', 'CSE'],
    'CGPA': [8.9, 7.2, 9.1, 6.8, 8.5, 7.9],
    'Attendance': [92, 78, 88, 65, 95, 70],
    'Placement_Status': ['Placed', 'Not Placed', 'Placed', 'Not Placed', 'Placed', 'Not Placed']
}

data_frame = pd.DataFrame(data)
print('\nOverall info of the dataframe: ')
data_frame.info()

print('\nStudent with highest CGPA:')
print(data_frame.loc[data_frame['CGPA'].idxmax()]) 
# .loc selects rows using labels.
# .iloc selects rows using integer positions.

print('\nStudent with lowest attendance:')
print(data_frame.loc[data_frame['Attendance'].idxmin()])

print('\nAverage GPA: ', data_frame['CGPA'].mean())

print('\n Students above 8 CGPA: ')
print(data_frame[data_frame['CGPA'] > 8])

print('\nAttendance from highest to lowest: ')
print(data_frame.sort_values('Attendance', ascending = False))

print('\n==== Example 2 ====')

np.random.seed(42) # this gives the exact random values everytime you run the code.
n = 50

new_data = pd.DataFrame({
    'Name': [f'Student_{i}' for i in range(1, n+1)],
    'Age': np.random.randint(18, 25, n),
    'Department': np.random.choice(['CSE', 'Civil', 'Mech', 'EE'], n),
    'CGPA': np.round(np.random.uniform(5.0, 10.0, n), 2),
    'Attendance': np.random.randint(50, 100, n),
})

print('\nOverall info of the dataframe: ')
new_data.info()
print()
print(new_data.describe())

print('\nStudent with highest CGPA:')
print(new_data.loc[new_data['CGPA'].idxmax()]) 

print('\nAverage GPA of each department: ')
avg_gpa = new_data.groupby('Department')['CGPA'].mean()
print(avg_gpa.sort_values()) # lowest to highest
print()