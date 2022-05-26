class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length) -> None:
        super().__init__(length, length)

    def what_am_i(self):
        return 'Square'


class Cube(Square):
    # Same params as a Square, no need to redefine the __init__

    def surface_area(self):
        # Look for .area() in Cube, then it looks in Square, then it looks and finally finds it in Rectanlge.
        face_area = self.area()
        return face_area * 6

    def volume(self):
        # Look straight to the super object, first Square, then Rectangle.
        face_area = super().area()
        return face_area * self.length

    def what_am_i(self):
        return 'Cube'

    def family_tree(self):
        return self.what_am_i() + ' and i am a child of ' + super().what_am_i()

class Triangle():
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def what_am_i(self):
        return 'Triangle'
    


# s = Square(3)
# print(f"Type: {s.__class__}")
# print(f"Inherits from: {s.__class__.__bases__}")

# c = Cube(3)
# print(c.volume())
# print(f"I am a {c.family_tree()}")