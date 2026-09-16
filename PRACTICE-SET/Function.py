'''Level 1 — Basic
1. Create a function greet() that prints "Welcome to Python".
2. Create a function show_name(name) that prints the user's name.
3. Create a function square(number) that returns the square.'''

# print("====Problem-1====")
# def greet():
#     print("Welcome to Python")
    
# greet()    


# print("====Problem-2====")    
# def show_name(name):
#     print(name)
    
# show_name("Naveen")    

# print("====Problem-3====")
# def square(num):
#     return num ** 2

# print(square(5))

'''Level 2 — Parameters + Return

4. Create:
add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)
Each function should return the answer.'''

print("====Problem-4===")

def add(a,b):
    return a + b
print(add(4,6))

def sub(a,b):
    return a - b
print(sub(30,40))

def multi(a,b):
    return a * b
print(multi(2,5))

def div(a,b):
    return a/b
print(div(9,3))

'''Conditions inside Functions

5. Create:check_even(number),Return "Even" or "Odd".'''

print("====Problem-5====")

def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even(4))  
print(check_even(7))   

'''6. Create:

check_age(age)

Return whether the person is eligible to vote.'''
print("====Problem-6====")
def check_age(age):
    if age < 18 :
        return"Not eligble to vote"
    else:
        return"Eligble to vote"
print(check_age(30))
print(check_age(12))


print("====Problem-7====")
'''Create:calculate_grade(marks),Return the appropriate grade.'''
    
def calculate_grade(marks):
    if 90 <= marks <= 100:
        return 'A'
    elif 80 <= marks < 90:
        return 'B'
    elif 70 <= marks < 80:
        return 'C'
    elif 60 <= marks < 70:
        return 'D'
    elif 0 <= marks < 60:
        return 'F'
    else:
        return 'Invalid marks'
score = 85
print(f"Marks: {score}, Grade: {calculate_grade(score)}")

        