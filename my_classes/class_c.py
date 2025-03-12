from class_b import Point

# any class may inherit from any other class
class SpacePoint(Point):
    # NB be docstring MUST be the first line of code in any structure
    '''as well as x and y (from Point) we also need a numeric 'z' value'''
    __slots__ = ['__x', '__y', '__z']
    def __init__(self, x, y, z):
        super().__init__(x, y) # we call the __init__ of the parent class (Point)
        self.z = z
    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self, new_z):
        if type(new_z) in (int, float):
            self.__z = new_z
        else:
            self.__z = 1
    def __str__(self):
        return f'This 3-d point is at {self.x}, {self.y}, {self.z}'
    # we may choose to add functionality to a class - often to derive values
    def deriveHypot(self):
        '''use the values of x and y to return the hypotenuse'''
        return (self.x*self.x+self.y*self.y)**0.5

if __name__ == '__main__':
    # we may createt instances of our class
    s1 = SpacePoint(3, 4, 3)
    SpacePoint.__doc__ = 'changed'
    print(s1) # this calls __str__
    print(SpacePoint.__doc__) # everything can access documentation string via __doc__
    print(s1.deriveHypot()) # 5.0
