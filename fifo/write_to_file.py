def writeOutput(t):
    '''write the text 't' to a text file'''
    # we need a file access object
    fout = open('my_text.txt', 'at')
    fout.write(t)
    fout.close()# always a good idea to tidy up

# exercise the code
t = 'more conent written to file'
writeOutput(t)