# class Point(object): # we may choose to explicitly inherit from 'object'
# class Point(): # or we may choose to implicitly inherit from 'object'
class Point: 
    '''define a point in planar space with numeric values for x and for y'''
    # we slots to restrict members
    __slots__ = ['__x', '__y'] # the only permitted members of this class are here
    def __init__(self, x, y):
        self.x = x # this calls the setter function to set self.__x
        # self.validateY(y) # this is not common syntax in Python
        self.y = y
    @property # this is called a property getter decorator
    def x(self):
        '''return the value of property x'''
        return self.__x # we use name mangling to protect data
    @x.setter # this is called a property setter decorator
    def x(self, new_x):
        if type(new_x) in (int, float):
            self.__x = new_x
        else:
            self.__x = 1 # just set a sensible default (we could raise an exception)
    # implement the getter and setter for y
    @property # @property must come before the setter
    def y(self):
        return self.__y # we use double underscore to 'protect' this property from direct access
    @y.setter
    def y(self, new_y):
        if type(new_y) in (int, float):
            self.__y = new_y
        else:
            self.__y = 1 # or raise an exception
    # def validateY(self, new_y):
    #     if type(new_y) in (int, float):
    #         self.__y = new_y
    # we overide the built in __str__ method with our own
    def __str__(self):
        '''define how this class should print'''
        return f'This point is at {self.x} and {self.y}'

if __name__ == '__main__':
    p1 = Point(3,4)
    p2 = Point('3', 2)
    # when we try to mutate properties, the setter method is used
    p2.x = 99 # this will run the function to set __x
    # when we try to access properties, the getter method is used
    print(p1.x, p1.y) # this will run the function def x() to return __x
    print(p2.x, p2.y)
    # check to see the slots are working
    # p1.__x = 99 # this will also fail - we do not permit direct acces to __x (or __y)
    # p1.__z = 3 # this will fail - not in the slots
    print(p2)