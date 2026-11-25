'''Number Analysis

Take an integer from the user and calculate:
1. Its square using **.
2. Its cube using **.
3. Its quotient when divided by 2 using //.
4. Its remainder when divided by 2 using %.
5. Check whether it is even or odd using the remainder.'''


number = int(input("Enter an integer:"))

# Square
square = number**2
print(square)

# Cube
cube = number**3
print(cube)

#quotient
quot = number//2
print(quot)

# Remainder
remain = number%2
print(remain)

# Even or odd
check = remain==0
print(bool(check))