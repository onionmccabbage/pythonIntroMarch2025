# import time
# import datetime # our module is called datetimes so it does not collide with this!!
from time import time # just import the time functionality
from datetime import * # import everything from the datetime library

# the time and datetime libraries are part of the Python Standard Library

print( time() ) # no need ot write time.time()
# we often need a human friendly date time format
print( datetime.date( datetime.today() ) )
