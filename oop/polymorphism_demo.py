import math
class Shape:
    def area(self):
        """Calculates the area of the shape. Should be overridden in derived classes."""
        raise NotImplementedError("This method should be overriden in derved classic.")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
