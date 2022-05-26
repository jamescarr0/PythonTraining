from shapes import Triangle, Square

class RightPyramid(Triangle, Square):
    '''
    Right Pyramid is 3D one, think The Pyramids of Giza.
    '''
    
    def __init__(self, base, slant_height) -> None:
        self.base = base
        self.slant_height = slant_height

    def what_am_i(self):
        return 'RightPyramid'

rp = RightPyramid(2, 4)
print(super(RightPyramid, rp).what_am_i()) # Returns only first parent, Triangle, as it was defined first!
print(rp.__class__.__bases__) # This will show all the classes that it is inherited from.

# MRO - METHOD RESOLUTION ORDER; The order in which python looks through the inheritance structure.
# Example: RightPyramid.__mro__
#    == (<class '__main__.RightPyramid'>, <class 'shapes.Triangle'>, <class 'shapes.Square'>, <class 'shapes.Rectangle'>, <class 'object'>)
# Looks in rightPyramid, then Triangle, then Square, Then Rectangle, Then Object <Top of the chain>

print(RightPyramid.__mro__)