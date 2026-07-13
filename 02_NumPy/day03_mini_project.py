import numpy as np
print('\n===== Mini Project: Student Marks Analysis =====')

marks = np.array([
    [90,87,94],
    [75,93,79],
    [85,94,90],
    [74,82,74]
])
students = ['Abheesh','Archit','Joshi','Rohan']
student_total = marks.sum(axis = 1)
student_avg = marks.mean(axis = 1)

print('\nMark Sheet: ')
for name, total in zip(students, student_total):
    print(f'{name}: {total} marks')
   
print('\nAverage Marks: ')
for name, avg in zip(students, student_avg):
    print(f'{name}: {avg:.2f} marks')

print('\nHighest Marks of each subject: ')
print(marks.max(axis = 0))

print('\nLowest Marks of each subject: ')
print(marks.min(axis = 0))

print('\nAverage Marks of each subject: ')
print(marks.mean(axis = 0))

print('\nGrades: ')
for name, avg in zip(students, student_avg):

    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f'{name}: {grade}')