print("\n===== Program 1: Student Class =====")
class Student:
    def __init__(self, name , age, department):
        self.name = name
        self.age = age
        self.department = department

    def display(self): #helps to reduce multiple usage of print
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print()

student1 = Student('Abheesh', 20, 'Civil')
student2 = Student('Archit', 21, 'Mechanical')

student1.display()
student2.display()


print("\n===== Program 2: Employee Class =====")
class Employee:
    def __init__(self, name , salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
    
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Designation:", self.designation)
        print()

employee1 = Employee('Rahul', 60000, 'AI Engineer')
employee2 = Employee('Ajay', 80000, 'Developer')

employee1.display()
employee2.display()


print("\n===== Program 3: Movie Class =====")
class Movie:
    def __init__(self, name , hero, rating):
        self.name = name
        self.hero = hero
        self.rating = rating
    
    def display(self):
        print("Movie Name:", self.name)
        print("Hero:", self.hero)
        print("Rating:", self.rating)
        print()

movie1_name = input('Enter movie name: ')
movie1_hero = input('Hero: ')

while True:
   try:
        movie1_rating = float(input('Rating: '))
        break

   except ValueError:
       print('Enter numbers only!')

movie1 = Movie(movie1_name, movie1_hero, movie1_rating)

movie2_name = input('Enter another movie name: ')
movie2_hero = input('Hero: ')

while True:
    try:
       movie2_rating = float(input('Rating: '))
       break

    except ValueError:
       print('Enter numbers only!')

movie2 = Movie(movie2_name, movie2_hero, movie2_rating)
print()

movie1.display()
movie2.display()    