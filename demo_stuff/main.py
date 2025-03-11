# often we call our module 'main.py'
# import utility # you can define a path the the module
# The is a potential problem...
# When we import another module, that module runs
import my_lib.my_tools # we can import from any path
from my_lib.utility import makeInt
# from .. import stuff # cannot import from the package above
# we may import from other packages

print(f'This module is called {__name__}')

# we can now use the code from other modules
i = makeInt(3.21)
print(i) # 3

l = 'this is my text'
u = my_lib.my_tools.convertUpper(l)
print(u)

