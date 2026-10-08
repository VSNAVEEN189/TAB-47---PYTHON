'''Student CSV Writer
You'll practice
Writing and reading CSV files
Collect 5 student records (name, age, grade) from the user and write them to a CSV file with a header row. Then read the file back and display its contents as a neat table.

Example (students.csv):
name,age,grade
Rahul,20,A
Priya,19,B

Displayed back:
Name    Age   Grade
Rahul   20    A
Priya   19    B
Use the with statement so the file is always closed properly.'''



students = []

for i in range(5):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")

    students.append(name + "," + age + "," + grade)

with open("students.csv", "w") as file:
    file.write("name,age,grade\n")

    for student in students:
        file.write(student + "\n")

with open("students.csv", "r") as file:
    lines = file.readlines()

print("\nName   Age   Grade")
for line in lines[1:]:
    data = line.strip().split(",")
    print(data[0], " ", data[1], " ", data[2])