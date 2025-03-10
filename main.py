# often we call our module 'main.py'
# import utility # you can define a path the the module
import my_tools
from utility import makeInt


# we can now use the code from other modules
i = makeInt(3.21)
print(i) # 3

l = 'this is my text'
u = my_tools.convertUpper(l)
print(u)