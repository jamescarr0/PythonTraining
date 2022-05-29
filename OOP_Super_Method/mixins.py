# Mixins: Independant as possible classes.
# Independant class that gets pulled into the inheritance heirachy but does
# affect impact anything that inherits it.

from shapes import Triangle, Square

class SurfaceAreaMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)
        return surface_area

class Cube(Square, SurfaceAreaMixin):
    def __init__(self, length) -> None:
        super().__init__(length)
        # 6 surfaces to a cube, top, bottom, and 4 sides.
        self.surfaces = [Square, Square, Square, Square, Square, Square]

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

class RightPyramid(Triangle, Square, SurfaceAreaMixin):
    '''
    Right Pyramid is 3D one, think The Pyramids of Giza.
    '''
    
    def __init__(self, base, slant_height) -> None:
        self.base = base
        self.slant_height = slant_height
        self.height = slant_height
        self.length = base
        self.width = base

        # List of surfaces
        # Square = its base,
        # 4 Triangles for each pyramid face.
        self.surfaces = [Square, Triangle, Triangle, Triangle, Triangle]

    def what_am_i(self):
        return 'RightPyramid'

pyramid = RightPyramid(2, 4)
cube = Cube(4)

print(pyramid.surface_area())
print(cube.surface_area())