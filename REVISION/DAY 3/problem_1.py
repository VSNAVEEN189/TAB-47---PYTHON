"""Employee Salary Calculator

Imagine you're developing a simple employee payroll calculator.

An employee enters their basic salary, bonus percentage, and tax percentage. 

Your requirements
1. Convert all three inputs into float.
2. Calculate the bonus amount.
3. Calculate salary after adding the bonus.
4. Calculate tax on the salary after bonus.
5. Calculate the final salary after tax.
6. Display all calculated amounts with two decimal places.
7. Display the data types of the calculated values.

"""
print("========Employee Salary Calculator========")

basic_salary = input("Enter basic salary : ")
bonus = input("Enter bonus % : ")
tax = input("Enter tax %: ")

basic_salary = (float(basic_salary))
bonus = (float(bonus))
tax = (float(tax))

# Calculating Bonus
bonus_amount = basic_salary*bonus/100

# Salary after bonus
salary_after_bonus = basic_salary + bonus_amount

# Calculating tax amount
tax_amount = salary_after_bonus*tax/100

# Salary after tax amount
final_salary = salary_after_bonus - tax_amount

print("======= The salary summary ========")
print(f"The bonus amount is ₹{bonus_amount:.2f}")
print(f"The salary after bonus is ₹{salary_after_bonus:.2f}")
print(f"The tax amount is ₹{tax_amount:.2f}")
print(f"The final salary is ₹{final_salary:.2f}")

# Checking data types
print("\n======= DATA TYPES =======")
print(type(basic_salary))
print(type(bonus_amount))
print(type(salary_after_bonus))
print(type(tax_amount))
print(type(final_salary))