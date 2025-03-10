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

# ask the user to guess a random number
def game():
    '''generate a random number, then keep asking t he user to guess until correct'''
    answer = random.randint(0,10) # single equals SETS equality
    while True:
        # ask the user to guess
        guess = input('guess a number: ')
        # we can validate to check the user entered a numeric value (as a string)
        if guess.isnumeric(): # isnumeric() CHECKS the string but does not alter
            guess_int = int(float(guess)) # convert the string to a float ten to an int
            # check to see if they are correct
            # we may use ==, <, >, !=, <=, >=
            if answer == guess_int: # double equals CHECKS equality
                print('correct')
                break # this ends the while loop
    
game()