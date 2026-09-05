# for loops and range()
# Ask the user for a number and print its multiplication table from 1 to 10 using a loop.

# Example (number = 7)

number = int(input("Enter the number:"))

for i in range(1,11):
    print(number , "x", i , "=",number*i)
    
    