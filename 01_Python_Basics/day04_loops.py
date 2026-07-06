# ============================================
# Day 4 - Loops
# Topics:
# 1. for loop
# 2. while loop
# 3. range()
#
# Programs:
# - Multiplication Table
# - Factorial
# - Fibonacci Series
# - Sum of First N Numbers
# - Prime Number Check
# ============================================



# Program 1: Multiplication Table
print( "\n ===Program 1: Multiplication Table (For Loop)===")
num = int(input("Enter a number: "))
print(num , 'Table:')

for i in range(1,11):
    print(num , 'X' , i , '=' , num*i)
print()

#same program using while loop
print("===Program 1: Multiplication Table (While Loop)===")
num1 = int(input('Enter a number: '))
print(num1, 'Table')
i = 1
while i<=10:
    print(num1, 'X' , i , '=' , num1*i)
    i +=1
print()

# Program 2 : Factorial Calculation
print("===Program 2: Factorial Calculation (For Loop)===")
n = int(input('Enter a number: '))

fact = 1
for i in range(1,n+1):
    fact *= i
print('Factorial of ', n, 'is ', fact)
print()

#same program using while loop
print("===Program 2: Factorial Calculation (While Loop)===")
n1 = int(input('Enter a number: '))

fact1 = 1
x = 1
while x <= n1:
    fact1 *= x
    x += 1

print('Factorial of ', n1, 'is ', fact1)
print()


 # Program 3 : Fibonacci Series
print("===Program 3: Fibonacci Series (For Loop)===")
number = int(input('Enter a number: '))
a = 0 
b = 1
for i in range (number):
    print( a , end=" ")

    a , b = b , a+b 

print()
print()

#same program using while loop
print("===Program 3: Fibonacci Series (While Loop)===")
number1 = int(input('Enter a number: '))

var1 = 0 
var2 = 1
const = 0
while const < number1:
    print(var1 , end=" ")

    var3 = var2 + var1
    var1 = var2
    var2 = var3
    const += 1

print()
print()


# Program 4 : Sum of First N terms.
print("===Program 4: Sum of First N terms (For Loop)===")
num2 = int(input('Enter a number: '))
total4 = 0

for i in range (1,num2+1):
    total4 += i

print("Sum of the first ", num2, 'numbers is: ', total4)
print()

#same program using while loop
print("===Program 4: Sum of First N terms (While Loop)===")
num3 = int(input('Enter a number: '))

total2 = 0
y = 1
while y <= num3:
    total2 += y
    y += 1
print("Sum of the first ", num3, 'numbers is: ', total2)
print()

# Program 5: Prime Numbers
print("===Program 5: Prime Numbers (For Loop)===")

integer = int(input('Enter a number: '))

if integer <= 1:
    print('Not a prime number!')

else:
    prime = True

    for i in range(2,integer):
        if integer % i == 0:
            prime = False
            break
    if prime:
        print('It is a prime number.')
    else:
        print('Not a Prime Number!')
print()


# Program 5: Prime Numbers
print("===Program 5: Prime Numbers (While Loop)===")

integer1 = int(input('Enter a number: '))

if integer1 <= 1:
    print('Not a prime number!')

else:
    m = 2
    prime = True

    while m < integer1:
        if integer1 % m == 0:
            prime = False
            break
        m += 1
    if prime:
        print('It is a prime number.')
    else:
        print('Not a Prime Number!')

print()
