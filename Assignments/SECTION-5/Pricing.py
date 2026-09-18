'''Combining several conditions into one price
Compute a cinema ticket price from three inputs: 
age, whether the person is a student (yes/no), and the day of the week.

Rules, applied to a base price of Rs 200:
• Age under 12 OR 60+  -> 50% off the base price
• Student               -> an extra 20% off
• Weekend (Saturday/Sunday) -> add a 50% surcharge, applied AFTER the discounts

Print a clear breakdown and the final price.'''

age = int(input("Enter your age:"))
whether_student = (input("Are you a student(yes/no:)"))
day = (input("Which day:"))

base_price = 200
age_discount = 0
student_discount = 0
if age < 12 or age >= 60:
    age_discount = base_price * 0.50
if whether_student == "yes":
  student_discount = base_price * 0.20
total_discount = age_discount + student_discount
price_after_discounts = max(0, base_price - total_discount)
is_weekend = day in ["saturday", "sunday"]
weekend_surcharge = price_after_discounts * 0.50 if is_weekend else 0

final_price = price_after_discounts + weekend_surcharge
    
print("=================================")
print("      TICKET PRICE RECEIPT      ")
print("=================================")
print(f"Base Ticket Price:    Rs {base_price:}")
if age_discount > 0:
    print(f"Age Discount (50%):  -Rs {age_discount:}")
if student_discount > 0:
    print(f"Student Discount(20%):-Rs {student_discount:}")
    print(f"Subtotal:             Rs {price_after_discounts:}")
if weekend_surcharge > 0:
    print(f"Weekend Surcharge(50%):+Rs {weekend_surcharge:}")
    print("--------------------------------------------------")
    print(f"FINAL PRICE:          Rs {final_price:}")
    print("==================================================")
