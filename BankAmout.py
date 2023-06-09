#write python program to simulate a bank amount for deposit , withdraw amount 
#operation 
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} successful. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. Current balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")

# Creating an instance of the BankAccount class
account = BankAccount()

# Test the program
account.deposit(1000)  # Deposit $1000
account.withdraw(500)  # Withdraw $500
account.withdraw(700)  # Withdraw $700 (Insufficient funds)
 