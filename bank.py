 # write a program simulated bank account deposit withd some amout then display amout and diposite some values and again print all deposit
    
class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def display_balance(self):
        print(f"Current balance: {self.balance}")

# Create a bank account 
account = BankAccount()

# Deposit initial amount
initial_amount = 100
account.deposit(initial_amount)
account.display_balance()

# Make additional deposits
deposit1 = 50
account.deposit(deposit1)
account.display_balance()

deposit2 = 75
account.deposit(deposit2)
account.display_balance()
