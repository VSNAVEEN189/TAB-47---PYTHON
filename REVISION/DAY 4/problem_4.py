'''Build a Simple Wallet Balance Tracker.

Assignment Operators

Imagine you have ₹5,000 in your digital wallet.

Requirements:
1. Create a variable balance = 5000.
2. Add ₹1,500 using +=.
3. Deduct ₹800 using -=.
4. Multiply the balance by 2 using *=.
5. Divide the balance by 2 using /=.
6. Display the final balance and its data type.'''


print("==== Wallet balance tracker ====")

# The total amount 
balance = 5000
print(balance)

# Adding 1500
balance += 1500
print(balance)

# Deducting 800
balance -= 800
print(balance)

# Multiplying by 2
balance *= 2
print(balance)

# Divide by 2
balance /= 2
print(balance)

# The fial balance and its type
print(f"The final balance in wallet is ₹{balance}")
print(type(balance))