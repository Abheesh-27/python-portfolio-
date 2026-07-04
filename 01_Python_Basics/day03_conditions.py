#Program 1: Voting Eligibility.
age = int(input('Enter your age: '))

if age>=18:
    print('You are eligible to vote.')
else:
    print('You are not eligible to vote!')

print()

#Program 2: Largest of the 3 numbers.
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))

if n1>=n2 and n1>=n3:
    print('Largest number is: ', n1)
elif n2>=n1 and n2>=n3:
    print('Largest number is: ', n2)
else:
    print('Largest number is: ', n3)

print()

#Program 3: Grade Calculator.
marks = int(input("Enter your marks: "))

if marks>=90:
    print("Grade A")
elif marks>=80:
    print('Grade B')
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")

#Program 4: Leap Year Calculator.
year = int(input("Enter year: "))

if year % 4 == 0:
    print('Leap Year')
else:
    print('Not a Leap Year')
