class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


initial_balance = float(input("Enter initial balance: "))

account = BankAccount(initial_balance)

account.deposit(50)
account.withdraw(20)

print(account.get_balance())
