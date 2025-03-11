# combine every member of a collection into a single string
from stuff import checkTuple


def combine(t):
    '''validate we have a tuple, 
    then combine each member of the tuple into a string'''
    values = checkTuple(t)
    s = '-'.join( str(t) )
    return s

if __name__ == '__main__':
    t = (True, None, 'all', 'is', 'good')
    print(combine(t))