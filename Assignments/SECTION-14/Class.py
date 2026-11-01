'''Rectangle Class
You'll practice
Creating a class with __init__, attributes, and methods
Create a Rectangle class with length and width as attributes set in __init__.

Add the following methods:
- area() — returns the area (length × width)
- perimeter() — returns the perimeter (2 × (length + width))
- is_square() — returns True if length equals width, False otherwise
- display() — prints all information about the rectangle in a readable format

Create at least 3 Rectangle objects with different dimensions (including one that is a square) and call every method on each to verify they work.

Example output:

Rectangle: 5 x 3
Area: 15
Perimeter: 16
Is Square: False

Rectangle: 4 x 4
Area: 16
Perimeter: 16
Is Square: True'''


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width

    def display(self):
        print(f"Rectangle: {self.length} x {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Is Square: {self.is_square()}")
        print()

# Create three Rectangle objects
rectangle1 = Rectangle(5, 2)
rectangle2 = Rectangle(6, 6)
rectangle3 = Rectangle(4, 7)

# Call every method on each object
rectangle1.display()
rectangle2.display()
rectangle3.display()
