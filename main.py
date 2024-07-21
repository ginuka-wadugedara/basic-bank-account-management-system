class Account:
    def __init__(self, acc_number, initial_deposit):
        self.acc_number = acc_number
        self.balance = initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.acc_number}.")
        else:
            print("deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} from account {self.acc_number}.")
            else:
                print("Insufficient funds.")
        else:
            print("withdrawal amount.")

    def check_balance(self):
        print(f"Account {self.acc_number} balance: Rs:{self.balance:.2f}")

    def transfer(self, recipient, amount):
        if amount > 0:
            if self.balance >= amount:
                self.withdraw(amount)
                recipient.deposit(amount)
                print(f"Transferred {amount} from account {self.acc_number} to account {recipient.acc_number}.")
            else:
                print("Insufficient funds.")
        else:
            print("transfer amount.")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_number, initial_deposit):
        if len(acc_number) == 8 and acc_number.isdigit():
            if acc_number in self.accounts:
                print("Account number already exists.")
            else:
                if initial_deposit >= 0:
                    self.accounts[acc_number] = Account(acc_number, initial_deposit)
                    print(f"Account {acc_number} created with initial deposit of {initial_deposit}.")
                else:
                    print("Initial deposit must be non-negative.")
        else:
            print("please enter 8 numbers.")

    def account_exists(self, acc_number):
        return acc_number in self.accounts

    def get_account(self, acc_number):
        return self.accounts.get(acc_number)

    def perform_deposit(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def perform_withdrawal(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def perform_balance_check(self, acc_number):
        account = self.get_account(acc_number)
        if account:
            account.check_balance()
        else:
            print("Account not found.")

    def perform_transfer(self, sender_acc_number, recipient_acc_number, amount):
        sender = self.get_account(sender_acc_number)
        recipient = self.get_account(recipient_acc_number)
        if sender and recipient:
            sender.transfer(recipient, amount)
        else:
            print("One or both accounts not found.")


def display_menu():
    print("\nWelcome to the Bank Account Management System")
    print("1. Create a new account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check account balance")
    print("5. Transfer money")
    print("6. Exit")


def input_with_prompt(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input
        else:
            print("Please enter a value.")


def main():
    bank = Bank()
    while True:
        display_menu()
        choice = input_with_prompt("Enter your choice: ")
        if choice == "1":
            acc_number = input_with_prompt("Enter account number: ")
            if bank.account_exists(acc_number):

                print("Account number already exists.")
            else:
                initial_deposit = input_with_prompt("Enter initial deposit amount: ")
                while True:
                    try:
                        initial_deposit = float(initial_deposit)
                        if initial_deposit >= 0:
                            break
                        else:
                            print(" deposit amount must be non-negative.")
                            initial_deposit = input_with_prompt("Enter initial deposit amount: ")
                    except ValueError:
                        print("Please enter a valid number.")
                        initial_deposit = input_with_prompt("Enter initial deposit amount: ")
                bank.create_account(acc_number, initial_deposit)
        elif choice == "2":
            acc_number = input_with_prompt("Enter account number: ")
            amount = input_with_prompt("Enter deposit amount: ")
            while True:
                try:
                    amount = float(amount)
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    amount = input_with_prompt("Enter deposit amount: ")
            bank.perform_deposit(acc_number, amount)
        elif choice == "3":
            acc_number = input_with_prompt("Enter account number: ")
            amount = input_with_prompt("Enter withdrawal amount: ")
            while True:
                try:
                    amount = float(amount)
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    amount = input_with_prompt("Enter withdrawal amount: ")
            bank.perform_withdrawal(acc_number, amount)
        elif choice == "4":
            acc_number = input_with_prompt("Enter account number: ")
            bank.perform_balance_check(acc_number)
        elif choice == "5":
            sender_acc_number = input_with_prompt("Enter sender account number: ")
            recipient_acc_number = input_with_prompt("Enter recipient account number: ")
            amount = input_with_prompt("Enter transfer amount: ")
            while True:
                try:
                    amount = float(amount)
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    amount = input_with_prompt("Enter transfer amount: ")
            bank.perform_transfer(sender_acc_number, recipient_acc_number, amount)
        elif choice == "6":
            print("Exiting.")
            break
        else:
            print("Please try again.")


if __name__ == "__main__":
    main()
