'''Student Manager
You'll practice
Using objects inside objects — a class that manages a collection of other objects
Create two classes: Student and StudentManager.
Student class:
- Attributes: name, marks, city
- Methods: calculate_grade() (A+ for 90+, A for 80+, B for 70+, C for 60+, F otherwise), display()
StudentManager class:
- Internally holds a list of Student objects (not dicts — actual Student objects)
- Methods:
  - add_student(name, marks, city) — creates a Student and adds it to the internal list
  - remove_by_name(name) — removes the student with that name. Print a warning if not found.
  - get_topper() — returns the Student with the highest marks
  - get_average() — returns the average marks across all students
  - get_students_by_city(city) — returns a list of Students from that city
  - display_all() — prints all students in a formatted table

Test with at least 6 students across 3 different cities. Demonstrate every method.
Example output:
All Students:
Name          Marks   City       Grade
Amit          85      Pune       A
Priya         92      Mumbai     A+
Rahul         67      Delhi      C
Sara          78      Pune       B
Karan         95      Mumbai     A+
Neha          55      Delhi      F
Topper: Karan (95)
Average: 78.67
Students from Pune: Amit, Sara
Removing Rahul...
Students remaining: 5'''


class Student:
    def __init__(self, name, marks, city):
        self.name = name
        self.marks = marks
        self.city = city

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"

    def display(self):
        print(f"{self.name:<14}{self.marks:<8}{self.city:<12}{self.calculate_grade()}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, marks, city):
        student = Student(name, marks, city)
        self.students.append(student)

    def remove_by_name(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                return
        print(f"Warning: {name} not found!")

    def get_topper(self):
        if not self.students:
            return None

        return max(self.students, key=lambda student: student.marks)

    def get_average(self):
        if not self.students:
            return 0

        total = sum(student.marks for student in self.students)
        return total / len(self.students)

    def get_students_by_city(self, city):
        return [
            student for student in self.students
            if student.city.lower() == city.lower()
        ]

    def display_all(self):
        print(f"{'Name':<14}{'Marks':<8}{'City':<12}{'Grade'}")

        for student in self.students:
            student.display()


# Creating StudentManager object
manager = StudentManager()

# Adding 6 students
manager.add_student("Amit", 85, "Pune")
manager.add_student("Priya", 92, "Mumbai")
manager.add_student("Rahul", 67, "Delhi")
manager.add_student("Sara", 78, "Pune")
manager.add_student("Karan", 95, "Mumbai")
manager.add_student("Neha", 55, "Delhi")

# Display all students
print("All Students:")
manager.display_all()

# Get topper
topper = manager.get_topper()
if topper:
    print(f"\nTopper: {topper.name} ({topper.marks})")

# Get average
print(f"Average: {manager.get_average():}")

# Get students by city
pune_students = manager.get_students_by_city("Pune")
names = ", ".join(student.name for student in pune_students)
print(f"Students from Pune: {names}")

# Remove a student
print("\nRemoving Rahul...")
manager.remove_by_name("Rahul")
print(f"Students remaining: {len(manager.students)}")
