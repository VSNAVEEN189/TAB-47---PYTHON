'''
Nested loops and spacing math
Ask for an odd number n and print a diamond of stars: n rows in the top half (including the widest middle row), then mirror it for the bottom half.

Example (n = 3
'''

n = int(input("Enter an odd number: "))

# Top half
for row in range(n):

    spaces = n - row - 1
    stars = 2 * row + 1

    for i in range(spaces):
        print(" ", end="")

    for i in range(stars):
        print("*", end="")

    print()


# Bottom half
for row in range(n - 2, -1, -1):

    spaces = n - row - 1
    stars = 2 * row + 1

    for i in range(spaces):
        print(" ", end="")

    for i in range(stars):
        print("*", end="")

    print()
 
    
    