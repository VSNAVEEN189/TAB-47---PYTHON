'''Reassignment order and why sequence matters
You are given three variables:

a = 10
b = 20
c = 30

Rotate their values so that:
• a takes b's value
• b takes c's value
• c takes a's ORIGINAL value

After the rotation, printing a, b, c should give:

20 30 10'''


a = 10
b = 20
c = 30

temp = a

a = b
 
b = c
 
c = temp

print(a,b,c)

# WHY ORDER MATTERS:
# If I write 'a = b' first, 'a' immediately changes to 20.
# The original value (10) is instantly erased from memory.
# Later, when I run 'c = a', 'c' gets the new value (20) instead of 10.
# Result becomes: 20 30 20 (The 10 is lost forever).