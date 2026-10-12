'''Crash-Proof Calculator
You'll practice
try/except and retry loops
Build a calculator that never crashes. The user enters two numbers and an operator (+, -, *, /). Handle:
• non-numeric input (ask again)
• division by zero (show a friendly message)
• an invalid operator

Keep looping until the user provides valid input (or chooses to quit).

Example:

Number: abc   -> That's not a number, try again.
Number: 10
Number: 0
Operator: /   -> Cannot divide by zero!

Catch specific exceptions (ValueError, ZeroDivisionError) rather than using a bare except.'''


while True:
    try:
        num1 = float(input("Number 1: "))
        break
    except ValueError:
        print("That's not a number, try again.")

while True:
    try:
        num2 = float(input("Number 2: "))
        break
    except ValueError:
        print("That's not a number, try again.")

while True:
    operator = input("Operator (+, -, *, /) or q to quit: ")

    if operator == "q":
        print("Calculator closed.")
        break

    if operator not in ["+", "-", "*", "/"]:
        print("Invalid operator, try again.")
        continue

    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        print("Result:", result)
        break

    except ZeroDivisionError:
        print("Cannot divide by zero! Try another operator.")
