from math import sqrt, pow , factorial , ceil ,floor
import random
import datetime
import os

print('\n ===== Program 1: Math Module =====')

try:
    number = float(input('Enter a number: '))
    print('\n Square Root of ', number , 'is: ', sqrt(number))
    print('Square of ', number, 'is: ', pow(number,2))
    print('Cube of ', number, 'is: ', pow(number,3))
    if number >= 0 and number.is_integer(): 
       print('Factorial of', number , 'is: ', factorial(int((number))))
    else:
       print("Factorial is only defined for non-negative integers.")

    print('Ceiling: ', ceil(number))
    print('Floor: ', floor(number))

except ValueError as e: #gives an error if user doesn't enter a number
    print('Error: ', e)

  
#generating a random number and guessing it thrrough user input
print('\n ===== Program 2.1(Random_Module): Number Guessing =====')

try: 
    guess_number = random.randint(1,100)
    user_number = int(input('Guess a number between 1 to 100: '))
 
    while user_number != guess_number:
        if user_number < guess_number:
           print('Too Low')
        else:
           print('Too High!')

        user_number = int(input('Guess again: '))
    print('Correct!')

except ValueError:
    print('Please enter numbers only!')

    
print('\n ===== Program 2.1(Random_Module): Shuffline List & Rolling a Dice =====')

numbers = [1,2,3,4,5,6]
random.shuffle(numbers) #shuffle the list.
print('Shuffled list: ', numbers)
print('Rolling a dice: ', random.randint(1,6))


print('\n ===== Program 3: DateTime Module =====')
#printing current date , time , year , month and weekday
now = datetime.datetime.now()
today = datetime.date.today()
time = now.time()

#current date and time
print('Current Date & Time; ', now)
print()

#today's date
print("Today's Date: ", today) 
print("Today's Date: ", now.strftime("%d-%m-%Y")) #gives in number format
print("Today's Date: ", now.strftime("%d %B %Y")) #gives date and year in number and month in text format
print()

print('Current Time: ', time) #current time method 1
print('Current Time: ', now.strftime("%H:%M:%S")) #current time method 2
print()

print('Current Year: ', now.year) #current year method 1
print('Current Year: ', now.strftime('%Y')) #current year method 2
print()

print('Current Month: ', now.month)  #current month method 1
print('Current Month: ', now.strftime('%B')) #current month method 2
print()

print('Current Weekday: ', now.weekday()) #current weekday method 1
print('Current Weekday: ', now.strftime('%A')) #current weekday method 2
print()


print('\n ===== Program 4: OS Module =====')

print('Current Working Directory: ', os.getcwd())
print('Files & Folders: ', os.listdir())

#creating a folder
if not os.path.exists('NewFolder'):
    os.mkdir("NewFolder")

#renaming file or folder
if os.path.exists('NewFolder'): 
    os.rename("NewFolder" , "MyFolder")

#removing an empty folder
if os.path.exists('MyFolder'): 
    os.rmdir('MyFolder')

#checking if path exists
print(os.path.exists('README.md'))

#joining paths
path = os.path.join(
    '01_Python_Basics',
    'day11_modules.py'
    )
print(path)
print()