'''Write three functions that each RETURN an area (do not print inside them):
• circle_area(r)        -> 3.14159 × r × r
• rectangle_area(l, w)  -> l × w
• triangle_area(b, h)   -> 0.5 × b × h
Then ask the user which shape they want, collect the needed inputs, call the correct function, and print the returned result.'''

def circle_area(r):
    return 3.14159 * r * r
def rectangle_area(l, w):
    return l * w
def triangle_area(b, h):
    return 0.5 * b * h

shape = input("Shape (circle/rectangle/triangle): ")
if shape == "circle":
    r = float(input("Radius: "))
    area = circle_area(r)
elif shape == "rectangle":
    l = float(input("Length: "))
    w = float(input("Width: "))
    area = rectangle_area(l, w)
elif shape == "triangle":
    b = float(input("Base: "))
    h = float(input("Height: "))
    area = triangle_area(b, h)
else:
    print("Invalid shape")
    area = None
if area is not None:
    print("Area:", area)