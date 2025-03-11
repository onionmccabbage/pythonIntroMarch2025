def readTextFile():
    '''retrieve the contents of a text file'''
    fin = open('my_file.txt', 'rt') # 'r' will read 't' specifies text
    t = fin.read() # retrieve the entire contents of the text file into memory
    fin.close()
    return t

# exercise the code
retrieved = readTextFile()
print(retrieved, type(retrieved))