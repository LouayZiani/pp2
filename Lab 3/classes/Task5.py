# Task 5:

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {amount}. New balance:{self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            print(f"withdraw: {amount}. New balance:{self.balance}")
        else:
            print("Insufficient funds")

account = Account(input("The owner is: "), abs(float(input("Balance:"))))

account.deposit(float(input("Amount to deposit: ")))
account.withdraw(float(input("Amount to withdraw:")))