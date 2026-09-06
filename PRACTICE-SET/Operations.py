'''
Arithmetic
Problem 1 — Basic calculator Take two numbers and calculate:
Addition,Subtraction,Multiplication,Division

Problem - 2 
Complete groups You have 53 chocolates.
Each box holds 10.
Find:Complete boxes,Remaining chocolates

Problem - 3 
Even/Odd : Take a number and determine whether it is even or odd.
'''


print("===========ARITHMETIC==========")
print("----------Problem -1--------------")

num_1 = int(input("Enter the number1 : "))
num_2 = int(input("Enter the number2 : "))

print(f"Addition of {num_1} and {num_2} is {num_1 + num_2}")
print(f"Subtraction of {num_1} and {num_2} is {num_1 - num_2}")
print(f"Multiplication of {num_1} and {num_2} is {num_1*num_2}")
print(f"Divison of {num_1} and {num_2} is {num_1/num_2}")
print(f"Floor of {num_1} and {num_2} is {num_1//num_2}")
print(f"Modulus of {num_1} and {num_2} is {num_1%num_2}")
print(f"Power of {num_1} and {num_2} is {pow(num_1,num_2)}")


print("------------Problem-2------------")
chocolates = 53
Boxes = 10
complete_box = chocolates//Boxes
remain_box = chocolates%Boxes
print(f"Complete boxes are {complete_box}")
print(f"Remaining chocolates are {remain_box}")


print("-------------Problem-3-----------")

num = int(input("Enter a number: "))
result = num % 2 == 0

print(result)


'''Comparisons
Problem 1 Take a number and check:Is it greater than 100?

Problem 2 Take a number and check whether it is:between 10 and 50'''


print("===========COMPARISON==========")
print("---------Problem-1----------")
age = int(input("Enter a number: "))
print(age > 100)

print("---------Problem-2---------")
num = float(input("Enter a number: "))
is_between = 10 <= num <= 50
print(is_between)