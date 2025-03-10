# here is a comment
# Python files are known as modules
# they are just plain text files

a = 3   # this is an integer
b = 8.7 # this is a float
a += 2 # we can increment or decrement += and -=
print( a, type(a), b, type(b) )

# other data types
c = True # or False boolean
d = None # quite handy, a bit like undefined
e = 'this is a string of text' # we may use single or double quotes
# here we do not mutate the original string, we create a new string to replace it
e += '------' # this is a string builder - take two strings and create a third new string
print(e)
# atrings are immutable ordinal collections of characters
print( e[11] ) # 't'
# we may use slicing on any ordinal collection
print( e[3:14:2] ) # start at member 3, stop BEFORE member 14, every other member
print( e[::-1] ) # print backwards

# we can use a string formatter like this
print( f'The value of a is {a}' ) # we may inject variables into a string

# list and tuple
# a list is a mutable ordinal collection of any data types
f = [] # this is a list (similr to an array in orher languages)