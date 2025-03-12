
class Device:
    '''Construct a device which knows about temperature and baud rate'''
    # every function that belongs to a class MUST take 'self' as the first argument
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
    d3 = Device(None, 'oops') # this gets validated

    print(d1, d2)