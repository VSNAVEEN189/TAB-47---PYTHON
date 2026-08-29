#Build a simple interest calculator driven by variables.
#Define three variables: principal, rate (percent per year), and time (in years). Then calculate:
# Simple Interest:  SI = (principal × rate × time) / 100
#• Total amount:     principal + SI

principal = 50000
rate = 7
time = 3

# Calculate simple interest and store it in a valid variable name
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest


print(f"Simple_Interest: {principal*rate*time/100}")
print(f"Total Amount: {principal + simple_interest}")