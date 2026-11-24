'''Problem 1 – Shopping Bill Calculator

Your tasks
1. Convert price into an integer.
2. Convert quantity into an integer.
3. Convert discount into a float.
4. Calculate the total price.
5. Subtract the discount.
6. Print the final bill.
7. Display the original and converted data types.

Rules:
- Don't modify the original variables.
- Create separate variables for converted values.
- Don't use a solution from Google.
- Try independently first.'''


price = input(f"Enter the price : ")
quantity = input(f"Enter the quantity : ")
discount = input(f"Enter the discount price : ")
            
print(type(price))
print(type(quantity))
print(type(discount))

price = (int(price))
quantity = (int(quantity))
discount = (float(discount))

total_price = price * quantity
discount_amount = total_price * (discount / 100)
final_bill = total_price - discount_amount

print("---TOTAL BILL----")
print("Total price :",total_price)
print("Discount amount applied :" ,discount_amount)
print("Total amount to pay :", final_bill)
print("---------------------------------")
print(type(total_price))
print(type(discount_amount))
print(type(final_bill))
