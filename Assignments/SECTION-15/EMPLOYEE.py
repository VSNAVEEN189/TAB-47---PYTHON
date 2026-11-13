'''Employee Factory
You'll practice
Alternative constructors with @classmethod — creating objects from different data formats
Create an Employee class with:

Class attributes:
- company_name = "Tab47 Inc"
- employee_count — auto-increments on each creation

Instance attributes:
- name, emp_id, email, department

Three ways to create an Employee (class methods):
- Standard __init__(name, emp_id, email, department)
- from_dict(data) — creates from a dictionary like {"name": "Amit", "emp_id": "E001", "email": "amit@tab47.com", "department": "Engineering"}
- from_csv_line(line) — creates from a CSV string like "Amit,E001,amit@tab47.com,Engineering"

Static method:
- is_valid_email(email) — returns True if email contains "@" and "." after the "@"

Instance method:
- display() — prints all employee info including company name

Create employees using all three methods. Validate emails. Print the total count.

Example output:

[Tab47 Inc] Amit (E001) — Engineering — amit@tab47.com
[Tab47 Inc] Priya (E002) — Design — priya@tab47.com
[Tab47 Inc] Rahul (E003) — Marketing — rahul@tab47.com

Total employees: 3
is_valid_email("amit@tab47.com"): True
is_valid_email("invalid-email"): False'''


class Employee:

    # Class attributes
    company_name = "Tab47 Inc"
    employee_count = 0

    def __init__(self, name, emp_id, email, department):
        self.name = name
        self.emp_id = emp_id
        self.email = email
        self.department = department

        # Increase count whenever an employee is created
        Employee.employee_count += 1

    # Alternative constructor: creates employee from dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["emp_id"],
            data["email"],
            data["department"]
        )

    # Alternative constructor: creates employee from CSV string
    @classmethod
    def from_csv_line(cls, line):
        data = line.split(",")

        return cls(
            data[0],
            data[1],
            data[2],
            data[3]
        )

    # Static method: validates email
    @staticmethod
    def is_valid_email(email):
        if "@" in email:
            at_position = email.index("@")

            if "." in email[at_position + 1:]:
                return True

        return False

    # Instance method: displays employee details
    def display(self):
        print(
            f"[{Employee.company_name}] "
            f"{self.name} ({self.emp_id}) — "
            f"{self.department} — {self.email}"
        )

# 1. Creating employee using standard constructor
employee1 = Employee(
    "Amit",
    "E001",
    "amit@tab47.com",
    "Engineering"
)

# 2. Creating employee using dictionary
employee_data = {
    "name": "Priya",
    "emp_id": "E002",
    "email": "priya@tab47.com",
    "department": "Design"
}

employee2 = Employee.from_dict(employee_data)

# 3. Creating employee using CSV string
csv_line = "Rahul,E003,rahul@tab47.com,Marketing"

employee3 = Employee.from_csv_line(csv_line)

# Display employee details
employee1.display()
employee2.display()
employee3.display()

# Print total employees
print("\nTotal employees:", Employee.employee_count)

# Validate emails
print(
    'is_valid_email("amit@tab47.com"):',
    Employee.is_valid_email("amit@tab47.com")
)

print(
    'is_valid_email("invalid-email"):',
    Employee.is_valid_email("invalid-email")
)