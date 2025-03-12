import datetime
# a generator can yield sequential values on demand

# maybe we nee a series of cube values
g = (i**3 for i in range(0, 1000)) # range is always start, slop-before

# we may write our own generator function (this might be inside a class)
def timestamp():
    '''This function will yield a datetime containing todays date and time'''
    while True: # careful - this is an endlless loop
        now = datetime.datetime.now()
        date_string = now.strftime('%d-%m-%Y %H:%M:%S') # we can provide any 'date picture'
        yield date_string # a function that uses yield becomes a generator

if __name__ == '__main__':
    # we may instantiate our generator
    ts_gen = timestamp()
    print( type(ts_gen) )