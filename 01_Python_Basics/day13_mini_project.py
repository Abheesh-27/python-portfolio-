print('\n===== Student Management System =====')

class Student:

    def __init__(self, roll_number , name , age , department):
        self.roll = roll_number
        self.name = name
        self.age = age
        self.department = department

    def display(self):
        print('-' * 30) #looks more organised.
        print('Roll Number     : ', self.roll)
        print('Name of student : ', self.name)
        print('Age             : ', self.age)
        print('Department      : ', self.department)
    
students = []

def display_students():
    if not students:
        print("No students available.")
        return

    for student in students:
        student.display()
        print()


def add_student():
    while True:
       student_roll = input("Enter Roll Number: ").strip().upper()

       if student_roll == "":
         print("Roll cannot be empty.")
       else:
          break
       
    while True:
       student_name = input("Enter Student Name: ").strip().title()

       if student_name.replace(" ", "").isalpha():
          break

       print("Enter a valid name!")

    while True:
       try:
          student_age = int(input('Enter age of the student: '))
          if student_age <=0:
              print('\nAge Must be Greater than Zero!\n')
              continue
          break
       except ValueError:
           print('\nEnter numbers only!')

    while True:
        student_department = input('Enter department: ').strip().title()

        if student_department.replace(' ','').isalpha():
            break
        print('Enter a Valid Department!')

    if any(student.roll == student_roll for student in students):
        print('\nRoll number already exists!')
    else:
        student = Student(student_roll, student_name, student_age, student_department)
        students.append(student)
        print('\nStudent Added Successfully!')

def delete_student():
    student_roll = input('Enter Roll Number to delete: ').upper()

    for i, student in enumerate(students):
        if student.roll == student_roll:
            del students[i]
            print('\nStudent Deleted Successfully!')
            return

    print("\nRoll number doesn't exist!")

def update_student():
    while True:
        print('a. Update Roll Number')
        print('b. Update Name')
        print('c. Update Age')
        print('d. Update Department')
        print('e. Back')
   
        update = input('\nWhat do you want to update?: ')
        
        if update == 'a':
            old_roll_number = input('Enter old roll number: ').upper()
            new_roll_number = input('Enter new roll number: ').upper()

            if any(student.roll == new_roll_number for student in students):
                 print("\nRoll Number already exists!")
                 continue

            for student in students:
                if student.roll == old_roll_number:
                   student.roll = new_roll_number
                   print('\nRoll Number Updated!')
                   return

            print('\nRoll Number Not Found!')
               

        elif update == 'b':
                roll_number = input('Enter Roll Number: ').upper()
                for student in students:
                    if student.roll == roll_number:
                        new_name = input('Enter new name: ').strip().title()
                        student.name = new_name
                        print('\nName Updated!')
                        return
                   
                print('\nRoll Number Not Found!')

        elif update == 'c':
                roll_number = input('Enter Roll Number: ').upper()

                for student in students:
                    if student.roll == roll_number:

                        while True:
                            try:
                              new_age = int(input('Enter new age: '))

                              if new_age <= 0:
                                 print('\nAge Must be Greater than Zero!')
                                 continue
                              break

                            except ValueError:
                                print('\nEnter Numbers only!')

                        student.age = new_age
                        print('\nAge Updated!')
                        return
                    
                print('\nRoll Number Not Found!')


        elif update == 'd':
                roll_number = input('Enter Roll Number: ').upper()
                for student in students:
                    if student.roll == roll_number:
                        new_department = input('Enter new department: ').title()
                        student.department = new_department
                        print('\nDepartment Updated Successfully!')
                        return

                print('\nRoll Number Not Found!')
        
        elif update == 'e':
            break
            
        else:
            print('Choose a Valid Option!')

def search_student():
    roll_number = input("Enter Roll Number: ").upper()

    for student in students:
        if student.roll == roll_number:
            student.display()
            return

    print('\nRoll Number Not Found!')

while True:
    print("\n1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display Students")
    print("6. Exit")

    while True:
       try:
          choice = int(input("\nEnter choice: "))
          break
       except ValueError:
          print('Enter numbers only!')

    if choice == 1:
        add_student()

    elif choice == 2:
        delete_student()

    elif choice == 3:
        update_student()

    elif choice == 4:
        search_student()

    elif choice == 5:
        display_students()

    elif choice == 6:
        print("Thank you for using Student Management System!")
        print()
        break

    else:
        print("Invalid Choice!")
        print()