'''Name Formatter
You'll practice
Slicing and string methods
Ask for a full name and produce:
• The first name and last name separately
• The initials (e.g. "Rahul Kumar Sharma" -> "R.K.S.")
• The name in Title Case

Handle names of any length — two words, three words, or more.
'''

full_name =input("Enter your full name: ")

def process_full_name(name):
  name_parts = name.split()

name_parts = full_name.split()
if name_parts:
    first_name = name_parts[0]
    last_name = name_parts[-1] if len(name_parts) > 1 else ""
    initials = ".".join([part[0].upper() for part in name_parts]) + "."
    title_case_name = " ".join([part.capitalize() for part in name_parts])
    print(f"First: {first_name}")
    print(f"Last: {last_name}")
    print(f"Initials: {initials}")
    print(f"Title Case: {title_case_name}")
