
class Device:
    '''Construct a device which knows about temperature and baud rate'''
    # every function that belongs to a class MUST take 'self' as the first argument
    # In Python there is no public, private, protected....
    def __init__(self, t, b): # this is 'dunder' init
        '''temperature and baud should be numeric values'''
        if type(t) in (int, float):
            self.temperature = t
        else:
            self.temperature = 12 # we maychoose to set a sensible default value
        if type(b) in (int, float):
            self.baud = b
        else:
            raise TypeError('Baud must be a numeric value')

if __name__ == '__main__':
    # we can create instances of the Device
    d1 = Device(12, 1024)
    d2 = Device(27, 2048)
    try:
        d3 = Device(None, 'oops') # this gets validated
    except TypeError as te:
        print(f'Problem: {te}')

    # we may mutate the properties of the class instances
    d1.baud = 2048 # we may access instance properties using dot-syntax

    print(d1.baud, d2)