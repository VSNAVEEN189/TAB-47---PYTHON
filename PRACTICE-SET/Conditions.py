print("=======CONDITIONS=========")
# 1. Check whether marks are greater than or equal to 40.
# 2. Check whether a number is even.
print("-------IF---------")
print("------Problem-1-------")
num_1 = 36

if num_1 >= 40:
    print("greater")

print("-------Problem-2-------")
num_2 = 8

if num_2 % 2 == 0:
    print("even")
    
print("--------ELSE-------")    
# 1. Positive or negative.
# 2. Even or odd.
    
num_3 = int(input("Enter the number: "))

if num_3 >= 0:
    if num_3 == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
    
    
num_4= int(input("Enter the number: "))
if num_4 % 2 == 0:
    print("even")
else:
    print("odd")  

# Grade Calculator
# 90+ → A, 80–89 → B,70–79 → C,60–69 → D,Below 60 → F

print("------IF ELIF ELSE-------")
print("========GRADE CALCULATOR=======")

marks = int(input("Enter the number:"))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")       
elif marks >= 60:
    print("D")
else:
    print("F")        
    