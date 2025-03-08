import random

class Bank:
    def __init__(self, name):
        self.name = name
        self.total_balance = 0
        self.total_loan = 0
        self.loan_status = True  
        self.accounts_list = {}  

    def create_account(self, name, email, address, account_type):
        account_no = random.randint(1000, 9999)  
        while account_no in self.accounts_list:
            account_no = random.randint(1000, 9999)
        new_account = Account(account_no, name, email, address, account_type)
        self.accounts_list[account_no] = new_account
        print(f"Account created successfully! Account Number: {account_no}")

    def delete_account(self, account_no):
        if account_no in self.accounts_list:
            account = self.accounts_list.pop(account_no)
            self.total_balance -= account.balance 
            print(f"Account {account_no} deleted successfully!")
        else:
            print("Account not found!")

    def show_users(self):
        if not self.accounts_list:
            print("No users in the bank.")
            return
        print("\nUsers in the bank:")
        for account_no, account in self.accounts_list.items():
            print(f"Account No: {account_no}, Name: {account.name}, Balance: {account.balance}")

    def print_total_balance(self):
        print(f"Total balance in the bank: {self.total_balance}")

    def print_total_loan(self):
        print(f"Total loan amount distributed by the bank: {self.total_loan}")

    def on_loan(self):
        self.loan_status = True
        print("Loan feature is now enabled.")

    def off_loan(self):
        self.loan_status = False
        print("Loan feature is now disabled.")


class Account:
    def __init__(self, account_no, name, email, address, account_type):
        self.account_no = account_no
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0  
        self.transaction_history = []
        self.loan_count = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            print(f"Deposited {amount} successfully!")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: {amount}")
            print(f"Withdrawn {amount} successfully!")

    def check_balance(self):
        print(f"Available balance: {self.balance}")

    def check_transaction_history(self):
        if not self.transaction_history:
            print("No transactions yet.")
            return
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, amount, bank):
        if not bank.loan_status:
            print("Loan feature is currently disabled.")
            return
        if self.loan_count >= 2:
            print("Loan limit exceeded. You can take a loan at most twice.")
            return
        self.balance += amount
        bank.total_loan += amount
        self.loan_count += 1
        self.transaction_history.append(f"Loan taken: {amount}")
        print(f"Loan of {amount} taken successfully!")

    def transfer(self, amount, recipient_account):
        if amount > self.balance:
            print("Transfer amount exceeded.")
        elif recipient_account is None:
            print("Recipient account does not exist.")
        else:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(f"Transferred: {amount} to {recipient_account.account_no}")
            recipient_account.transaction_history.append(f"Received: {amount} from {self.account_no}")
            print(f"Transferred {amount} successfully to Account No: {recipient_account.account_no}")

def user_menu(bank):
    account_no = int(input("Enter your account number: "))
    if account_no not in bank.accounts_list:
        print("Account not found!")
        return

    user = bank.accounts_list[account_no]
    
    while True:
        print(f"\nWelcome {user.name}!!")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")
        
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            user.deposit(amount)
            bank.total_balance += amount  
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(amount)
            bank.total_balance -= amount  
        elif choice == 3:
            user.check_balance()
        elif choice == 4:
            user.check_transaction_history()
        elif choice == 5:
            amount = float(input("Enter loan amount: "))
            user.take_loan(amount, bank)
        elif choice == 6:
            recipient_no = int(input("Enter recipient account number: "))
            if recipient_no not in bank.accounts_list:
                print("Recipient account does not exist.")
                continue
            recipient = bank.accounts_list[recipient_no]
            amount = float(input("Enter amount to transfer: "))
            user.transfer(amount, recipient)
        elif choice == 7:
            break
        else:
            print("Invalid Input!")


def admin_menu(bank):
    while True:
        print("\nWelcome Admin!")
        print("1. Create New Account")
        print("2. Delete Account")
        print("3. Show All Users")
        print("4. Check Total Bank Balance")
        print("5. Check Total Loan Amount")
        print("6. Enable Loan Feature")
        print("7. Disable Loan Feature")
        print("8. Exit")
        
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            name = input("Enter Account Holder's Name: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            account_type = input("Enter Account Type (Savings/Current): ")
            bank.create_account(name, email, address, account_type)
        elif choice == 2:
            account_no = int(input("Enter Account Number to Delete: "))
            bank.delete_account(account_no)
        elif choice == 3:
            bank.show_users()
        elif choice == 4:
            bank.print_total_balance()
        elif choice == 5:
            bank.print_total_loan()
        elif choice == 6:
            bank.on_loan()
        elif choice == 7:
            bank.off_loan()
        elif choice == 8:
            break
        else:
            print("Invalid Input!")


mamar_bank = Bank("Mamar Bank")
while True:
    print("\nWelcome to Mamar Bank!")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        user_menu(mamar_bank)
    elif choice == 2:
        admin_menu(mamar_bank)
    elif choice == 3:
        print("Thank you for using Mamar Bank. Goodbye!")
        break
    else:
        print("Invalid Input!")