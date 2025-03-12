import datetime
import time
# a generator can yield sequential values on demand

# maybe we nee a series of cube values
g = (i**3 for i in range(0, 1000)) # range is always start, slop-before

# we may write our own generator function (this might be inside a class)
def timestamp():
    '''This function will yield a datetime containing todays date and time'''
    while True: # careful - this is an endless loop
    # for i in range(0,2): # this would only yield two values
        # the generator remembers the state... yield the next value in sequence until the loop ends
        now = datetime.datetime.now()
        date_string = now.strftime('%d-%m-%Y %H:%M:%S') # we can provide any 'date picture'
        yield date_string # a function that uses yield becomes a generator

if __name__ == '__main__':
    # we may instantiate our generator
    ts_gen = timestamp()
    print( type(ts_gen) )
    # here is how we access the next member of any generator
    print( ts_gen.__next__() ) # yield the next available result from the generator
    # we can wait a while
    time.sleep(5.0)
    print( ts_gen.__next__() ) # yield the next available result from the generator
    time.sleep(5.0)
    print( ts_gen.__next__() )