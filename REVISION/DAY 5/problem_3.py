'''Student Grade Calculator
Your task: Build a Python program that calculates a student's total, average, pass/fail status, and final grade.
Requirements
1. Accept marks for three subjects.
2. Calculate total marks.
3. Calculate average marks.
4. Check whether the student passed (minimum 40 marks in every subject).
5. Assign a grade based on the average.

Grade criteria
Average marks	Grade
90–100	A+
80–89.99	A
70–79.99	B
60–69.99	C
Below 60	D

Important: A student who fails even one subject must receive an F, regardless of their average.'''

print("===== Student Grade Calculator =====")

# Asking marks
m1 = float(input("Enter marks for maths: "))
m2 = float(input("Enter marks for science: "))
m3 = float(input("Enter marks for english: "))

# Calculating marks and average
total_marks = m1 + m2 + m3
average = total_marks/3

# Grade criteria
if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100:
    print("Invalid marks")
elif m1 < 40 or m2 < 40 or m3 < 40:
    status = "Fail"
    grade = "F"

    print(f"Status: {status}")
    print(f"Grade: {grade}")
    print(f"Total marks: {total_marks:.2f}")
    print(f"Average marks: {average:.2f}")
else:
    status = "Pass"
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    print(f"Status: {status}")
    print(f"Grade: {grade}")
    print(f"Total marks: {total_marks:.2f}")
    print(f"Average marks: {average:.2f}")
