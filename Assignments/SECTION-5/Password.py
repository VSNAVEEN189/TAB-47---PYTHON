'''Password Strength Checker
You'll practice
String checks without loops
Ask for a password and rate its strength by checking 5 criteria:
• At least 8 characters long
• Contains an uppercase letter
• Contains a lowercase letter
• Contains a digit
• Contains a special character (one of !@#$%^&*)

Count how many criteria pass and rate it: 0–2 Weak, 3–4 Medium, 5 Strong. Print a checklist showing which criteria passed. Use only the "in" operator and string methods — no loops.'''


password = input("Password: ")

length = len(password) >= 8
uppercase = any(char.isupper() for char in password)
lowercase = any(char.islower() for char in password)
digit = any(char.isdigit() for char in password)
special = any(char in "!@#$%^&*" for char in password)

score = length + uppercase + lowercase + digit + special

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("Length >= 8:", "Yes" if length else "No")
print("Uppercase:  ", "Yes" if uppercase else "No")
print("Lowercase:  ", "Yes" if lowercase else "No")
print("Digit:       ", "Yes" if digit else "No")
print("Special char:", "Yes" if special else "No")
print("Strength:", strength, f"({score}/5)")