'''Store a distance in kilometers in one variable, 
then convert it into several units, each held in its own variable.

From km, compute:
• miles       = km × 0.621
• meters      = km × 1000
• centimeters = km × 100000
• feet        = km × 3280.84

Print a formatted summary.'''

# Taken km value
km = 15

# Conversion units
miles = km * 0.621
meters = km * 1000
centimeters = km * 100000
feet = km * 3280.84


print("====CONVERSION SUMMARY====")
print(f"miles:  {miles}mi")
print(f"meters:   {meters}m")
print(f"centimeters:  {centimeters}cm")
print(f"feet:   {feet}ft")