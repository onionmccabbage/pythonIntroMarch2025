# There are seversal scopes in Python
# module scope refers to everything within a module
# An imported module has a different scope to the main module
# We are often concerned with global and local scope
# Global scope refers to everything in a module that is not inside a code block
# Local scope refers to anything in a module that is inside a code block

x = 'this is in the global scope of this module'

def fn():
    global x # we noiw have acces to the global variable called x
    x = 'we have access to the global variable inside this local scope'
    return x
def fnB():
    x='this is in the local scope of a code block (a function)'
    return x

if __name__ == '__main__':
    print(x)
    print(fnB()) # a local variable
    print(fn())
    print(x)
