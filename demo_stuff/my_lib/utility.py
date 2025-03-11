def makeInt(val):
    '''try to convert the val to an integer'''
    return int(float(val))

print(f'This module is called {__name__}')

# exercise this code
# When we run a module directly, Python ALWAYS sets __name__ to '__main__'
# When a module is run by importing, then Python sets __name__ to the name of the module
# __name__ is a built in part of Python, of type string
# By the way, ANYTHING in Python called __nnn__ is a buiilt in feature of Python
if __name__ == '__main__':
    print( makeInt('3453.66') )