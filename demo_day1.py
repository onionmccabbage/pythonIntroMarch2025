# collections
s = 'an immutable collection of characters - we may use slicing'
# s[0] = 'A' # this fails - we CANNOT mutate a string
print(s[6:16])

t = (5, 'hello', True) # immutable
l = [6, 'ok', None]    # mutable
l[0] = 'A' # all good

for i in range(0,10):
    print(i)

def doStuff(x):
    if type(x)==str:
        print(f'{x} is a sting')
    elif type(x)==int:
        print(f'{x} is an int')
    else:
        print('it is something else')

doStuff('hello')
doStuff(4)
doStuff(5.0)