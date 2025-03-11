def readTextFile():
    '''retrieve the contents of a text file'''
    fin = open('my_text.txt', 'rt') # 'r' will read 't' specifies text
    t = fin.read() # retrieve the entire contents of the text file into memory
    fin.close()
    return t

# we may also read just a part of the file
def readSomeText():
    '''Retreive just a part of the text file'''
    fin = open('my_text.txt', 'rt')
    t = fin.readline() # just retrieve one line
    return t

# exercise the code
retrieved = readTextFile()
print(retrieved, type(retrieved))
line = readSomeText()
print(line)