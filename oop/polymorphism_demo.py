import math

class Shape:
    def area(self):
        """Raises an error to enforce method overriding."""
        raise NotImplementedError("Subclasses must override the area method")

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * self.radius ** 2
