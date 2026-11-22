'''
PERSONAL EXPENSE CALCULATOR

Imagine you purchased three items today.

Create a Python program that stores:
Item	Price
Notebook	₹50
Pen	₹20
Bag	₹750

Requirements:
1. Store the three prices in separate variables.
2. Calculate the total expense.
3. Calculate the average price of the three items.
4. Display the total and average.
5. Display the data type of total and average.'''


print("=======PERSONAL EXPENSE CALCULATOR=======")
notebook = (50)
pen = (20)
bag = (750)

total_expense = notebook + pen + bag
average = total_expense/3

print(f"The total of 3 items is :", total_expense)
print(f"The average of 3 items is :",average)

print(type(total_expense))
print(type(average))