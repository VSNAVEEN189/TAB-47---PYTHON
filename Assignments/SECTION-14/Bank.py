'''Bank Account
You'll practice
Methods with validation, object interaction, and error handling
Create a BankAccount class with owner (string) and balance (number, default 0) attributes.
Add the following methods:
- deposit(amount) — adds to balance. Raise ValueError if amount is zero or negative.
- withdraw(amount) — subtracts from balance. Raise ValueError if amount is zero or negative. Raise ValueError if amount exceeds current balance (no overdraft allowed).
- get_balance() — returns the current balance
- display() — prints owner name and current balance formatted as currency
Then create two accounts and implement a transfer between them:
- Withdraw from Account A
- Deposit into Account B
- Print both accounts before and after the transfer to verify
Test all edge cases:
- Depositing a negative amount
- Withdrawing more than the balance
- Withdrawing zero
Each edge case should print the error message, not crash the program'''


class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

    def get_balance(self):
        return self.balance

    def display(self):
        print(f"{self.owner}: Rs {self.balance:,.2f}")

# Creating two accounts
account_a = BankAccount("Amit", 10000)
account_b = BankAccount("Priya", 5000)

# Display balances before transfer
print("Before Transfer:")
account_a.display()
account_b.display()

# Transfer money from Amit to Priya
transfer_amount = 3000

print(f"\nTransferring Rs {transfer_amount:,.0f} from Amit to Priya...")

try:
    account_a.withdraw(transfer_amount)
    account_b.deposit(transfer_amount)

except ValueError as e:
    print("Error:", e)

# Display balances after transfer
print("\nAfter Transfer:")
account_a.display()
account_b.display()

# Testing edge cases
print("\nTesting edge cases:")

# 1. Depositing a negative amount
try:
    account_a.deposit(-500)

except ValueError as e:
    print("Error:", e)

# 2. Withdrawing more than the balance
try:
    account_a.withdraw(20000)

except ValueError as e:
    print("Error:", e)

# 3. Withdrawing zero
try:
    account_a.withdraw(0)

except ValueError as e:
    print("Error:", e)