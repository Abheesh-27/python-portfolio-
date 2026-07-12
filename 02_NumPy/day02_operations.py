import numpy as np
print('\n===== NumPy Operations =====')

print('\n1. Creating an array and experimenting with operations on it.\n')

arr = np.array([10, 20, 30, 40, 50])

print('Square of each element: ', arr ** 2) # Square of each element
print('Square root of each element: ', np.sqrt(arr)) # Square root of each element
print('Median of the array: ', np.median(arr)) # Median of the array

# Comparison returns a boolean array
print('Elements greater than 30: ', arr > 30) # Elements greater than 30
print('Elements equal to 40: ', arr == 40) # Elements equal to 40
print()


# operations between arrays
print('\n2. Operations between arrays.\n')

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])
addition = a + b
subtraction = a - b
multiplication = a * b
division = b / a
print('Addition: ', addition) # Addition
print('Subtraction: ', subtraction) # Subtraction
print('Multiplication: ', multiplication) # Multiplication
print('Division: ', division) # Division


# boolean masking
print('\n3. Boolean Masking.\n')
print('Elements greater than or equal to 30: ', arr[arr >= 30]) # Elements greater than or equal to 30

c = np.arange(11)
print('Even numbers from 0 to 10: ', c[c % 2 == 0]) # Even numbers from 0 to 10
print('Odd numbers from 0 to 10: ', c[c % 2 != 0]) # Odd numbers from 0 to 10


# broadcasting
print('\n4. Broadcasting.\n')
print('Adding 10 to each element of arr: ', arr + 10) # Adding 10 to each element of arr

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])
# NumPy broadcasts the vector across each row of the matrix before addition.
broadcasted_addition = matrix + vector
print('Matrix + Vector: ') # Matrix + Vector
print(broadcasted_addition)


# aggregate functions
print('\n5. Aggregate Functions.\n')
print('Sum of all elements : ', np.sum(arr)) # Sum of all elements
print('Mean of all elements: ', np.mean(arr)) # Mean of all elements
print('Maximum element     : ', np.max(arr)) # Maximum element
print('Minimum element     : ', np.min(arr)) # Minimum element
print('Standard deviation  : ', np.std(arr)) # Standard deviation
print('Variance            : ', np.var(arr)) # Variance

# axis
print('\n6. Axis.\n')

marks = np.array([ # rows are students and columns are subjects
    [70, 80, 90],
    [60, 75, 95],
    [85, 76, 93]
])

print('Total marks of each student: ', np.sum(marks, axis = 1)) # Total marks of each student
print('Highest marks of each subject: ', np.max(marks, axis = 0)) # Highest marks of each subject
print('Average marks of each subject: ', np.mean(marks, axis = 0)) # Average marks of each subject

# combining boolean masking and aggregate functions
print('\n7. Combining Boolean Masking and Aggregate Functions.\n')
marks_2 = np.array([60, 75, 88, 54, 95])
print('Number of students who scored more than or equal to 75: ', (marks_2 >= 75).sum()) # Number of students who scored more than or equal to 75 in each subject
print('Average marks of students who scored more than or equal to 75: ', marks_2[marks_2 >= 75].mean()) # Average marks of students who scored more than or equal to 75 in each subject
print()