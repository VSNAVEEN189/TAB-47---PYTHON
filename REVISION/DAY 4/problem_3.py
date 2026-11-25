'''Discount Eligibility Checker

Logical operator

A store gives a discount when a customer meets both conditions:
- The bill is at least ₹1,000.
- The customer is a member.
Write a program that:
1. Takes the bill amount and converts it to float.
2. Takes whether the customer is a member (True or False) and converts it to a Boolean.
3. Uses and to check whether the customer qualifies.
4. Prints the eligibility result.'''


bill = input("Enter the bill amount : ₹")

bill = float(bill)

check = bill >=1000

member = input("Enter are you a member yes or no: ")

checks = member.lower() == "yes"

qualify = check and checks

print(qualify)