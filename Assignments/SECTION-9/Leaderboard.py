'''Student Leaderboard
Lists of lists and sorting with a key
Take n students, each stored as [name, marks], into a list of lists. Then produce:
• The top 3 and bottom 3 students by marks
• Students above and below the class average
• The full leaderboard sorted from highest to lowest'''

print("===== STUDENT LEADERBOARD =====")
students = []
n = int(input("Enter number of students: "))

# Taking student details
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    students.append([name, marks])

# Sorting students from highest to lowest
for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[i][1] < students[j][1]:
            temp = students[i]
            students[i] = students[j]
            students[j] = temp

# Full leaderboard
print("\n===== LEADERBOARD =====")
for i in range(len(students)):
    print(i + 1, ".", students[i][0], "-", students[i][1])

# Calculate average
total = 0
for student in students:
    total = total + student[1]
average = total / len(students)
print("\nClass Average:", average)

# Above and below average
above_average = []
below_average = []
for student in students:
    if student[1] > average:
        above_average.append(student[0])
    elif student[1] < average:
        below_average.append(student[0])
print("\nAbove Average:")
for name in above_average:
    print(name)
print("\nBelow Average:")
for name in below_average:
    print(name)

# Top 3
print("\n===== TOP 3 =====")
top_limit = 3
if len(students) < 3:
    top_limit = len(students)
for i in range(top_limit):
    print(students[i][0], "-", students[i][1])

# Bottom 3
print("\n===== BOTTOM 3 =====")
bottom_limit = 3
if len(students) < 3:
    bottom_limit = len(students)
for i in range(bottom_limit):
    student = students[len(students) - 1 - i]
    print(student[0], "-", student[1])