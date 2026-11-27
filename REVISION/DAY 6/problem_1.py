'''Student Discount Calculator.

Write a program that:
1. Takes the customer’s name and purchase amount.
2. Applies a discount based on the purchase amount:
Purchase amount	Discount
Below ₹1,000	0%
₹1,000–₹4,999	5%
₹5,000–₹9,999	10%
₹10,000 and above	15%
3. Calculates and displays the discount amount and final amount.
4. Rejects a negative purchase amount.

Example: Purchase amount ₹6,000 → 10% discount → ₹600 discount → ₹5,400 final amount.'''


# 1. Take customer's name and purchase amount
customer_name = input("Enter customer's name: ")
purchase_amount = float(input("Enter purchase amount (₹): "))

# 4. Reject a negative purchase amount
if purchase_amount < 0:
    print("Error: Purchase amount cannot be negative.")
else:
    # 2. Determine discount percentage based on purchase amount
    if purchase_amount < 1000:
        discount_rate = 0
    elif purchase_amount < 5000:
        discount_rate = 5
    elif purchase_amount < 10000:
        discount_rate = 10
    else:
        discount_rate = 15

    # 3. Calculate and display discount amount and final amount
    discount_amount = (purchase_amount * discount_rate) / 100
    final_amount = purchase_amount - discount_amount

    print(f"\n--- Receipt for {customer_name} ---")
    print(f"Purchase Amount : ₹{purchase_amount:,.2f}")
    print(f"Discount ({discount_rate}%)  : ₹{discount_amount:,.2f}")
    print(f"Final Amount    : ₹{final_amount:,.2f}")
