class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return True
        elif amount > self._account_balance:
            print("Insufficient funds.")
            return False
        else:
            print("Withdrawal amount must be positive.")
            return False
    def display_balance(self):
        print(f"Current balance: ${self._account_balance:.2f}")

