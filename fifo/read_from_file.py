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
    # t = fin.readline() # just retrieve one line
    # t = fin.readlines()  # retrieve the entire file into a list of lines
    # we may retrieve a few lines
    lines_list = []
    # or use a for loop
    lines_list.append( fin.readline() ) # the file access object has a 'cursor' which remembers where we are
    lines_list.append( fin.readline() ) # retrieves the next line
    lines_list.append( fin.readline() )
    lines_list.append( fin.readline() )
    fin.close()
    return lines_list

# exercise the code
retrieved = readTextFile()
print(retrieved, type(retrieved))
line = readSomeText()
print(line, type(line)) # we have a list