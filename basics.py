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
f = [4,5,6, '7', 55.55, None, True, a, b, c, e] # this is a list (similar to an array in orher languages)
f[1]=-5 # we can mutate members of a list
f.append(7)
f.pop() # remove the last member

print( f, type(f) )

# a tuple is an immutable ordinal collection of any data type
g = (7,6,5, a, f, e)
# g[1] = 'oops' # this will raise an exception
print( g, type(g) )

# difference between list and tuple is mutability
# always start by using a tuple and only use list if you need mutability - this is efficiency

# iteration (loops)
# we may iterate over ANY ordinal collection
for i in e:
    print(i)

# Python code is very fussy about indentation
for i in f: # the colon indicates the start of a code block
    print(i) # every line within teh code block MUST be indented
    print(type(i))

# when we no longer indent the code, that is the end of the code block
print('oustide the code block')

