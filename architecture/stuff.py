def checkTuple(t):
    if type(t) == tuple:
        return t
    else:
        raise TypeError('We do not have a tuple')
    
# we only want to exercise the code if this module is run directly (not if it is imported elsewhere)
if __name__ == '__main__':
    checkTuple( (True, False) )
    checkTuple( (None) ) # not a tuple!!