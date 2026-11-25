'''Electricity Bill Calculator

Beginner level
Imagine you're developing a simple electricity bill calculator.

An electricity company charges customers based on units consumed.

Requirements
1. Ask the user to enter electricity units consumed.
2. Convert the input into an integer.
3. Calculate the bill using the following rates:
   - First 100 units: ₹5 per unit.
   - Next 100 units (101–200): ₹7 per unit.
   - Above 200 units: ₹10 per unit.
4. Display the total electricity bill.
5. Display the data type of the bill.
For now, assume the customer consumes between 1 and 100 units. We'll handle multiple slabs after learning conditions.'''


print("==== Electricity Bill Calculator ====")

units = input("Enter the units consumed- ")

units = (int(units))

rate = 5

total_bill = units*rate

print(f"The total electricity bill is {total_bill}")
print(type(total_bill))