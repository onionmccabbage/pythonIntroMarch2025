# we may choose to write functions
def fnA(): # we define a function and start a code block with a colon
    a=3
    b=8.5
    return b/a # or + - * as usual

def fnB(a, b): # optionally a function may recieve variables (also called arguments)
    '''we often write a docstring to explain the purpose of a code block
    Triple quotes let us have new lines within a string object
    In this case, take a and b and calculate mathematical results'''
    total = a+b
    diff  = a-b
    prod  = a*b
    pow   = a**b
    modulo= b//a
    rem   = b%a
    return (total, diff, prod, pow, modulo, rem) # a list of all my results

# we may call the function
r = fnA() # the () invoke the function (it runs)
print( r, type(fnA) )  

print( fnB() )