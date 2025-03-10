# Python includes many built in features
# It also oncludes the Python Standard Library (loads of additional features)
# We can easily import from the many aspects of this library
import random

def makeRandNumber():
    '''We can generate a random number'''
    r = random.randint(0,10) # return a random integer
    # by default every functio will return anyway
    # but in this case we probably want to return something
    return r

# sometimes we need to call a function repeatedly
for i in range(0,10): # range givves us values between (start, stop-before)
    print( makeRandNumber() )
