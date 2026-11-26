'''Problem 6 — Student Scholarship Eligibility Checker. 

It combines comparison and logical operators.

Requirements
A student qualifies for a scholarship only if all three conditions are met:
- Marks are at least 85%.
- Attendance is at least 75%.
- The student has no pending fees.


Write a program that:
1. Takes marks and attendance as float.
2. Asks whether the student has pending fees (yes or no).
3. Checks all three conditions using and.
4. Prints the eligibility result as True or False.
'''

print("===== Student Scholarship Eligibility Checker =======")

marks = input("Enter your marks: ")
marks = float(marks)
check_marks = marks >=85

attend = input("Enter your attendace: ")
attend = float(attend)
check_attend = attend >=75 

fee = input("Enter any fees pending 'yes' or 'no': ")

checks = check_marks and check_attend

eligible = checks and (fee == "no")

print("Scholarship eligibe :",eligible)