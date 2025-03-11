# we will ask the user for a number, then validate it is a number

def askUser():
    '''ask for a value (which must be a string) then check is is numeric'''
    n = input('Please enter a numeric value: ') # this will be a string
    if n.isdecimal(): # decimal allows digits
        num = float(n)
        return num
    else:
        raise TypeError('Value must be a number')

# here we check if a value  is either int or float
def validateNum(n):
    '''Check to see if we have an int or a float'''
    # in old Python we used || for 'or' we can use && for 'and'  - do not do this!!
    # if type(n) == int or type(n) == float: # or and not are all permitted
    if type(n) in (int, float):
        return n # all good we have an integer or a float
    else:
        # we may choose to set a sensible default
        n = 1
        return n

# exercise the code
try:
    val = askUser()
    print(val, type(val))
except TypeError as te:
    print(f'Problem: {te}')
except Exception as err:
    print('Unexpected exception')

# now validate the number
v = validateNum(val)
print(v)