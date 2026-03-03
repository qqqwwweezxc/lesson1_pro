# Write a function calculate_circle_area(radius) that:

#     Takes the radius of a circle.
#     Returns the area of ​​a circle.
#     Use this function in a program that asks the user for a radius and prints out the area.

import math


def calculate_circle_area(radius):
    return math.pi * radius**2


# Create a Rectangle class that represents a rectangle.

# Class requirements:

#     Class attributes:
#     width — the width of the rectangle.
#     height — the height of the rectangle.
#     Class methods:
#     __init__(self, width, height) — a constructor that accepts the width and height of the rectangle.
#     area(self) — a method that returns the area of ​​the rectangle.
#     perimeter(self) — a method that returns the perimeter of the rectangle.
#     is_square(self) — a method that returns True if the rectangle is a square (the width is equal to the height), otherwise False.
#     resize(self, new_width, new_height) — a method that changes the width and height of the rectangle.

# Create an object of the Rectangle class and test all the methods.


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height} has square {self.get_square()}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 3)

assert r1.get_area() == 8, "Test 1"
assert r2.get_area() == 9, "Test 2"

assert r1.get_perimeter() == 12, "Test 3"
assert r2.get_perimeter() == 12, "Test 4"

assert r1.is_square() == False, "Test 5"
assert r2.is_square() == True, "Test 6"

r1.resize(5, 5)
assert r1.get_area() == 25, "Test 7"
assert r1.is_square() == True, "Test 8"
print("OK")
