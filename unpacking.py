# sometimes we need to asign several veriables at one time
def doUnpack(struct):
    name, age, creation = struct
    return f'We have {name}, {age} and {creation}'

def packIntoStruct(a,b,c,d,e):
    s = [a,b,c,d,e] # we have a list
    return s

if __name__ == '__main__':
    # here is a structure
    t = ('Ada', '124', 'Difference Engine')
    r = doUnpack(t)
    print(r)
    # also good if we have a list
    l = ['Floella', 68, 'TV']
    r = doUnpack(l)
    print(r)
    # we can collect separate things together into a single structure
    m='Coffee'
    n='Tea'
    p='Orange'
    q='Water'
    w='Other'
    z = packIntoStruct(m, n, p, q, w)
    print(z, type(z))