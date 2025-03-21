# Python includes a 'range' object to generate a series of values

a = range(0,10) # (start, stop-before, step)
print(a, type(a))
for i in a:
    pass # do nothing!!!
    print(i)



# we can use a range to generate calculated values
odd_numbers = range(1,10,2) # we get 1, 3, 5, 7, 9
# we can use a range to generate calculated values
square_numbers = [i*i for i in range(0,10)] # 0, 1, 4, 9, 16, 25...
print(square_numbers)

# Python includes a 'generator' object
# suppose we need a sequence of integers, from zero to 10^1000
g = (i for i in range(0, 1000)) # this is a generator
print(type(g))
# we may access the next member of the generator by iterating
for i in g:
    print(i)

# what about tuple...
t = (range(0,10),True)