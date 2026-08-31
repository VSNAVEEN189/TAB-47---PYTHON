'''Take two numbers from the user and report on their relationship.

Print:
• Which number is larger (or whether they are equal)
• The remainder when the larger is divided by the smaller
• Whether both are even, both odd, or mixed'''


num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

larger = num1 * (num1 > num2) + num2 * (num2 > num1)
is_remaind_of = (num1 % num2)
result = (num1 % 2 == 0) + 2 * (num2 % 2 == 0)

both_even = (num1 % 2 == 0) and (num2 % 2 == 0)
both_odd = (num1 % 2 != 0) and (num2 % 2 != 0)


result = both_even or both_odd
number = both_even * 2 + both_odd

print(f"The larger number is {larger}")
print(f"The remainder of {num1} and {num2}: {is_remaind_of}")
print(f"Both are {number}")