import pandas as pd

# filtering data - selecting rows based on conditions
students = {
    "Name" : ['Rahul', 'Ajay', 'Kriti', 'Ramesh', 'Neha'],
    "Age" : [20, 21, 19, 20, 21],
    "Department": ['Civil', 'Electrical', 'CSE', 'Civil', 'Mechanical'],
    "Marks": [83, 79, 92, 89, 96]

}

df = pd.DataFrame(students)

print('\n===== PART 1: FILTERING DATA =====')
print('===== Single Condition: Students with marks more than 80 =====')
print(df[df['Marks'] > 80])

print('\n===== Multiple Conditions: Students in Civil department with marks greater than 80 =====')
print(df[(df["Department"] == 'Civil') & (df['Marks'] > 80)])

print('\n===== OR Condition: Students in CSE or with marks greater than 80 =====')
print(df[(df['Department'] == 'CSE') | (df['Marks'] > 90)])

print('\n===== NOT Condition: students not in Electrical Department =====')
print(df[~(df['Department'] == 'Electrical')])

print('\n===== isin() ====')
print(df[df['Department'].isin(['CSE', 'Civil'])]) 
# isin() helps to check if those values are there in the collection reducing multiple lines of code.

print('\n===== between() =====')
print(df[df['Marks'].between(80,90)])

print('\n===== String Filtering_1: Students whose name starts with "R" =====')
print(df[df['Name'].str.startswith('R')])

print('\n===== String Filtering_2: Students with "a" in their name =====')
print(df[df['Name'].str.contains('a', case = False)]) 
# case = False , checks by ignoring uppercase/lowercase

print('\n===== Query =====')
print(df.query("Marks > 80 and Age >= 20 and Department == 'Civil'"))
# query() is used for cleaner syntax especially for large operations and reduces the line of the code


print('\n===== PART 2: GroupBy =====')
df.groupby('Marks').count() # count() ignore missing values

print('Number of students:')
print(df.groupby("Department").size()) # size() counts all rows 

mean_marks = df.groupby("Department")["Marks"].mean().sort_values(ascending = False) # gives mean marks of each department in descending order
max_marks = df.groupby("Department")["Marks"].max()
min_marks = df.groupby("Department")["Marks"].min()
total_marks = df.groupby("Department")["Marks"].sum()

# grouping multiple columns
df.groupby("Department")[["Marks", "Age"]].mean()


print('\n===== PART 3: AGGREGATION =====')
print('===== Single Aggregation =====')
print(df['Marks'].median())# similarly for min, mean , sum or max

print('\n===== Multiple Aggregation =====')
print(df["Marks"].agg(["mean","max","min","sum"]))

print('\n===== Group Aggregation =====')
print(df.groupby("Department")["Marks"].agg(
    ["mean","max","min","count"]
))

print('\n===== Custom Aggregation =====') # calculating max and min marks and only mean age
print(df.groupby("Department").agg(
    {"Marks":["mean","max"],
    "Age":"mean"}
    ))

print('\n===== Rename Aggregation =====')
print(df.groupby("Department").agg(
    Average_Marks=("Marks","mean"),
    Highest_Marks=("Marks","max"),
    Average_Age=("Age","mean")
))


print('\n===== PART 4: MERGE & JOIN =====')

names = pd.DataFrame({
        'ID': [1, 2, 3, 4, 5],
        'Name': ['Abheesh', 'Rahul', 'Alex', 'Troy', 'Vijay']
    })

marks = pd.DataFrame({
    'ID': [2, 3, 4, 5],
    'Marks': [85, 68, 76, 95]
})
print('Merge:')
print(pd.merge(names, marks, on = "ID")) # intersection of both ID's , same as inner merge

print('\nLeft Merge:')
print(pd.merge(names, marks, on = "ID", how = 'left')) # keep all ID's in left dataframe only

print('\nRight Merge:')
print(pd.merge(names, marks, on = 'ID', how = 'right')) # keep all ID's in right dataframe only

print('\nOuter Merge: ')
print(pd.merge(names, marks, on = 'ID', how = 'outer')) # keep all ID's from both dataframes

print('\nMerge on different column names:')

new_names = pd.DataFrame({
    'Students_ID': [1,3,5,7],
    'Names': ['A', "AB", 'C', 'D']
})
print(pd.merge(
    new_names,
    names,
    left_on = "Students_ID",
    right_on = "ID"
))

print('===== JOIN =====')
print('Left Join: ') # joins left dataframe with right, similar to left join, keeps all indexes from left dataframe
print(new_names.set_index('Students_ID').join(names)) 
# join() matches indexes. set_index() converts Students_ID into the index so it can match the ID index in the other DataFrame.

print('\nRight Join: ') # keeps all indexes from right dataframe
print(new_names.join(names, how = 'right'))

print('\nInner Join: ') # Joins matching indexes
print(new_names.join(names, how = 'inner'))

print('\nOuter Join: ') # keep every index from both dataframes
print(new_names.join(names, how = 'outer'))

#new_names.join(names, marks) you can join multiple dataframes like this which merge() cannot