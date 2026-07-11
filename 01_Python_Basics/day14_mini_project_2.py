class BankAccount:
    def __init__(self, account_number , name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def display(self):
        print('-' * 30)
        print('Account Number: ', self.account_number)
        print('Account Holder: ', self.name)
        print(f'Balance       : {self.balance:.2f} /-')

    def deposit(self, amount):
        self.balance += amount
        print('\nAmount Deposited Successfully!')
        print(f"Updated Balance: {self.balance:.2f} /-")

    def withdrawal(self, amount):
        if amount > self.balance:
            print('\nInsufficient balance!')
        
        else:
            self.balance -= amount
            print('\nWithdrawal Successful.')
            print(f"Updated Balance: {self.balance:.2f} /-")

    def check_balance(self):
        print(f'\nAccount Balance: {self.balance:.2f} /-')

accounts = []

def valid_account_number():
    while True:
        try:
            account_number = int(input('\nEnter Account Number: '))
            if account_number <= 0 :
                print('\nAccount number must be positive!')
                continue

            return account_number

        except ValueError:
            print('\nEnter Numbers Only!')


def create_account():
    account_number = valid_account_number()
    for account in accounts:
        if account.account_number == account_number:
            print('\nAccount Already Exists:')
            return
    while True:
        name = input('Enter Name: ').strip().title()

        if name:
            break
        else:
            print('Name cannot be empty!')

    while True:
        try:
            balance = float(input('Enter Initial Balance: '))
            if balance < 0:
                print('Balance cannot be negative!')
                continue
            break
        
        except ValueError:
            print('Enter Numbers Only!')

    customer = BankAccount(account_number, name, balance)
    accounts.append(customer)
    print('Account Added Successfully.')

def search_account():
    account_number = valid_account_number()
    account = find_account(account_number)

    if account:
        account.display()

    else:        
        print("Account Doesn't Exist!")

def find_account(account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None

def valid_amount():
    while True:
        try:
            amount = float(input('Enter Amount: '))
            if amount <= 0:
                print('Amount should be greater than Zero!')
                continue
            return amount

        except ValueError:
            print('Enter Numbers Only!')

while True:
    print('\n===== Bank Management System =====')
    print('\n1. Create Account')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Check Balance')
    print('5. Display Account Details')
    print('6. Exit')
    
    while True:
        try:
            choice = int(input('\nEnter a choice: '))
            break
        except ValueError:
            print('\nInvalid Choice!')

    if choice == 1:
        create_account()
    
    elif choice == 2:
        account_number = valid_account_number()
        account = find_account(account_number)
        if account:
            amount = valid_amount()
            account.deposit(amount)

        else:
            print("Account Doesn't Exist!")

    elif choice == 3:
        account_number = valid_account_number()
        account = find_account(account_number)
        if account:
            amount = valid_amount()
            account.withdrawal(amount)

        else:
            print("Account Doesn't Exist!")
    
    elif choice == 4:
        account_number = valid_account_number()
        account = find_account(account_number)
        if account:
            account.check_balance()
        
        else:
            print("Account Doesn't Exist!")
    
    elif choice == 5:
        search_account()
        
    elif choice == 6:
        print('Thank you for using Bank Management System!')
        break

    else:
        print('Invalid Choice!')