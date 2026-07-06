import math 
print('\n ===== SIMPLE CALCULATOR =====')
def add(num1 , num2):
    return num1 + num2

def subtract(num1 , num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 * num2

def divide(num1 , num2):
     if num2 == 0:
           return 'Cannot Divide by Zero'
     return num1 / num2

num1 = float(input('Enter first Number: '))
num2 = float(input('Enter second number: '))

print()

print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

print()
select = int(input('Enter your choice: '))

if select == 1:
     print('Answer = ', add(num1,num2))
elif select == 2:
     print('Answer = ', subtract(num1,num2))
elif select == 3:
     print('Answer = ', multiply(num1,num2))
elif select == 4:
     print('Answer = ', divide(num1,num2))
else:
     print('Invalid Input!')



print('\n ===== AREA CALCULATOR =====')

def circle(radius):
     return math.pi * (radius ** 2)

def triangle(base , height):
     return 0.5 * base * height

def square(side):
     return side ** 2

def rectangle(length , breadth):
     return length * breadth  

print('1. Circle')   
print('2. Triangle')   
print('3. Square ')   
print('4. Rectangle')   

print()
choice = int(input('Select a shape: '))

if choice == 1:
     r = float(input('Enter radius:'))
     print('Area = ', circle(r))

elif choice == 2:
     base = float(input('Enter base length:'))
     h = float(input('Enter height:'))
     print('Area = ', triangle(base,h))

elif choice == 3:
     s = float(input('Enter side: '))
     print('Area = ', square(s))

elif choice == 4:
     l = float(input('Enter length: '))
     br = float(input('Enter breadth: '))
     print('Area = ', rectangle(l,br))
else:
     print('Invalid Input!')
     



# Finding largest of the 3 numbers.
print('\n ===== Largest Number =====')
def largest(a, b, c):
     if a >= b and a >= c:
         return a 
     elif b >= a and b >= c:
         return b 
     else :
          return c

first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
third_num = int(input('Enter third number: '))

print()

maximum = largest(first_num, second_num , third_num)
print(maximum , 'is the largest number')



#Program to find simple interest
print('\n ===== Simple Interest =====')
def simple_interest(principal, rate , time):
     return (principal * rate * time) / 100

p = float(input('Principal: '))
r = float(input('Rate: '))
t = float(input('Time: '))

si = simple_interest(p,r,t)

print()

print("Simple Interest =",si)
print("Total Amount =",p+si)



print('\n ===== Compund Interest =====')

def compound_interest(principal, rate, time):
    amount = principal * ((1 + rate / 100) ** time)
    return amount

p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))

amount = compound_interest(p, r, t)

print()
print("Compound Interest =", amount - p)
print("Total Amount =", amount)

print()
