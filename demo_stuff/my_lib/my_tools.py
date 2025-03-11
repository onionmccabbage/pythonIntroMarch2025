def convertUpper(s):
    '''convert a string to all upper case'''
    return s.upper()

print(f'This module is called {__name__}')

# sometimes we need to exercise the code
if __name__ == '__main__':
    print( convertUpper('some text') )