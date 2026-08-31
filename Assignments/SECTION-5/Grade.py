'''if/elif/else chains and input validation
Ask the user for marks out of 100 and print a grade:
• 90–100 -> A
• 75–89  -> B
• 60–74  -> C
• 40–59  -> D
• below 40 -> Fail

Also print whether the student passed (40 or above). 
If the marks are less than 0 or greater than 100, 
print an "Invalid input" message instead of a grade.'''

marks = float(input("Enter your marks:"))

if marks <0 or marks >100:
    print("Invalid input")
elif marks >=90:
    grade="A"
elif marks >=75:
    grade="B"
elif marks >=60:
    grade="C"
elif marks >=40:
    grade="D"
else:
    grade = "Better luck next time!"


print(f"Grade:{grade}")
     
if marks >= 40:
    print("Status: Pass")
else:
    print("Status: Fail")