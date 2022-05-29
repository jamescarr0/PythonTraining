from math import pi as PI

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Triangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)
    
    def area(self):
        return 0.5 * self.length * self.width

class VolumeMixin:
    def volume(self):
        radius = self.width
        height = self.length
        return 1/3 * (radius*radius) * height * PI

class Cone(Rectangle, VolumeMixin):
    def __init__(self, height, radius):
        super().__init__(height, radius)
    

square = Square(2)
rectangle = Rectangle(2, 4)
triangle = Triangle(3, 4)
cone = Cone(height=3, radius=11)
print(square.area())
print(rectangle.area())
print(triangle.area())
print("*" * 10)
print("Using cone Mixin for volume = ", end="")
print("{:.2f}".format(cone.volume()))
print("Using method from parent for area = " + str(cone.area()))

