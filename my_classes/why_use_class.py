# we already have plenty of stuctures to collect related data into (list, tuple, dict...)
# The problem is none of the built in stutures have any means to validate

# suppose we need to guarantee the 'name' is a string, and the 'age' is a positive integer
# we need to write validation code
# classes let us build the validation into the data structure

p1 = ('Sharon', 54)
p2 = ['Ethel', 33]
p3 = {'Oenid', 67}
p4 = {True, -55} # this is not suitable for a person

# here is the most basic Python class
class Person:
    # we usually include an __init__ method in a class
    def __init__(self): # this function gets caled every time we use this class to make an instance
        pass

if __name__ == '__main__':
    # we can make instances of our 'Person' class
    pA = Person() # when we create this instance, the __init__ method runs ONCE
    pB = Person()