'''Problem 1
Ask the user for:Name,Age  Then print:
My name is ___ and I am ___ years old.

Problem 2 Take two numbers from the user and print their sum.

Problem 3
Take:length,width,Calculate the area.
Formula:
area = length × width

Problem 4
Take:price,quantity,Calculate total bill.'''



print("Problem1")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old")

print("Problem-2")
num_1 = int(input("Enter num1 : "))
num_2 = int(input("Enter num_2 : "))
num_3 = num_1 + num_2
print(num_3)


print("Problem-3")
length = int(input("Enter the legth: "))
width = int(input("Enter the width: "))
area = length * width
print(area)

print("Problem-4")
price = int(input("Enter the price:"))
quant = float(input("Enter the quantity - "))
total = price * quant
print(total)
