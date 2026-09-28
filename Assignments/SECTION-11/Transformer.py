'''Student Data Transformer

Dict comprehensions and filtering
Given a list of student dictionaries (each with name, city, marks, department), produce — using ONLY comprehensions:
• a {name: grade} dictionary
• a filtered list of students from a given city whose marks are above a cutoff
• a list of names sorted by marks (highest first)
• a {department: average_marks} dictionary'''

students = [
    {"name": "Amit", "city": "Delhi", "marks": 72, "department": "CSE"},
    {"name": "Sneha", "city": "Mumbai", "marks": 88, "department": "ECE"},
    {"name": "Arjun", "city": "Delhi", "marks": 95, "department": "ME"}]
city = "Delhi"
cutoff = 80

grades = {
    student["name"]: (
        "A" if student["marks"] >= 90
        else "B" if student["marks"] >= 80
        else "C"
    )
    for student in students}

filtered_students = [
    student
    for student in students
    if student["city"] == city and student["marks"] > cutoff]

names_by_marks = [
    student["name"]
    for student in sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True)]

departments = {student["department"] for student in students}

average_marks = {
    department:
        sum(
            student["marks"]
            for student in students
            if student["department"] == department
        )/
        sum(
            1
            for student in students
            if student["department"] == department
        )
    for department in departments}

print("Grades:", grades)
print("Filtered:", filtered_students)
print("Names by marks:", names_by_marks)
print("Average marks:", average_marks)