'''f-strings, and using a number as both text and math
Ask the user for 5 inputs: a name, an animal, a number, a food, and a city. 
Then weave them into a funny paragraph using an f-string.

The number must be used TWICE: once as plain text in the story, and once inside a calculation that also appears in the story.
'''



N = input("Enter a name:")
A = input("Enter a animal:")
n = input("Enter a number:")
f = input("Enter a food item:")
c = input("Enter a city:")

para = (f"While vacationing in {c}, {N} adopted a pet {A}.\n "
    f"The local shelter warned that this specific {A} required exactly\n "
    f"{n} servings of {f} per day. However, after a massive growth spurt\n "
    f"the beast ate three times that amount, destroying a total of\n "
    f"{n}*3 = 6plates of {f} by dinnertime!")

print(f"{para}")