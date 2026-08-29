'''Multiple inputs feeding a real-world formula
Ask the user for a loan amount, an annual interest rate (percent), and a tenure in months. Compute the monthly EMI (equated monthly instalment).

Formula:r = (annual_rate / 12) / 100          # monthly rate as a decimal
EMI = P * r * (1 + r)**n / ((1 + r)**n - 1)
where P is the loan amount and n is the number of months.

Print the EMI rounded to 2 decimal places.'''

# P = 100000 is the loan ammount, n = 12 is the no.of months, Annual rate = 11.5%

p = int(input("Enter loan amount:"))
r = float(input("Enter annual rate(%):"))
n = int(input("Enter number of months:"))

r = (r/12) / 100      

EMI = p * r * (1 + r)**n / ((1 + r)**n - 1)

print(f"Monthly EMI is :Rs{EMI}")