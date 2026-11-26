'''Student Result and Grade Calculator

Build a program that:
1. Accepts marks in three subjects.
2. Calculates total marks.
3. Calculates average marks.
4. Checks whether the student passed (minimum 40 in every subject).
5. Displays the result.

Grade criteria:
- 90+ average: A+
- 80–89: A
- 70–79: B
- 60–69: C
- Below 60: D'''


print("===== Student Result and Grade Calculator =====")

# Taking input from students
sub_1 = float(input("Enter marks for subject 1: "))
sub_2 = float(input("Enter marks for subject 2: "))
sub_3 = float(input("Enter marks for subject 3: "))


# Calculate total marks and average
total_marks = (sub_1 + sub_2 + sub_3)
print(f"Total marks: {total_marks:.2f}")
average = (total_marks/3)
print(f"Average marks: {average:.2f}")

# Checking whether the student passed by atleast 40 in each subject
check_1 = sub_1 >= 40 
check_2 = sub_2 >=40
check_3 = sub_3 >=40

passed = check_1 and check_2 and check_3

# Print the result
print("The student is: ",passed)