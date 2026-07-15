print('\n ===== Program 1: Create File =====')
 
with open('Students.txt','w') as file:
    file.write('Abheesh\n')
    file.write('Archit\n')
    file.write('Joshi')

print('File Created Successfully!')


print('\n ===== Program 2: Read File =====')
with open('Students.txt','r') as file:
    content = file.read()
    print('Content in the file is:\n',content)


print('\n ===== Program 3: Append File =====')

with open('Students.txt','a') as file:
    file.write('\nRohan')

#to read the file again we need to open the file again and enter read mode
with open("Students.txt","r") as file:
    print('Updated File: ')
    print(file.read())


print('\n ===== Program 4: Count Lines =====')

with open('Students.txt','r') as file:
#readlines() stored the file as a list.
    lines = file.readlines()
print('Total Students = ',len(lines))


print("\n===== Program 5: Search a Student =====")

name = input('Enter student name: ').title()

with open('Students.txt','r') as file:
    students = file.read().splitlines()

    if name in students:
        print('Student Found.')
    else:
        print('Student Not Found!')


print("\n===== Program 6: Add a Student =====")

name = input('Enter name of the student: ')
with open('Students.txt','a') as file:
    file.write('\n' + name)

print('Student Added Successfully.')


print("\n===== Program 7: Read Line by Line =====")

with open('Students.txt','r') as file: 
    for line in file:
        print(line.strip())
#strip() removes extra whitespace and doesnt give blank lines between outputs.
print()



