# ==========================================
#       PERSONAL FINANCE PLANNER
# ==========================================

print("==========================================")
print("        PERSONAL FINANCE PLANNER")
print("==========================================")

# ------------------------------------------
# 1. BASIC INFORMATION
# ------------------------------------------

name = input("Enter your name: ")

income = float(input("Enter your monthly income: ₹"))

print("\nEnter your monthly expenses:")

rent = float(input("Rent: ₹"))
food = float(input("Food: ₹"))
travel = float(input("Travel: ₹"))
shopping = float(input("Shopping: ₹"))
other = float(input("Other expenses: ₹"))

# ------------------------------------------
# 2. EXPENSE CALCULATOR
# ------------------------------------------

total_expenses = rent + food + travel + shopping + other

remaining_money = income - total_expenses

print("\n==========================================")
print("           EXPENSE SUMMARY")
print("==========================================")

print(f"Monthly Income:       ₹{income:}")
print(f"Total Expenses:       ₹{total_expenses:}")
print(f"Money Remaining:      ₹{remaining_money:}")


# ------------------------------------------
# 3. BUDGET CALCULATOR
# ------------------------------------------

expense_percentage = (total_expenses / income) * 100

print("\n==========================================")
print("           BUDGET ANALYSIS")
print("==========================================")

print(f"Expense Percentage:   {expense_percentage:}%")

if expense_percentage < 50:
    print("Budget Status:        Excellent")
elif expense_percentage < 70:
    print("Budget Status:        Good")
elif expense_percentage < 90:
    print("Budget Status:        Warning")
else:
    print("Budget Status:        Critical")


# ------------------------------------------
# 4. SAVINGS CALCULATOR
# ------------------------------------------

monthly_savings = remaining_money

if income > 0:
    savings_rate = (monthly_savings / income) * 100
else:
    savings_rate = 0

print("\n==========================================")
print("           SAVINGS ANALYSIS")
print("==========================================")

print(f"Monthly Savings:      ₹{monthly_savings:}")
print(f"Savings Rate:         {savings_rate:}%")

if monthly_savings > 0:
    print("Savings Status:       You are saving money")
elif monthly_savings == 0:
    print("Savings Status:       No money left to save")
else:
    print("Savings Status:       You are spending more than income")


# ------------------------------------------
# 5. SAVINGS GOAL
# ------------------------------------------

goal = float(input("\nEnter your savings goal: ₹"))

if monthly_savings > 0:
    months_needed = goal / monthly_savings

    print(f"Amount Needed:        ₹{goal:}")
    print(f"Estimated Time:       {months_needed:} months")
else:
    print("You cannot calculate goal time because")
    print("your current monthly savings is ₹0 or negative.")


# ------------------------------------------
# 6. EMI CALCULATOR
# ------------------------------------------

print("\n==========================================")
print("              LOAN DETAILS")
print("==========================================")

loan_amount = float(input("Enter loan amount: ₹"))
annual_rate = float(input("Enter annual interest rate (%): "))
loan_years = int(input("Enter loan duration (years): "))

# Convert annual interest rate into monthly rate
monthly_rate = (annual_rate / 100) / 12

# Convert years into months
number_of_months = loan_years * 12

if monthly_rate > 0:

    emi = (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** number_of_months
        / ((1 + monthly_rate) ** number_of_months - 1)
    )

else:
    # If interest rate is 0%
    emi = loan_amount / number_of_months


# ------------------------------------------
# 7. LOAN CALCULATOR
# ------------------------------------------

total_payment = emi * number_of_months

total_interest = total_payment - loan_amount

print("\n==========================================")
print("              LOAN ANALYSIS")
print("==========================================")

print(f"Loan Amount:          ₹{loan_amount:}")
print(f"Interest Rate:        {annual_rate:}%")
print(f"Loan Duration:        {loan_years} years")
print(f"Number of Months:     {number_of_months}")
print(f"Monthly EMI:          ₹{emi:}")
print(f"Total Payment:        ₹{total_payment:}")
print(f"Total Interest:       ₹{total_interest:}")


# ------------------------------------------
# 8. FINAL FINANCIAL SUMMARY
# ------------------------------------------

print("\n==========================================")
print("        FINAL FINANCIAL SUMMARY")
print("==========================================")

print(f"Name:                 {name}")
print(f"Monthly Income:       ₹{income:}")
print(f"Monthly Expenses:     ₹{total_expenses:}")
print(f"Monthly Savings:      ₹{monthly_savings:}")
print(f"Savings Rate:         {savings_rate:}%")
print(f"Monthly EMI:          ₹{emi:}")

print("------------------------------------------")

# Check whether EMI is affordable
if monthly_savings >= emi:
    print("Loan Status:          EMI is affordable")
else:
    print("Loan Status:          EMI may be difficult to afford")

print("==========================================")
print("       END OF PERSONAL FINANCE PLANNER")
print("==========================================")