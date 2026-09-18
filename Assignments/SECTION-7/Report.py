'''Report Card Generator
You'll practice
Composing several small functions together
Build a report card for a student across at least 5 subjects. Write these functions and have them call each other:
• calculate_percentage(marks_list) -> average percentage
• get_grade(percentage)            -> letter grade
• get_gpa(percentage)              -> GPA on a 10-point scale
• generate_report(name, marks_list) -> prints a full formatted report using the above
'''


def calculate_percentage(marks_list):
    total = sum(marks_list)
    percentage = total / len(marks_list)
    return percentage
def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
def get_gpa(percentage):
    return percentage / 10
def generate_report(name, marks_list):
    percentage = calculate_percentage(marks_list)
    grade = get_grade(percentage)
    gpa = get_gpa(percentage)

    print("===== REPORT CARD =====")
    print("Name:", name)
    print("Subjects:", len(marks_list))
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
    print("GPA:", gpa)

name = input("Enter student name: ")
marks = []
for i in range(5):
    mark = float(input("Enter Subject marks: "))
    marks.append(mark)
generate_report(name, marks)