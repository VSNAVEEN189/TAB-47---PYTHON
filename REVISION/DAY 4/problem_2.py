'''Compare Two Expenses

Comparison operator

Write a program that:
1. Takes two expense amounts as input and converts them to float.
2. Prints whether the first expense is greater than the second.
3. Prints whether the two expenses are equal.
4. Prints whether the first expense is less than or equal to the second.'''

expense_1 = input("Enter the expense amount:")
expense_2 = input("Enter the expense amount:")

expense_1 = (float(expense_1))
expense_2 = (float(expense_2))

print(f"The first expense is greater than second expense :{expense_1 > expense_2}")

print(f"The 2 expenses are equal :{expense_1 == expense_2}")

print(f"The first expense is less than or equal to second :{expense_1 <= expense_2}")