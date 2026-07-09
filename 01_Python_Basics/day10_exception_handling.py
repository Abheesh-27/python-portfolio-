class WrongOperation(Exception):
        pass

class NegativeNumber(Exception):
    pass


print('\n ===== Program 1: Else =====')
try:
    num = int(input('Enter a number:'))
    print(10 / num)
except ValueError:
    print('Please enter numbers only!')
except ZeroDivisionError:
    print('Cannot divide by zero.')

else:
    print('Program Executed Successfully.')
print()


#same code using finally
print('\n ===== Program 2: Finally =====')
try:
    num1 = int(input('Enter a number: '))
    print(10 / num1)
except Exception:
    print('Something went wrong')
finally: #finally always executes even if theres a error or not.
    print('Program ended.')
print()


#exception as 'e'
print('\n ===== Program 3: Exception as e =====')
try:
    number = int(input('Enter a number: '))
    print(100 / number)
except Exception as e:
     print('Error: ', e)
print()


#creating your own error
print('\n ===== Program 4: Creating your own error =====')
age = int(input('Enter your age: '))

if age < 18:
    raise ValueError('Age must be atleast 18')

print('Eligible.')
print()


#customising exception
print('\n ===== Program 5: Customised Error =====')
number_1 = int(input('Enter a number: '))
if number_1 < 0:
    raise NegativeNumber('Negative numbers are not allowed!') 

else:
    print('Valid Input.')
print()


#calculator exception handling
print('\n ===== Program 6: Calculator Exception Handling =====')
try: 
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))

    operation = input("Choose (+, -, *, /): ")

    if operation == '+':
       print('Answer: ', first_number + second_number)
    elif operation == '-':
        print('Answer: ', first_number - second_number )
    elif operation == '*':
        print('Answer: ', first_number * second_number )
    elif operation == '/':
        print('Answer: ', first_number / second_number)
    else:
        raise WrongOperation('Invalid Operation!')

except ValueError as e:
    print('Error: ', e)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except WrongOperation as e:
    print('Error: ', e)


#ATM Withdrawal
print('\n ===== Program 7: ATM Withdrawal =====')
try: 
    balance = float(input('Enter Balance: '))
    amount = float(input('Enter Amount: '))

    if amount > balance:
        raise ValueError('Amount must be less than the Balance in your account!')

    print('Money debited successfully.')

except ValueError as e:
     print('Error: ', e)


#Simple login
print('\n ===== Program 8: Simple Login =====')
try: 
    password = input('Enter Password: ')

    if password != 'python123' :
        raise ValueError('Incorrect Password!')
    print('Login Successfull.')

except ValueError as e:
     print('Error: ', e)